import requests

from ..poker_model import Action

def parse_next_actions(response, history: str):
    actions = []
    if response:
        if not isinstance(response, dict):
            print(f"Error: response is not a dict")
            return actions
        if "next_actions" not in response:
            print(f"Error: no next_actions in response")
            return actions 
        if "available_actions" not in response["next_actions"]:
            print(f"Error: no available_actions in response")
            return actions
        if "next_actions" in response and  "available_actions" in response["next_actions"]:
            for action_resp in response["next_actions"]["available_actions"]:
                action_code = action_resp.get("action", {}).get("code", "")
                bet_size = action_resp.get("action", {}).get("betsize", "")
                position = action_resp.get("action", {}).get("position", "")
                if action_code:
                    h = history + '-' + action_code if history != '' else action_code
                    actions.append(Action(action_code, bet_size, position, h))
    return actions 
