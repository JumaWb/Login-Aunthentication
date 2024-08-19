from flask import Flask, render_template, request, redirect


app = Flask(__name__, template_folder='./template')

@app.route("/")
def index():
    print(app.jinja_loader.list_templates())
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)

