from flask import Flask, render_template, redirect, abort, request, make_response, jsonify
from data import db_session, news_api, news_resources
from data.users import User
from data.news import News
from forms.user import RegisterForm, LoginForm
from forms.news import NewsForm
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from flask_restful import reqparse, abort, Api, Resource

app = Flask(__name__)
api = Api(app)


def main():
    api.add_resource(news_resources.NewsListResource, '/api/v2/news')

    # для одного объекта
    api.add_resource(news_resources.NewsResource, '/api/v2/news/<int:news_id>')

    db_session.global_init("db/blogs.db")
    app.run()


if __name__ == '__main__':
    main()
