import os
from sizer import file_size
from bottle import Bottle, request, response, redirect

app = Bottle()
upload_dir = './myfiles'

template = """<html>
<head><title>Home</title></head>
<body>
<h1>Upload a file</h1>
<form method='post' action='/upload' enctype='multipart/form-data'>
    <input type='file' name='newfile'>
    <input type='submit' value='Submit'>
</form>
</body>
</html>"""


@app.get('/')
def home():
    return template


@app.post('/upload')
def upload():
        newfile = request.files.get('newfile')
        if newfile.content_type != 'image/jpeg' and \
                        newfile.content_type != 'image/png' and \
                        newfile.content_type != 'image/gif':
            return "Only image files allowed"
        save_path = os.path.join(upload_dir, newfile.filename)
        newfile.save(save_path)
        # check if already exists
        if file_size(save_path) > 2:
            return '<h1>File is too big</h1>'
            #delete the created fie
        return redirect('/')


if __name__ == "__main__":
    app.run(debug=True, reloadable=True)
