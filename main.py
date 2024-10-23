
from src.preflop_parser import parse_preflop_actions_v2
from src.wizard_helper import WizardHelper

wizard_helper = WizardHelper()

# read refresh token from file
with open('data/refresh_token.txt', 'r') as f:
    CURRENT_REFRESH_TOKEN = f.read()

with open('data/access_token.txt', 'r') as f:
    CURRENT_ACCESS_TOKEN = f.read()

wizard_helper._refresh_token = CURRENT_REFRESH_TOKEN
wizard_helper._access_token = CURRENT_ACCESS_TOKEN

print(wizard_helper.renew_access_token(CURRENT_REFRESH_TOKEN))

# params = {
#     'gametype': 'MTTGeneral',
#     'depth': '50.125',
#     'stacks': '',
#     'preflop_actions': '',
#     'flop_actions': '',
#     'turn_actions': '',
#     'river_actions': ''
# }

# print(wizard_helper.get_next_actions(params))

# params = {
#     'gametype': 'MTTGeneral',
#     'depth': '50.125',
#     'stacks': '',
#     'preflop_actions': 'F',
#     'flop_actions': '',
#     'turn_actions': '',
#     'river_actions': '',
#     'board': ''
# }

# print(wizard_helper.get_solution(params))

#parse_preflop_actions_v2(game_type='MTTGeneral', depth='50.125', wizard_helper=wizard_helper)

# print(f"Parsing depth 2.125")
# parse_preflop_actions_v2(game_type='MTTGeneral', depth='2.125', wizard_helper=wizard_helper)

print(f"Parsing depth 8.125")
parse_preflop_actions_v2(game_type='MTTGeneral', depth='8.125', wizard_helper=wizard_helper)

# print(f"Parsing depth 10.125")
# parse_preflop_actions_v2(game_type='MTTGeneral', depth='10.125', wizard_helper=wizard_helper)

# print(f"Parsing depth 12.125")
# parse_preflop_actions_v2(game_type='MTTGeneral', depth='12.125', wizard_helper=wizard_helper)

