from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api import scrapper
import os


app = FastAPI(openapi_url="/api/v1/neurond-social-medial-tool/tasks/openapi.json",
              docs_url="/api/v1/neurond-social-medial-tool/tasks/docs")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)

app.include_router(scrapper.router, prefix='/api/v1/scrapper')
#app.include_router(analyzer.router, prefix='/api/v1/analyzer')
#app.include_router(notifier.router, prefix='/api/v1/notifier')
