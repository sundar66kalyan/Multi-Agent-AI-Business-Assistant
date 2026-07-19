from datetime import datetime


class NotificationService:

    notifications = [

        {
            "type":"success",
            "message":"PDF Report Generated",
            "time":"2 min ago"
        },

        {
            "type":"info",
            "message":"Employee Handbook Indexed",
            "time":"8 min ago"
        },

        {
            "type":"success",
            "message":"Finance Database Updated",
            "time":"20 min ago"
        },

        {
            "type":"warning",
            "message":"Vector Database Rebuilt",
            "time":"35 min ago"
        },

        {
            "type":"info",
            "message":"Administrator Login",
            "time":"1 hour ago"
        }

    ]

    @staticmethod
    def get_notifications():

        return NotificationService.notifications