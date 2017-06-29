// Make sure to add this endpoint to manifest.json permissions
var MESSAGES_URL = "<PATH-TO-SLACK-SERVER-ENDPOINT>/get-repo-messages-json";

chrome.runtime.onMessage.addListener(function(request, sender, callback) {
    if (request.type == "get_messages") {
        var xhttp = new XMLHttpRequest();

        xhttp.onload = function() {
            callback(JSON.parse(xhttp.responseText));
        };
        xhttp.onerror = function() {
            console.log("Oops, error from Slack server");
            callback();
        };

        xhttp.open('GET', MESSAGES_URL, true);
        xhttp.send();
        return true;
    } else if (request.type == "get_repo_name") {
        var queryInfo = {
            active: true,
            currentWindow: true
        };
        chrome.tabs.query(queryInfo, function(tabs) {
            callback(tabs[0].url);
        });
        return true;
    }
});
