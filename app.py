import os
from sizer import file_size
from files_handler import remove_file, is_file_exists
from bottle import Bottle, request, run, template, route, post

app = Bottle()
upload_dir = './myfiles'


@route('/')
def index():
    return template('index')


@post('/upload')
def upload():
        newfile = request.files.get('newfile')
        if newfile.content_type != 'image/jpeg' and \
                        newfile.content_type != 'image/png' and \
                        newfile.content_type != 'image/gif':
            return "Only image myfiles allowed"
        save_path = os.path.join(upload_dir, newfile.filename)
        if is_file_exists(save_path):
            return '<h1>File already exists</h1><a href="http://localhost:8080">Back Home</a><br>'
        newfile.save(save_path)
        if file_size(save_path) > 2:
            remove_file(save_path)
            return '<h1>File is too big</h1><a href="http://localhost:8080">Back Home</a><br>'
        return template('uploaded', filename=newfile.filename)


if __name__ == "__main__":
    run(debug=True, reloadable=True)
