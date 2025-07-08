from datetime import datetime, timezone
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import TYPE_CHECKING
from sharq_models.database import Base

# --- User ---
if TYPE_CHECKING:
    from .passport_data import PassportData
    from .study_info import StudyInfo

class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    phone_number: Mapped[str] = mapped_column(nullable=True)
    password: Mapped[str] = mapped_column(nullable=True)
    
    role_id: Mapped[int] = mapped_column(ForeignKey("roles.id"), nullable=False)
    role: Mapped["Role"] = relationship("Role", back_populates="users")

    passport_data: Mapped["PassportData"] = relationship(
        "PassportData", back_populates="user", uselist=False, cascade="all, delete-orphan"
    )
    study_info: Mapped["StudyInfo"] = relationship(
        "StudyInfo", back_populates="user", uselist=False, cascade="all, delete-orphan"
    )
    
    def __repr__(self):
        return f"<User(id={self.id}, phone_number='{self.phone_number}')>"

    def __str__(self):
        return f"User {self.id} - Phone: {self.phone_number}"


class Role(Base):
    __tablename__ = "roles"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)

    users: Mapped[list["User"]] = relationship("User", back_populates="role")

    def __repr__(self):
        return f"<Role(id={self.id}, name='{self.name}')>"
    
    def __str__(self):
        return f"Role {self.id} - Name: {self.name}"
    
    
class SMSVerificationSession(Base):
    __tablename__ = "sms_verification_sessions"
    
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    phone_number: Mapped[str] = mapped_column(nullable=False, index=True)
    code: Mapped[str] = mapped_column(nullable=False)
    created_at: Mapped[datetime] = mapped_column(default=datetime.now(timezone.utc), nullable=False)
    expires_at: Mapped[datetime] = mapped_column(nullable=False)
    verified: Mapped[bool] = mapped_column(default=False, nullable=False)
    attempts: Mapped[int] = mapped_column(default=0, nullable=False)
    
    
    def __repr__(self):
        return f"<SMSVerificationSession(id={self.id}, phone_number='{self.phone_number}')>"
    
    def __str__(self):
        return f"SMSVerificationSession {self.id} - Phone: {self.phone_number}"
    
    def is_expired(self) -> bool:
        return datetime.now(timezone.utc) > self.expires_at
    
    def is_valid(self) -> bool:
        return not self.is_expired() and not self.verified 
    
    
