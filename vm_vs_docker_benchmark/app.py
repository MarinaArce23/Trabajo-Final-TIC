from flask import Flask, render_template, request, send_file, flash, redirect, url_for
from PIL import Image
import io
import os

template_folder = os.path.join(os.path.dirname(__file__), "templates")
static_folder = os.path.join(os.path.dirname(__file__), "static")

app = Flask(__name__, template_folder=template_folder, static_folder=static_folder)
app.secret_key = "supersecretkey"  # Necesario para mostrar mensajes flash

@app.route("/", methods=["GET", "POST"])
def index():
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
            return send_file(img_io, mimetype="image/png", as_attachment=True, download_name="converted.png")
        except Exception:
            flash("❌ Error al procesar la imagen.")
            return redirect(url_for("index"))

    return render_template("index.html")
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
