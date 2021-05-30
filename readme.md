# Jango Aano?
The project is done as a part of Build From Home conducted by Tinkerhub.
The project is a binary image classifier to classy images of mango and jackfruit, also it can detect whether the image is neither of the two. 
it returns the output with a decent accuracy.We did the project using pytorch in google colab.
We have used images downloaded from google images and kaggle after saving it in our google drive. 
The link for dataset from google drive:  https://drive.google.com/drive/folders/1BzkwvN86s5fE2Mxhz6jFq6Bq2_8XPwdA?usp=sharing
We have used a simple Lenet 5 based CNN architecture to implement the model.It has 5 layers - 2 convolution and maxpool layers and 3 fully connected layers.The trained model is saved to derive. 
The pretrained model saved in derive is obtained hosted as a url

 

## Team members
1. Sanjana A R [https://github.com/Sanj112]
2. Sanjay s Nair[https://github.com/Sanjaysnair0721]

## Team id : 
BFH/recHYFLbYimQhCULF/2021

## Link to product walkthrough
https://www.loom.com/share/596f2350b88c416886aab0ac1c33ee05

## How it Works ?
1. We have used a simple Lenet 5 based CNN architecture to implement the model.It has 5 layers - 2 convolution and maxpool layers and 3 fully connected layers.
The trained model is saved to derive. 
2.The pretrained model saved in derive is obtained hosted as a url

## Libraries used
flask == 1.1.1
matplotlib == 3.2.0
imageio ==2.0.0
torchvision
pytorch == 1.6.0
pillow==6.0.0
gunicorn==20.0.0

## How to configure and run
We have given the python noteboks and link to open in colab, you can copy and create your own file. Obtain the link for Traioning dataset and change the path to your convenienvce and python notebook can be run and model trained further.
For running web app download jango classifier.pt and import it from drive and run it in a new colab notebook as mentioned above. After the cell app.py runs, the output line which mentions  "Running on" ouput will have a url, clicking on to that we can get the web page, grab a url and paste it on the page, you will get the predication

