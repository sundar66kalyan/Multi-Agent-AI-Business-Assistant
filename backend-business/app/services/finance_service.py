# app/services/finance_service.py

from sqlalchemy.orm import Session
from app.repositories.finance_repository import FinanceRepository


class FinanceService:

    @staticmethod
    def answer_question(db: Session, question: str):
        """
        Answer finance-related questions by retrieving data from FinanceRepository.
        
        Args:
            db (Session): SQLAlchemy database session
            question (str): User's finance-related question
            
        Returns:
            dict: Finance data based on the question
        """
        # Step 1: Get finance data through FinanceRepository
        finance = FinanceRepository.get_latest(db)
        
        # Step 2: Handle case where no data exists
        if finance is None:
            return {
                "message": "No finance data found."
            }
        
        # Step 3: Normalize question for keyword matching
        question = question.lower()
        
        # Step 4: Route to appropriate data based on keywords
        
        # Summary-type questions should return all finance metrics
        if any(word in question for word in [
            "summary",
            "finance summary",
            "revenue this month",
            "overview",
            "report"
        ]):
            return {
                "month": finance.month,
                "revenue": finance.revenue,
                "expenses": finance.expenses,
                "profit": finance.profit
            }
        
        elif "profit" in question:
            return {"profit": finance.profit}
        
        elif "expense" in question:
            return {"expenses": finance.expenses}
        
        elif "revenue" in question:
            return {"revenue": finance.revenue}
        
        elif "month" in question:
            return {"month": finance.month}
        
        else:
            # Default: Return all data
            return {
                "month": finance.month,
                "revenue": finance.revenue,
                "expenses": finance.expenses,
                "profit": finance.profit
            }