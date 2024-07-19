from datetime import datetime
from sqlalchemy import DateTime, Integer, String, Float # type: ignore
from sqlalchemy.orm import  Mapped, mapped_column,  relatioship # type: ignore
from worKout_api.contrib.models import BaseModel
from sqlalchemy import ForeignKey # type: ignore



class AtletaModel(BaseModel):
    __tablename__ = 'atletas'


    pk_id: Mapped[int] = mapped_column(Integer, primary_Key=True) # type: ignore
    nome: Mapped[str] = mapped_column(String(50), nullable=False)
    cpf: Mapped[str] = mapped_column(String(11), unique=True, nullable=False)
    idade: Mapped[int] = mapped_column(Integer, nullable=False)
    peso: Mapped[float] = mapped_column(Float, nullable=False)
    altura: Mapped[float] = mapped_column(Float, nullable=False)
    sexo: Mapped[str] = mapped_column(String(1), nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    categoria: Mapped['CategoriaMobel'] = relatioship('categorias.pk_id')
    categoria_id: Mapped[int] = mapped_column(ForeignKey('categorias.pk_id'))
    centro_treinamento: Mapped['CentroTreinamento'] = relatioship(back_populates='atleta')
    ccentro_treinamento_id: Mapped[int] = mapped_column(ForeignKey('centro_treinamento.pk_id'))