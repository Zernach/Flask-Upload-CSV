from flask import Flask, render_template, request, redirect, url_for
import pandas as pd
import os

app = Flask(__name__)

# Upload folder
UPLOAD_FOLDER = 'static/files'
app.config['UPLOAD_FOLDER'] =  UPLOAD_FOLDER


# Root URL - user uploads file
@app.route('/')
def index_route():
     # Set The upload HTML template '\templates\index.html'
    return render_template('index.html')


# Catches uploaded file from user
@app.route("/uploader", methods=['POST'])
def uploadFiles():
      # get the uploaded file
      uploaded_file = request.files['file']
      if uploaded_file.filename != '':
           file_path = os.path.join(app.config['UPLOAD_FOLDER'], uploaded_file.filename)
          # set the file path
           uploaded_file.save(file_path)
          # save the file
      return redirect(url_for('index_route'))

# Run app
if (__name__ == "__main__"):
     app.run(debug=True) # set to false when deploying to live production website environment