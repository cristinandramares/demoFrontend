from flask import Flask, render_template, request


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if request.method == 'POST':
  
        # Get the list of files from webpage
        files = request.files.getlist("file")
  
        # Iterate for each file in the files List, and Save them
        for file in files:
            file.save(file.filename)
        return "<h1>Files Uploaded Successfully.!</h1>"

if __name__ == '__main__':
    app.run(debug=True)