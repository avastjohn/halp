from flask import Flask, render_template, redirect, request, g, session, url_for, flash
from model import User, Post
from flask.ext.login import LoginManager, login_required, login_user, current_user, logout_user
from flaskext.markdown import Markdown
import config
import forms
import model

app = Flask(__name__)
app.config.from_object(config)

# Stuff to make login easier
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

@app.route("/login", methods=["POST"])
def authenticate():
    form = forms.LoginForm(request.form)
    error = None
    if not form.validate(): 
        return render_template("index.html", error="Invalid username or password")

    email = form.email.data
    password = form.password.data

    user = User.query.filter_by(email=email).first()
    if not user or not user.authenticate(password):
        return render_template("index.html", error="Incorrect email or password")

# Adding markdown capability to the app
Markdown(app)

@app.route("/register")
def registration():
    return render_template("register.html")
############################################################    REGISTER    ######
@app.route("/register", methods=["POST"])
def register():
    error = None
    email = request.form.get("email")
    password = request.form.get("password")
    role = request.form.get("role")
    if email and password and role:
        user = model.register(email, password, int(role))
        # user = User.query.filter_by(email=email).first()
        print "****************************user", user.is_active()
        login_user(user)

        
        return redirect(url_for("index"))
    else:
        return render_template("registration.html", error="** All Fields Required **")

@app.route("/")
def index():
    posts = Post.query.all()
    return render_template("index.html", posts=posts)


@app.route("/post/new")
@login_required
def new_post():
    return render_template("new_post.html")

@app.route("/post/new", methods=["POST"])
@login_required
############################################################    POST    ######
def create_post():
    form = forms.NewPostForm(request.form)
    if not form.validate():
        flash("Error, all fields are required")
        return render_template("new_post.html")

    post = Post(title=form.title.data, location=form.location.data, urgency=form.urgency.data)
    current_user.posts.append(post) 
    model.session.commit()
    model.session.refresh(post)

    return redirect(url_for("index"))

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/logout")
def logout():
    session.clear()
    logout_user()
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)
