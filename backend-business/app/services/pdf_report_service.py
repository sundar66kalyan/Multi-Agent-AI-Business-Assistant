# app/services/pdf_report_service.py

from pathlib import Path
from datetime import datetime

from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
    Image,
)

from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.enums import TA_CENTER
from reportlab.lib import colors

from app.services.chart_service import ChartService  # ← NEW IMPORT


class PDFReportService:

    @staticmethod
    def generate(report_data: dict):
        """
        Generate a PDF report from report data.
        
        Args:
            report_data (dict): Dictionary containing report, finance, and analytics data
            
        Returns:
            str: Path to the generated PDF file
        """
        # Extract data from report_data
        finance = report_data["finance"]
        analytics = report_data["analytics"]
        report_text = report_data["report"]

        # Generate revenue chart
        chart_path = ChartService.revenue_chart(finance)  # ← NEW: Generate chart

        reports_dir = Path("reports")
        reports_dir.mkdir(exist_ok=True)

        # Generate unique filename with timestamp
        filename = f"Business_Report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"
        output_file = reports_dir / filename

        doc = SimpleDocTemplate(str(output_file))

        styles = getSampleStyleSheet()

        title = styles["Heading1"]
        title.alignment = TA_CENTER

        heading = styles["Heading2"]
        heading.alignment = TA_CENTER

        body = styles["BodyText"]
        body.alignment = TA_CENTER

        story = []

        # ============================================================
        # LOGO SECTION
        # ============================================================
        logo_path = Path("assets/logo/logo.png")

        if logo_path.exists():
            logo = Image(str(logo_path))
            logo.drawHeight = 80
            logo.drawWidth = 80
            story.append(logo)
            story.append(Spacer(1, 10))

        # ============================================================
        # HEADER / TITLE SECTION
        # ============================================================
        story.append(
            Paragraph(
                "MULTI-AGENT AI BUSINESS ASSISTANT",
                title,
            )
        )

        # Company Information
        story.append(
            Paragraph(
                "Kalyana Sundar AI Solutions.",
                body,
            )
        )

        story.append(
            Paragraph(
                "Tirunelveli, Tamil Nadu, India",
                body,
            )
        )

        story.append(
            Paragraph(
                "support@kalyanasundaraisolutions.com",
                body,
            )
        )

        story.append(
            Paragraph(
                "www.ksaisolutions.com",
                body,
            )
        )

        story.append(Spacer(1, 12))

        # ============================================================
        # REPORT TITLE SECTION
        # ============================================================
        story.append(
            Paragraph(
                "Enterprise Business Report",
                heading,
            )
        )

        story.append(
            Paragraph(
                f"Generated On: {datetime.now().strftime('%d-%b-%Y %I:%M %p')}",
                body,
            )
        )

        story.append(Spacer(1, 20))

        # Divider line
        story.append(
            Paragraph(
                "<hr width='100%'/>",
                body,
            )
        )

        story.append(Spacer(1, 12))

        # ============================================================
        # FINANCE TABLE
        # ============================================================
        finance_table = Table(
            [
                ["Metric", "Value"],
                ["Revenue", str(finance["revenue"])],
                ["Expenses", str(finance["expenses"])],
                ["Profit", str(finance["profit"])],
                ["Month", finance["month"]],
            ],
            colWidths=[180, 180],
        )

        finance_table.setStyle(
            TableStyle(
                [
                    ("BACKGROUND", (0, 0), (-1, 0), colors.grey),
                    ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
                    ("GRID", (0, 0), (-1, -1), 1, colors.black),
                    ("BACKGROUND", (0, 1), (-1, -1), colors.beige),
                    ("BOTTOMPADDING", (0, 0), (-1, 0), 8),
                ]
            )
        )

        story.append(Paragraph("<b>Finance Summary</b>", heading))
        story.append(finance_table)

        # ============================================================
        # REVENUE CHART SECTION
        # ============================================================
        story.append(Spacer(1, 15))

        story.append(
            Paragraph(
                "Revenue Analysis",
                heading,
            )
        )

        story.append(Spacer(1, 8))

        # Add the revenue chart image
        chart = Image(chart_path)
        chart.drawWidth = 400
        chart.drawHeight = 260
        story.append(chart)

        story.append(Spacer(1, 20))

        # ============================================================
        # ANALYTICS TABLE
        # ============================================================
        analytics_table = Table(
            [
                ["Metric", "Value"],
                ["Indexed Documents", str(analytics["documents"])],
                ["Chunks", str(analytics["chunks"])],
                ["Finance Records", str(analytics["finance_records"])],
            ],
            colWidths=[180, 180],
        )

        analytics_table.setStyle(
            TableStyle(
                [
                    ("BACKGROUND", (0, 0), (-1, 0), colors.darkblue),
                    ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
                    ("GRID", (0, 0), (-1, -1), 1, colors.black),
                    ("BACKGROUND", (0, 1), (-1, -1), colors.whitesmoke),
                    ("BOTTOMPADDING", (0, 0), (-1, 0), 8),
                ]
            )
        )

        story.append(Paragraph("<b>System Analytics</b>", heading))
        story.append(analytics_table)

        # ============================================================
        # FOOTER
        # ============================================================
        story.append(Spacer(1, 30))
        footer_style = styles["Normal"]
        footer_style.alignment = TA_CENTER
        story.append(
            Paragraph(
                f"Generated by Multi-Agent AI Assistant • {datetime.now().strftime('%Y')}",
                footer_style,
            )
        )

        # Build the document
        doc.build(story)

        return str(output_file)