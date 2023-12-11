from sqlalchemy import select,delete
from sqlalchemy.orm import Session
from src.schemas import schemas
from src.infra.sqlalchemy.models import models


class GRUD_serie():
    def __init__(self,db:Session) :
        self.db = db

    def setAdd(self,serie:schemas.Serie):
        db_serie = models.Serie(titulo=serie.titulo,
                                ano=serie.ano,
                                genero=serie.genero,
                                qtd_temporada=serie.qtd_temporada)
        self.db.add(db_serie)
        self.db.commit()
        self.db.refresh(db_serie)
        return db_serie
    
    def get(self):
        return self.db.query(models.Serie).all()
    
    def get_id(self,idSerie):
        return self.db.execute(select(models.Serie).filter_by(id=idSerie)).one()
    
    def delSerieID(self,idSerie):
        self.db.execute(delete(models.Serie).where(models.Serie.id == idSerie))
        self.db.commit()
        