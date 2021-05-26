# -*- coding: utf-8 -*-
"""Flask.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1AdT1aFdc9hiLKTWii3hzbAz6X2r3n2kI
"""

from flask import Flask, redirect, url_for, request, render_template
from flask_ngrok import run_with_ngrok
from imageio import imread
from PIL import Image
import matplotlib.pyplot as plt
import torchvision
from torchvision import models, datasets
import torchvision.transforms as transforms
import torch
import torch.nn as nn
import torch.nn.functional as F

#example valid urls
urll = "https://thumbs.dreamstime.com/b/fruits-mango-scientific-name-mangifera-indica-anacardiaceae-ripened-fruit-piled-up-sale-thiruvananthapuram-kerala-india-48649430.jpg"
urll_strawberry="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTlVUvJaC6A7E6v6BiwlGbK-fbDhbOqFdF7Ig&usqp=CAU"
urlll = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSIbYghVvP244wnntIFb9K4sgaFbqW5lrCE-w&usqp=CAU"

from google.colab import drive
drive.mount('/content/drive')

device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')
device

#architecture based on Lenet5
class Net_jango(nn.Module):
  #defining basic layers
  def __init__(self):
        super(Net_jango, self).__init__()
	# 3 input image channel, 6 output channels, 5x5 square convolution kernel
        self.conv1 = nn.Conv2d(3, 6, 5)
	# Max pooling over a (2, 2) window
        self.maxpool = nn.MaxPool2d(2, 2)
	# 6 input image channel, 16 output channels, 5x5 square convolution kernel
        self.conv2 = nn.Conv2d(6, 16, 5) 
  #3 fully connected layers
        self.fullyconnected1 = nn.Linear(16 * 5 * 5, 120)
        self.fullyconnected2 = nn.Linear(120, 84)
        self.fullyconnected3 = nn.Linear(84, 2)

  def forward(self, x):
	# the forward propagation algorithm 
        x = self.maxpool(F.relu(self.conv1(x)))
        x = self.maxpool(F.relu(self.conv2(x)))
        x = x.view(-1, 16 * 5 * 5)
        x = F.relu(self.fullyconnected1(x))
        x = F.relu(self.fullyconnected2(x))
        x = self.fullyconnected3(x)
        return x

#loading model 
model = Net_jango()
model_save_name = 'jango_classifier.pt'
path_model = "/content/drive/MyDrive/jackfruit_mango_classifier/" + model_save_name
model.load_state_dict(torch.load(path_model))
#model.to(device)

#required transforms
def transform_images(im):
  mean = torch.tensor([0.485, 0.456, 0.406], dtype=torch.float)
  std = torch.tensor([0.229, 0.224, 0.225], dtype=torch.float)
  transform1 = transforms.Compose([
      transforms.Resize((32,32)),
      transforms.ToTensor(),
      transforms.Normalize(mean=mean, std=std)])
  image = transform1(im)
  return image.unsqueeze(0)

app = Flask(__name__,template_folder='/content/drive/MyDrive/jackfruit_mango_classifier/templates')
run_with_ngrok(app)
 
@app.route('/')
def home():
  return render_template('jango.html')
 
@app.route('/predict', methods=['GET', 'POST'])
def predict():
  if request.method == 'GET':
    user = request.args.get('source')
    print(user)
    image = imread(user,pilmode="RGB")
    image = Image.fromarray(image)
    plt.imshow(image)
    with torch.no_grad():
      # transform the image    
      transformed_image = transform_images(image)
      
      # use the model to predict the class
      outputs = model(transformed_image)
      output = nn.Softmax(dim=1)(outputs)[0]*100
      max,id=torch.max(output,0)
      classes =["chakka", "manga"]

      if(max>85):
        out = "The given image belongs to category : "+classes[id]
      else:
        out = "The given image is not mango or jackfruit"
    return redirect(url_for('success', out = out)) 

@app.route('/success/<out>')
def success(out):
    return render_template('jango.html', prediction_text = out)
 
#"https://images.app.goo.gl/PH1nAmmAPwf5dQBh7" - mang
#https://images.app.goo.gl/b6X46swmbpNgXWkZ6 - jack

app.run()
