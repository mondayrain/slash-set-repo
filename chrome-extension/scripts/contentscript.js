var MESSAGES_URL = "http://slash-set.ngrok.io/get-repo-messages-json";

chrome.runtime.sendMessage({
    method: 'GET',
    action: 'xhttp',
    url: MESSAGES_URL,
}, function(responseText) {
    console.log(responseText);
});
