from flask import Flask, render_template, request, send_file
from transcript import resumir_video_youtube, salvar_resumo_em_arquivo
import os

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    resumo = None
    error = None

    if request.method == "POST":
        url = request.form.get("youtube_url")
        try:
            if not url or "youtube.com" not in url:
                raise ValueError("Por favor, insira uma URL válida do YouTube.")

            resumo = resumir_video_youtube(url)
            salvar_resumo_em_arquivo(resumo)

        except Exception as e:
            error = str(e)

    return render_template("index.html", resumo=resumo, error=error)

@app.route("/download")
def download():
    file_path = "resumo_video.txt"
    if os.path.exists(file_path):
        return send_file(file_path, as_attachment=True)
    return "Arquivo não encontrado.", 404

if __name__ == "__main__":
    app.run(debug=True)
from flask import Flask, render_template, request, send_file
from transcript import resumir_video_youtube, salvar_resumo_em_arquivo
import os

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    resumo = None
    error = None

    if request.method == "POST":
        url = request.form.get("youtube_url")
        try:
            if not url or "youtube.com" not in url:
                raise ValueError("Por favor, insira uma URL válida do YouTube.")

            resumo = resumir_video_youtube(url)
            salvar_resumo_em_arquivo(resumo)

        except Exception as e:
            error = str(e)

    return render_template("index.html", resumo=resumo, error=error)

@app.route("/download")
def download():
    file_path = "resumo_video.txt"
    if os.path.exists(file_path):
        return send_file(file_path, as_attachment=True)
    return "Arquivo não encontrado.", 404

if __name__ == "__main__":
    app.run(debug=True)
# app.py