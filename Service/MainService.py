import requests
from Logger.Logger import log_request_time


class Service:

    # Below function return response from URL as json()
    @log_request_time
    def get_response(self, url, param):
        req = requests.get(url, params=param)
        return req.json()
