from fastapi import FastAPI
from app.lifespan import lifespan
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Project er nam ki?",
    description="doctor project",
    version="1.0.0",
    lifespan=lifespan)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


from app.routes import baseroute
from app.routes import login
from app.routes import signup

# mount all the endpoints:
app.include_router(baseroute.router)
app.include_router(login.router)
app.include_router(signup.router)
