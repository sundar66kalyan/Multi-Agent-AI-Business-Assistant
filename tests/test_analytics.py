from app.database.database import SessionLocal
from app.services.analytics_service import AnalyticsService

db = SessionLocal()

print("=" * 60)
print("SYSTEM ANALYTICS")
print("=" * 60)

print(
    AnalyticsService.system_summary(db)
)

db.close()