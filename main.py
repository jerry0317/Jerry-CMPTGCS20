from flask import Flask, url_for, render_template, request
import os
import gitGQL
import json
app = Flask(__name__)

@app.route("/")
def render_index():
    lastC = gitGQL.recentCommits()
    return render_template('index.html', lastC = lastC)

@app.route("/api", methods=['POST'])
def parse_request():
    name = request.form['name']
    if name == "":
        msg = "Please provide your name..."
    else:
        msg = "Hi, {}!".format(name)
    rt = {
        "message": msg
    }
    rt = json.dumps(rt)
    return rt

if __name__ == "__main__":
    app.run(port=5000)
