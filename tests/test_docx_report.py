from app.database.database import SessionLocal

from app.services.report_service import ReportService
from app.services.docx_report_service import DocxReportService

db = SessionLocal()

report = ReportService.generate(db)

docx = DocxReportService.generate(report)

print("=" * 60)
print("DOCX REPORT TEST")
print("=" * 60)

print("DOCX Report Created:")
print(docx)

db.close()