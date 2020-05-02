
import os 
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'
from flask import Flask, render_template, jsonify, request
import image_process


UPLOAD_FOLDER = os.path.join('static', 'images', 'uploads')
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

STYLES_DIR = os.path.join('static', 'images', 'styles')
STYLES_PATHS = [
    os.path.join(STYLES_DIR, 'kandinsky5.png'), 
    os.path.join(STYLES_DIR, 'kandinsky5.png')
]

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER



@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        print(request.files)
        if request.files.get('file'):
            # read the file
            file = request.files['file']
            # read the filename
            filename = file.filename
            # Save the file to the uploads folder
            content_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(content_path)
            # image_lists = []
            # for style_path in STYLES_PATHS:
            #     stylized_picture = image_process.predict(content_path, style_path)
            #     image_lists.append(stylized_picture)
            image_lists = [
                {
                    "content": content_path,
                    "stylized": image_process.predict(content_path, style_path),
                    "style": style_path
                }
                for style_path in STYLES_PATHS
            ]
            return render_template("index.html",images = image_lists)
    # return render_template("form.html")
    return render_template("index.html", images=[])
    
# @app.route('/test')
# def test():
#     image_dog = "static/puppies1.JPG"
#     return render_template("index.html",image_dog=image_dog)




if __name__ == "__main__":
    app.run(debug = True, port=5001)