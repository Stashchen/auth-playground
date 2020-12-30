import requests
from django.conf import settings


class DataService:
    base_data_service_path = settings.BASE_DATA_SERVICE_PATH

    def authorize_user_by_request(self, request):
        """Make request to get session from server service/"""
        url = f"{self.base_data_service_path}/Auth"

        credentials = {
            'username': request.POST["username"],
            'password': request.POST["password"]
        }

        session = requests.Session()
        response_with_session = session.post(url, data=credentials)
        return response_with_session

    def get_user_data(self, request):
        cookies = {**request.COOKIES, "sessionid": request.user.session_id_for_data_service}
        url = f"{self.base_data_service_path}/GetPerson"
        response = requests.get(url, cookies=cookies)
        return response.json()
