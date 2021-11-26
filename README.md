* `export FLASK_DEBUG=1 `
* `export FLASK_APP= app.py` => to set the man file which we will run .
* To render a template we need to import `render_template` from flask
* `return render_template('home.html')`
* `pip install flask-sqlalchemy `
* `from flask_sqlalchemy import SQLAlchemy`
* `db=SQLAlchemy(app)`
* URI -> uniform Resource identifier : file just identify a database.
* `model.query.all()` -> get all table 
* `model.query.filter_by(name='hamza').first()`


# forms 
* `pip install flask-wtf wtforms `
* `pip install email_validator `
* to secure password we use `pip install flask_bcrypt `
* `from flask_bcrypt import Bcrypt ` 
* `bcrypt=Bcrypt(app)`
* `pip install flask_login `
* `from flask_login import LoginManager`
* `login_manager=LoginManager(app)`

