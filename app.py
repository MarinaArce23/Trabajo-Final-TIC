from flask import Flask, render_template, request, send_file
from PIL import Image
import io
import os

template_folder = os.path.join(os.path.dirname(__file__), "templates")
app = Flask(__name__, template_folder=template_folder)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        file = request.files.get("image")
        if not file:
            return "No se subió ningún archivo", 400
        try:
            img = Image.open(file.stream)
        except Exception:
            return "Archivo no es una imagen válida", 400

        img_io = io.BytesIO()
        img.save(img_io, "PNG")
        img_io.seek(0)
        return send_file(img_io, mimetype="image/png", as_attachment=True, download_name="converted.png")

    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
