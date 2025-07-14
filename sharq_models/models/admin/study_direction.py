from sqlalchemy.orm import Mapped, mapped_column , relationship
from sqlalchemy import String,  Integer, Numeric
from sharq_models.database import Base
from sharq_models.models.study_info import StudyInfo



class StudyDirection(Base):
    __tablename__ = "study_directions"

    id: Mapped[int] = mapped_column(primary_key=True)
    
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    exam_title: Mapped[str] = mapped_column(String(255), nullable=False)
    
    education_years: Mapped[int] = mapped_column(Integer, nullable=False)
    contract_sum: Mapped[float] = mapped_column(Numeric(10, 2), nullable=False)
    study_code: Mapped[str] = mapped_column(String(50), nullable=False, unique=True)
    
    status: Mapped[str] = mapped_column(String(50), nullable=False, default="inactive")
    
    study_infos: Mapped[list["StudyInfo"]] = relationship("StudyInfo", back_populates="study_direction")
    
    def __repr__(self):
        return (
            f"<StudyDirection(id={self.id}, name='{self.name}', study_form='{self.study_form}', "
            f"contract_sum='{self.contract_sum}', education_years='{self.education_years}', "
            f"study_code='{self.study_code}')>"
        )
