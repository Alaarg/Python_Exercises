from flask import Flask, render_template


app = Flask(__name__)

# Exercises  1---------------------------------------------------------------------


@app.route('/')
def HomePage():
    return render_template('index.html')


@app.route('/hello')
def hello():
    return render_template('hello.html')


@app.route('/members')
def members():
    return render_template('members.html')

# Exercise 1 ---------------------------------------------------------------------


# Exercise 2 ---------------------------------------------------------------------

@app.route('/score/<int:marks>')
def marks(marks):
    return render_template('marks.html', marks=marks)

# Exercise 2 ---------------------------------------------------------------------

# Exercise 3 ---------------------------------------------------------------------




# Exercise 3 ---------------------------------------------------------------------




if __name__ == '__main__':
    app.run()



