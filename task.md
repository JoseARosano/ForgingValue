# 📝 Tareas de InvestIQ

- `[ ]` uncompleted tasks
- `[/]` in progress tasks
- `[x]` completed tasks

## Fase 0 — Diseño y Arquitectura (Semana 1-2)
- `[/]` Inicializar repositorio y monorepo
  - `[ ]` Crear `/backend` (FastAPI)
  - `[ ]` Crear `/frontend` (React + Vite + TS)
- `[ ]` Configurar `docker-compose.yml` (Postgres, Redis, Backend, Frontend, Celery)
- `[ ]` Escribir `README.md` profesional con arquitectura
- `[ ]` Diseñar esquema de base de datos (Backend - Alembic init)
- `[ ]` Setup i18n base en frontend (`es/`, `en/`)
- `[ ]` Configurar CI/CD base en GitHub Actions

## Fase 1 — Backend Core & Ingesta de Datos (Semana 3-5)
- `[ ]` **Sprint 1.1 — Fundamentos del Backend**
  - `[ ]` Configurar FastAPI, dependencias
  - `[ ]` Configurar SQLAlchemy (Neon) + Upstash Redis
  - `[ ]` Crear modelos SQLAlchemy (`Company`, `FinancialStatement`, `KeyMetric`, `CompanyUniverse`, `Valuation`, `LboAnalysis`)
  - `[ ]` Middlewares (CORS, error handling)
- `[ ]` **Sprint 1.2 — Sistema de Providers & Ingesta**
  - `[ ]` `DataProvider` interface
  - `[ ]` `FMPProvider`
  - `[ ]` `AlphaVantageProvider`
  - `[ ]` `QuotaManager`
  - `[ ]` Lazy loading endpoints (`/search`, `/companies/{ticker}`)
  - `[ ]` Tareas de Celery (`sync_company`)
- `[ ]` **Sprint 1.3 — Motor de Métricas & 3-Model Backend**
  - `[ ]` `MetricsCalculator` (30+ KPIs)
  - `[ ]` `ThreeStatementModel`
  - `[ ]` Endpoints (`/metrics`, `/statements`, `/three-model`)

## Fase 2 — Motores de Valoración & Scoring (Semana 6-10)
- `[ ]` **Sprint 2.1 — DCF Interactivo**
  - `[ ]` Servicio `DCFValuation`
  - `[ ]` Endpoints DCF
- `[ ]` **Sprint 2.2 — Modelos de Scoring**
  - `[ ]` `PiotroskiFScore`
  - `[ ]` `GreenblattMagicFormula`
  - `[ ]` `Screener` engine y endpoints
- `[ ]` **Sprint 2.3 — Motor LBO**
  - `[ ]` Servicio `LBOModel` (Sources & Uses, Debt Schedule, Returns)
  - `[ ]` Endpoints LBO

## Fase 3 — Frontend & UX Premium (Semana 11-17)
- `[ ]` **Sprint 3.1 — Design System & i18n**
  - `[ ]` Tailwind / Shadcn UI setup
  - `[ ]` React Query + Axios
- `[ ]` **Sprint 3.2 — Dashboard Principal**
- `[ ]` **Sprint 3.3 — 3-Model Statement UI**
- `[ ]` **Sprint 3.4 — DCF Interactivo UI**
- `[ ]` **Sprint 3.5 — LBO Interactivo UI**
- `[ ]` **Sprint 3.6 — Screener & Scoring UI**
- `[ ]` **Sprint 3.7 — Peer Comparison**

## Fase 4 — Educación Integrada & Glosario (Semana 18)
- `[ ]` Componentes Tooltip contextuales
- `[ ]` Página `/learn` interactiva

## Fase 5 — Auth (Opcional), Polish & Testing (Semana 19-21)
- `[ ]` Watchlist en `localStorage`
- `[ ]` (Opcional) Auth JWT
- `[ ]` Testing E2E, Unit Tests

## Fase 6 — Despliegue & Documentación (Semana 22)
- `[ ]` Deploy (Vercel + Render)
- `[ ]` Revisión final README
