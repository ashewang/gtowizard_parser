# GTOWizard Parser

## Description

GTOWizard Parser is a Python project designed to parse and analyze poker-related data, specifically focusing on Multi-Table Tournament (MTT) scenarios. This tool is aimed at helping poker players and analysts to process and understand complex game situations.

To use this GTOWizard Parser, you'll need to obtain your authentication tokens from GTOWizard. Here's how you can find them:
1. Log in to your GTOWizard account in a web browser.
2. Open the browser's developer tools (usually F12 or right-click and select "Inspect").
3. Go to the "Network" tab in the developer tools.
Filter the network requests to show only "XHR" or "Fetch" requests.
4. Look for a request to the login endpoint (it might be named "login" or "token").
5. Click on this request and look in the "Response" tab.
6. In the response JSON, you should find two tokens:
access_token: This is your access token
- refresh_token: This is your refresh token
Once you have these tokens, you need to add them to your project:
- Create a file named refresh_token.txt in the data directory.
- Paste your refresh token into this file.
Create a file named access_token.txt in the data directory.
- Paste your access token into this file.
The parser will use these tokens to authenticate with the GTOWizard API. Make sure to keep these tokens secure and do not share them publicly.
You can see how these tokens are used in the main.py file:

```python
with open('data/refresh_token.txt', 'r') as f:
    CURRENT_REFRESH_TOKEN = f.read()

with open('data/access_token.txt', 'r') as f:
    CURRENT_ACCESS_TOKEN = f.read()
```

Remember to update these tokens periodically or if you encounter authentication issues. Note that GTOwizard may limit your access to the API if you are making too many requests.

## Features

- Parses MTT data from various game situations
- Supports different stack sizes and betting rounds
- Analyzes actions for different positions (SB, CO, HJ, etc.)
- Handles various game states (Fold, Call, Raise, All-in)

## Installation

This project requires Python 3.12 or higher. To install the necessary dependencies, run:



## Data Format

The `data` directory contains MTT scenarios organized by stack sizes and action sequences. Each scenario includes:

- `actions_metadata.txt`: Contains information about the action sequence, final action, pot size, and position.
- `solution.json`: Contains the solution data for the scenario (currently empty in the provided snippets).