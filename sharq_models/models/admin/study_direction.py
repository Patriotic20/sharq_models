from sqlalchemy.orm import Mapped, mapped_column , relationship
from sqlalchemy import String,  Integer, Numeric, ForeignKey
from sharq_models.database import Base
from typing import TYPE_CHECKING

from sharq_models.models.admin.study_lenguage import StudyLanguage


if TYPE_CHECKING:
    from models.study_info import StudyInfo, StudyForm, StudyType, EducationType


class StudyDirection(Base):
    __tablename__ = "study_directions"

    id: Mapped[int] = mapped_column(primary_key=True)
    
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    exam_title: Mapped[str] = mapped_column(String(255), nullable=False)
    
    education_years: Mapped[int] = mapped_column(Integer, nullable=False)
    contract_sum: Mapped[float] = mapped_column(Numeric(10, 2), nullable=False)
    study_code: Mapped[str] = mapped_column(String(50), nullable=False, unique=True)
    
    study_form_id: Mapped[int] = mapped_column(Integer, ForeignKey("study_forms.id"), nullable=False)
    study_type_id: Mapped[int] = mapped_column(Integer, ForeignKey("study_types.id"), nullable=False)
    study_language_id: Mapped[int] = mapped_column(Integer, ForeignKey("study_languages.id"), nullable=False)
    education_type_id: Mapped[int] = mapped_column(Integer, ForeignKey("education_types.id"), nullable=False)

    status: Mapped[str] = mapped_column(String(50), nullable=False, default="inactive")

    study_form: Mapped["StudyForm"] = relationship("StudyForm", back_populates="study_directions")
    study_language: Mapped["StudyLanguage"] = relationship("StudyLanguage", back_populates="study_directions")
    study_type: Mapped["StudyType"] = relationship("StudyType", back_populates="study_directions")
    education_type: Mapped["EducationType"] = relationship("EducationType", back_populates="study_directions")
    
    
    
    study_infos: Mapped["StudyInfo"] = relationship("StudyInfo" , back_populates="study_direction")


    def __repr__(self):
        return (
            f"<StudyDirection(id={self.id}, name='{self.name}', study_form='{self.study_form}', "
            f"contract_sum='{self.contract_sum}', education_years='{self.education_years}', "
            f"study_code='{self.study_code}')>"
        )
