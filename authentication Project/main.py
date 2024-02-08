from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret-key-goes-here'


# CREATE DATABASE
class Base(DeclarativeBase):
    pass
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)

login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id) :
    return db.session.get(User,user_id)




# CREATE TABLE IN DB
class User(UserMixin,db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    email: Mapped[str] = mapped_column(String(100), unique=True)
    password: Mapped[str] = mapped_column(String(100))
    name: Mapped[str] = mapped_column(String(1000))
 
with app.app_context():
    db.create_all()



@app.route('/',methods=["GET"])
def home():
    return render_template("index.html",logged_in=current_user.is_authenticated)


@app.route('/register',methods=['GET','POST'])
def register():
    if request.method == "POST" :
        usernane = request.form['name']
        email_of_user = request.form['email']
        result = db.session.execute(db.select(User).where(User.email == email_of_user))
        user = result.scalar()
        if user :
            flash("You've already signed up with that email, log in instead!")
            return redirect(url_for('login'))
        passwd = request.form['password']
        passwd = generate_password_hash(passwd,'pbkdf2:sha256',salt_length=8)
        newUser = User(name=usernane,email=email_of_user,password=passwd)
        db.session.add(newUser)
        db.session.commit()
        login_user(newUser)
        return redirect(url_for('secrets',name=usernane))        

    return render_template("register.html",logged_in=current_user.is_authenticated)


@app.route('/login',methods=["GET","POST"])
def login():
    if request.method == "POST" :
        email = request.form['email']
        password = request.form['password']

        result = db.session.execute(db.select(User).where(User.email == email))
        user = result.scalar()
        # Email doesn't exist or password incorrect.
        if not user:
            flash("That email does not exist, please try again.")
            return redirect(url_for('login'))
        elif not check_password_hash(user.password, password):
            flash('Password incorrect, please try again.')
            return redirect(url_for('login'))
        else:
            login_user(user)
            return redirect(url_for('secrets'))

    return render_template("login.html",logged_in=current_user.is_authenticated)


@app.route('/secrets')
@login_required
def secrets():
    if current_user.is_authenticated:
        return render_template("secrets.html",name_of_user = current_user.name,logged_in=current_user.is_authenticated)
    else:
        return redirect(url_for('login'))


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route('/download')
@login_required
def download():
    file_path = 'static/files/cheat_sheet.pdf'
    return send_from_directory(directory='static/files', filename='cheat_sheet.pdf', as_attachment=True)
    


if __name__ == "__main__":
    app.run(debug=True)
