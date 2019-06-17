
# Contents


## Overviews


## Data Preparation


## Model Training


## Result


## How to run the code


## Overviews



<p id="gdcalert1" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/overview-documents0.png). Store image on your image server and adjust path/filename if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert2">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/overview-documents0.png "image_tooltip")


Figure 1: Car make and model detection process

The implementation for detecting car make and model is started by doing data preprocessing to obtain car label for training and testing. The next step is to train the deep learning model for car make and model detection. After training the model, car make and model detection is performed from testing dataset.

The method for detect car make and model is implemented by using Inception-V3 network by Google. The training and testing code is borrowed from [https://github.com/brucechou1983/CheXNet-Keras](https://github.com/brucechou1983/CheXNet-Keras) with a modification.  Data preprocessing is implemented using Python. Keras is also used to implement the model for the deep learning method. For evaluation, Sklearn is used to compute accuracy, precision and recall.


## Data Preparation

Image annotation is performed before feeding the training data to the model. For each image in dataset, the car object is cropped from the background. The reason to perform cropping on the image is to minimize the noise from the background. 

<p id="gdcalert2" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/overview-documents1.jpg). Store image on your image server and adjust path/filename if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert3">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/overview-documents1.jpg "image_tooltip")


Figure 2: Original Image



<p id="gdcalert3" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/overview-documents2.jpg). Store image on your image server and adjust path/filename if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert4">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/overview-documents2.jpg "image_tooltip")


Figure 3: Cropped Image

After cropping the car object from the label, the next step is to index each image to their correct label accordingly. There are 196 labels for the dataset. Each label is the representation of the car make, model and model year. **Dodge Challenger SRT8 2011** is the example of the label for the dataset where **Dodge **is the car make, **Challenger SRT8 **is the car model, and **2011** is the car model year. The dataset is represented in .csv file. The table below is the representation of the dataset in the .csv file.


<table>
  <tr>
   <td>Image Index
   </td>
   <td>Finding Labels
   </td>
   <td>Car Label 1
   </td>
   <td>…………..
   </td>
   <td>Car Label <em>N</em>
   </td>
  </tr>
  <tr>
   <td>123.jpg
   </td>
   <td>Car Label 1
   </td>
   <td>1
   </td>
   <td>……….
   </td>
   <td>0
   </td>
  </tr>
  <tr>
   <td>……….
   </td>
   <td>……….
   </td>
   <td>0
   </td>
   <td>……….
   </td>
   <td>0
   </td>
  </tr>
  <tr>
   <td>999.jpg
   </td>
   <td>Car Label <em>N</em>
   </td>
   <td>0
   </td>
   <td>……….
   </td>
   <td>1
   </td>
  </tr>
</table>



## Model Training

For training the model, training file provided by [https://github.com/brucechou1983/CheXNet-Keras](https://github.com/brucechou1983/CheXNet-Keras) is used. 3-fold cross-validation strategy is also used to train the model. The model training is validated using Area Under the Receiver Operating Characteristic Curve (ROC AUC). Below is the graph for the model training evaluation using Inception-V3 network.



<p id="gdcalert4" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/overview-documents3.png). Store image on your image server and adjust path/filename if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert5">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/overview-documents3.png "image_tooltip")




<p id="gdcalert5" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/overview-documents4.png). Store image on your image server and adjust path/filename if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert6">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/overview-documents4.png "image_tooltip")



## Result



<p id="gdcalert6" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/overview-documents5.png). Store image on your image server and adjust path/filename if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert7">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/overview-documents5.png "image_tooltip")




<p id="gdcalert7" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/overview-documents6.png). Store image on your image server and adjust path/filename if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert8">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/overview-documents6.png "image_tooltip")




<p id="gdcalert8" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/overview-documents7.png). Store image on your image server and adjust path/filename if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert9">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/overview-documents7.png "image_tooltip")



## How to run the code



*   Please follow this guide for deep learning framework initialization - [https://github.com/brucechou1983/CheXNet-Keras](https://github.com/brucechou1983/CheXNet-Keras) Download the pre-processed dataset file (Anotated images of car) - [all-car-data.zip](https://drive.google.com/file/d/1nEsxR8dGAqcrEb7TCYufpTI7amNjza1N/view?usp=sharing)
*   Replace files train.py and config.ini from https://github.com/brucechou1983/CheXNet-Keras repository, with these files [train.py](https:) - modified train.py and [config.ini](https:) - modified config.ini
*   Put car_split, car_split_2, and car_split_3 folders in file index in /data folder together with default_split folder
*   run python train.py to train or test.py to test the file

<!-- Docs to Markdown version 1.0β17 -->
