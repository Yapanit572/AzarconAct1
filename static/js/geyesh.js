// JavaScript code for a personalized welcome message, digital clock, and toggle content
document.addEventListener("DOMContentLoaded", function() {
    // Personalized Welcome Message
    const welcomeMessage = document.querySelector('.welcome-message');
    const userName = prompt("What's your name?");
    if (welcomeMessage && userName) {
        welcomeMessage.textContent = `Welcome, ${userName}!`;
    }

    // Digital Clock
    const clockDisplay = document.querySelector('.clock');
    function updateClock() {
        const now = new Date();
        const hours = now.getHours().toString().padStart(2, '0');
        const minutes = now.getMinutes().toString().padStart(2, '0');
        const seconds = now.getSeconds().toString().padStart(2, '0');
        if (clockDisplay) {
            clockDisplay.textContent = `Current Time: ${hours}:${minutes}:${seconds}`;
        }
    }
    setInterval(updateClock, 1000);
    updateClock(); // Initial call to display clock immediately

    // Show/Hide Additional Content
    const toggleButton = document.querySelector('#toggleContent');
    const additionalContent = document.querySelector('.additional-content');
    if (toggleButton && additionalContent) {
        toggleButton.addEventListener('click', function() {
            if (additionalContent.style.display === 'none' || !additionalContent.style.display) {
                additionalContent.style.display = 'block';
                toggleButton.textContent = 'Hide Content';
            } else {
                additionalContent.style.display = 'none';
                toggleButton.textContent = 'Show Content';
            }

        });
    }
});
document.getElementById("image").addEventListener("mouseover", function() {
    var pakboy = document.getElementById("pakboy").value;
    this.src = pakboy;
});

document.getElementById("image").addEventListener("mouseout", function() {
    var imagePath = document.getElementById("imagePath").value;
    this.src = imagePath;
});