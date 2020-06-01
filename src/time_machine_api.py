import requests


class TimeMachineApi:
    url = 'http://192.168.0.111:8080/v1/'

    def _get(self, url):
        response = requests.get(url)
        try:
            response.raise_for_status()
        except requests.exceptions.HTTPError as e:
            return "Error: " + str(e)
        result = []
        for item in response.json():
            result.append({'name': item.get('name')})

        return result

    def _post(self, url, data):
        try:
            response = requests.post(url, json=data)
        except requests.exceptions.HTTPError as e:
            return "Error: " + str(e)

    def _put(self, url, data):
        try:
            response = requests.put(url, json=data)
        except requests.exceptions.HTTPError as e:
            return "Error: " + str(e)

    def _delete(self, url, data):
        try:
            response = requests.delete(url, json=data)
        except requests.exceptions.HTTPError as e:
            return "Error: " + str(e)
