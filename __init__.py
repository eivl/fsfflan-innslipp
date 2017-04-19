from flask import Flask, render_template

app = Flask(__name__, static_url_path='')


@app.route('/')
def homepage():
    # return render_template("main.html")
    return "Hei på deg!"
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')


@app.route('/<path:path>')
def static_file(path):
    return app.send_static_file(path)
