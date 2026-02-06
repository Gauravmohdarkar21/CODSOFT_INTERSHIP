from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def calculator():
    expression = ""
    error = ""

    if request.method == "POST":
        expression = request.form.get("expression", "")

        try:
            expression_eval = expression.replace("%", "/100")
            expression = str(eval(expression_eval))  # result goes into display
        except:
            error = "Invalid Expression!"

    return render_template("index.html", expression=expression, error=error)

if __name__ == "__main__":
    app.run(debug=True)
