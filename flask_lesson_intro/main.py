from flask import Flask, render_template
from flask_lesson_intro.utils import get_data


app = Flask(__name__)


@app.route('/')
def get_home_page():
    return render_template("home.html", data=get_data())


@app.route('/author')
def get_author_page():
    return render_template("author.html")


@app.route('/<item>')
def get_items_page(item):
    data = get_data()
    for elem in data:
        if item == elem['title']:
            return render_template("items.html", title=elem['title'], text=elem['text'],
                                   item_img=item + '.png', count=len(elem['text'].split()))


if __name__ == "__main__":
    app.run(debug=True)
