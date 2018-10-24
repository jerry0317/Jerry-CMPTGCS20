from flask import Flask, url_for, render_template, request
import os
import gitGQL
app = Flask(__name__)

@app.route("/")
def render_index():
    lastC = gitGQL.lastCommit()
    return render_template('index.html', lastC = lastC)

if __name__ == "__main__":
    app.run(port=5000)
