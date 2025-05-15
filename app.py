from flask import Flask, render_template, request
import os
from classify import classify_image, load_image
import cv2
import shutil  # to move files

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Make sure target folders exist
for folder in ['black', 'transparent', 'colorful']:
    os.makedirs(folder, exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'image' not in request.files:
        return render_template('index.html', result="No image found.")
    
    file = request.files['image']
    filename = file.filename
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(filepath)

    # Load image and classify
    image = load_image(filepath)
    result = classify_image(image)

    # Decide destination folder based on result
    if "Black" in result:
        dest_folder = 'black'
    elif "Transparent" in result:
        dest_folder = 'transparent'
    else:
        dest_folder = 'colorful'

    # Move the file
    dest_path = os.path.join(dest_folder, filename)
    shutil.move(filepath, dest_path)

    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
