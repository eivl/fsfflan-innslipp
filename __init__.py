from flask import Flask, render_template, send_from_directory

app = Flask(__name__, static_url_path='')


@app.route('/')
def homepage():
    return render_template("main.html")
    # return "Hei på deg!"
if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0')


# @app.route('/<path:path>')
# def static_file(path):
#     return app.send_static_file(path)


# @app.route('/static/<path:path>')
# def send_static(path):
#     return send_from_directory('static', path)


# @app.route('/templates/<path:path>')
# def send_templates(path):
#     return send_from_directory('templates', path)


