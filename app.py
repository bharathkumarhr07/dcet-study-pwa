from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/submit", methods=["POST"])
def submit():

    # Get data from HTML form
    name = request.form.get("username")
    age = request.form.get("age")

    # Process the data
    age = int(age)

    if age >= 18:
        message = "You are an adult."
    else:
        message = "You are under 18."

    # Send data to result.html
    return render_template(
        "result.html",
        name=name,
        age=age,
        message=message
    )


if __name__ == "__main__":
    app.run(debug=True)