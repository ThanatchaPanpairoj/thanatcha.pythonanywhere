
# A very simple Flask Hello World app for you to get started with...

from flask import Flask, render_template, redirect, request, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["DEBUG"] = True
SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://{username}:{password}@{hostname}/{databasename}".format(
    username="Thanatcha",
    password="mysqlmysql",
    hostname="Thanatcha.mysql.pythonanywhere-services.com",
    databasename="Thanatcha$comments",
)
app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
app.config["SQLALCHEMY_POOL_RECYCLE"] = 299

db = SQLAlchemy(app)

class Comment(db.Model):
    __tablename__ = "comments"
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(4096))

@app.route('/', methods = ['GET', 'POST'])
def index():
    if request.method == "GET":
        return render_template("main_page.html", comments=Comment.query.all())

    comment = Comment(content=request.form["contents"][:50])
    db.session.add(comment)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/links', methods = ['GET'])
def link_index():
    if request.method == 'GET':
        return render_template("link_page.html", links={"CalCental" : "1eo.me"})
