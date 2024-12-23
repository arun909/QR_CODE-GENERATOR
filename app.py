from flask import Flask, request, render_template
import pyqrcode
import io
import base64

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    qr_code_img = None
    if request.method == "POST":
        url = request.form.get("url")
        if url:
            # Generate QR code
            qr = pyqrcode.create(url)
            buffer = io.BytesIO()
            qr.png(buffer, scale=8)
            buffer.seek(0)
            # Encode the image to base64 for display in HTML
            qr_code_img = base64.b64encode(buffer.read()).decode()
    return render_template("index.html", qr_code_img=qr_code_img)

if __name__ == "__main__":
    app.run(debug=True)
