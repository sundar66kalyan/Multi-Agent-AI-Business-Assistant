# app/routes/dashboard_routes.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from pathlib import Path
import logging
import os
from datetime import datetime

from app.database.database import get_db
from app.dependencies.auth import get_current_user
from app.models.user import User

from app.services.finance_service import FinanceService
from app.services.analytics_service import AnalyticsService
# from app.services.rag_service import RAGService

from app.orchestrator.orchestrator_service import AgentManager

logger = logging.getLogger(__name__)

router = APIRouter(
    prefix="/dashboard",
    tags=["Dashboard"],
)


@router.get("/summary")
def dashboard_summary(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """
    Enterprise Dashboard Summary
    """
    try:
        finance = FinanceService.answer_question(
            db,
            "summary",
        )

        analytics = AnalyticsService.system_summary(db)

        # RAG service status (commented out - not connected)
        # rag = RAGService().status()
        rag = {
            "message": "RAG service not connected"
        }

        # Agent manager
        manager = AgentManager()
        agent_names = manager.list_agents()

        return {
            "success": True,
            "timestamp": datetime.now().isoformat(),
            "user": {
                "name": current_user.full_name,
                "email": current_user.email,
                "role": current_user.role
            },
            "dashboard": {
                "finance": finance,
                "analytics": analytics,
                "rag": rag,
                "agents": [
                    {
                        "name": name,
                        "status": "Running",
                        "description": _get_agent_description(name)
                    }
                    for name in agent_names
                ],
                "agent_count": len(agent_names),
            },
        }
    except Exception as e:
        logger.error(f"Error generating dashboard summary: {str(e)}")
        return {
            "success": False,
            "error": str(e),
            "message": "Failed to generate dashboard summary"
        }


@router.get("/metrics")
def business_metrics(db: Session = Depends(get_db)):
    """
    Business KPI Metrics
    """
    try:
        finance = FinanceService.answer_question(
            db,
            "summary",
        )

        analytics = AnalyticsService.system_summary(db)

        revenue = finance.get("revenue", 0)
        expenses = finance.get("expenses", 0)
        profit = finance.get("profit", 0)

        profit_margin = 0
        if revenue > 0:
            profit_margin = round((profit / revenue) * 100, 2)

        return {
            "success": True,
            "timestamp": datetime.now().isoformat(),
            "metrics": {
                "revenue": revenue,
                "expenses": expenses,
                "profit": profit,
                "profit_margin": profit_margin,
                "documents": analytics.get("documents", 0),
                "chunks": analytics.get("chunks", 0),
                "finance_records": analytics.get("finance_records", 0),
                "month": finance.get("month", "N/A"),
            },
        }
    except Exception as e:
        logger.error(f"Error generating business metrics: {str(e)}")
        return {
            "success": False,
            "error": str(e),
            "message": "Failed to generate business metrics"
        }


@router.get("/agents")
def agent_status():
    """
    Registered Agent Status
    """
    try:
        # Agent manager (commented out - not connected)
        # manager = AgentManager()
        
        return {
            "success": True,
            "timestamp": datetime.now().isoformat(),
            "total_agents": 0,
            "agents": []
        }
    except Exception as e:
        logger.error(f"Error getting agent status: {str(e)}")
        return {
            "success": False,
            "error": str(e),
            "message": "Failed to get agent status"
        }


def _get_agent_description(name: str) -> str:
    """Get description for each agent type."""
    descriptions = {
        "Sales": "Handles sales, customer, and product inquiries",
        "Finance": "Handles financial data, revenue, and expense queries",
        "Document": "Handles document analysis and summarization",
        "HR": "Handles employee, leave, attendance, and payroll",
        "Marketing": "Handles campaigns, social media, and brand management",
        "Research": "Handles market research, analysis, and trends",
        "Analytics": "Handles dashboards, KPIs, and business intelligence",
        "Report": "Handles report generation and export",
        "General": "Fallback agent for general queries",
    }
    return descriptions.get(name, "No description available")


@router.get("/health")
def system_health():
    """
    System Health Status
    """
    try:
        # Agent manager (commented out - not connected)
        # manager = AgentManager()

        # Check database status
        db_status = "Connected"
        
        # Check vector database
        vector_db_path = Path("data/vector_db")
        vector_db = "Available" if vector_db_path.exists() else "Missing"
        
        # Check documents folder
        documents_path = Path("data/documents")
        documents = "Available" if documents_path.exists() else "Missing"
        
        # Check reports folder
        reports_path = Path("reports")
        reports = "Available" if reports_path.exists() else "Missing"
        
        # Check assets folder
        assets_path = Path("assets/logo")
        assets = "Available" if assets_path.exists() else "Missing"
        
        # Check if vector_db has files
        vector_db_files = 0
        if vector_db_path.exists():
            vector_db_files = len(list(vector_db_path.glob("*")))

        # Check if documents folder has files
        document_files = 0
        if documents_path.exists():
            document_files = len(list(documents_path.glob("*")))

        # Overall health status
        health_status = "Healthy"
        if vector_db == "Missing" or documents == "Missing":
            health_status = "Degraded"
        if vector_db == "Missing" and documents == "Missing":
            health_status = "Unhealthy"

        return {
            "success": True,
            "timestamp": datetime.now().isoformat(),
            "health": {
                "status": health_status,
                "database": db_status,
                "vector_database": vector_db,
                "vector_database_files": vector_db_files,
                "documents_folder": documents,
                "document_files": document_files,
                "reports_folder": reports,
                "assets_folder": assets,
                "registered_agents": 0,
                "memory_usage_mb": _get_memory_usage(),
            }
        }
    except Exception as e:
        logger.error(f"Error getting system health: {str(e)}")
        return {
            "success": False,
            "error": str(e),
            "message": "Failed to get system health"
        }


def _get_memory_usage() -> float:
    """Get current memory usage in MB."""
    try:
        import psutil
        process = psutil.Process(os.getpid())
        memory_mb = process.memory_info().rss / 1024 / 1024
        return round(memory_mb, 2)
    except ImportError:
        return 0.0
    except Exception:
        return 0.0


@router.get("/health/detailed")
def detailed_health():
    """
    Detailed System Health Status
    """
    try:
        # Agent manager (commented out - not connected)
        # manager = AgentManager()

        # Check all paths
        paths = {
            "data/vector_db": Path("data/vector_db"),
            "data/documents": Path("data/documents"),
            "data/metadata": Path("data/metadata"),
            "reports": Path("reports"),
            "assets/logo": Path("assets/logo"),
            "assets/charts": Path("assets/charts"),
        }

        path_status = {}
        for name, path in paths.items():
            if path.exists():
                if path.is_dir():
                    files = len(list(path.glob("*")))
                    path_status[name] = {
                        "exists": True,
                        "type": "directory",
                        "files": files,
                        "size_mb": round(_get_dir_size(path) / 1024 / 1024, 2),
                    }
                else:
                    path_status[name] = {
                        "exists": True,
                        "type": "file",
                        "size_mb": round(path.stat().st_size / 1024 / 1024, 2),
                    }
            else:
                path_status[name] = {
                    "exists": False,
                    "type": "missing",
                    "files": 0,
                    "size_mb": 0,
                }

        return {
            "success": True,
            "timestamp": datetime.now().isoformat(),
            "system": {
                "memory_usage_mb": _get_memory_usage(),
                "registered_agents": 0,
                "agent_names": [],
            },
            "paths": path_status,
        }
    except Exception as e:
        logger.error(f"Error getting detailed health: {str(e)}")
        return {
            "success": False,
            "error": str(e),
            "message": "Failed to get detailed health"
        }


def _get_dir_size(path: Path) -> int:
    """Get directory size in bytes."""
    total = 0
    try:
        for item in path.rglob("*"):
            if item.is_file():
                total += item.stat().st_size
    except Exception:
        pass
    return total


@router.get("/health/check-db")
def check_database(db: Session = Depends(get_db)):
    """
    Check database connection status.
    """
    try:
        # Try to execute a simple query
        from sqlalchemy import text
        db.execute(text("SELECT 1"))
        return {
            "success": True,
            "status": "Connected",
            "message": "Database connection successful"
        }
    except Exception as e:
        logger.error(f"Database connection error: {str(e)}")
        return {
            "success": False,
            "status": "Disconnected",
            "error": str(e),
            "message": "Database connection failed"
        }


@router.get("/charts/finance")
def finance_chart(db: Session = Depends(get_db)):
    """
    Finance Chart Data
    """

    finance = FinanceService.answer_question(
        db,
        "summary"
    )

    return {
        "success": True,
        "chart": {
            "labels": [
                "Revenue",
                "Expenses",
                "Profit"
            ],
            "values": [
                finance.get("revenue", 0),
                finance.get("expenses", 0),
                finance.get("profit", 0),
            ]
        }
    }