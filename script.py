from flask import Flask, render_template, request, url_for, redirect
import jinja2
from checkmypass import main, showcase, gottem


app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')


def stored(data):
    a = data
    return a

@app.route('/<string:i>')
def reee():
    return redirect('index.html')


@app.route('/search_up', methods = ['GET', 'POST'],)
def search_up():
    if request.method  == 'POST':
        data = request.form.to_dict()
        password = data['password']
        strpass = str(password)
        if strpass == '':
            return redirect('index.html')
        else:
            a = stored(strpass)
            matches = main(a)
            hashes_obj = gottem(a)
            print(hashes_obj)
            return render_template('result.html' , hashpass = matches, hashs=hashes_obj)
    else:
        return 'something went wrong'