import os
import re
from flask import Flask, request, render_template, url_for, redirect
from werkzeug.utils import secure_filename
UPLOAD_FOLDER="./data"

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route("/")
def fileFrontPage():
    return render_template('index.html')

@app.route("/handleUpload", methods=['POST'])


# For Uploading File
def handleFileUpload():
    if 'raw_data' in request.files:
        txt_file =request.files['raw_data']
        filename = secure_filename(txt_file.filename)
        txt_file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        print("*********",(os.path.join(app.config['UPLOAD_FOLDER'], filename)))
        reed_txt = open((os.path.join(app.config['UPLOAD_FOLDER'], filename)), 'r')



# For creating new Text File and it will save automatically in the project folder with Structured format
        with open('New.txt', 'w') as c7:
            for line in reed_txt:
                c7.write(line + '\n')
                print(line)



    return redirect(url_for('fileFrontPage'))

if __name__ == '__main__':
    app.run()
