from datetime import datetime, timezone
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import JSON
from sharq_models.models.user import User
from sharq_models.database import Base


class AMOCrmLead(Base):
    __tablename__ = "amo_crm_leads"
    
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    
    user_id: Mapped[int] = mapped_column(nullable=False, index=True)
    
    contact_id: Mapped[int] = mapped_column(nullable=False, index=True)
    lead_id: Mapped[int] = mapped_column(nullable=False, index=True)
    
    phone_number: Mapped[str] = mapped_column(nullable=False, index=True)
    
    contact_data: Mapped[dict] = mapped_column(JSON, nullable=False)
    lead_data: Mapped[dict] = mapped_column(JSON, nullable=False)

    created_at: Mapped[datetime] = mapped_column(default=datetime.now(timezone.utc), nullable=False)
    updated_at: Mapped[datetime] = mapped_column(default=datetime.now(timezone.utc), nullable=False)
    
    def __repr__(self):
        return f"<AMOCrmLead(id={self.id}, contact_id={self.contact_id}, lead_id={self.lead_id})>"
    
    def __str__(self):
        return f"AMOCrmLead {self.id} - Contact: {self.contact_id}, Lead: {self.lead_id}"