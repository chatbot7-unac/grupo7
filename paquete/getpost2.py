import os
from flask import flash
from flask import Flask, request, redirect, url_for
from werkzeug.utils import secure_filename
from conjf import problem1


UPLOAD_FOLDER = '/home/casey/Escritorio/bd/'
ALLOWED_EXTENSIONS = set([ 'wav','mp3'])



app = Flask(__name__)
app.secret_key = "super secret key"  #key
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])	
def upload_file():
    
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            flash("file{}saved".format(file.filename))
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            
            #return redirect('/')#url_for('uploaded_file',filename=filename))
            
    problem1("/home/casey/Escritorio/bd/",0.75,30000)            
    return ''' nel '''
        


        
    	


if __name__=='__main__':
    app.run (host = '0.0.0.0', debug = True)
    #app.run (host = '0.0.0.0', debug = True, port = 3134)