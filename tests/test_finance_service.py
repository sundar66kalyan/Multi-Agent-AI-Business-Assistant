from app.database.database import SessionLocal
from app.services.finance_service import FinanceService

db = SessionLocal()

try:
    result = FinanceService.answer_question(
        db,
        "What is our profit?"
    )
    print(result)
finally:
    db.close()