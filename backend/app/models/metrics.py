import uuid
from datetime import date, datetime, timezone
from typing import Optional, TYPE_CHECKING
from sqlalchemy import Date, Numeric, Integer, DateTime, ForeignKey, Index
from sqlalchemy.dialects.postgresql import UUID, JSONB
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base import Base

if TYPE_CHECKING:
    from app.models.company import Company

class KeyMetric(Base):
    __tablename__ = "key_metrics"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    company_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey("companies.id", ondelete="CASCADE"), nullable=False, index=True)
    fiscal_date: Mapped[date] = mapped_column(Date, nullable=False)

    # 1. Rentabilidad
    roic: Mapped[Optional[float]] = mapped_column(Numeric(8, 4)) # Return on Invested Capital
    roe: Mapped[Optional[float]] = mapped_column(Numeric(8, 4))  # Return on Equity
    roa: Mapped[Optional[float]] = mapped_column(Numeric(8, 4))  # Return on Assets
    gross_margin: Mapped[Optional[float]] = mapped_column(Numeric(8, 4))
    operating_margin: Mapped[Optional[float]] = mapped_column(Numeric(8, 4))
    net_margin: Mapped[Optional[float]] = mapped_column(Numeric(8, 4))

    # 2. Solvencia & Apalancamiento
    debt_to_ebitda: Mapped[Optional[float]] = mapped_column(Numeric(8, 2))
    debt_to_equity: Mapped[Optional[float]] = mapped_column(Numeric(8, 2))
    current_ratio: Mapped[Optional[float]] = mapped_column(Numeric(8, 2))
    interest_coverage: Mapped[Optional[float]] = mapped_column(Numeric(8, 2))

    # 3. Valoración de Mercado & Yields
    pe_ratio: Mapped[Optional[float]] = mapped_column(Numeric(8, 2))
    pb_ratio: Mapped[Optional[float]] = mapped_column(Numeric(8, 2))
    ev_to_ebitda: Mapped[Optional[float]] = mapped_column(Numeric(8, 2))
    fcf_yield: Mapped[Optional[float]] = mapped_column(Numeric(8, 4))
    dividend_yield: Mapped[Optional[float]] = mapped_column(Numeric(8, 4))

    # 4. Scoring Cuantitativo
    piotroski_f_score: Mapped[Optional[int]] = mapped_column(Integer) # 0 a 9
    piotroski_breakdown: Mapped[Optional[dict]] = mapped_column(JSONB) # 9 señales individuales
    greenblatt_earnings_yield: Mapped[Optional[float]] = mapped_column(Numeric(8, 4))
    greenblatt_roic: Mapped[Optional[float]] = mapped_column(Numeric(8, 4))
    greenblatt_combined_rank: Mapped[Optional[int]] = mapped_column(Integer)

    calculated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))

    # Relación
    company: Mapped["Company"] = relationship("Company", back_populates="metrics")

    __table_args__ = (
        Index("ix_metrics_lookup", "company_id", "fiscal_date", unique=True),
    )
