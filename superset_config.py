from superset.security import SupersetSecurityManager
from flask_appbuilder.security.manager import AUTH_REMOTE_USER

class CustomSecurityManager(SupersetSecurityManager):
    def get_user(self):
        from flask_appbuilder.security.sqla.models import User
        return self.find_user("admin")
    

FEATURE_FLAGS = {"EMBEDDED_DASHBOARDS": True}

HTTP_HEADERS = {'X-Frame-Options': 'ALLOWALL'}

ENABLE_IFRAME_EMBED = True

WTF_CSRF_ENABLED = False

AUTH_TYPE = AUTH_REMOTE_USER
CUSTOM_SECURITY_MANAGER = CustomSecurityManager
