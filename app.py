# from flask import Flask, render_template
# app = Flask(__name__)

# @app.route("/")
# def home():
#     return render_template("home.html")

# if __name__ == "__main__":
#     app.run(debug=True, host="0.0.0.0", port=3000)















# """Flask application for Paws Rescue Center."""
from flask import Flask,render_template
app = Flask(__name__)

"""View function for home page"""
@app.route("/")
def homepage():
    return render_template('home.html')


"""View function for about page"""
@app.route("/about")
def about():
    return render_template('about.html')


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=3000)
