from flask import Flask,render_template,request,redirect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import validators
import os
import string,random
#Created by Dhruv Dixit
#Do not copy without permission
#Linkedin: https://www.linkedin.com/in/dhruv-dixit/
app=Flask(__name__)

basedir=os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///'+os.path.join(basedir,'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db=SQLAlchemy(app)
Migrate(app,db)

class URL(db.Model):
    __tablename__='urls'
    id=db.Column(db.Integer,primary_key=True)
    full_url=db.Column(db.Text)
    shorten_url=db.Column(db.Text)
    
    def __init__(self,full_url,shorten_url):
        self.full_url=full_url
        self.shorten_url=shorten_url
  
@app.route('/', methods=['GET','POST'])
def home():
    if request.method=='POST':
        url=request.form['in']
        curr_url = URL.query.filter_by(full_url=url).first()
        if curr_url:
            return render_template('home.html', err=0,furl=curr_url.shorten_url)
        else:
            if validators.url(url):
                t=string.ascii_letters
                while True:
                    finalurl=random.choices(t,k=5)
                    finalurl = ''.join(finalurl)
                    short_url = URL.query.filter_by(shorten_url=finalurl).first()
                    if not short_url:
                        obj=URL(url,finalurl)
                        db.session.add(obj)
                        db.session.commit()
                        return render_template('home.html',err=0,furl=finalurl)
            else:
                return render_template('home.html',err=1)
    return render_template("home.html")

@app.route('/history',methods=['GET','POST'])
def history():
    detail=URL.query.all()
    return render_template('history.html',content=detail)

@app.route('/<finalurl>')
def redirection(finalurl):
    fullurl = URL.query.filter_by(shorten_url=finalurl).first()
    if fullurl:
        return redirect(fullurl.full_url)
    else:
        return f"<h1>Url doesn't Exist</h1>"

if __name__=="__main__":
    app.run(debug=True)