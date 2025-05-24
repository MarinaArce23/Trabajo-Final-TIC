from flask import Flask, render_template, request, flash, redirect, url_for
from PIL import Image
import io
import os
import base64

template_folder = os.path.join(os.path.dirname(__file__), "templates")
app = Flask(__name__, template_folder=template_folder)
app.secret_key = "supersecretkey"

@app.route("/", methods=["GET", "POST"])
def index():
    image_data = None
    if request.method == "POST":
        file = request.files.get("image")
        if not file:
            flash("❌ No se ha subido ninguna imagen.")
            return redirect(url_for("index"))

        if not file.mimetype.startswith("image/jpeg"):
            flash("⚠️ Solo se permiten archivos JPG.")
            return redirect(url_for("index"))

        try:
            img = Image.open(file.stream)
            img_io = io.BytesIO()
            img.save(img_io, "PNG")
            img_io.seek(0)
            # Convertimos a base64 para incrustar en HTML
            image_data = base64.b64encode(img_io.read()).decode('utf-8')
        except Exception:
            flash("❌ Error al procesar la imagen.")
            return redirect(url_for("index"))

    return render_template("index.html", image_data=image_data)

if __name__ == "__main__":
    print("🟢 Servidor Flask iniciándose...")
    app.run(host="0.0.0.0", port=5000, debug=True)
