from flask import Flask
import subprocess

app = Flask(__name__)

@app.route("/open_notepad")
def open_notepad():
    subprocess.Popen('C:\\Windows\\System32\\notepad.exe')
    return "New notepad application created"

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
