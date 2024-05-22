from flask import Flask, render_template
from blueprints.zestaw1 import zestaw1
from blueprints.zestaw2 import zestaw2
from blueprints.zestaw3 import zestaw3
from blueprints.zestaw5 import zestaw5
from blueprints.zestaw6 import zestaw6

app = Flask(__name__)
app.register_blueprint(zestaw1, url_prefix='/zestaw1')
app.register_blueprint(zestaw2, url_prefix='/zestaw2')
app.register_blueprint(zestaw3, url_prefix='/zestaw3')

app.register_blueprint(zestaw5, url_prefix='/zestaw5')
app.register_blueprint(zestaw6, url_prefix='/zestaw6')

@app.route('/')
def get_index():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)
