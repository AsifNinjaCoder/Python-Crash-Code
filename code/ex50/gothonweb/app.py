from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route("/", methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        massage = request.form['massage']
        return render_template('confrim.html', confrim={'name': name, 'email': email, 'massage': massage})
    else:
        return render_template('webform.html')

if __name__ == "__main__":
    app.run()