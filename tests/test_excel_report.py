from app.database.database import SessionLocal

from app.services.report_service import ReportService
from app.services.excel_report_service import ExcelReportService

db = SessionLocal()

report = ReportService.generate(db)

excel = ExcelReportService.generate(report)

print("=" * 60)
print("EXCEL REPORT TEST")
print("=" * 60)

print("Excel Report Created:")
print(excel)

db.close()