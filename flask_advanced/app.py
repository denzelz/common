from datetime import timedelta
from flask import Flask, render_template, session
from Blueprint.products.main import products
from Blueprint.supermarkets.main import supermarkets


app = Flask(__name__)
app.register_blueprint(products)
app.register_blueprint(supermarkets)
app.config['SECRET_KEY'] = 'simple_key'
app.permanent_session_lifetime = timedelta(seconds=120)



@app.route('/')
def get_home_page():
    session['login'] = 'ok'
    return render_template("home.html")


@app.errorhandler(404)
def handle_404(error):
    return render_template("error_404.html"), 404


if __name__ == '__main__':
    app.run(debug=True)
