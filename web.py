from flask import Flask
from flask import send_file
from individualism import individualism

app = Flask(__name__)
png = open("./image/개인주의.png", "rb")

@app.route("/<num>")
def Main(num=4):
    buf = individualism(png, discriminator=num)
    return send_file(buf, mimetype='image/png')

app.run(host="0.0.0.0", port=80)