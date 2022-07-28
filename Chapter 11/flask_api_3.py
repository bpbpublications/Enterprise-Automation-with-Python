from flask import Flask, url_for
from markupsafe import escape

app = Flask(__name__)

@app.route("/")
def automation_bot():
    return "Automation Bot"

@app.route('/bot/<botname>')
def show_bot_profile(botname):
    return f'User {escape(botname)}'

with app.test_request_context():
    print(url_for('automation_bot'))
    print(url_for('automation_bot', next='/'))
    print(url_for('show_bot_profile', botname='TestBot'))
