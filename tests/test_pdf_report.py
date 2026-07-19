from app.database.database import SessionLocal

from app.services.report_service import ReportService
from app.services.pdf_report_service import PDFReportService


db = SessionLocal()

print("=" * 60)
print("PDF REPORT TEST")
print("=" * 60)

# Generate report text
report = ReportService.generate(db)

# Generate PDF
pdf_path = PDFReportService.generate(report)

print(f"PDF Generated Successfully!")

print(f"Location : {pdf_path}")

db.close()