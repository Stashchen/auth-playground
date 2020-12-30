import datetime

from django.contrib.auth import logout
from django.shortcuts import redirect


class CheckSessionMiddleware:
    """
    Check session expire date from service of truth
    if date is expired than logout user and redirect him to login page
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        exp = request.session.get("expire_date_API")

        if exp:
            expire_date = datetime.datetime.strptime(exp, "%Y-%m-%dT%H:%M:%S.%f")
            current_time = datetime.datetime.now()
            if expire_date - current_time < datetime.timedelta():
                request.user.session_id_for_data_service = None
                request.user.save()
                logout(request)
                return redirect("login")
        return response
