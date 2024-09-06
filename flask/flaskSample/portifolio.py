from flask import Flask,request,redirect,render_template,url_for

app = Flask(__name__)

@app.route('/')
def Profile():
     return render_template('portifolio/profile.html')

@app.route('/edu')
def Edu():
     return render_template('portifolio/edu.html')

@app.route('/exp')
def Exp():
     return render_template('portifolio/exp.html')

@app.route('/project')
def Project():
     return render_template('portifolio/project.html')

@app.route('/personalinfo')
def Personalinfo():
     return render_template('portifolio/personalinfo.html')


app.run()