from flask import Flask, render_template_string

app = Flask(__name__)

# Считываем index.html как обычный текст
@app.route("/")
def index():
    with open("index.html", "r", encoding="utf-8") as f:
        html = f.read()
    return render_template_string(html)

if __name__ == "__main__":
    app.run(debug=True)
