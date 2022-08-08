from flask import Flask, render_template, redirect, url_for, request, flash
from flask_login import current_user, login_required, login_user, logout_user, UserMixin
from flask_login import LoginManager
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///loandata.db'

app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://evgen@myvenox:Lutik115@myvenox.mysql.database.azure.com:3306/venox1"
app.config['SECRET_KEY'] = "123"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)  # primary keys are required by SQLAlchemy
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(200))
    name = db.Column(db.String(30))
    loan_requests = db.relationship('Loan', backref='author', lazy=True)


class Loan(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    loan = db.Column(db.Text, nullable=False)
    payday = db.Column(db.Text, nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)


class Userdata(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    lastname = db.Column(db.String(30))
    phone = db.Column(db.Integer, nullable=True)
    address = db.Column(db.String(30))
    datebirth = db.Column(db.String(30))


db.create_all()

login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    # since the user_id is just the primary key of our user table, use it in the query for the user
    return User.query.get(int(user_id))


# display all teams
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/profile')
@login_required
def profile():
    return render_template('profile.html', name=current_user.name)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route("/all")
@login_required
def user_loan_request():
    user = User.query.filter_by(email=current_user.email).first_or_404()
    loan_requests = user.loan_requests
    return render_template('all_requests.html', loan_requests=loan_requests, user=user)



@app.route("/new")
@login_required
def new_loan_request():
    return render_template('make_request.html')


@app.route("/new", methods=['POST'])
@login_required
def new_loan_request_post():
    loan = request.form.get('loan')
    payday = request.form.get('payday')
    print(loan, payday)
    loan_request = Loan(loan=loan, payday=payday, author=current_user)
    db.session.add(loan_request)
    db.session.commit()
    flash('Your loan request has been added! We will contact you shortly!')
    return redirect(url_for('user_loan_request'))


@app.route("/request/<int:loan_request_id>/update", methods=['GET', 'POST'])
@login_required
def update_request(loan_request_id):
    loan_request = Loan.query.get_or_404(loan_request_id)
    if request.method == "POST":
        loan_request.loan = request.form['loan']
        loan_request.payday = request.form['payday']
        db.session.commit()
        flash('Your loan request has been updated!')
        return redirect(url_for('user_loan_request'))

    return render_template('update_request.html', loan_request=loan_request)



@app.route("/request/<int:loan_request_id>/delete", methods=['GET', 'POST'])
@login_required
def delete_request(loan_request_id):
    loan_request = Loan.query.get_or_404(loan_request_id)
    db.session.delete(loan_request)
    db.session.commit()
    flash('Your loan request has been deleted!')
    return redirect(url_for('user_loan_request'))


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/login', methods=['POST'])
def login_post():
    email = request.form.get('email')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False

    user = User.query.filter_by(email=email).first()

    # check if user actually exists
    # take the user supplied password, hash it, and compare it to the hashed password in database
    if not user or not check_password_hash(user.password, password):
        flash('Please check your login details and try again.')
        return redirect(url_for('login'))  # if user doesn't exist or password is wrong, reload the page

    # if the above check passes, then we know the user has the right credentials
    login_user(user, remember=remember)
    return redirect(url_for('profile'))


@app.route('/signup')
def signup():
    return render_template('signup.html')


@app.route('/signup', methods=['POST'])
def signup_post():
    email = request.form.get('email')
    name = request.form.get('name')
    password = request.form.get('password')
    lastname = request.form.get('lastname')
    phone = request.form.get('phone')
    datebirth = request.form.get('datebirth')
    address = request.form.get('address')

    # if this returns a user, then the email already exists in database
    user = User.query.filter_by(email=email).first()
    print(user)

    if user:  # if a user is found, we want to redirect back to signup page so user can try again
        flash('Email address already exists')
        return redirect(url_for('signup'))

    # create new user with the form data. Hash the password so plaintext version isn't saved.
    new_user = User(email=email, name=name, password=generate_password_hash(password, method="sha256"))
    new_acc = Userdata(lastname=lastname, phone=phone, datebirth=datebirth, address=address)
    # add the new user to the database
    db.session.add(new_user)
    db.session.add(new_acc)
    db.session.commit()

    return redirect(url_for('login'))


@app.route('/logout')
@login_required
def logout():
    logout_user()

    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(port=5000, debug=True, host='0.0.0.0')
