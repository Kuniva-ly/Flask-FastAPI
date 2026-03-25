import uvicorn
from fastapi import FastAPI
from routers.users import router as router01
from routers.mdp_validation import router as router02
from routers.produits import router as router03

app = FastAPI(
    title="FastAPI Exercices",
    description="API regroupant les exercices de FastAPI ",
    version="1.0.0"
)

app.include_router(router01, prefix="/users")
app.include_router(router02, prefix="/password-validation")
app.include_router(router03, prefix="/products")

if __name__ == "__main__":
    uvicorn.run(app, port=8000)
