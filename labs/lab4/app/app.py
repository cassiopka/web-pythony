from typing import Dict
from flask import Flask, render_template, request, session, redirect, url_for, flash
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from flask_sqlalchemy import SQLAlchemy
import re
from flask_migrate import Migrate
from flask_session import Session
import bcrypt

app = Flask(__name__)

app.config.from_object('config.Config')

db = SQLAlchemy(app)

migrate = Migrate(app, db)

login_manager = LoginManager()

login_manager.init_app(app)

login_manager.login_view = 'login'
login_manager.login_message = 'Для доступа необходимо пройти аутентификацию'
login_manager.login_message_category = 'warning'


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(150), unique=True, nullable=False)
    password_hash = db.Column(db.String(150), nullable=False)
    last_name = db.Column(db.String(150), nullable=True)
    first_name = db.Column(db.String(150), nullable=False)
    middle_name = db.Column(db.String(150), nullable=True)
    role_id = db.Column(db.Integer, db.ForeignKey('role.id'), nullable=True)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())

class Role(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    description = db.Column(db.String(150), nullable=True)
    users = db.relationship('User', backref='role', lazy=True)

def password_validation(password: str) -> str:
    re1 = re.compile(r'''^[-A-ZА-Яa-zа-я\d~!?@#$%^&*_+()\[\]{}></\\|"'.,:;]{8,}$''')
    re2 = re.compile(r'''^[-A-ZА-Яa-zа-я\d~!?@#$%^&*_+()\[\]{}></\\|"'.,:;]{,128}$''')
    re3 = re.compile(r'''^(?=.*?[a-zа-я])(?=.*?[A-ZА-Я]).*$''')
    re4 = re.compile(r'''^(?=.*?[0-9]).*$''')
    re6 = re.compile(r'''^(?=.*?[-~!?@#$%^&*_+()\[\]{}><\/\\|"'.,:;]{0,}).*$''')
    error = []
    if not re1.match(password):
        error.append("Пароль должен быть не менее 8 символов")
    if not re2.match(password):
        error.append("Пароль должен быть не более 128 символов")
    if not re3.match(password):
        error.append("В пароле должны быть как минимум одна заглавная и одна строчная буква,а также только латинские или кириллические буквы")
    if not re4.match(password):
        error.append("В пароле должны быть как минимум одна цифра и только арабские цифры")
    if password.find(' ') != -1:
        error.append("Пароль должен быть без пробелов")
    if not re6.match(password):
        error.append(r'''Другие допустимые символы:~ ! ? @ # $ % ^ & * _ - + ( ) [ ] { } > < / \ | " ' . , : ;''')
    return "; ".join(error) + '.' if len(error) > 0 else ''

def login_validation(login: str) -> bool:
    reg = re.compile(r'^[0-9a-zA-Z]{5,}$')
    if reg.match(login):
        return True
    else:
        return False

def validate(login: str, password: str, last_name: str, first_name: str) -> Dict[str, str]:
    errors = {}
    error = password_validation(password)
    if len(error) != 0:
        errors['p_class'] = "is-invalid"
        errors['p_message_class'] = "invalid-feedback"
        errors['p_message'] = error
    if not login_validation(login):
        errors['l_class'] = "is-invalid"
        errors['l_message_class'] = "invalid-feedback"
        errors['l_message'] = "Логин должен состоять только из латинских букв и цифр и иметь длину не менее 5 символов"
    if len(login) == 0:
        errors['l_class'] = "is-invalid"
        errors['l_message_class'] = "invalid-feedback"
        errors['l_message'] = "Логин не должен быть пустым"
    if len(password) == 0:
        errors['p_class'] = "is-invalid"
        errors['p_message_class'] = "invalid-feedback"
        errors['p_message'] = "Пароль не должен быть пустым"
    if len(last_name) == 0:
        errors['ln_class'] = "is-invalid"
        errors['ln_message_class'] = "invalid-feedback"
        errors['ln_message'] = "Фамилия не должна быть пустой"
    if len(first_name) == 0:
        errors['fn_class'] = "is-invalid"
        errors['fn_message_class'] = "invalid-feedback"
        errors['fn_message'] = "Имя не должно быть пустым"
    return errors

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        login = request.form['login']
        password = request.form['password']
        check = request.form.get('secretcheck') == 'on'
        user = User.query.filter_by(login=login).first()
        if user:
            # Используйте bcrypt для проверки пароля
            if bcrypt.checkpw(password.encode('utf-8'), user.password_hash.encode('utf-8')): 
                login_user(user, remember=check)
                param_url = request.args.get('next')
                flash('Вы успешно вошли!', 'success')
                return redirect(param_url or url_for('index'))
            else:
                flash('Ошибка входа!', 'danger')
        else:
            flash('Ошибка входа!', 'danger')
    return render_template('login.html')

@app.route('/logout', methods = ['GET'])
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/users/')
@login_required
def show_users():
    users = User.query.all()
    return render_template('users/index.html', users=users)

def get_roles():
    roles = Role.query.all()
    return roles

import bcrypt  # Убедитесь, что bcrypt импортирован

@app.route('/users/create', methods=['POST', 'GET'])
@login_required
def create():
    roles = get_roles()
    if request.method == 'POST':
        login = request.form['login']
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        middle_name = request.form['middle_name']
        password = request.form['oldpassword']  # Возможно, стоит переименовать в 'password' для ясности
        role_id = request.form['role_id']
        errors = validate(login, password, last_name, first_name)
        if errors:
            return render_template('users/create.html', **errors, roles=roles)

        try:
            salt = bcrypt.gensalt()
            hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)

            new_user = User(
                login=login,
                last_name=last_name,
                first_name=first_name,
                middle_name=middle_name,
                password_hash=hashed_password.decode('utf-8'),  
                role_id=role_id
            )
            db.session.add(new_user)
            db.session.commit()
            flash(f'Пользователь {login} успешно создан.', 'success')
            return redirect(url_for('show_users'))  # Или на другую страницу после создания
        except Exception as e:
            db.session.rollback()
            flash(f'При создании пользователя произошла ошибка: {str(e)}', 'danger')
            return render_template('users/create.html', roles=roles)

    return render_template('users/create.html', roles=roles)


@app.route('/users/show/<int:user_id>')
def show_user(user_id):
    user = User.query.get_or_404(user_id)
    return render_template('users/show.html', user=user)

@app.route('/users/edit/<int:user_id>', methods=["POST", "GET"])
@login_required
def edit(user_id):
    roles = get_roles()
    user = User.query.get_or_404(user_id)
    if request.method == 'POST':
        user.first_name = request.form['first_name']
        user.last_name = request.form['last_name']
        user.middle_name = request.form['middle_name']
        user.role_id = request.form['role_id']
        try:
            db.session.commit()
            flash(f'Данные пользователя {user.first_name} успешно обновлены.', 'success')
            return redirect(url_for('show_users'))  # Добавьте редирект
        except Exception as e:
            db.session.rollback()
            flash(f'При обновлении пользователя произошла ошибка: {str(e)}', 'danger')
            return render_template('users/edit.html', user=user, roles=roles)
    # Не забудьте вернуть шаблон и вне блока if
    return render_template('users/edit.html', user=user, roles=roles) 


@app.route('/users/delete/', methods=['POST'])
@login_required
def delete():
    try:
        user_id = request.form.get('user_id')
        user = User.query.get_or_404(user_id)
        db.session.delete(user)
        db.session.commit()
        flash(f'Пользователь {user_id} успешно удален.', 'success')
    except Exception as e:
        db.session.rollback()
        flash(f'При удалении пользователя произошла ошибка: {str(e)}', 'danger')
        return render_template('users/index.html', user_id=user_id)

    return redirect(url_for('show_users'))


@app.route('/users/change/', methods=["POST", "GET"])
@login_required
def change():
    if request.method == "POST":
        user_id = current_user.id
        oldpassword = request.form['oldpassword']
        newpassword = request.form['newpassword']
        newpassword2 = request.form['newpassword2']

        user = User.query.filter_by(id=user_id).first() # Получите пользователя по ID

        if user:
            # Проверьте старый пароль с помощью bcrypt
            if bcrypt.checkpw(oldpassword.encode('utf-8'), user.password_hash.encode('utf-8')): 
                errors = validate('login', newpassword, 'name', 'name')
                if errors:
                    if len(errors.keys()) > 0:
                        flash(errors['p_message'], 'danger')
                        return render_template('users/change.html')
                elif newpassword != newpassword2:
                    flash(f'Пароли не совпадают', 'danger')
                    return render_template('users/change.html')
                else:
                    # Хешируйте новый пароль с помощью bcrypt
                    salt = bcrypt.gensalt()
                    hashed_password = bcrypt.hashpw(newpassword.encode('utf-8'), salt)
                    user.password_hash = hashed_password.decode('utf-8')
                    try:
                        db.session.commit()
                        flash(f'Пароль обновлен', 'success')
                        return redirect(url_for('index'))
                    except Exception as e:
                        db.session.rollback()
                        flash(f'Ошибка при обновлении пароля: {str(e)}', 'danger')
                        return render_template('users/change.html')
            else:
                flash(f'Неправильный пароль', 'danger')
                return render_template('users/change.html')
        else:
            flash(f'Пользователь не найден', 'danger')
            return render_template('users/change.html')

    else:
        return render_template('users/change.html')
    
    
def create_admin():
    admin_login = 'admin'
    admin_password = '123qweASD@'
    admin_first_name = 'Admin'
    admin_last_name = 'Adminov'
    admin_role_name = 'admin'

    # Проверка наличия роли администратора
    admin_role = Role.query.filter_by(name=admin_role_name).first()
    if not admin_role:
        admin_role = Role(name=admin_role_name, description='Administrator role')
        db.session.add(admin_role)
        db.session.commit()

    # Проверка наличия администратора
    admin_user = User.query.filter_by(login=admin_login).first()
    if not admin_user:
        admin_user = User(
            login=admin_login,
            password_hash=admin_password,
            first_name=admin_first_name,
            last_name=admin_last_name,
            role_id=admin_role.id
        )
        db.session.add(admin_user)
        db.session.commit()

if __name__ == '__main__':
    app.run(debug=True)
