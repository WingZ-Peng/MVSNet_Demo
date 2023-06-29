from flask import Flask, render_template, request, send_from_directory
import os

app = Flask(__name__)

UPLOAD_FOLDER = 'data'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def upload():
    if 'image' not in request.files:
        return render_template('index.html', error_message='No image file selected')
    
    image = request.files['image']
    image_name = image.filename
    if image_name == '':
        return render_template('index.html', error_message='No image file selected')

    # Save the uploaded image
    image.save(os.path.join(app.config['UPLOAD_FOLDER'], image_name))
    
    # Process the image name to find related images
    image_result_name = image_name.replace('.png', '-reconstruction.png')
    video_result_name = image_name.replace('.png', '-reconstruction.mp4')
    
    # Check if the related images exist
    image_result_path = os.path.join(app.config['UPLOAD_FOLDER'], image_result_name)
    video_result_path = os.path.join(app.config['UPLOAD_FOLDER'], video_result_name)
    
    if not os.path.exists(image_result_path) or not os.path.exists(video_result_path):
        return render_template('index.html', error_message='Fly is flying Weng Weng')
    
    return render_template('result.html', 
                           image_filename=image_name,
                           image_result_filename=image_result_name,
                           video_filename=video_result_name)

@app.route('/data/<path:filename>')
def download_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == '__main__':
    app.run()
