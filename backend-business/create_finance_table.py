from app.database.database import engine
from app.models.finance import Finance

print("Creating finance table...")

Finance.__table__.create(bind=engine, checkfirst=True)

print("Finance table created successfully.")