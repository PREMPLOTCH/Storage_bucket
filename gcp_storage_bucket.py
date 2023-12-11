from flask import Flask, render_template, request, redirect, url_for
from google.cloud import storage
import os

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = 'E:/plotch/workspace/Background-Jobs/gcp_upload/nodebox-392708-b171c935bcba.json'
bucket_name = "noderetail-analytics"
destination_file_name = 'testing/'
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return redirect(request.url)

    file = request.files['file']

    if file.filename == '':
        return redirect(request.url)
    
    destination_file = destination_file_name + file.filename


    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination_file)

    blob.upload_from_file(file)

    return "File '{}' successfully uploaded to '{}' in bucket '{}'.".format(file.filename, destination_file, bucket_name)

if __name__ == '__main__':
    app.run(debug=True)
