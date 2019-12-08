from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def HomePage():
    return render_template('index.html' )


@app.route('/score/<int:score>' , )
def score(score):
    return render_template('html_score.html', score = score)

@app.route('/<user>')
def HomePage_name(user):

    return render_template('index.html', name=user, title=(f'welocme mr {user} '))



@app.route('/index/<name>')
def index_name(name):
    return 'Hello %s!' % name


if __name__ == '__main__':
    app.run(debug=True)
