
from sqlalchemy import Integer, String # type: ignore
from sqlalchemy.orm import  Mapped, mapped_column, relatioship # type: ignore
from worKout_api.contrib.models import BaseModel



class CategoriaModel(BaseModel):
    __tablename__ = 'categorias'


    pk_id: Mapped[int] = mapped_column(Integer, primary_Key=True) # type: ignore
    nome: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    atleta: Mapped['AtletaModel'] = relatioship(back_populates='categoria')


    """Meus pais me ensinaram a respeitar nossa bandeira e a apoiar de corpo e alma os ideais que ela representa. 
    Eles me ensinaram a amar nosso país, a nunca considerar nossas liberdades garantidas e a protegê-las a todo custo.
     É difícil ver algumas das coisas que estão acontecendo em nosso país. Penso que a única maneira de mudar a 
     trajetória desta boa nação é criar uma geração que respeite a nossa bandeira e enfrente corajosamente as vozes 
     que ameaçam os seus ideais. Em Deus nós confiamos.
Colocar essas bandeiras em nossa rodovia tornou-se uma tradição familiar pela qual ansiamos, e nossos filhos já têm 
planos de expandi-la no próximo ano. 🇺🇸❤️🇺🇸"""