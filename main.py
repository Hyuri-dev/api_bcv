from fastapi import FastAPI
from routers import tasas
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

# Configuramos el middleware para que el api sea accesible a los demas
origins = [
    "http://127.0.0.1:5500",
    "https://https://fast-bcv-ten.vercel.app/",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(router=tasas.router)

@app.get("/inicio")
async def root():
  return {"Bienvenidos al api para consulta del BCV, te recomiendo ingresar a la documentacion para visualizar mejor como funcionan los endpoints :)"}

if __name__ == "__name__":
  import uvicorn
  uvicorn.run(app, host="0.0.0.0", port=8000)