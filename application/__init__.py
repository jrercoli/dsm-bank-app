from flask import Flask
import os

IMAGE_FOLDER = os.path.join('static', 'images')

app = Flask(__name__)
app.config['UPLOAD_IMAGE'] = IMAGE_FOLDER

from application import routes

if __name__ == '__main__':
    app.run()
