from sqlalchemy import String
from sharq_models.database import Base
from sqlalchemy.orm import Mapped, mapped_column , relationship
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from models.study_info import StudyInfo
    from models.admin.study_direction import StudyDirection
    
class StudyForm(Base):
    """
    Examples:
        - Kunduzgi
        - Kechki
        - Masofaviy
        - Sirtqi
    """
    __tablename__ = "study_forms"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False, unique=True)
    
    status: Mapped[str] = mapped_column(String(50), nullable=False, default="inactive")

    study_infos: Mapped[list["StudyInfo"]] = relationship("StudyInfo", back_populates="study_form")
    study_directions: Mapped[list["StudyDirection"]] = relationship("StudyDirection", back_populates="study_form")

    def __repr__(self):
        return f"<StudyForm(id={self.id}, name='{self.name}')>"

    def __str__(self):
        return self.name
