
import os 
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'
from flask import Flask, render_template, jsonify, request
# --- Tensorflow libraries
import tensorflow as tf
import tensorflow_hub as hub
# --- Numpy and Pillow libraries
import numpy as np
import PIL.Image

UPLOAD_FOLDER = 'UPLOAD_FOLDER'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


hub_module = hub.load('1')
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



@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        print(request)
        if request.files.get('file'):
            # read the file
            file = request.files['file']
            # read the filename
            filename = file.filename
            # Save the file to the uploads folder
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], 'filename'))
            return "Image Saved!"
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <p><input type=file name=file>
         <input type=submit value=Upload>
    </form>
    '''


@app.route("/style-image")
def style():
    content_path = 'UPLOAD_FOLDER/filename'
    style_path = 'static/kandinsky5.png'
    content_image = load_img(content_path)
    style_image = load_img(style_path)
    stylized_image = hub_module(tf.constant(content_image), tf.constant(style_image))[0]
    image = tensor_to_image(stylized_image)
    image.save("static/styled-image.jpg")
    image_dog = os.path.join('static', 'styled-image.jpg')
    return render_template("index.html",image_dog=image_dog)


# @app.route("/new-route")
# def upload_files():
#     if request.method == 'POST':
#         print(request)
#         if request.files.get('file'):
#             # read the file
#             file = request.files['file']
#             # read the filename
#             filename = file.filename
#             # Save the file to the uploads folder
#             file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
#             return "Image Saved!"
#     return '''
#     <!doctype html>
#     <title>Upload new File</title>
#     <h1>Upload new File</h1>
#     <form method=post enctype=multipart/form-data>
#       <p><input type=file name=file>
#          <input type=submit value=Upload>
#     </form>
#     '''
#     content_path = 'UPLOAD_FOLDER/coco.1.jpg'
#     style_path = 'static/kandinsky5.png'
#     content_image = load_img(content_path)
#     style_image = load_img(style_path)
#     stylized_image = hub_module(tf.constant(content_image), tf.constant(style_image))[0]
#     image = tensor_to_image(stylized_image)
#     image.save("static/styled-image.jpg")
#     image_dog = os.path.join('static', 'styled-image.jpg')
#     return render_template("index.html",image_dog=image_dog)



if __name__ == "__main__":
    app.run(debug = True, port=5001)