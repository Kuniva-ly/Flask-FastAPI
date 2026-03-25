import uvicorn
from fastapi import FastAPI
from routers.users import router as router01
from routers.mdp_validation import router as router02
from routers.produits import router as router03
from routers.commandes import router as router04
from routers.respond_complet import router as router05
from routers.settings import router as router06
from routers.evenement import router as router07
from models.settings import settings

app = FastAPI(
    title=settings.app_name,
    description="API regroupant les exercices de FastAPI ",
    version="1.0.0",
    debug=settings.debug
)

app.include_router(router01, prefix=f"{settings.api_v1_prefix}/users")
app.include_router(router02, prefix=f"{settings.api_v1_prefix}/password-validation")
app.include_router(router03, prefix=f"{settings.api_v1_prefix}/products")
app.include_router(router04, prefix=f"{settings.api_v1_prefix}/commandes")
app.include_router(router05, prefix=f"{settings.api_v1_prefix}/response-test")
app.include_router(router06, prefix=f"{settings.api_v1_prefix}/settings")
app.include_router(router07, prefix=f"{settings.api_v1_prefix}/evenements")

if __name__ == "__main__":
    uvicorn.run(app, port=8000)
