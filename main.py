from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import uvicorn

from data import produto_repo, cliente_repo  # Certifique-se de que cliente_repo existe

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# Cria tabelas
produto_repo.criar_tabela()
cliente_repo.criar_tabela()


@app.get("/")
async def root(request: Request):
    produtos = produto_repo.obter_todos()
    return templates.TemplateResponse("index.html", {"request": request, "produtos": produtos})


@app.get("/clientes")
async def listar_clientes(request: Request):
    clientes = cliente_repo.obter_todos()
    return templates.TemplateResponse("clientes.html", {"request": request, "clientes": clientes})


if __name__ == "__main__":
    uvicorn.run(app="main:app", host="127.0.0.1", port=8000, reload=True)
