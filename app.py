from flask import Flask, render_template
app = Flask(__name__)
Data = ["I", "G", "S"]

@app.route('/')
def home():
    return render_template
@app.route("/igs")
def igs():
    return render_template('igs,html', Data=Data)

if __name__ == '__main__':
    app.run(debug=True)