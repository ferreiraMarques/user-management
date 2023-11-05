from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.config.config import settings
from app.routes import users, auth

app = FastAPI()

origins = [
    settings.CLIENT_ORIGIN,
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(auth.router, tags=['Auth'], prefix='/api/v1/users')
app.include_router(users.router, tags=['Users'], prefix='/api/v1/users')


@app.get('/api/health')
def root():
    return {'status': 200}
