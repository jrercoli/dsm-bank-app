from flask import Flask
import os

IMAGE_FOLDER = os.path.join('static', 'images')

app = Flask(__name__)

# store image folder directory to flask config dictionary
app.config['UPLOAD_IMAGE'] = IMAGE_FOLDER

from application import routes

if __name__ == '__main__':
    app.run()
