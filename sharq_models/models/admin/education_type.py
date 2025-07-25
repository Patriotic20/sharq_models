from sqlalchemy import String
from sharq_models.database import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from models.study_info import StudyInfo
    from models.admin.study_direction import StudyDirection

class EducationType(Base):
    __tablename__ = "education_types"
    
    """
    Examples:
        - Maktab
        - Oliy
        - Kolledj
    """

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False, unique=True)
    
    status: Mapped[str] = mapped_column(String(50), nullable=False, default="inactive")

    study_infos: Mapped[list["StudyInfo"]] = relationship("StudyInfo", back_populates="education_type")

    def __repr__(self):
        return f"<EducationType(id={self.id}, name='{self.name}')>"

    def __str__(self):
        return self.name
