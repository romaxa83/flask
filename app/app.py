from flask import Flask
from config import Configuration
# подключение бд
from flask_sqlalchemy import SQLAlchemy

# создаем приложение
app = Flask(__name__)
# заполняем конфигурацие
app.config.from_object(Configuration)

#создание подключение к бд
db = SQLAlchemy(app)

