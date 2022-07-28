from flask import Flask
from markupsafe import escape

app = Flask(__name__)

@app.route('/bot/<botname>')
def show_bot_profile(botname):
    return f'User {escape(botname)}'

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)



