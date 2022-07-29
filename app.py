from flask import Flask, render_template


app = Flask(__name__)

app.config['ENV'] = 'development'
app.config['DEBUG'] = True
app.config['TESTING'] = True

@app.route('/')
def index():
    return render_template('main.html')





if __name__ == '__main__': app.run(debug=True)