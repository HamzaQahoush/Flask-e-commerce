from market import app, db
from flask import render_template, redirect, url_for, flash
from market.models import Item, User
from market.forms import RegisterForm, LoginForm
from flask_login import login_user


@app.route('/')
@app.route('/home')
def home_page():  # put application's code here
    return render_template('home.html', title="home")


@app.route('/market')
def market_page():
    items = Item.query.all()
    return render_template('market.html', title='market', items=items)


@app.route('/register', methods=['GET', 'POST'])
def register_page():
    form = RegisterForm()
    if form.validate_on_submit():
        user_to_create = User(username=form.username.data, email_address=form.email_address.data,
                              password=form.password1.data)
        db.session.add(user_to_create)
        db.session.commit()
        flash('Congratulation , You are now registered user ')
        return redirect(url_for('market_page'))
    if form.errors:
        for err in form.errors:
            flash(f'There is an error with creating a user {err}', category='danger')

    return render_template('register.html', form=form, title='register')


@app.route('/login', methods=['GET', 'POST'])
def login_page():
    form = LoginForm()
    if form.validate_on_submit():
        attempted_user = User.query.filter_by(username=form.username.data).first()
        if attempted_user and attempted_user.check_password_login(attempted_password=form.password.data):
            login_user(attempted_user)
            flash(f' Success You are logged in as {attempted_user.username} ', category='success')
            return redirect(url_for('market_page'))
        else :
            flash('user name and password are not match please try again ', categoty='danger')
    return render_template('login.html', form=form)