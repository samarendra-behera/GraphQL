import typing

from jwt.exceptions import DecodeError
from strawberry.types import Info
from strawberry.permission import BasePermission
from Middleware.JWTManager import JWTManager

class IsAuthenticated(BasePermission):
    message = "User is not Authenticated"

    def has_permission(self, source:typing.Any, info:Info, **kwargs: typing.Any)->bool:
        try:
            request = info.context['request']
            # Access the headers authentication
            authentication = request.headers['authentication']
            if authentication:
                token = authentication.split("Bearer ")[-1]
                print(token)
                return JWTManager.verify_jwt(token)
            return False
        except KeyError:
            self.message = "Please provide jwt token!"
            return False
        except DecodeError:
            self.message = "Invalid jwt token!"
            return False