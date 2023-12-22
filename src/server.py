from fastapi import FastAPI,Depends
from sqlalchemy.orm import Session
from src.infra.sqlalchemy.config.database import get_db,engine
from src.infra.sqlalchemy.GRUD.serie import GrudSerie
from src.schemas import schemas
from src.infra.sqlalchemy.models import models
from fastapi.middleware.cors import CORSMiddleware
#models.Base.metadata.create_all(bind=engine)
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.get('/')
async def root():
    return {'msg':'ok'}

@app.post('/serie')
async def setSerie(serie:schemas.Serie,db:Session=Depends(get_db)):
    dados_serie = GrudSerie(db).setAdd(serie) 
    return dados_serie

@app.get('/serie')
async def getSerie(db:Session= Depends(get_db)):
    return GrudSerie(db=db).get()

