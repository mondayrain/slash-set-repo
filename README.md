# Slash-Set Repo

Slash-Set Repo is a Slack integration + Chrome extension pairing that lets you set messages about a GitHub repo in Slack, and have them show up in Pull Requests. This lets you easily inform anybody hoping to merge into your repository about important information, such as breakages, current demos (a.k.a. don't merge!), and so forth.

## Setup

#### Set up and run the Flask server

```
pip install -r requirements.txt
python run.py
```

Make sure the server has a publicly accessible URL. If you are just testing against a local server, you can use [ngrok](https://ngrok.com).


#### Set up a Slack app + integrate it with your Slack team

- Go to [https://api.slack.com](https://api.slack.com) and sign up for an account.
- Click "Your Apps" on the top-right corner
- Hit "Create New App"
- Choose a name for your app & your slack team

You should now be in the "Basic Information" page, where you can add features and functionality to your app.

Now, click "Slash Commands", and create commands for the following endpoints (you can name the slash commands as you like):

- <YOUR-ENDPOINT>/set-repo-message
- <YOUR-ENDPOINT>/unset-repo-message
- <YOUR-ENDPOINT>/get-repo-messages

#### Install the Chrome extension

- Go to the "chrome-extension" folder and update both "manifest.json" and "scripts/background.js" to use your Slack server endpoint
- Navigate to [chrome://extensions](chrome://extensions)
- Enable 'Developer Mode' at the top-right corner
- Click "Load unpacked extension"
- Select the "chrome-extension" folder in the repo and load it

