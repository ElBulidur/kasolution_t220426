from config_db import Base


from typing import List
from typing import Optional
from sqlalchemy import ForeignKey
from sqlalchemy import String, DateTime
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

class Aluno(Base):
    __tablename__ = "alunos"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    create_time: Mapped[DateTime] = mapped_column(DateTime)
    name: Mapped[str] = mapped_column(String(30))
    nota: Mapped[Optional[int]]

    def __repr__(self) -> str:
        return f"Aluno(id={self.id!r}, name={self.name!r})"
    