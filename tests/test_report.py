from app.database.database import SessionLocal

from app.services.report_service import ReportService

db = SessionLocal()

print("=" * 60)
print("BUSINESS REPORT")
print("=" * 60)

print(
    ReportService.generate(db)
)

db.close()