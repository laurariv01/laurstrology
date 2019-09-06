'''
ROUTES.py
'''
from flask import render_template, redirect
from astrologyapp import app
from astrologyapp.forms import RequestForm, SignUpForm,LoginForm
from astrologyapp.models import db, Request 

#flask login import for login
from flask_login import login_user, current_user, logout_user, login_required

#importing database model
from astrologyapp.models import db, User, check_password_hash

@app.route("/")
def hello_world():
    return render_template("home.html")


@app.route("/about_my_sign")
def about_my_sign():
    return render_template("about.html")


@app.route("/compatability")
def compatability():
    return render_template("compatability.html")



@app.route("/request", methods=["GET", "POST"])
def request():
    form=RequestForm()
    email=form.email.data

    db.session.commit()
    return render_template("request.html", form=form)




@app.route("/learntarot")
def learn_tarot():
    return render_template("learntarot.html")

@app.route("/learnastro")
def learn_astro():
    return render_template("learnastro.html")

@app.route("/calculator", methods=["POST","GET"])
def calculator():
    return render_template("calculator.html")


@app.route("/aries")
def aries():
    return render_template("aries.html")

@app.route("/sagittarius")
def sagittarius():
    return render_template("sagittarius.html")

@app.route("/leo")
def leo():
    return render_template("leo.html")

@app.route("/cancer")
def cancer():
    return render_template("cancer.html")

@app.route("/pisces")
def pisces():
    return render_template("pisces.html")

@app.route("/scorpio")
def scorpio():
    return render_template("scorpio.html")

@app.route("/aquarius")
def aquarius():
    return render_template("aquarius.html")

@app.route("/gemini")
def gemini():
    return render_template("gemini.html")

@app.route("/libra")
def libra():
    return render_template("libra.html")

@app.route("/taurus")
def taurus():
    return render_template("taurus.html")

@app.route("/virgo")
def virgo():
    return render_template("virgo.html")

@app.route("/capricorn")
def capricorn():
    return render_template("capricorn.html")




@app.route("/ariescompat")
def ariescompat():
    return render_template("ariescompat.html")

@app.route("/sagittariuscompat")
def sagittariuscompat():
    return render_template("sagittariuscompat.html")

@app.route("/leocompat")
def leocompat():
    return render_template("leocompat.html")

@app.route("/cancercompat")
def cancercompat():
    return render_template("cancercompat.html")

@app.route("/piscescompat")
def piscescompat():
    return render_template("piscescompat.html")

@app.route("/scorpiocompat")
def scorpiocompat():
    return render_template("scorpiocompat.html")

@app.route("/aquariuscompat")
def aquariuscompat():
    return render_template("aquariuscompat.html")

@app.route("/geminicompat")
def geminicompat():
    return render_template("geminicompat.html")

@app.route("/libracompat")
def libracompat():
    return render_template("libracompat.html")

@app.route("/tauruscompat")
def tauruscompat():
    return render_template("tauruscompat.html")

@app.route("/virgocompat")
def virgocompat():
    return render_template("virgocompat.html")

@app.route("/capricorncompat")
def capricorncompat():
    return render_template("capricorncompat.html")



@app.route("/register", methods=["GET","POST"])
def createUser():
    form = SignUpForm()
    if form.validate_on_submit():
        print("The username is {}".format(form.username.data))
        user=User(form.username.data, form.email.data, form.password.data)
        db.session.add(user)
        db.session.commit()       
        return redirect(url_for("login"))
    else:
        print("Form not valid")
    return render_template("register.html", form=form)

@app.route("/login", methods=["GET","POST"])
def login ():
        form = LoginForm()
        user_username= form.username.data
        password= form.password.data
        user = User.query.filter(User.username == user_username).first()
        if user and check_password_hash(user.password, password):
            login_user(user)
            print(current_user.username)
            return redirect(url_for('hello_world'))
        print(form.username.data, form.password.data)
        return render_template("login.html", form=form)
     
