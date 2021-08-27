
from bottle import Bottle ,run

app=Bottle()

upload_path='./Download'
@app.route('/upload')
def upload():
    return template('upload')

@app.route('./upload',method='POST')
def do_upload():
    uploadfile=request.files.get('data')
    uploadfile.save(upload_path,overwrite=True)
    return u"上传成功，文件名为:%s,文件类型味：%s"%(uploadfile.filename,uploadfile.content_type)

run(app,host='0.0.0.0',port=8080,debug=True)
