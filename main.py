from flask import Flask, url_for, render_template, request
import os
app = Flask(__name__)

@app.route("/")
def render_index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(port=5000)
