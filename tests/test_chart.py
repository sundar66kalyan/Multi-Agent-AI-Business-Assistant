from app.database.database import SessionLocal

from app.services.report_service import ReportService
from app.services.chart_service import ChartService

db = SessionLocal()

report = ReportService.generate(db)

chart = ChartService.revenue_chart(report["finance"])

print("=" * 60)
print("CHART TEST")
print("=" * 60)

print("Chart Created:")

print(chart)

db.close()