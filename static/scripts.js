function sendMessage() {
    const userInput = document.getElementById("user_input").value;
    fetch('/chat', {
        method: 'POST',
        body: new URLSearchParams({ 'user_input': userInput })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById("story").innerText += "\n" + data.story;
        const optionsDiv = document.getElementById("options");
        optionsDiv.innerHTML = data.options.map(option => 
            `<button onclick="sendOption('${option}')">${option}</button>`
        ).join('');
    });
}

function sendOption(option) {
    document.getElementById("user_input").value = option;
    sendMessage();
}

