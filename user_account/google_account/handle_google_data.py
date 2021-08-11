import requests
import json

# the method get_userinfo uses the access-token to get the user data at the endpoint "endpoint" using a get request.
# the method returns a json response (a dict for python) with the follow keys:

# json response:
# {
#   "id": "",
#   "name": "",
#   "given_name": "",
#   "family_name": "",
#   "picture": "",
#   "locale": ""
# }


class GoogleData:

    @staticmethod
    def get_userinfo(user_token):
        endpoint = "https://www.googleapis.com/oauth2/v2/userinfo"

        response = requests.get(endpoint, headers={"Authorization": "Bearer {}".format(user_token)})

        return json.loads(response.text)