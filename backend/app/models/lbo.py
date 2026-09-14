import uuid
from datetime import datetime, timezone
from typing import Optional, TYPE_CHECKING
from sqlalchemy import Numeric, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import UUID, JSONB
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base import Base

if TYPE_CHECKING:
    from app.models.company import Company

class LBOAnalysis(Base):
    __tablename__ = "lbo_analyses"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    company_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey("companies.id", ondelete="CASCADE"), nullable=False, index=True)

    # 1. Supuestos de transacción
    # Ej: { "entry_multiple": 8.5, "senior_debt_pct": 0.40, "sub_debt_pct": 0.20, "exit_year": 5, "exit_multiple": 8.5 }
    transaction_assumptions: Mapped[dict] = mapped_column(JSONB, nullable=False)

    # 2. Estructura de Sources & Uses
    sources_uses: Mapped[dict] = mapped_column(JSONB, nullable=False)

    # 3. Proyecciones operativas (P&L proyectado 5 años)
    operating_projections: Mapped[dict] = mapped_column(JSONB, nullable=False)

    # 4. Calendario de amortización y desapalancamiento (Debt Schedule con Cash Sweep)
    debt_schedule: Mapped[dict] = mapped_column(JSONB, nullable=False)

    # 5. Métricas de retorno
    irr: Mapped[float] = mapped_column(Numeric(8, 4), nullable=False)  # Tasa Interna de Retorno (Ej: 0.2250 -> 22.5%)
    moic: Mapped[float] = mapped_column(Numeric(6, 2), nullable=False) # Múltiplo de Capital Invertido (Ej: 2.85x)

    # 6. Matriz de sensibilidad (Entry Multiple x Exit Multiple -> IRR & MOIC)
    sensitivity_matrix: Mapped[Optional[dict]] = mapped_column(JSONB)

    # 7. Desglose de creación de valor (EBITDA growth, Multiple expansion, Debt paydown)
    value_drivers: Mapped[Optional[dict]] = mapped_column(JSONB)

    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))

    # Relación
    company: Mapped["Company"] = relationship("Company", back_populates="lbo_analyses")
