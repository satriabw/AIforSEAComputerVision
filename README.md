
# Contents

### Overviews
### Result
### How to run the code
-
## Overviews

![alt_text](images/preview_process.png "preview")

<br>

The implementation for detecting car make and model is started by doing data preprocessing to obtain car label for training and testing. The next step is to train the deep learning model for car make and model detection. After training the model, car make and model detection is performed from testing dataset.

The method for detect car make and model is implemented by using Inception-V3 network by Google. The training and testing code is borrowed from [Chexnet-Keras implementation](https://github.com/brucechou1983/CheXNet-Keras) with a modification.  Data preprocessing is implemented using Python. Keras is also used to implement the model for the deep learning method. For evaluation, Sklearn is used to compute accuracy, precision and recall.


## Result


![alt_text](images/auroc.png "auroc")

![alt_text](images/mean-loss.png "mean-loss")

![alt_text](images/time.png "time")



## How to run the code

*   Please follow this guide for deep learning framework initialization - [https://github.com/brucechou1983/CheXNet-Keras](https://github.com/brucechou1983/CheXNet-Keras) Download the pre-processed dataset file (Anotated images of car) - [all-car-data.zip](https://drive.google.com/file/d/1nEsxR8dGAqcrEb7TCYufpTI7amNjza1N/view?usp=sharing)
*   Replace files train.py and config.ini from https://github.com/brucechou1983/CheXNet-Keras repository, with these files [train.py](https:) - modified train.py and [config.ini](https:) - modified config.ini
*   Put car_split, car_split_2, and car_split_3 folders in file index in /data folder together with default_split folder
*   run python train.py to train or test.py to test the file


