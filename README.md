1. Header & Vision
# Fintech Asset Integrity Monitor
A high-performance monitoring engine designed for institutional digital asset management. This system ensures mandate compliance and real-time risk mitigation through automated price-drift detection.

2. The Problem (Contexto de Negócio)
Aqui ligas ao que a SCRYPT faz.

Institutional investors require 24/7 oversight of their assets. Manual monitoring is prone to human error and latency. This solution automates the detection of "Mandate Breaches" (e.g., unexpected price drops) to protect Assets Under Management (AUM).

3. Key Features
Real-time Ingestion: Async WebSocket integration with Tier-1 exchanges.

Risk Engine: Automated calculation of price volatility and drift using Python/Pandas.

Institutional Dashboard: High-performance React UI with atomic state updates.

Audit Trail: Every breach is logged with millisecond precision for compliance reporting.

4. Tech Stack & Architecture Decisions
Esta é a parte onde justificas as tuas escolhas (o CISO vai ler isto com atenção).

Backend (Python/FastAPI): Chosen for its superior data processing capabilities and async I/O performance.

Frontend (Next.js/Zustand): Implemented to ensure zero-lag rendering during high-frequency data updates.

Reliability: Integrated Pydantic models for strict data validation, preventing "garbage-in, garbage-out" scenarios.

5. Quick Start (How to run)
