from flask import Flask, render_template, request
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/run_python', methods=['POST'])
def run_python():
    subprocess.Popen(['python', 'time.py'])

if __name__ == '__main__':
    app.run()