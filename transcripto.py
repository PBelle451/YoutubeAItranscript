import whisper
from transformers import pipeline
from yt_dlp import YoutubeDL
import os

def baixar_audio(url):
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': 'video_audio.mp3',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

    if os.path.exists("video_audio.mp3.mp3"):
        os.rename("video_audio.mp3.mp3", "video_audio.mp3")
    elif not os.path.exists("video_audio.mp3"):
        raise FileNotFoundError("O arquivo de áudio não foi encontrado após o download.")

    return os.path.abspath("video_audio.mp3")


def transcrever_audio(audio_file):
    model = whisper.load_model("base")
    result = model.transcribe(audio_file)
    return result["text"]


def dividir_texto(texto, tamanho_maximo=1000):
    """Divide o texto em pedaços menores para evitar ultrapassar o limite de tokens."""
    palavras = texto.split()
    partes = []
    parte_atual = []
    contagem_palavras = 0

    for palavra in palavras:
        contagem_palavras += len(palavra) + 1
        if contagem_palavras > tamanho_maximo:
            partes.append(" ".join(parte_atual))
            parte_atual = []
            contagem_palavras = len(palavra) + 1
        parte_atual.append(palavra)

    if parte_atual:
        partes.append(" ".join(parte_atual))

    return partes


def resumir_texto(texto):
    summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")
    partes_texto = dividir_texto(texto)
    resumos = [summarizer(parte, max_length=150, min_length=30, do_sample=False)[0]['summary_text'] for parte in
               partes_texto]
    return " ".join(resumos)


def salvar_resumo_em_arquivo(resumo, nome_arquivo="resumo_video.txt"):
    with open(nome_arquivo, "w", encoding="utf-8") as f:
        f.write(resumo)
    print(f"Resumo salvo em {nome_arquivo}")

def resumir_video_youtube(url):
    print("Baixando áudio do vídeo...")
    audio_file = baixar_audio(url)

    print("Transcrevendo áudio...")
    texto = transcrever_audio(audio_file)

    print("Gerando resumo em texto...")
    resumo = resumir_texto(texto)

    return resumo


if __name__ == '__main__':
    url = input("Digite a URL do video do Youtube que deseja resumir: ")
    resumo = resumir_video_youtube(url)
    salvar_resumo_em_arquivo(resumo)
    print("\nResumo do vídeo:\n", resumo)
