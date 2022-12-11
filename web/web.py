from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import os
import main
import re



app = Flask(__name__)

UPLOAD_FOLDER = './'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        print(request.files)
        f = request.files['image']
        typ = request.form['type']
        f.save(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(f.filename)))
        data = main.parser(main.extract(f.filename),int(typ))
        stat = main.Statistics(data[0],data[1])
        return render_template('index.html',stat=stat)
    data = main.parser(main.test())
    stat = main.Statistics(data[0],data[1])
    return render_template('index.html',stat=stat)

def cleaner(form):
    data=[]
    int_list=[]
    toggle=0
    risk=0
    for i in form.values():
        toggle = risk%2
        if toggle==0:
            data.append([i])
        else:
            data[-1].append(i)
        risk+=1
    if form['type']=='1':
         data[-1].pop(-1)
    print(data)
    for i in data[:-1]:
        split_list = [s.split(",") for s in i]
        flattened_list = [item for sublist in split_list for item in sublist]
        stripped_list = [s.strip("() ") for s in flattened_list]
        int_list.append([int(s) for s in stripped_list])
    return int_list,int(form['type'])



@app.route('/re', methods=['GET', 'POST'])
def re():
    if request.method == 'POST':
        tmp=cleaner(request.form)
        print(tmp)
        stat = main.Statistics(tmp[0],tmp[1])
        return render_template('index.html',stat=stat)
    data = main.parser(main.test())
    stat = main.Statistics(data)
    return render_template('index.html',stat=stat)


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0', port=5000)

