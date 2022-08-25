from __future__ import unicode_literals
import json
import jwt
from user_model.models import User
import user_service
from django.http import HttpResponse
from rest_framework.views import APIView

KEY = user_service.settings.SECRET_KEY
TOKEN_LIFE = user_service.settings.TOKEN_LIFE
# the function for validating the user
def user_validation(uname, password):
    user_data = User.objects.get(email_id=uname, password=password)
    return user_data


# this function for getting username and password
class UserApiView(APIView):
    def post(self, request, *args, **kwargs):
        uname = request.data.get("username")
        password = request.data.get("password")
        resp = {}
        if uname and password:
            respdata = user_validation(uname, password)
            if respdata:
                # code for token generation
                user_data = {"username": respdata.email_id}
                token = jwt.encode(
                    payload=user_data,
                    key=f"Token {KEY}",
                    algorithm="HS256",
                )
                resp["token"] = token.decode("utf-8") 
                resp["status"] = "Success"
                resp["status_code"] = "200"
                resp["message"] = "User login successfully"
            else:
                resp["status"] = "Failed"
                resp["status_code"] = "400"
                resp["message"] = "Invalid credentials"
        else:
            resp["status"] = "Failed"
            resp["status_code"] = "400"
            resp["message"] = "all fields are mandatory"
        return HttpResponse(json.dumps(resp), content_type="application/json")
