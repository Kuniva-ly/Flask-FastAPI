import uvicorn
from fastapi import FastAPI
from exercice01 import router as router01
from exercice02 import router as router02
from exercice03 import router as router03

app = FastAPI(
    title="FastAPI Exercices",
    description="API regroupant les exercices de FastAPI ",
    version="1.0.0"
)

app.include_router(router01, prefix="/exercice01")
app.include_router(router02, prefix="/exercice02")
app.include_router(router03, prefix="/exercice03")

if __name__ == "__main__":
    uvicorn.run(app, port=8000)
