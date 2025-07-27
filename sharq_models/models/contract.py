from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey
from sharq_models.database import Base
from typing import TYPE_CHECKING
from datetime import datetime
if TYPE_CHECKING:
    from .user import User

class Contract(Base):
    __tablename__ = "contracts"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    file_path: Mapped[str] = mapped_column(nullable=True)
    file_url: Mapped[str] = mapped_column(nullable=True)
    status: Mapped[bool] = mapped_column(default=False, server_default="false")
    
    contract_type: Mapped[str] = mapped_column(nullable=True)
    
    user: Mapped["User"] = relationship("User", back_populates="contracts")
    
    created_at: Mapped[datetime] = mapped_column(default=datetime.now)
    updated_at: Mapped[datetime] = mapped_column(default=datetime.now)
