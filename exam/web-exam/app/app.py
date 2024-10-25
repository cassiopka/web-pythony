import math
from flask import Flask, render_template, request, abort, send_from_directory, redirect
from flask_login import current_user, login_required
from sqlalchemy import MetaData
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy import distinct, desc
import markdown



app = Flask(__name__)
application = app

app.config.from_pyfile('config.py')

convention = {
    "ix": 'ix_%(column_0_label)s',
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
}

metadata = MetaData(naming_convention=convention)
db = SQLAlchemy(app, metadata=metadata)
migrate = Migrate(app, db)

from auth import bp as auth_bp, init_login_manager
from book import bp as book_bp
from tools import BooksFilter

app.register_blueprint(auth_bp)
app.register_blueprint(book_bp)

init_login_manager(app)

from models import *

PER_PAGE = 10


@app.route('/')
def index():
    genres = Genre.query.all()
    book_genre = Books_has_Genres.query.all()
    books_counter = Book.query.count()
    years = db.session.query(distinct(Book.year)).order_by(desc(Book.year)).all()
    years = [str(year[0]) for year in years]

    page = request.args.get('page', 1, type=int)
    books = db.session.execute(db.select(Book).order_by(desc(Book.year)).limit(PER_PAGE).offset(PER_PAGE * (page - 1))).scalars()
    page_count = math.ceil(books_counter / PER_PAGE)

    title = request.args.get('title', '')
    genres_list = request.args.getlist('genre_id')
    years_list = request.args.getlist('year')
    amount_from = request.args.get('amount_from', '')
    amount_to = request.args.get('amount_to', '')
    author = request.args.get('author', '')
    
    
    genres_list = [int(x) for x in genres_list]
    flag = True
    if books == []:
        flag = False
    rating = Book.rating
    return render_template('index.html', books=books, genres=genres, years=years, book_genre=book_genre, page=page,
        page_count=page_count, rating=rating, title=title, genres_list=genres_list, years_list=years_list, amount_from=amount_from, 
        amount_to=amount_to, author=author, flag=flag)
        
@app.route('/media/images/<cover_id>')
def image(cover_id):
    cover = Cover.query.get(cover_id)
    if cover is None:
        abort(404)
    return send_from_directory(app.config['UPLOAD_FOLDER'], cover.file_name)


@app.route('/reviews')
@login_required
def reviews():
    reviews = Review.query.filter_by(user_id=current_user.id).all()

    markdown_comments = []
    if reviews:
        for comment in reviews:
            markdown_comments.append({
                'get_user': comment.get_user,
                'rating': comment.rating,
                'text': markdown.markdown(comment.text),
                'status': comment.status_id
            })

    return render_template('reviews/reviews.html', reviews=markdown_comments)

@app.route('/reviewmoderation')
@login_required
def reviews_moder():
    reviews_counter = Review.query.filter_by(status_id=1).count()

    page = request.args.get('page', 1, type=int)
    reviews = Review.query.filter_by(status_id=1).limit(PER_PAGE).offset(PER_PAGE * (page - 1)).all()
    page_count = math.ceil(reviews_counter / PER_PAGE)
    
    #reviews = Review.query.filter_by(status_id=1).all()

    markdown_comments = []
    if reviews:
        for comment in reviews:
            markdown_comments.append({
                'id': comment.id,
                'get_user': comment.get_user,
                'rating': comment.rating,
                'text': markdown.markdown(comment.text),
                'status': comment.status_id
            })

    return render_template("reviews/moder.html", reviews=markdown_comments, page=page, page_count=page_count)

@app.route('/checkreview/<review_id>')
@login_required
def check_review(review_id):
    review = Review.query.get(review_id)
    get_user = review.get_user
    rating = review.rating
    text = markdown.markdown(review.text)
    status = review.status_id

    return render_template("reviews/edit.html", review_id=review_id, user=get_user(), rating=rating, text=text, status=status)

@app.route('/checkreview/aprove/<review_id>', methods=['GET', 'POST'])
@login_required
def aprove(review_id):
    db.session.query(Review).filter(Review.id == review_id).update({'status_id': 2})
    db.session.commit()
    return redirect(url_for('reviews_moder'))
    
@app.route('/checkreview/reject/<review_id>', methods=['GET', 'POST'])
@login_required
def reject(review_id):
    db.session.query(Review).filter(Review.id == review_id).update({'status_id': 3})
    db.session.commit()
    return redirect(url_for('reviews_moder'))
    