<h2>Style Transfer - Project 3</h2>

We used the model from https://www.tensorflow.org/tutorials/generative/style_transfer to do an exploration of Neural style transfer. Using a convolutional network, we are extracting pixels out of images and using them as nodes for machine learning. A node takes the input from the style guide image as a set of coefficients, that will alter the image output as it passes through matrices, with calculations that will sharpen or blur parts of the image or the colors therein. The result is any image that a user inputs can be quickly stylized through the model. <br>

To run the app locally, clone the repository, install the requirements.txt file, activate the pipenv, and run app.py in Python.  <br>
You do not need a local version, as this is deployed through FloydHub here: XX__URL__XX.  <br> <br>
As a user, you can use the form on the homepage to upload an image of anything you like, and see returned stylized images in various known styles.  <br>
We started with the Kandinsky style as this was used in our model, but we also added styles such as Monet, Mucha, and Simpsons. <br>
A really great thing about our app is that if you download the repo locally, you can swap the style for any that you want by adding other styles of image to the Styles folder.  <br>

<h4>Requirements / Built With: </h4><br>
flask <br>
Pillow <br>
tensorflow <br>
tensorflow_hub <br>
jupyter <br>
keras <br>
numpy <br>
matplotlib <br>
 <br>
When interacting with our web app, the URL should direct you to a homepage that includes a form where you can input an image. When you upload and submit the image, your original image will be returned along with each of the styles that we have currently in our Styles folder. We included our research, and the research of those who created this model, and an about me page so you can get to know the team members. We have tested the local app in Postman and confirmed that the web app works by distributing the app to several test users.  <br>
 <br>
<h4>Team Members: </h4><br>
Claudia Ibarra - Front End <br>
Erin Bentley - Project Manager / Tester <br>
Sana Khan - Back End <br>

<h4>License <br></h4>
TensorFlow is an open source platform for machine learning. It has a comprehensive, flexible ecosystem of tools, libraries and community resources that lets researchers push the state-of-the-art in ML and developers easily build and deploy ML powered applications. It is used for both research and production at Google.‍  TensorFlow was developed by the Google Brain team for internal Google use. <br>

Licensed under the Apache License, Version 2.0 (the "License"); <br>
you may not use this file except in compliance with the License. <br>
You may obtain a copy of the License at <br>
 <br>
    http://www.apache.org/licenses/LICENSE-2.0 <br>
 <br>
Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License. <br>
 <h4><br>
Acknowledgments </h4><br>
Manuel Lara - guidance and instruction through this project <br>
Google Brain - created the model and documentation that was easily accessed on TensorFlow  <br>
 <br>
