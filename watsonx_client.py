import requests

class WatsonxClient:
    def __init__(self, api_key, model_id, url):
        self.api_key = api_key
        self.model_id = model_id
        self.url = url
        self.token = self.get_token()

    def get_token(self):
        response = requests.post(
            "https://iam.cloud.ibm.com/identity/token",
            data={
                "grant_type": "urn:ibm:params:oauth:grant-type:apikey",
                "apikey": self.api_key
            },
            headers={"Content-Type": "application/x-www-form-urlencoded"}
        )
        return response.json()["access_token"]

    def ask(self, prompt):
        headers = {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json"
        }
        payload = {
            "model_id": self.model_id,
            "input": prompt,
            "parameters": {
                "decoding_method": "greedy",
                "max_new_tokens": 200
            }
        }
        response = requests.post(self.url, headers=headers, json=payload)
        return response.json()["results"][0]["generated_text"]
