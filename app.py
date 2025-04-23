from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from wtforms import SelectField
from wtforms.validators import DataRequired

# Создаём Flask-приложение
app = Flask(__name__)
app.config['SECRET_KEY'] = 'supersecretkey'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Создаём базу данных
db = SQLAlchemy(app)

# Модель задачи
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    category = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f"<Task {self.name}>"

# Список категорий
CATEGORY_CHOICES = [
    ('Шутки', 'Шутки'),
    ('Факт дня', 'Факт дня'),
    ('Мини-игра', 'Мини-игра'),
    ('Задача', 'Задача')
]

# Настройка отображения модели в админке
class TaskModelView(ModelView):
    column_searchable_list = ['name', 'description']
    form_columns = ['name', 'description', 'category']
    
    # Используем SelectField для выбора категории
    form_overrides = {
        'category': SelectField
    }
    
    form_args = {
        'category': {
            'choices': CATEGORY_CHOICES,  # Список категорий
            'validators': [DataRequired()]  # Сделать поле обязательным
        }
    }

# Инициализация админки
admin = Admin(app, name="Не скучай - Админка", template_mode='bootstrap4')
admin.add_view(TaskModelView(Task, db.session))

# Точка входа
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
