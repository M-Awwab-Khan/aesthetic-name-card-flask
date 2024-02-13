from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    info = {
        'name': 'M. Awwab Khan',
        'designation': 'Machine Learning Scientist'
    }
    return render_template('index.html', info=info)

if __name__ == '__main__':
    app.run(debug=True)