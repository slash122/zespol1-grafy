from flask import Flask, render_template
from blueprints.zestaw1 import zestaw1

app = Flask(__name__)
app.register_blueprint(zestaw1, url_prefix='/zestaw1')

@app.route('/')
def get_index():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)