import uuid
from typing import List, Optional
from datetime import datetime
from sqlalchemy import String, Boolean, Integer, DateTime, Text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base import Base, TimestampMixin

class Company(Base, TimestampMixin):
    __tablename__ = "companies"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    ticker: Mapped[str] = mapped_column(String(10), unique=True, index=True, nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    sector: Mapped[Optional[str]] = mapped_column(String(100), index=True)
    industry: Mapped[Optional[str]] = mapped_column(String(100), index=True)
    exchange: Mapped[Optional[str]] = mapped_column(String(20), index=True) # NYSE, NASDAQ
    country: Mapped[Optional[str]] = mapped_column(String(50))
    currency: Mapped[str] = mapped_column(String(10), default="USD")
    description: Mapped[Optional[str]] = mapped_column(Text)
    logo_url: Mapped[Optional[str]] = mapped_column(String(500))
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)

    # Relaciones con otros modelos
    statements: Mapped[List["FinancialStatement"]] = relationship(
        "FinancialStatement", back_populates="company", cascade="all, delete-orphan"
    )
    metrics: Mapped[List["KeyMetric"]] = relationship(
        "KeyMetric", back_populates="company", cascade="all, delete-orphan"
    )
    valuations: Mapped[List["Valuation"]] = relationship(
        "Valuation", back_populates="company", cascade="all, delete-orphan"
    )
    lbo_analyses: Mapped[List["LBOAnalysis"]] = relationship(
        "LBOAnalysis", back_populates="company", cascade="all, delete-orphan"
    )


class CompanyUniverse(Base):
    """
    Control del universo de empresas para la estrategia 'Search & Discover'
    y optimización de cuota de API (FMP 250 calls/día).
    """
    __tablename__ = "company_universe"

    ticker: Mapped[str] = mapped_column(String(10), primary_key=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    exchange: Mapped[Optional[str]] = mapped_column(String(20))
    sector: Mapped[Optional[str]] = mapped_column(String(100))
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    first_fetched: Mapped[Optional[datetime]] = mapped_column(DateTime(timezone=True))
    last_synced: Mapped[Optional[datetime]] = mapped_column(DateTime(timezone=True))
    sync_priority: Mapped[int] = mapped_column(Integer, default=0) # 0=on-demand, 1=weekly, 2=daily
    data_quality: Mapped[int] = mapped_column(Integer, default=0)  # 0=parcial, 1=completo, 2=verificado
