from flask import Flask, render_template
from flask.ext import pymongo
from filters import register_filters

DEBUG = True
MONGO_DBNAME = 'lurkingideas'

app = Flask(__name__)
app.config.from_object(__name__)
register_filters(app)
mongo = pymongo.PyMongo(app)

if app.config['DEBUG']:
    from werkzeug import SharedDataMiddleware
    import os
    app.wsgi_app = SharedDataMiddleware(app.wsgi_app, {
        '/': os.path.join(os.path.dirname(__file__), 'static')
    })


@app.route('/')
def index():
    return render_template(
        'index.html',
        posts=mongo.db.posts.find().sort('created_date', direction=pymongo.DESCENDING)
    )

@app.route('/<slug>/')
def detail(slug):
    return render_template(
        'detail.html',
        post=mongo.db.posts.find_one({'slug' :slug}),
    )

if __name__ == '__main__':
    app.run(debug=app.config['DEBUG'])

