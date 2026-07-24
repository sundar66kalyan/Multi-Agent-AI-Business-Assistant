# app/routes/report_routes.py

from fastapi import APIRouter, Depends, HTTPException  # ← NEW IMPORT
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.services.report_service import ReportService
from app.services.pdf_report_service import PDFReportService
from app.services.excel_report_service import ExcelReportService
from app.services.docx_report_service import DocxReportService

router = APIRouter(
    prefix="/report",
    tags=["Report"],
)


@router.get("/summary")
def business_report(db: Session = Depends(get_db)):
    """
    Generate Business Report Summary
    """

    report = ReportService.generate(db)

    return {
        "success": True,
        "data": report,
    }


@router.get("/pdf")
def download_pdf(db: Session = Depends(get_db)):
    """
    Generate and download PDF Business Report.
    """

    report = ReportService.generate(db)

    pdf_path = PDFReportService.generate(report)

    return FileResponse(
        path=pdf_path,
        filename="Business_Report.pdf",
        media_type="application/pdf",
    )


@router.get("/excel")
def download_excel(db: Session = Depends(get_db)):
    """
    Generate and download Excel Business Report.
    """

    report = ReportService.generate(db)

    excel_path = ExcelReportService.generate(report)

    return FileResponse(
        path=excel_path,
        filename="Business_Report.xlsx",
        media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
    )


@router.get("/docx")
def download_docx(db: Session = Depends(get_db)):
    """
    Generate and download DOCX Business Report.
    """

    report = ReportService.generate(db)

    docx_path = DocxReportService.generate(report)

    return FileResponse(
        path=docx_path,
        filename="Business_Report.docx",
        media_type="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
    )


@router.get("/export")
def export_report(
    format: str,
    db: Session = Depends(get_db)
):
    """
    Export Business Report
    Supported formats: pdf, excel, docx
    """

    report = ReportService.generate(db)

    format = format.lower()

    if format == "pdf":
        path = PDFReportService.generate(report)

        return FileResponse(
            path=path,
            filename="Business_Report.pdf",
            media_type="application/pdf"
        )

    elif format == "excel":
        path = ExcelReportService.generate(report)

        return FileResponse(
            path=path,
            filename="Business_Report.xlsx",
            media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )

    elif format == "docx":
        path = DocxReportService.generate(report)

        return FileResponse(
            path=path,
            filename="Business_Report.docx",
            media_type="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
        )

    raise HTTPException(
        status_code=400,
        detail="Supported formats: pdf, excel, docx"
    )