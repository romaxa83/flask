from app import app
from app import db

# импортируем приложение posts
from posts.blueprint import posts

import view

# регистрируем blueprint (модуль)
app.register_blueprint(posts, url_prefix='/blog')

if __name__ == '__main__':
	app.run()