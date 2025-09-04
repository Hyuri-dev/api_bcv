from fastapi import FastAPI
from routers import tasas

app = FastAPI()

app.include_router(router=tasas.router)

@app.get("/inicio")
async def root():
  return {"Bienvenidos al api para consulta del BCV, te recomiendo ingresar a la documentacion para visualizar mejor como funcionan los endpoints :)"}

if __name__ == "__name__":
  import uvicorn
  uvicorn.run(app, host="0.0.0.0", port=8000)