import uuid
from datetime import date, datetime, timezone
from typing import Optional, TYPE_CHECKING
from sqlalchemy import String, Date, Numeric, DateTime, ForeignKey, Index
from sqlalchemy.dialects.postgresql import UUID, JSONB
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base import Base

if TYPE_CHECKING:
    from app.models.company import Company

class FinancialStatement(Base):
    __tablename__ = "financial_statements"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    company_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey("companies.id", ondelete="CASCADE"), nullable=False, index=True)
    
    statement_type: Mapped[str] = mapped_column(String(20), nullable=False) # 'income', 'balance', 'cashflow'
    period: Mapped[str] = mapped_column(String(10), nullable=False)         # 'annual', 'quarter'
    fiscal_date: Mapped[date] = mapped_column(Date, nullable=False)
    fiscal_year: Mapped[int] = mapped_column(nullable=False)
    fiscal_quarter: Mapped[Optional[int]] = mapped_column(nullable=True)    # 1, 2, 3, 4 o None si anual

    # Payload completo obtenido de la API para máxima flexibilidad
    raw_data: Mapped[dict] = mapped_column(JSONB, nullable=False, default=dict)

    # Campos normalizados clave para consultas rápidas y modelos financieros
    revenue: Mapped[Optional[float]] = mapped_column(Numeric(18, 2))
    cost_of_revenue: Mapped[Optional[float]] = mapped_column(Numeric(18, 2))
    gross_profit: Mapped[Optional[float]] = mapped_column(Numeric(18, 2))
    operating_income: Mapped[Optional[float]] = mapped_column(Numeric(18, 2)) # EBIT
    ebitda: Mapped[Optional[float]] = mapped_column(Numeric(18, 2))
    net_income: Mapped[Optional[float]] = mapped_column(Numeric(18, 2))
    
    total_assets: Mapped[Optional[float]] = mapped_column(Numeric(18, 2))
    total_liabilities: Mapped[Optional[float]] = mapped_column(Numeric(18, 2))
    total_equity: Mapped[Optional[float]] = mapped_column(Numeric(18, 2))
    total_debt: Mapped[Optional[float]] = mapped_column(Numeric(18, 2))
    cash_and_equivalents: Mapped[Optional[float]] = mapped_column(Numeric(18, 2))
    
    cash_from_operations: Mapped[Optional[float]] = mapped_column(Numeric(18, 2)) # CFO
    capex: Mapped[Optional[float]] = mapped_column(Numeric(18, 2))
    free_cash_flow: Mapped[Optional[float]] = mapped_column(Numeric(18, 2))        # FCF

    fetched_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))

    # Relación
    company: Mapped["Company"] = relationship("Company", back_populates="statements")

    __table_args__ = (
        Index("ix_statement_lookup", "company_id", "statement_type", "period", "fiscal_date", unique=True),
    )
