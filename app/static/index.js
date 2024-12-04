function typeWriter(element, text, delay = 100) {
    let i = 0;
    const interval = setInterval(() => {
        element.textContent += text[i];
        i++;
        if (i >= text.length) {
            clearInterval(interval);
        }
    }, delay);
}

function sendMessage(message) {
    // Sending message to server using fetch API
    fetch('/chat', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ message: message })
    })
    .then(response => response.json())
    .then(data => {
        const chatContainer = document.getElementById('chat-container');
        
        // Display the user's message
        const userMessageDiv = document.createElement('div');
        userMessageDiv.classList.add('user-message');
        userMessageDiv.textContent = message;
        chatContainer.appendChild(userMessageDiv);

        // Display the chatbot's response with the typewriter effect
        const botMessageDiv = document.createElement('div');
        botMessageDiv.classList.add('bot-message');
        chatContainer.appendChild(botMessageDiv);
        
        const botResponse = data.response;
        typeWriter(botMessageDiv, botResponse, 50); // You can adjust the typing speed here
    })
    .catch(error => console.error('Error:', error));
}

// Example usage
document.querySelector('#send-message-button').addEventListener('click', () => {
    const message = document.querySelector('#user-message').value;
    sendMessage(message);
});
