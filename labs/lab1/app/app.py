import random
from flask import Flask, render_template, request, redirect, url_for
from faker import Faker

fake = Faker()

app = Flask(__name__)

images_ids = ['7d4e9175-95ea-4c5f-8be5-92a6b708bb3c',
              '2d2ab7df-cdbc-48a8-a936-35bba702def5',
              '6e12f3de-d5fd-4ebb-855b-8cbc485278b7',
              'afc2cfe7-5cac-4b80-9b9a-d5c65ef0c728',
              'cab5b7f2-774e-4884-a200-0c0180fa777f']

def generate_comments(replies=True):
    comments = []
    for i in range(random.randint(1, 3)):
        comment = { 'author': fake.name(), 'text': fake.text() }
        if replies:
            comment['replies'] = generate_comments(replies=False)
        comments.append(comment)
    return comments

def generate_post(i):
    return {
        'title': 'Заголовок поста',
        'text': fake.paragraph(nb_sentences=100),
        'author': fake.name(),
        'date': fake.date_time_between(start_date='-2y', end_date='now'),
        'image_id': f'{images_ids[i]}.jpg',
        'comments': generate_comments()
    }

posts_list = sorted([generate_post(i) for i in range(5)], key=lambda p: p['date'], reverse=True)

@app.route('/')
def index():
    msg = 'Hello world'
    return render_template('index.html',msg=msg)

@app.route('/posts')
def posts():
    return render_template('posts.html',postlist=posts_list)

@app.route('/about')
def about():
    msg='about'
    return render_template('about.html',msg=msg)

@app.route('/posts/<int:index>')
def post(index):
    post = posts_list[index]
    return render_template('post.html', post=post, post_index=index)

@app.route('/posts/<int:post_index>/add_comment', methods=['POST'])
def add_comment(post_index):
    comment_text = request.form.get('comment_text')
    comments = posts_list[post_index]['comments']
    new_comment = {'author': fake.name(), 'text': comment_text, 'replies': []}
    comments.append(new_comment)
    return redirect(url_for('post', index=post_index))

if __name__ == '__main__':
    app.run(debug=True)
