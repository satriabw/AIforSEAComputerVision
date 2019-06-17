'''
    This code is taken from https://github.com/brucechou1983/CheXNet-Keras
'''
import numpy as np
import os
from configparser import ConfigParser
from generator import AugmentedImageSequence
from models.keras import ModelFactory
from sklearn.metrics import roc_auc_score, accuracy_score, precision_score, recall_score
from utility import get_sample_counts

def main():
    # parser config
    config_file = "./config.ini"
    cp = ConfigParser()
    cp.read(config_file)

    # default config
    output_dir = cp["DEFAULT"].get("output_dir")

    base_model_name = cp["DEFAULT"].get("base_model_name")
    class_names = cp["DEFAULT"].get("class_names").split(",")
    image_source_dir = cp["DEFAULT"].get("image_source_dir")

    # train config
    image_dimension = cp["TRAIN"].getint("image_dimension")

    # test config
    batch_size = cp["TEST"].getint("batch_size")
    test_steps = cp["TEST"].get("test_steps")
    use_best_weights = cp["TEST"].getboolean("use_best_weights")

    # parse weights file path
    output_weights_name = cp["TRAIN"].get("output_weights_name")
    weights_path = os.path.join(output_dir, output_weights_name)
    best_weights_path = os.path.join(output_dir, f"best_{output_weights_name}")

    # get test sample count
    test_counts, _ = get_sample_counts(output_dir, "test", class_names)

    # compute steps
    if test_steps == "auto":
        test_steps = int(test_counts / batch_size)
    else:
        try:
            test_steps = int(test_steps)
        except ValueError:
            raise ValueError(f"""
                test_steps: {test_steps} is invalid,
                please use 'auto' or integer.
                """)
    print(f"** test_steps: {test_steps} **")

    print("** load model **")
    if use_best_weights:
        print("** use best weights **")
        model_weights_path = best_weights_path
    else:
        print("** use last weights **")
        model_weights_path = weights_path
    model_factory = ModelFactory()
    model = model_factory.get_model(
        class_names,
        model_name=base_model_name,
        use_base_weights=False,
        weights_path=model_weights_path)

    print("** load test generator **")
    test_sequence = AugmentedImageSequence(
        dataset_csv_file=os.path.join(output_dir, "test.csv"),
        class_names=class_names,
        source_image_dir=image_source_dir,
        batch_size=batch_size,
        target_size=(image_dimension, image_dimension),
        augmenter=None,
        steps=test_steps,
        shuffle_on_epoch_end=False,
    )

    print("** make prediction **")
    y_hat = model.predict_generator(test_sequence, verbose=1)
    y_hat_max_index = np.argmax(y_hat, axis=1)

    # Decode one hot label to index
    y = test_sequence.get_y_true()
    y_gt = [np.where(r == 1)[0][0] for r in y]

    test_log_path = os.path.join(output_dir, "test.log")
    print(f"** write log to {test_log_path} **")

    pred_label = []
    with open(test_log_path, "w") as f:
        for i in range(len(y_hat)):
            # Append prediction confidence score and prediction label output
            y_pred = np.zeros(len(y_hat[i]))
            y_pred[y_hat_max_index[i]] = 1

            # convert one hot label to indexs
            y_pred_label = np.where(y_pred==1)[0][0]

            # Compute score
            confidence_score = np.amax(y_hat[i])

            pred_label.append(y_pred_label)
            f.write(f"{class_names[y_gt[i]]}\nConfidence Score: {confidence_score}\n")


        accuracy = accuracy_score(y_gt, pred_label)
        precision = precision_score(y_gt, pred_label, average='macro')
        recall = recall_score(y_gt, pred_label, average='macro')
        f.write("-------------------------\n")
        f.write(f"accuracy: {accuracy}\n")
        f.write(f"precision: {precision}\n")
        f.write(f"recall: {recall}\n")
        print(f"accuracy: {accuracy}")
        print(f"precision: {precision}")
        print(f"recall: {recall}")

if __name__ == "__main__":
    main()
