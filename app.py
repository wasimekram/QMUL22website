from flask import Flask, render_template, request
from sqlalchemy import false, true
from scripts.twolink import twolink

app = Flask(__name__, static_url_path='/static')

app.config['ENV'] = 'development'
app.config['DEBUG'] = True
app.config['TESTING'] = True

@app.route('/', methods = ['GET', 'POST'])
def index():
    if request.method == 'GET':
        print(request.args)
        celsius = request.args.get("exampleInputEmail2", "")
        if celsius:
            print(celsius)
            fahrenheit = twolink(celsius)
            return render_template('main.html')

        else:
            return render_template('main.html')
    if request.method == 'POST':
        exampleInputEmail2 = request.form.get('exampleInputEmail2')
        data = request.args
        print(data)
        print(request.form.get('exampleInputEmail2'))
        twolink(request.form.get('exampleInputEmail2'))
        return render_template('main.html', test=exampleInputEmail2)






if __name__ == '__main__': app.run(debug=True)