import sys
import json

class PegasusBot:
    def __init__(self):
        self.current_question = 0
        self.questions = [
            {
                "question": "What can I help you with today?",
                "options": [
                    "1. Learn about Pegasus Automation products",
                    "2. Get technical support for my devices",
                    "3. General inquiry about home automation"
                ],
                "responses": ["learn_products", "technical_support", "general_inquiry"]
            },
            {
                "question": "Which type of smart device are you interested in?",
                "options": [
                    "1. Smart Lighting",
                    "2. Security Cameras",
                    "3. Thermostats",
                    "4. Other Devices"
                ],
                "responses": ["smart_lighting", "security_cameras", "thermostats", "other_devices"],
                "triggered_by": "learn_products"
            },
            {
                "question": "What kind of issue are you facing?",
                "options": [
                    "1. Connectivity issues",
                    "2. Device not responding",
                    "3. App not working properly"
                ],
                "responses": ["connectivity_issue", "device_not_responding", "app_issue"],
                "triggered_by": "technical_support"
            },
            {
                "question": "Can I provide more information on the following topics?",
                "options": [
                    "1. How to get started with home automation",
                    "2. Benefits of home automation",
                    "3. Pricing of smart devices"
                ],
                "responses": ["getting_started", "benefits", "pricing"],
                "triggered_by": "general_inquiry"
            }
        ]
        self.flow_responses = {
            "smart_lighting": "Pegasus offers smart lighting solutions that allow you to control your lights from anywhere.",
            "security_cameras": "We offer a range of security cameras for home monitoring, providing safety and peace of mind.",
            "thermostats": "Our smart thermostats help you manage your home's temperature efficiently.",
            "other_devices": "Pegasus provides a variety of devices, including smart locks and sensors.",
            "connectivity_issue": "If you're facing connectivity issues, please try restarting your router or resetting the device.",
            "device_not_responding": "If your device isn't responding, check if it's properly powered and connected.",
            "app_issue": "For app issues, please ensure you're using the latest version and try reinstalling it if necessary.",
            "getting_started": "Home automation allows you to control your home devices remotely. You can start with simple lighting or security solutions.",
            "benefits": "Home automation offers convenience, security, and energy efficiency.",
            "pricing": "The pricing of our devices varies based on the model. Please visit our website for more details."
        }

    def get_initial_question(self):
        """Return the first question and options as a JSON response."""
        current = self.questions[self.current_question]
        return json.dumps({
            "question": current["question"],
            "options": current["options"],
            "responses": current["responses"]
        })

    def handle_response(self, user_response):
        """Process the user's response and return the next question or final response."""
        current = self.questions[self.current_question]

        if user_response in current["responses"]:
            if user_response in self.flow_responses:
                return json.dumps({
                    "response": self.flow_responses[user_response],
                    "end": True
                })
            else:
                # Find the next question based on the trigger
                for i, question in enumerate(self.questions):
                    if question.get("triggered_by") == user_response:
                        self.current_question = i
                        next_question = self.questions[self.current_question]
                        return json.dumps({
                            "question": next_question["question"],
                            "options": next_question["options"],
                            "responses": next_question["responses"],
                            "end": False
                        })

        return json.dumps({
            "error": "Invalid input. Please select a valid option.",
            "end": False
        })

if __name__ == "__main__":
    bot = PegasusBot()
    if len(sys.argv) > 1:
        user_input = sys.argv[1]
        print(bot.handle_response(user_input))
    else:
        print(bot.get_initial_question())
