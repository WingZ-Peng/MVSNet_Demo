from flask import Flask, render_template, request, send_from_directory
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    # Get the uploaded file
    file = request.files['image']
    filename = file.filename

    # Generate the result filename
    result_filename = filename.replace('.jpg', '-result.jpg')
    result_filepath = os.path.join('data', result_filename)

    if os.path.exists(result_filepath):
        # Return the result image filename to be displayed in the web page
        return render_template('result.html', filename=result_filename)

    # If the result file doesn't exist, display an error message
    error_message = f"Fly is flying!"
    return render_template('index.html', error_message=error_message)

@app.route('/data/<path:filename>')
def download_file(filename):
    # Serve the image file
    return send_from_directory('data', filename)

if __name__ == '__main__':
    app.run(debug=True)
