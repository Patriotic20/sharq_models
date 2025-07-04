from sharq_models.db import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from models.study_info import StudyInfo

class StudyLanguage(Base):
    __tablename__ = "study_languages"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False, unique=True)

    study_infos: Mapped[list["StudyInfo"]] = relationship("StudyInfo", back_populates="study_language")

    def __repr__(self):
        return f"<StudyLanguage(id={self.id}, name='{self.name}')>"

    def __str__(self):
        return self.name
