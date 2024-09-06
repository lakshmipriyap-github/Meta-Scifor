from flask import Flask,request,redirect,render_template,url_for

app = Flask(__name__)

@app.route('/success/<uname>')
def success(uname):
     return render_template('welcome.html',context = uname)
     # return 'welcome %s' %uname

@app.route('/login',methods=['POST','GET'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        return redirect(url_for('success',uname=username))
    else:
        username = request.args.get('username')
        return redirect(url_for('success', uname=username))

@app.route('/')
def IndexPage():
     return render_template('index.html')

app.run()