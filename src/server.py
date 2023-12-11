from fastapi import FastAPI,Depends
from sqlalchemy.orm import Session
from src.infra.sqlalchemy.config.database import get_db,engine
from src.infra.sqlalchemy.GRUD.serie import GRUD_serie
from src.schemas.schemas import Serie
from src.infra.sqlalchemy.models import models

#models.Base.metadata.create_all(bind=engine)
app = FastAPI()

@app.get('/')
async def root():
    return {'msg':'ok'}

@app.post('/serie')
async def setSerie(serie:Serie,db:Session=Depends(get_db)):
    dados_serie = GRUD_serie(db).setAdd(serie) 
    return dados_serie

@app.get('/serie')
async def getSerie(db:Session= Depends(get_db)):
    return GRUD_serie(db=db).get()

@app.get('/serie/{id}')
async def getSerieID(id:int,db:Session = Depends(get_db)):
    return GRUD_serie(db).get_id(id)

@app.delete('/serie/{id}')
async def delSerie(id:int,db:Session= Depends(get_db)):
    return GRUD_serie(db).delSerieID(id)