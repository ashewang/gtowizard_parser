import time
import requests
import json

class WizardHelper:
    def __init__(self):
        self.renew_token_url = "https://api.gtowizard.com/v1/token/refresh/"
        self.get_next_actions_url = "https://api.gtowizard.com/v1/poker/next-actions/"
        self.get_solution_url = "https://api.gtowizard.com/v1/poker/solution/"
        self.headers = {
            'Accept': 'application/json, text/plain, */*',
            'Accept-Language': 'en-US,en;q=0.9',
            'Connection': 'keep-alive',
            'Content-Type': 'application/json',
            'GWCLIENTID': 'e8d23c8d-2624-4f0e-b994-030291e042df',
            'Origin': 'https://app.gtowizard.com',
            'Referer': 'https://app.gtowizard.com/',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
            'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Google Chrome";v="128"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"macOS"'
        }

        self._access_token = None 
        self._refresh_token = None 

    def renew_access_token(self, refresh_token):
        self.headers['Authorization'] = f'Bearer {self._access_token}'
        
        payload = {
            'refresh': refresh_token
        }

        try:
            response = requests.post(
                self.renew_token_url,
                headers=self.headers,
                data=json.dumps(payload)
            )
            response.raise_for_status()
            self._access_token = response.json()['access']
            # store the access token to file 
            with open('data/access_token.txt', 'w') as f:
                f.write(self._access_token)
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error renewing access token: {e}")
            print(f"Request data: {payload}")
            self._access_token = None
            return None

    def get_next_actions(self, params):
        headers = {
            'Accept': 'application/json, text/plain, */*',
            'Accept-Language': 'en-US,en;q=0.9',
            'Authorization': f'Bearer {self._access_token}',
            'Connection': 'keep-alive',
            'GWCLIENTID': 'e8d23c8d-2624-4f0e-b994-030291e042df',
            'Origin': 'https://app.gtowizard.com',
            'Referer': 'https://app.gtowizard.com/',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
            'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Google Chrome";v="128"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"macOS"'
        }

        try:
            response = requests.get(self.get_next_actions_url, params=params, headers=headers)
            response.raise_for_status()
            return response.json()  # Assuming the response is JSON
        except requests.exceptions.RequestException as e:
            if response.status_code == 401:
                try:
                    print("Unauthorized, renewing access token...")
                    self.renew_access_token(self._refresh_token)
                    response = requests.get(self.get_next_actions_url, params=params, headers=headers)
                    response.raise_for_status()
                    return response.json()
                except requests.exceptions.RequestException as e:
                    print(f"Error getting next actions: {e}")
                    return None
            else:
                print(f"Error getting next actions: {e}")
                return None

    def get_solution(self, params):
        headers = {
            'Accept': 'application/json, text/plain, */*',
            'Accept-Language': 'en-US,en;q=0.9',
            'Authorization': f'Bearer {self._access_token}',
            'Connection': 'keep-alive',
            'GWCLIENTID': 'e8d23c8d-2624-4f0e-b994-030291e042df',
            'Origin': 'https://app.gtowizard.com',
            'Referer': 'https://app.gtowizard.com/',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
            'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Google Chrome";v="128"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"macOS"'
        }

        try:
            response = requests.get(self.get_solution_url, params=params, headers=headers)
            response.raise_for_status()
            return response.json()  # Assuming the response is JSON
        except requests.exceptions.RequestException as e:
            if response.status_code == 401:
                try:
                    self.renew_access_token(self._refresh_token)
                    response = requests.get(self.get_solution_url, params=params, headers=headers)
                    response.raise_for_status()
                    return response.json()
                except requests.exceptions.RequestException as e:
                    print(f"[401] Error getting solution: {e}")
                    return None
            elif response.status_code == 429:
                time.sleep(1)
                try:
                    response = requests.get(self.get_solution_url, params=params, headers=headers)
                    response.raise_for_status()
                    return response.json()
                except requests.exceptions.RequestException as e:
                    print(f"[429] Error getting solution: {e}")
                    return None
            else:
                print(f"[Other]Error getting solution: {e}")
                return None
    

