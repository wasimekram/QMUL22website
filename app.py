from flask import Flask, render_template, request
#from sqlalchemy import false, true
from scripts.twolink import twolink

app = Flask(__name__, static_url_path='/static')

app.config['ENV'] = 'development'
app.config['DEBUG'] = True
app.config['TESTING'] = True

@app.route('/', methods = ['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('main.html')
    if request.method == 'POST':
        armfirst = request.form.get('armfirst')
        data = request.form.to_dict()
        print(data)
        try:
            twolink(data)
            return render_template('main.html', test=data)
        except Exception as e: 
            print(e)
            return render_template('main.html', test=data, e=e)
       






if __name__ == '__main__': app.run(debug=True)