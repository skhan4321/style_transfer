
import os 
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'
from flask import Flask, render_template, jsonify
# --- Tensorflow libraries
import tensorflow as tf
import tensorflow_hub as hub
# --- Numpy and Pillow libraries
import numpy as np
import PIL.Image
app = Flask(__name__)
# --- style functions
def tensor_to_image(tensor):
    tensor = tensor*255
    tensor = np.array(tensor, dtype=np.uint8)
    if np.ndim(tensor)>3:
        assert tensor.shape[0] == 1
        tensor = tensor[0]
    return PIL.Image.fromarray(tensor)
def load_img(path_to_img):
    max_dim = 512
    img = tf.io.read_file(path_to_img)
    img = tf.image.decode_image(img, channels=3)
    img = tf.image.convert_image_dtype(img, tf.float32)
    shape = tf.cast(tf.shape(img)[:-1], tf.float32)
    long_dim = max(shape)
    scale = max_dim / long_dim
    new_shape = tf.cast(shape * scale, tf.int32)
    img = tf.image.resize(img, new_shape)
    img = img[tf.newaxis, :]
    return img
hub_module = hub.load('1')
@app.route("/")
def home():
    return "Hello World"
@app.route("/style-image")
def style():
    content_path = 'YellowLabradorLooking_new.jpg'
    style_path = 'kandinsky5.jpg'
    content_image = load_img(content_path)
    style_image = load_img(style_path)
    stylized_image = hub_module(tf.constant(content_image), tf.constant(style_image))[0]
    image = tensor_to_image(stylized_image)
    image.save("styled-image.jpg")
    return "Done"
if __name__ == "__main__":
    app.run(debug = True, port=5001)

