import os

from flask import request, render_template, redirect, url_for, flash, session
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user
from config import app, db, login_manager
from models import Users, Tasks
from forms import RegisterForm
from flask_bootstrap import Bootstrap5

bootstrap = Bootstrap5(app)

# Connect to DB
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DB_URI')
db.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    return db.get_or_404(Users, user_id)


# Create the tables
with app.app_context():
    db.create_all()


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        password = generate_password_hash(form.password.data, 'pbkdf2')
        user = Users(name=name, email=email, password=password)
        db.session.add(user)
        db.session.commit()
        login_user(user)
        return redirect(url_for('home'))
    return render_template('register.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        email = request.form.get('email')
        pwd = request.form.get('password')
        if not email or not pwd:
            flash("Email and password is required")
        else:
            user = db.session.execute(db.select(Users).where(Users.email == email)).scalar()
            if check_password_hash(user.password, pwd):
                login_user(user)
                return redirect(url_for('home'))
            else:
                flash("Wrong Password or Email")
    return render_template('login.html')


@app.route('/', methods=['POST', 'GET'])
def home():
    if current_user.is_authenticated:
        tasks_to_display = db.session.execute(
            db.select(Tasks).where(Tasks.user_id == current_user.id)).scalars().all()
        return render_template('index.html', tasks=tasks_to_display)
    # else:
    #     print(anonym_user_tasks)
    #     render_template('index.html', tasks=anonym_user_tasks)
    return render_template('index.html')


@app.route('/add', methods=['POST', 'GET'])
def add():
    if request.method == 'POST':
        if not request.form.get('task'):
            flash('Please fill the task input')
        else:
            if current_user.is_authenticated:
                task = request.form.get('task')
                task_db = Tasks(task=task, user_id=current_user.id)
                db.session.add(task_db)
                db.session.commit()
                return redirect(url_for('home'))
            # else:
            #     task = request.form.get('task')
            #     print(task)
            #     anonym_user_tasks.append(task)
            #     return redirect(url_for('home'))
    # return render_template('index.html', task=anonym_user_tasks)


@app.route('/delete/<int:task_id>', methods=['GET', 'POST'])
def delete(task_id):
    task = db.get_or_404(Tasks, task_id)
    db.session.delete(task)
    db.session.commit()
    return redirect(url_for('home'))


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True)
