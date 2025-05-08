function sendMessage() {
    let userInput = document.getElementById("user-input").value.trim();
    if (userInput === "") return;

    document.getElementById("typing-indicator").style.display = "block";

    fetch("/chatbot-response/", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message: userInput.toLowerCase() })  
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById("typing-indicator").style.display = "none";
        location.reload();  // Ensure messages appear dynamically
    });

    document.getElementById("user-input").value = "";
    scrollToBottom();
}

function quickReply(message) {
    document.getElementById("user-input").value = message;
    sendMessage();
}

function handleKeyPress(event) {
    if (event.key === "Enter") {
        sendMessage();
    }
}

function scrollToBottom() {
    let chatBox = document.getElementById("chat-box");
    chatBox.scrollTop = chatBox.scrollHeight;
}
window.onload = scrollToBottom;

document.getElementById("user-input").addEventListener("input", function () {
    let query = this.value.trim();
    let suggestionBox = document.getElementById("suggestion-box");

    if (query.length < 2) { 
        suggestionBox.style.display = "none";
        return;
    }

    fetch(`/autocomplete-suggestions/?q=${query}`)
    .then(response => response.json())
    .then(data => {
        suggestionBox.innerHTML = ""; // Clear previous suggestions

        data.suggestions.forEach(suggestion => {
            let suggestionItem = document.createElement("div");
            suggestionItem.classList.add("suggestion-item");
            suggestionItem.textContent = suggestion;
            suggestionItem.onclick = function () {
                document.getElementById("user-input").value = suggestion;
                suggestionBox.style.display = "none"; // Hide suggestions
            };
            suggestionBox.appendChild(suggestionItem);
        });

        suggestionBox.style.display = data.suggestions.length ? "block" : "none";
    });
});

// Hide suggestions when clicking outside
document.addEventListener("click", function(event) {
    if (!event.target.closest(".input-container")) {
        document.getElementById("suggestion-box").style.display = "none";
    }
});