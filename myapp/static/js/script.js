// script.js

// Define the chatbot logic
class PegasusBot {
    constructor() {
        this.currentStep = 0;
        this.questions = [
            {
                question: "What can I help you with today?",
                options: [
                    "Learn about Pegasus Automation products",
                    "Get technical support for my devices",
                    "General inquiry about home automation"
                ],
                responses: ["learn_products", "technical_support", "general_inquiry"]
            },
            {
                question: "Which type of smart device are you interested in?",
                options: [
                    "Smart Lighting",
                    "Security Cameras",
                    "Thermostats",
                    "Other Devices"
                ],
                responses: ["smart_lighting", "security_cameras", "thermostats", "other_devices"],
                triggered_by: "learn_products",
                random_responses: [
                    "We offer the latest in smart lighting technology.",
                    "Our security cameras are equipped with AI for enhanced safety.",
                    "Our thermostats are energy-efficient and easy to control."
                ]
            },
            {
                question: "What kind of issue are you facing?",
                options: [
                    "Connectivity issues",
                    "Device not responding",
                    "App not working properly"
                ],
                responses: ["connectivity_issue", "device_not_responding", "app_issue"],
                triggered_by: "technical_support",
                random_responses: [
                    "For connectivity issues, try restarting your router.",
                    "If your device is not responding, ensure it’s powered on and connected.",
                    "App issues can often be resolved by reinstalling or updating."
                ]
            },
            {
                question: "Can I provide information on specific products or services?",
                options: [
                    "Yes, please.",
                    "No, that's all for now."
                ],
                responses: ["specific_products", "end"],
                triggered_by: "general_inquiry",
                random_responses: [
                    "We offer solutions tailored to home and business needs.",
                    "Our products are designed with ease of use in mind.",
                    "If you’d like, I can also send you product documentation."
                ]
            }
        ];
        this.currentQuestion = this.questions[0];
    }

    start() {
        this.currentQuestion = this.questions[0];
        return this.formatQuestionMessage();
    }

    processMessage(userMessage) {
        if (!this.currentQuestion) {
            return "I'm not sure I understood that. Can you clarify?";
        }

        // Match the user's message to an option by checking for keywords in options
        let matchedResponse = null;
        this.currentQuestion.options.forEach((option, index) => {
            if (userMessage.toLowerCase().includes(option.toLowerCase())) {
                matchedResponse = this.currentQuestion.responses[index];
            }
        });

        if (matchedResponse) {
            // Get a random response from available responses for this question
            const randomResponse = this.getRandomResponse();

            // Find the next question based on the matched response
            const nextQuestion = this.questions.find(
                question => question.triggered_by === matchedResponse
            );
            this.currentQuestion = nextQuestion || null;
            return randomResponse + "<br>" + (nextQuestion ? this.formatQuestionMessage() : "Thank you for chatting with Pegasus Bot!");
        }

        return "I'm not sure I understood that. Please choose one of the available options.";
    }

    formatQuestionMessage() {
        let message = this.currentQuestion.question + "<br>";
        this.currentQuestion.options.forEach((option, index) => {
            message += `${index + 1}. ${option}<br>`;
        });
        return message;
    }

    getRandomResponse() {
        if (this.currentQuestion.random_responses) {
            const responses = this.currentQuestion.random_responses;
            const randomIndex = Math.floor(Math.random() * responses.length);
            return responses[randomIndex];
        }
        return "";
    }
}

// Initialize the bot instance
const bot = new PegasusBot();
const chatBody = document.getElementById("chatbot-body");

// Display the bot's initial message
chatBody.innerHTML += `<p><strong>Bot:</strong> ${bot.start()}</p>`;

// Function to handle sending messages
document.getElementById("send-btn").addEventListener("click", function () {
    const userInput = document.getElementById("user-input").value.trim();

    if (userInput !== "") {
        // Display user's message
        chatBody.innerHTML += `<p><strong>You:</strong> ${userInput}</p>`;

        // Get bot's response
        const botResponse = bot.processMessage(userInput);
        chatBody.innerHTML += `<p><strong>Bot:</strong> ${botResponse}</p>`;

        // Scroll to the latest message
        chatBody.scrollTop = chatBody.scrollHeight;

        // Clear input field
        document.getElementById("user-input").value = "";
    }
});

// Function to show/hide the chatbot popup
document.getElementById("chatbot-btn").addEventListener("click", function () {
    const chatbotPopup = document.getElementById("chatbot-popup");
    chatbotPopup.style.display = chatbotPopup.style.display === "none" ? "block" : "none";
});

// Function to close the chatbot popup
document.getElementById("close-btn").addEventListener("click", function () {
    document.getElementById("chatbot-popup").style.display = "none";
});

// Optional: Send message on pressing Enter key
document.getElementById("user-input").addEventListener("keypress", function (event) {
    if (event.key === "Enter") {
        event.preventDefault();  // Prevent form submission
        document.getElementById("send-btn").click();  // Trigger the send button click
    }
});
