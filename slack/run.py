from flask import Flask, request, abort
import json

# The parameters included in a slash command request (with example values):
#   token=gIkuvaNzQIHg97ATvDxqgjtO
#   team_id=T0001
#   team_domain=example
#   channel_id=C2147483705
#   channel_name=test
#   user_id=U2147483697
#   user=Steve
#   command=/weather
#   text=94070
#   response_url=https://hooks.slack.com/commands/1234/5678

set_repos = {}

class Repo(object):
    def __init__(self, name, message, user):
        self.name = name
        self.message = message
        self.user = user

app = Flask(__name__)

@app.route('/set-repo-message', methods=['POST'])
def set_repo():
    params = _parse_params(request)
    if not params['token']:
        abort(400)

    if len(params['text'].split(' ')) <= 1:
        return "ERROR: You need to provide a message to set for repository <{}>".format(params["text"])
    else:
        repo_name, message = params['text'].split(' ', 1)

        if set_repos.get(repo_name):
            return "Repository <{}> has already been set by {} with the message '{}'. Please first unset it.".format(
            repo_name,
            set_repos[repo_name].user,
            set_repos[repo_name].message
            )
        else:
            new_repo = Repo(repo_name, message, params['user'])
            set_repos[repo_name] = new_repo
            return "SUCCESS! Repository <{}> has been set with the message '{}'.".format(repo_name, message)

@app.route('/unset-repo-message', methods=['POST'])
def unset_repo():
    params = _parse_params(request)
    if not params['token']:
        abort(400)

    if len(params['text'].split(' ')) > 1:
        return "ERROR: Please only enter the name of the repository."
    else:
        repo_name = params['text']
        repo = set_repos.pop(repo_name, None)

        if repo:
            return "SUCCESS! Message '{}' for repository <{}> has been unset".format(repo.message, repo_name)
        else:
            return "Nothing happened: repository <{}> wasn't set in the first place!".format(repo_name)

@app.route('/get-repo-messages', methods=['POST'])
def get_repos():
    response = "Currently set repositories: \n\n" 
    for name, repo in set_repos.items():
        response = response + "<{}>: '{}'\n".format(name, repo.message)

    return response

@app.route('/get-repo-messages-json', methods=['POST'])
def get_repos_json():
    repos = {}
    for name, repo in set_repos.items():
        repos[name] = { 'message': repo.message, 'user': repo.user}

    return json.dumps(repos)

def _parse_params(request):
    token = request.form.get('token', None)
    command = request.form.get('command', None)
    text = request.form.get('text', None)
    user = request.form.get('user_name', None)
    return { 'token': token, 'command': command, 'text': text, 'user': user }

if __name__ == "__main__":
    app.run(debug=True)
