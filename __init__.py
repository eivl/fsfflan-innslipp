from flask import Flask, render_template, send_from_directory

app = Flask(__name__)


@app.route('/')
def homepage():
    # return render_template('main.html')
    return "Hei på deg!, Flask virker som det skal.. men mest sannsynlig ikke render_template"


@app.route('/m2')
def m2():
    return render_template('main.html')

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')


# @app.route('/<path:path>')
# def static_file(path):
#     return app.send_static_file(path)


# @app.route('/static/<path:path>')
# def send_static(path):
#     return send_from_directory('static', path)


# @app.route('/templates/<path:path>')
# def send_templates(path):
#     return send_from_directory('templates', path)


