from fastapi import FastAPI

from db.database import Base, engine
from routers import auth, players, teams, matches
import uvicorn

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Babyfoot API")

app.include_router(auth.router)
app.include_router(players.router)
app.include_router(teams.router)
app.include_router(matches.router)


@app.get("/public/ping")
def ping():
    return {"message": "pong"}


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)