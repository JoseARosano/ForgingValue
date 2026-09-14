import uuid
from datetime import datetime, timezone
from typing import Optional, TYPE_CHECKING
from sqlalchemy import String, Numeric, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import UUID, JSONB
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base import Base

if TYPE_CHECKING:
    from app.models.company import Company

class Valuation(Base):
    __tablename__ = "valuations"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    company_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey("companies.id", ondelete="CASCADE"), nullable=False, index=True)

    model_type: Mapped[str] = mapped_column(String(20), nullable=False) # 'dcf', 'graham'
    
    # Supuestos definidos por el usuario o generados automáticamente
    # Ej: { "growth_rate": 0.08, "wacc": 0.09, "terminal_growth": 0.025, "projection_years": 5 }
    assumptions: Mapped[dict] = mapped_column(JSONB, nullable=False)

    # Resultados calculados
    intrinsic_value: Mapped[float] = mapped_column(Numeric(12, 2), nullable=False)
    current_price: Mapped[Optional[float]] = mapped_column(Numeric(12, 2))
    margin_of_safety_pct: Mapped[Optional[float]] = mapped_column(Numeric(6, 4)) # Ej: 0.2540 (+25.4%)

    # Matriz de sensibilidad (WACC x Terminal Growth)
    sensitivity_matrix: Mapped[Optional[dict]] = mapped_column(JSONB)

    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))

    # Relación
    company: Mapped["Company"] = relationship("Company", back_populates="valuations")
