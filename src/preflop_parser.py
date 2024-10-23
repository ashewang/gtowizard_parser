import json
import os
from .poker_model import Action
from .utils.helper import parse_next_actions
from .wizard_helper import WizardHelper

def get_dir(history:str):
    return history.replace('-', '/')



def parse_preflop_actions(game_type: str = 'MTTGeneral', depth: str = '50.125', wizard_helper: WizardHelper = None, output_dir: str = 'data'):
    params = {
        'gametype': game_type,
        'depth': depth,
        'preflop_actions': '',
        'flop_actions': '',
        'turn_actions': '',
        'river_actions': ''
    }
    # wirte to json file  
    # Check if the directory exists, if not create it
    if not os.path.exists(f"{output_dir}/{game_type}/{depth}"):
        os.makedirs(f"{output_dir}/{game_type}/{depth}")

    # bfs to get all possible actions
    actions = [Action('', '', '', '')]
    next_action_solutions = {}
    total_actions = 0
    while actions: 
        a = actions.pop(0)
        total_actions += 1
        # materialize every 100 actions 

        print(f"Parsing action: {a}, remaining actions: {len(actions)}, total actions: {total_actions}")
        params['preflop_actions'] = a.history

        next_action_resp = wizard_helper.get_next_actions(params)
        if next_action_resp:
            next_actions = parse_next_actions(next_action_resp, a.history)
            next_action_solutions[a.history] = next_actions
            print(f"Next actions for {a.history}: {','.join([str(na.code) for na in next_actions])}")
            actions.extend(next_actions)
        else:
            print(f"Error: empty next_action_resp")
            break
    print(f"Total actions: {len(next_action_solutions)}")


    with open(f"{output_dir}/{game_type}/{depth}/next_actions.json", 'w') as f:
        json.dump(next_action_solutions, f)
    if actions:
        with open(f"{output_dir}/{game_type}/{depth}/remaining_actions.json", 'w') as f:
            json.dump(actions, f)
    return actions

def parse_preflop_actions_v2(game_type: str = 'MTTGeneral', depth: str = '50.125', wizard_helper: WizardHelper = None, output_dir: str = 'data'):
    params = {
        'gametype': game_type,
        'depth': depth,
        'preflop_actions': '',
        'flop_actions': '',
        'turn_actions': '',
        'river_actions': ''
    }
    # wirte to json file  
    # Check if the directory exists, if not create it
    if not os.path.exists(f"{output_dir}/{game_type}/{depth}"):
        os.makedirs(f"{output_dir}/{game_type}/{depth}")

    total_actions = 0

    def dfs(history:str):
        nonlocal total_actions
        total_actions += 1
        print(f"Depth {depth} Parsing action: {history}, total actions: {total_actions}")
        params = {
            'gametype': game_type,
            'depth': depth,
            'preflop_actions': history,
            'flop_actions': '',
            'turn_actions': '',
            'river_actions': ''
        }

        next_action_resp = wizard_helper.get_next_actions(params)
        if next_action_resp and next_action_resp.get('next_actions', {}).get('game', {}).get('current_street', {}).get('type', '') == 'PREFLOP':
            # log next actions
            next_actions = parse_next_actions(next_action_resp, history)
            print(f"Next actions for {history}: {','.join([str(na.code) for na in next_actions])}")
            if len(next_actions) > 0:
                # get solution for current history
                solution_resp = wizard_helper.get_solution(params)
                dir = get_dir(history)
                if solution_resp:
                    with open(f"{output_dir}/{game_type}/{depth}/{dir}/solution.json", 'w') as f:
                        json.dump(solution_resp, f)
            
            for na in next_actions:
                dir = get_dir(na.history)
                if not os.path.exists(f"{output_dir}/{game_type}/{depth}/{dir}"):
                    os.makedirs(f"{output_dir}/{game_type}/{depth}/{dir}")
                with open(f"{output_dir}/{game_type}/{depth}/{dir}/actions_metadata.txt", 'w') as f:
                    f.write(str(na))
                dfs(na.history)
        else:
            print(f"Error: empty next_action_resp or not preflop for history: {history}")



    # bfs to get all possible actions
    dfs('')
    return 