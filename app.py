
from flask import Flask,render_template,request

app=Flask(__name__,template_folder="templates",static_folder="static")
global nme
global id

count=0
@app.route('/')

def index():
    return render_template('index.html')

@app.route('/t.html')
def t():
    return render_template('t.html')

@app.route('/newsample.html',methods=['GET','POST'])
def newsample():
    if request.method=='POST':
        nme=request.form['name']
        id=request.form['id']
        print(nme,id)
        return render_template('newsample.html')
    elif request.method=='GET':
        return render_template('newsample.html')

@app.route('/hmm.html')
def hmm():
    return render_template('hmm.html')

@app.route('/about.html')
def about():
    return render_template('about.html')

@app.route('/tafter.html')
def tafter():
    return render_template('tafter.html')

@app.errorhandler(404)
def invalid(e):
    return render_template('error.html')

if __name__=='__main__':
    app.run()
