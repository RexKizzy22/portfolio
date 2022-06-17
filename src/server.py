from flask import Flask, render_template

app = Flask(__name__)

@app.route("/<string:page_name>")
def page(page_name):
    return render_template(page_name)
