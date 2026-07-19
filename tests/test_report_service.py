from app.database.database import SessionLocal
from app.services.report_service import ReportService

db = SessionLocal()

result = ReportService.generate(db)

print("=" * 60)
print("REPORT SERVICE TEST")
print("=" * 60)

print(result)

db.close()