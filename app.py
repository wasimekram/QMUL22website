from flask import Flask, render_template, request
from scripts.twolink import twolink as twolink
from scripts.twolink2 import twolink as twolink2
import glob
import os
import scripts.pyplot as pyplotresult

app = Flask(__name__, static_url_path='/static')

app.config['ENV'] = 'development'
app.config['DEBUG'] = True
app.config['TESTING'] = True


@app.route('/', methods = ['GET', 'POST'])
def index():
    #code for carousel    
    script_dir = os.path.dirname(__file__)
    results_dir = os.path.join(script_dir + os.sep + "static" + os.sep + "images" + os.sep + "results" + os.sep)
    imgs = glob.glob(results_dir + "/*.png")

    if request.method == 'GET':
        return render_template('main.html', imgs=imgs, graphJSON=pyplotresult.graphJSON(), graphJSON1=pyplotresult.graphJSON1())
    if request.method == 'POST':
        #armfirst = request.form.get('armfirst')
        data = request.form.to_dict()
        print(data)
        try:
            twolink(data)
            return render_template('main.html', test=data, imgs=imgs)
        except Exception as e: 
            print(e)
            twolink({'armfirst': 0.5, 'armsecond': 1.0, 'divisions': 2, 'anglestart1':0, 'angleend1':45, 'anglestart2':0, 'angleend2':45})
            return render_template('main.html', test=data, imgs=imgs, e=e)
       
@app.route('/faq', methods = ['GET', 'POST'])
def faq():
    if request.method == 'GET':
        return render_template('faq/faq.html')

if __name__ == '__main__': app.run(debug=True)
