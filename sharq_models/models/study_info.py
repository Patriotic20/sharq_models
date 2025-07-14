from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, String
from sharq_models.database import Base
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .admin.study_form import StudyForm
    from .admin.study_lenguage import StudyLanguage
    from .admin.study_direction import StudyDirection
    from .admin.education_type import EducationType
    from .admin.study_type import StudyType

class StudyInfo(Base):
    __tablename__ = "study_info"

    id: Mapped[int] = mapped_column(primary_key=True)

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    
    study_direction_id: Mapped[int] = mapped_column(ForeignKey("study_directions.id"), nullable=True)
    study_direction: Mapped["StudyDirection"] = relationship("StudyDirection", back_populates="study_infos")
    
    study_form_id: Mapped[int] = mapped_column(ForeignKey("study_forms.id"), nullable=True)
    study_form: Mapped["StudyForm"] = relationship("StudyForm", back_populates="study_infos")
    
    study_type_id: Mapped[int] = mapped_column(ForeignKey("study_types.id"), nullable=True)
    study_type: Mapped["StudyType"] = relationship("StudyType", back_populates="study_infos")
    
    study_language_id: Mapped[int] = mapped_column(ForeignKey("study_languages.id"), nullable=True)
    study_language: Mapped["StudyLanguage"] = relationship("StudyLanguage", back_populates="study_infos")
    
    education_type_id: Mapped[int] = mapped_column(ForeignKey("education_types.id"), nullable=True)
    education_type: Mapped["EducationType"] = relationship("EducationType", back_populates="study_infos")
    
    graduate_year: Mapped[str] = mapped_column(String(4), nullable=True)
    
    
