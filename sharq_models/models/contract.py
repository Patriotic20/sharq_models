from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey
from sharq_models.database import Base
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .user import User

class Contract(Base):
    __tablename__ = "contracts"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    file_path: Mapped[str] = mapped_column()
    status: Mapped[bool] = mapped_column(default=False, server_default="false")
    
    user: Mapped["User"] = relationship("User", back_populates="contracts")
