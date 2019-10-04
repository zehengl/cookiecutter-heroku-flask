from flask import Flask, render_template, request
from whitenoise import WhiteNoise

app = Flask(__name__)
app.wsgi_app = WhiteNoise(app.wsgi_app, root="static/")


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        input1 = request.form["input1"]
        input2 = request.form["input2"]
        output = f"Input1={input1} Input2={input2}"
        return output
    else:
        return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
