from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey
from sharq_models.database import Base
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .admin.study_form import StudyForm
    from .admin.study_lenguage import StudyLanguage
    from .admin.study_direction import StudyDirection
    from .admin.education_type import EducationType
    from .admin.study_type import StudyType
    from .user import User
    from .application import Application

class StudyInfo(Base):
    __tablename__ = "study_info"

    id: Mapped[int] = mapped_column(primary_key=True)

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    study_direction_id: Mapped[int] = mapped_column(ForeignKey("study_directions.id"), nullable=True)
    study_form_id: Mapped[int] = mapped_column(ForeignKey("study_forms.id"), nullable=True)
    study_language_id: Mapped[int] = mapped_column(ForeignKey("study_languages.id"), nullable=True)
    education_type_id: Mapped[int] = mapped_column(ForeignKey("education_types.id"), nullable=True)
    study_type_id: Mapped[int] = mapped_column(ForeignKey("study_types.id"), nullable=True)
    graduate_year: Mapped[str] 
    certificate_path: Mapped[str | None]
    dtm_sheet: Mapped[str | None]

    # Relationships
    user: Mapped["User"] = relationship("User", back_populates="study_info")
    
    study_direction: Mapped["StudyDirection"] = relationship("StudyDirection", back_populates="study_infos")
    study_form: Mapped["StudyForm"] = relationship("StudyForm", back_populates="study_infos")
    study_type: Mapped["StudyType"] = relationship("StudyType" , back_populates="study_infos")
    education_type: Mapped["EducationType"] = relationship("EducationType" , back_populates="study_infos")
    study_language: Mapped["StudyLanguage"] = relationship("StudyLanguage", back_populates="study_infos")
    
    application: Mapped["Application"] = relationship("Application", back_populates="study_info", uselist=False)

    def __repr__(self):
        return (
            f"<StudyInfo(id={self.id}, user_id={self.user_id}, "
            f"study_direction_id={self.study_direction_id}, "
            f"study_form_id={self.study_form_id}, study_language_id={self.study_language_id})>"
        )

    def __str__(self):
        return (
            f"StudyInfo for User {self.user_id} — "
            f"Direction: {self.study_direction.name if self.study_direction else 'N/A'}, "
            f"Form: {self.study_form.name if self.study_form else 'N/A'}, "
            f"Language: {self.study_language.name if self.study_language else 'N/A'}"
        )
