import wikipedia
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    response = {
        'message': 'Salom bu 1chi projectim'
    }
    return response


@app.get("/{lang}/{info}")
async def wiki(info: str, lang: str):
    wikipedia.set_lang(lang)
    info = wikipedia.summary(info)
    response = {
        'lang': lang,
        'info': info
    }
    return response
