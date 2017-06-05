from flask import Flask, request, abort

# The parameters included in a slash command request (with example values):
#   token=gIkuvaNzQIHg97ATvDxqgjtO
#   team_id=T0001
#   team_domain=example
#   channel_id=C2147483705
#   channel_name=test
#   user_id=U2147483697
#   user_name=Steve
#   command=/weather
#   text=94070
#   response_url=https://hooks.slack.com/commands/1234/5678

set_repos = {"repos": {}}

class Repo(object):
    def __init__(self, name, message):
        self.name = name
        self.message.message

app = Flask(__name__)

@app.route('/set-repo', methods=['POST'])
def set_repo():
    params = parse_params(request)
    if not params['token']:  # or some other failure condition
        abort(400)

    repo_name, message = tuple(params["text"].split(' ', 1))

    if set_repose["repos"].get(repo_name):
        return "Repo {} has already been set with message '{}'. Please first unset it.".format(repo_name, set_repos["repos"][repo_name])
    else:
        set_repos["repos"][repo_name] = message
        return "Setting repo '{}' with message '{}'".format(repo_name, message)

@app.route('/unset-repo', methods=['POST'])
def unset_repo():
    params = parse_params(request)
    if not params['token']:
        abort(400)

    repo_name = params["text"]
    repo_was_set = set_repos.pop(repo_name, None)

    if repo_was_set:
        return "Repo {} has been unset".format(repo_name)
    else:
        return "Repo {} was not set; nothing to unset.".format(repo_name)
    

    

@app.route('/get-repos', methods=['GET'])
def get_repos():
    return str(set_repos)

def parse_params(request):
    token = request.form.get('token', None)
    command = request.form.get('command', None)
    text = request.form.get('text', None)
    return { 'token': token, 'command': command, 'text': text }

if __name__ == "__main__":
    app.run(debug=True)
