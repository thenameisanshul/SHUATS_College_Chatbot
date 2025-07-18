conversation = [
    "Hi", 
    "Helloo!", 
    "Hey",

    "How are you?", 
    "I'm good.</br> <br>Go ahead and write the number of any query. 😃✨ <br> 1.&emsp;Student's Section Enquiry.</br>2.&emsp;Faculty Section Enquiry. </br>3.&emsp;Parent's Section Enquiry.</br>4.&emsp;Visitor's Section Enquiry.</br>",

    "Great", 
    "Go ahead and write the number of any query. 😃✨ <br> 1.&emsp;Student's Section Enquiry.</br>2.&emsp;Faculty Section Enquiry. </br>3.&emsp;Parent's Section Enquiry.</br>4.&emsp;Visitor's Section Enquiry.</br>",

    "Bye", 
    "Thank you for visiting! Have a great day. 😊✨",

    "1", 
    "<b>STUDENT <br>The following are frequently searched terms related to students. Please select one from the options below: <br> <br> 1.1 Curriculars <br>1.2 Extra-Curriculars<br>1.3 Administrative<br>1.4 Examination <br>1.5 Placements </b>",

    # Add all other specific responses as per your previous conversation list
]

# Default Response
default_response = "I didn't quite catch that. Could you please choose a number from 1 to 4?"

# Function to get the appropriate response
def get_response(user_input):
    if user_input in conversation:
        # Return the response if the user input matches any in the list
        return conversation[conversation.index(user_input) + 1]
    else:
        # Return default response if user input is not in the list
        return default_response

while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        break
    response = get_response(user_input)
    print("Bot:", response)
