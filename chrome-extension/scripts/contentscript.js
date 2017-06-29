chrome.runtime.sendMessage({
    type: 'get_messages'
}, function(responseText) {

    // Parse JSON
    var response_json = JSON.parse(responseText);

    // Get current repo name
    chrome.runtime.sendMessage({
        type: 'get_repo_name'
    }, function(responseText) { 
      var current_url = responseText;
      var repo_name = current_url.match("wealthsimple/(.*)/pull")[1];

      // Only change DOM if we are on a repo with a message
      if (response_json[repo_name]) {
        var merge_details = document.getElementsByClassName("mergeability-details")[0];

        var message_div = document.createElement("div");
        message_div.className = "branch-action-item js-details-container slash-set-repo"

        var header = document.createElement('h3');
        header.className = "status-heading h4 text-purple";
        header.textContent = "Message from " + response_json[repo_name]["user"] + ":"

        var message = document.createElement("p")
        message.className = "text-emphasized";
        message.textContent = response_json[repo_name]["message"]

        message_div.appendChild(header);
        message_div.appendChild(message);
        merge_details.insertBefore(message_div, merge_details.firstChild);
      }
    });
});