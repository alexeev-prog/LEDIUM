#!/usr/bin/python3
from random import randint
from datetime import datetime
from flask import Blueprint, render_template, url_for, redirect, request, flash, get_flashed_messages  # noqa: F401
from app.models import User, Article, Comment, Like, db
from app.utils import render_markdown

main_bp = Blueprint('main', __name__)


@main_bp.app_errorhandler(404)
def handle_404(error):
	return render_template('error.html', code=404, 
							description='Страница не найдена. Попробуйте проверить URL.',
							title='404'), 404


@main_bp.app_errorhandler(401)
def handle_401(error):
	return render_template('error.html', code=401, description='Доступ запрещен. Возможно, эта страница доступна для зарегистрированных пользователей.',
							title='401'), 401


@main_bp.route('/')
def index():
	articles = Article.query.order_by(Article.creation_date.desc()).all()
	return render_template('index.html', title='Главная', articles=articles)


@main_bp.route('/article/<id>')
def get_article(id):
	article = Article.query.get_or_404(id)
	return render_template('article.html', title='Главная', article=article, text=article.text)


@main_bp.route('/new_article', methods=['GET', 'POST'])
def new_article():
	print(request.method)
	if request.method == 'POST':
		title = request.form['title']
		category = request.form['category']
		tags = request.form['tags']
		intro = request.form['intro']
		content = request.form['content']

		article = Article(title=title, article_category=category, tags=tags, intro=intro, text=content, creation_date=datetime.now(), user_id=0)

		try:
			db.session.add(article)
			db.session.commit()
		except Exception as ex:
			flash(f'Ошибка добавления в базу данных: {ex}')
			print(ex)
			return render_template('newarticle.html', title='Создать статью')

		return redirect('/')

	return render_template('newarticle.html', title='Создать статью')
