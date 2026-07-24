from fastapi import APIRouter

from app.services.notification_service import NotificationService

router = APIRouter(
    prefix="/notifications",
    tags=["Notifications"]
)


@router.get("")
def notifications():

    return {

        "success":True,

        "count":len(NotificationService.notifications),

        "notifications":NotificationService.get_notifications()

    }