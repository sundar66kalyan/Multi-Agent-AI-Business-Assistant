from app.core.permissions import ROLE_PERMISSIONS


class PermissionService:
    @staticmethod
    def has_permission(role, page):
        return page in ROLE_PERMISSIONS.get(role, [])