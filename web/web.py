from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import os
import main



app = Flask(__name__)

UPLOAD_FOLDER = './'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        print(request.files)
        f = request.files['image']
        f.save(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(f.filename)))
        data = main.parser(main.extract(f.filename))
        print(data)
        stat = main.Statistics(data)
        stat.stat_print()
        print("Mean:-",stat.mean)
        print("Median:-",stat.median)
        print("Mode:-",stat.mode)
        print("Range:-",stat.range)
        print("Variance:-",stat.variance)
        print("Standard Deviation:-",stat.std_dev)
        print("Quartile:-",stat.quartiles)
        print("Skewness:-",stat.skewness)
        print("Kurtosis:-",stat.kurtosis)
        return render_template('index.html',vars={'data':stat.data,'mean':stat.mean,'median':stat.median,'mode':stat.mode,'range':stat.range,'variance':stat.variance,'std_dev':stat.std_dev,'quartiles':stat.quartiles,'skewness':stat.skewness,'kurtosis':stat.kurtosis})
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0', port=5000)

