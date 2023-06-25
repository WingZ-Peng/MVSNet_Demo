from flask import Flask, render_template, request, send_from_directory
import os

app = Flask(__name__)

DATA_FOLDER = 'data'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'image' not in request.files:
        return render_template('index.html', error_message='No image file selected')
    
    image_file = request.files['image']
    if image_file.filename == '':
        return render_template('index.html', error_message='No image file selected')

    # Remove file extension from image filename
    image_name = os.path.splitext(image_file.filename)[0]
    
    # Find corresponding image and video filenames
    image_result_filename = f"{image_name}-result.jpg"
    video_result_filename = f"{image_name}-result.mp4"
    
    # Check if the image and video files exist in the data folder
    image_exists = os.path.isfile(os.path.join(DATA_FOLDER, image_result_filename))
    video_exists = os.path.isfile(os.path.join(DATA_FOLDER, video_result_filename))
    
    if not image_exists or not video_exists:
        return render_template('index.html', error_message='No matching image or video found')
    
    return render_template('result.html', image_filename=image_result_filename, video_filename=video_result_filename)

@app.route('/data/<filename>')
def download_file(filename):
    return send_from_directory(DATA_FOLDER, filename)

if __name__ == '__main__':
    app.run()
