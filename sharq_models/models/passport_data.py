from sharq_models.database import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey
from datetime import date as py_date
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .user import User
    from .application import Application


class PassportData(Base):
    __tablename__ = "passport_data"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))

    # From PersonalInfo
    first_name: Mapped[str] 
    last_name: Mapped[str] 
    third_name: Mapped[str]   # fatherName
    date_of_birth: Mapped[py_date]   # birthDate
    passport_series_number: Mapped[str] 
    jshshir: Mapped[str] 
    issue_date: Mapped[py_date]
    gender: Mapped[str] 
    passport_filepath: Mapped[str]

    # Additional fields from PersonalInfo
    citizenship: Mapped[str] 
    nationality: Mapped[str] 
    country: Mapped[str] 
    region: Mapped[str] 
    district: Mapped[str] 
    address: Mapped[str] 
    

    
    user: Mapped["User"] = relationship("User", back_populates="passport_data")
    application: Mapped["Application"] = relationship("Application", back_populates="passport_data", uselist=False)

    def __repr__(self):
        return (
            f"<PassportData(id={self.id}, user_id={self.user_id}, "
            f"passport='{self.passport_series_number}', issue_date={self.issue_date})>"
        )

    def __str__(self):
        return (
            f"PassportData for User {self.user_id}: "
            f"{self.passport_series_number}, Issued: {self.issue_date}"
        )
