# --- Tensorflow libraries
import os
import tensorflow as tf
import tensorflow_hub as hub
# --- Numpy and Pillow libraries
import numpy as np
import PIL.Image

STYLIZED_DIR = os.path.join('static', 'images', 'final')
hub_module = hub.load('https://styletransfer-196116601428-us-east-2.s3.us-east-2.amazonaws.com/1.tar.gz')
# hub_module = hub.load('1.tar.gz')

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

def predict(content_path, style_path):
    filename = os.path.split(content_path)[-1]
    style_filename = os.path.split(style_path)[-1].split(".")[0]
    filename = style_filename + "-" + filename
    stylized_picture = os.path.join(STYLIZED_DIR, filename)
   
    print(stylized_picture)
    
    content_image = load_img(content_path)
    style_image = load_img(style_path)
    stylized_image = hub_module(tf.constant(content_image), tf.constant(style_image))[0]
    image = tensor_to_image(stylized_image)
    image.save(stylized_picture)
    return stylized_picture

