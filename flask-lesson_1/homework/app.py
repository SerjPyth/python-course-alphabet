import os

from flask import Flask, request, render_template, jsonify, make_response, abort, url_for, session
from werkzeug.utils import secure_filename, redirect


app = Flask(__name__)


@app.route('/home')
def home_page():
    return render_template('home.html')


@app.route('/about')
def about_page():
    return render_template('about.html')


vegetables_dict = ["Beet", "Carrot", "Potato", "Cabbage"]
fruits_dict = ["Tomato", "Orange", "Watermelon", "Peach"]


@app.route('/vegetables')
@app.route('/vegetables/<string:value>', methods=['GET', 'POST', 'DELETE'])
def vegetables(value=None):
    if request.method == 'POST':
        do_post(value)
        return "Ahh, fresh vegetables!"
    if request.method == 'DELETE':
        do_delete(value)
        return "Eww, throw it in the dumpster!"
    else:
        return do_get()


def do_post(value):

    return vegetables_dict.append(value)


def do_get():

    return render_template('vegetables.html', values=vegetables_dict, name="a")


def do_delete(value):

    for i, elem in enumerate(vegetables_dict):
        if elem == value:
            vegetables_dict.pop(i)


@app.route('/fruits')
@app.route('/fruits/<string:value>', methods=['GET', 'POST', 'DELETE'])
def fruits(value=None):
    if request.method == 'POST':
        do_post_f(value)
        return "Mmm, what a juicy fruit!"
    if request.method == 'DELETE':
        do_delete_f(value)
        return "Give me a burger, goddamnit!"
    else:
        return do_get_f()


def do_post_f(value):

    return fruits_dict.append(value)


def do_get_f():

    return render_template('fruits.html', values=fruits_dict, name="a")


def do_delete_f(value):

    for i, elem in enumerate(fruits_dict):
        if elem == value:
            fruits_dict.pop(i)


@app.route("/file", methods=["POST"])
def save_file():
    f = request.files['file']
    file_path = os.path.join("files", secure_filename(f.filename))
    f.save(file_path)

    with open(file_path) as file:
        return file.read()


@app.route("/wrong_way")
def test_redirect():
    return redirect(url_for("home_page"))


@app.route("/test_abort")
def test_abort():
    abort(501, "Our program has an error")


@app.errorhandler(501)
def error_501_handler(error):
    return render_template("error_501.html")



@app.errorhandler(418)
def error_418_handler(error):
    return render_template("error_418.html", error=error)


app.secret_key = b'"\xaa;\x0b\x12\x8a\xa1V+\x16\xc5\x91\xfb,\xcb#'


@app.route("/test_session")
def test_session():
    app.logger.warning("this is warning")
    app.logger.error("This is error")
    session["key"] = "value"
    return "hello"


if __name__ == '__main__':
    app.run()
