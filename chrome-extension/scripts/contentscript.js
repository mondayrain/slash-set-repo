let messages = {};

function displayMessage (repoName) {
  var merge_details = document.querySelector(".mergeability-details");

  if (!merge_details) {
    return;
  }

  if (document.querySelector('.slash-set-repo')) {
    document.querySelector('.slash-set-repo').remove()
  }

  var message_div = document.createElement("div");
  message_div.className = "branch-action-item js-details-container slash-set-repo"

  var icon = document.createElement('div');
  icon.className = "branch-action-item-icon";
  icon.style.fontSize = "31px";
  icon.innerText = "⚠️";

  var header = document.createElement('h3');
  header.className = "status-heading h4 text-purple";
  header.textContent = "Message from " + messages[repoName]["user"] + ":"

  var message = document.createElement("p")
  message.className = "text-emphasized";
  message.textContent = messages[repoName]["message"]

  message_div.appendChild(icon);
  message_div.appendChild(header);
  message_div.appendChild(message);
  merge_details.insertBefore(message_div, merge_details.firstChild);
}

function getRepoName () {
  var current_url = window.location.href;
  [_, repoName] = current_url.match("wealthsimple/(.*)/pull/");

  // Only change DOM if we are on a repo with a message
  if (messages[repoName]) {
    displayMessage(repoName);
  }
}

function getMessages (response) {
  messages = response || {};

  // Get current repo name
  chrome.runtime.sendMessage({
      type: 'get_repo_name'
  }, getRepoName);
}

chrome.runtime.sendMessage({
    type: 'get_messages'
}, getMessages);

setInterval(() => {
  chrome.runtime.sendMessage({
      type: 'get_messages'
  }, getMessages);
}, 30000);

detectPageChanged(() => getRepoName());

function detectPageChanged (callback) {
 let oldPathname = window.location.pathname;
 let oldSearch = window.location.search;
 const DETECT_INTERVAL = 100;

 setInterval(() => {
   if(oldPathname != window.location.pathname && !document.querySelector('.is-loading') || oldSearch != window.location.search && !document.querySelector('.is-loading')) {
     oldPathname = window.location.pathname;
     oldSearch = window.location.search;
     callback();
   }
 }, DETECT_INTERVAL);
};
