
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import spacy, logging

spacy.load('en_core_web_sm')  # Ensures spaCy is loaded

logger = logging.getLogger()
logger.setLevel(logging.CRITICAL)

chatbot = ChatBot(
    'CollegeEnquiryBot',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        {
            'import_path': 'chatterbot.logic.BestMatch',
            'default_response': "I'm sorry, I didn't understand that. Please choose an appropriate option.",
            'maximum_similarity_threshold': 0.80
        }
    ],
    database_uri='sqlite:///database.sqlite3'
)

trainer = ListTrainer(chatbot)


# python app.py
# Training with Personal Ques & Ans 
conversation = [
   # Greetings
    "Hi", "Hello! 😊 How can I assist you today? Please enter a number for any query:",
    "Hey", "Hello there! 😃 Select an option below to proceed:",
    "Good Morning", "Hello Good Morning 😃 Select an option below to proceed",
    "How are you?", "I'm great, thank you! 😃 Go ahead and write the number for your query below:",

    # B.Tech Course Information
    "Tell me about B.Tech course", "The B.Tech program offers various streams. You can find more information here: <a href='https://shuats.org/webwapp/admission2024/courses_display.asp'>Click Here</a>",
    "What is the B.Tech course?", "The B.Tech program is a 4-year undergraduate course with multiple specializations. Details are available here: <a href='https://shuats.org/webwapp/admission2024/courses_display.asp'>Click Here</a>",

    # Faculty Section
    "Tell me about the faculty of agriculture", "The Faculty of Agriculture provides top-notch education and research opportunities. Learn more: <a href='https://shuats.org/webwapp/fac_agriculture.asp'>Click Here</a>",
    "What is the faculty of agriculture?", "The Faculty of Agriculture at SHUATS offers undergraduate and postgraduate courses. More details: <a href='https://shuats.org/webwapp/fac_agriculture.asp'>Click Here</a>",

    # Default fallback
    "What do you do?", "I am here to help you with SHUATS college-related information.",
    "What else can you do?", "I can guide you with details about Students, Faculty, Parents, and Visitor-related queries. 😊",

    # Section 1 - Student's Section
    "1", "<b>STUDENT SECTION</b><br>Choose from the options below:<br>1.1 Curriculars<br>1.2 Extra-Curriculars<br>1.3 Administrative<br>1.4 Examination<br>1.5 Placements",

    # 1.1 Curriculars
    "1.1", "<b>CURRICULAR</b><br>Select one:<br>1.1.1 Moodle<br>1.1.2 Academic Calendar<br>1.1.3 Syllabus",
    "1.1.1", "Here is the link to Moodle 👉 <a href='https://en.wikipedia.org/wiki/Sam_Higginbottom_University_of_Agriculture,_Technology_and_Sciences'>Click Here</a>",
    "1.1.2", "Find the Academic Calendar 👉 <a href='https://shuats.org/deppage/uploads/ACADEMIC-CALENDER-JAN-TO-JUNE-2024.pdf'>Click Here</a>",
    "1.1.3", "Access the Syllabus here 👉 <a href='https://shuats.edu.in/syllabus/BTFT.pdf'>Click Here</a>",

    # 1.2 Extra-Curriculars
    "1.2", "<b>EXTRA-CURRICULAR</b><br>Select one:<br>1.2.1 Events<br>1.2.2 Student Chapters<br>1.2.3 Student's Council",
    "1.2.1", "Check out Events 👉 <a href='https://shuats.org/webwapp/special_event_committee.asp'>Click Here</a>",
    "1.2.2", "Find Student Chapters 👉 <a href='http://www.frcrce.ac.in/index.php/students/forums'>Click Here</a>",
    "1.2.3", "Learn about the Student's Council 👉 <a href='https://shuats.org/webwapp/sch_council.asp'>Click Here</a>",

    # 1.3 Administrative
    "1.3", "<b>ADMINISTRATIVE</b><br>Select one:<br>1.3.1 Students Portal<br>1.3.2 Notices",
    "1.3.1", "Access the Students Portal 👉 <a href='https://shiatsmail.edu.in/webappsta/abpnhwwqjLisA85hKHKnC7rLwpq/?ID='>Click Here</a>",
    "1.3.2", "View Notices 👉 <a href='http://www.frcrce.ac.in/index.php/students/crce-notices/109-office-administration'>Click Here</a>",

    # Section 2 - Faculty Section
    "2", "<b>FACULTY SECTION</b><br>Select an option:<br>2.1 Faculty of VIAET<br>2.2 Facutly of Agriculture<br>2.3 Faculty of Health Sciences",

    # 2.1 Faculty of VIAET
    "2.1", "<b>Faculty Section</b><br>2.1.1 faculty of VIAET<br>",
    "2.1.1", "Faculty of VIAET 👉 <a href='https://shuats.org/webwapp/coll_vaugh.asp'>Click Here</a>",
    "2.1.2", "Access Moodle 👉 <a href='http://gyan.fragnel.edu.in:2222/moodle'>Click Here</a>",

    # 2.2 Faculty of Agriculture
    "2.2", "<b>Faculty Section</b><br>2.2.2 faculty of Agriculture<br>",
    "2.2.2", "Faculty of Agriculture 👉 <a href='https://shuats.org/webwapp/fac_agriculture.asp'>Click Here</a>",

    # 2.3 Faculty of Health Sciences 
    "2.3", "Faculty Section</br><br>2.3.3 faculty of Health Sciences<br>",
    "2.3.3", "Faculty of Health Sciences 👉 <a href='https://shuats.org/webwapp/fac_health_science.asp'>Click Here</a>",

    # Section 3 - Parents Section
    "3", "<b>PARENTS SECTION</b><br>Select an option:<br>3.1 About Us<br>3.2 Notices<br>3.3 Fee Payment<br>",
    "3.1", "<b>ABOUT US</b><br>Choose one:<br>3.1.1 About SHUATS<br>3.1.2 Director's of SHUATS<br>",
    "3.1.1", "Learn more About SHUATS 👉 <a href='https://shuats.org/webwapp/the_university.asp'>Click Here</a>",
    "3.1.2", "Director's of SHUATS 👉 <a href='https://shuats.org/webwapp/directors.asp'>Click Here</a>",

    "3.2", "<b>Notices</br><br>3.2.1 Notices<br>",
    "3.2.1", "Notices 👉 <a href='https://shuats.org/webwapp/admission2024/imp_dates.asp'>Click Here</a>",


    "3.3", "<b>Fee Payment</br><br>3.3.1 Fee Payment<br>",
    "3.3.1", "Fee Payment 👉 <a href='https://shuats.org/webwapp/pay_educational_fee.asp'>Click Here</a>",


    
    
    # Section 4 - Visitor's Section
    "4", "<b>VISITORS SECTION</b><br>Select an option:<br>4.1 About Us<br>4.2 Programs We Offer<br>4.3 Cost & Payment<br>4.4 Campus Life",
    "4.1", "<b>ABOUT US</b><br>4.1.1 About SHUATS<br>",
    "4.1.1", "About SHUATS 👉 <a href='https://shuats.org/webwapp/the_university.asp'>Click Here</a>",

    "4.2", "<b>Programs We Offer</br><br>4.2.2 Programs We Offer<br>",
    "4.2.2", "Programs We Offer 👉 <a href='https://shuats.org/webwapp/admission2024/courses_display.asp'>Click Here</a>",

    "4.3", "<b>Cost & Payment</br><br>4.3.3 Cost & Payment<br>",
    "4.3.3", "Cost & Payment 👉 <a href='https://shuats.org/webwapp/finan_assist.asp'>Click Here</a>",

    "4.4", "<b>Campus Life</br><br>4.4.4 Campus Life<br>",
    "4.4.4", "Campus Life 👉 <a href=https://shuats.org/webwapp/campus_life.asp>Click Here</a>",

    # Fallback for invalid input
    "default", "I'm sorry, I didn't understand that. Please enter a valid query number to proceed."
]


trainer.train(conversation)

# Default Response
default_response = "I didn't quite catch that. Could you please choose a number ?"

def get_response(user_input):
    user_input = user_input.lower()  # To handle case-insensitive input

    # Greeting section handling
    greetings = ["hi", "hey", "hello", "good morning", "how are you?", "hy"]
    if any(greeting in user_input for greeting in greetings):
        return "Hello! 😊 How can I assist you today? Please enter a number for any query:"

    # Faculty Section Query
    # Faculty Section Query
    if 'faculty' in user_input and 'viaet' in user_input:
        return ("<b>FACULTY OF VIAET</b><br>"
            "Learn more 👉 <a href='https://shuats.edu.in/VIAET.asp'>Click Here</a>")

    elif 'faculty' in user_input and 'agriculture' in user_input:
        return ("<b>FACULTY OF AGRICULTURE</b><br>"
            "Learn more 👉 <a href='https://shuats.edu.in/agriculture.asp'>Click Here</a>")

    elif 'faculty' in user_input and 'health sciences' in user_input:
        return ("<b>FACULTY OF HEALTH SCIENCES</b><br>"
             "Learn more 👉 <a href='https://shuats.edu.in/health_sciences.asp'>Click Here</a>")

    # General Faculty Section Query
    elif 'faculty' in user_input:
        return ("<b>FACULTY SECTION</b><br>"
            "Choose an option below:<br>"
            "1. Faculty of VIAET 👉 <a href='https://shuats.org/webwapp/coll_vaugh.asp'>Click Here</a><br>"
            "2. Faculty of Agriculture 👉 <a href='https://shuats.org/webwapp/fac_agriculture.asp'>Click Here</a><br>"
            "3. Faculty of Health Sciences 👉 <a href='https://shuats.org/webwapp/fac_health_science.asp'>Click Here</a>")



    # Student Section Query
    if 'student' in user_input and 'section' in user_input:
        return ("<b>STUDENT SECTION</b><br>"
                "Choose from the options below:<br>"
                "1.1 Curriculars<br>"
                "1.2 Extra-Curriculars<br>"
                "1.3 Administrative<br>"
                "1.4 Examination<br>"
                "1.5 Placements")

    # Curricular Queries
    if 'curricular' in user_input:
        return ("<b>CURRICULAR</b><br>Select one:<br>"
                "1.1.1 Moodle<br>1.1.2 Academic Calendar<br>1.1.3 Syllabus")

    if 'moodle' in user_input:
        return "Here is the link to Moodle 👉 <a href='https://en.wikipedia.org/wiki/Sam_Higginbottom_University_of_Agriculture,_Technology_and_Sciences'>Click Here</a>"
    if 'academic calendar' in user_input:
        return "Find the Academic Calendar 👉 <a href='https://shuats.org/deppage/uploads/ACADEMIC-CALENDER-JAN-TO-JUNE-2024.pdf'>Click Here</a>"
    if 'syllabus' in user_input:
        return "Access the Syllabus here 👉 <a href='https://shuats.edu.in/syllabus/BTFT.pdf'>Click Here</a>"

    # Extra-Curricular Queries
    if 'extra-curricular' in user_input:
        return ("<b>EXTRA-CURRICULAR</b><br>Select one:<br>"
                "1.2.1 Events<br>1.2.2 Student Chapters<br>1.2.3 Student's Council")

    if 'events' in user_input:
        return "Check out Events 👉 <a href='https://shuats.org/webwapp/special_event_committee.asp'>Click Here</a>"
    if 'student chapters' in user_input:
        return "Find Student Chapters 👉 <a href='http://www.frcrce.ac.in/index.php/students/forums'>Click Here</a>"
    if "student's council" in user_input:
        return "Learn about the Student's Council 👉 <a href='https://shuats.org/webwapp/sch_council.asp'>Click Here</a>"

    # Administrative Queries
    if 'administrative' in user_input:
        return ("<b>ADMINISTRATIVE</b><br>Select one:<br>"
                "1.3.1 Students Portal<br>1.3.2 Notices")

    if 'students portal' in user_input:
        return "Access the Students Portal 👉 <a href='https://shiatsmail.edu.in/webappsta/abpnhwwqjLisA85hKHKnC7rLwpq/?ID='>Click Here</a>"
    if 'notices' in user_input:
        return "View Notices 👉 <a href='http://www.frcrce.ac.in/index.php/students/crce-notices/109-office-administration'>Click Here</a>"

    # Parent Section Queries
    if 'parent' in user_input and 'section' in user_input:
        return ("<b>PARENTS SECTION</b><br>Choose an option:<br>"
                "3.1 About Us<br>3.2 Notices<br>3.3 Fee Payment")

    if 'fee payment' in user_input:
        return "Fee Payment 👉 <a href='https://shuats.org/webwapp/pay_educational_fee.asp'>Click Here</a>"
    if 'about us' in user_input and 'parent' in user_input:
        return "Learn more About SHUATS 👉 <a href='https://shuats.org/webwapp/the_university.asp'>Click Here</a>"

    # Visitor Section Queries
    if 'visitor' in user_input and 'section' in user_input:
        return ("<b>VISITORS SECTION</b><br>Choose an option:<br>"
                "4.1 About Us<br>4.2 Programs We Offer<br>4.3 Cost & Payment<br>4.4 Campus Life")

    if 'about us' in user_input and 'visitor' in user_input:
        return "About SHUATS 👉 <a href='https://shuats.org/webwapp/the_university.asp'>Click Here</a>"
    if 'programs' in user_input:
        return "Programs We Offer 👉 <a href='https://shuats.org/webwapp/admission2024/courses_display.asp'>Click Here</a>"
    if 'cost' in user_input or 'payment' in user_input:
        return "Cost & Payment 👉 <a href='https://shuats.org/webwapp/finan_assist.asp'>Click Here</a>"
    if 'campus life' in user_input:
        return "Campus Life 👉 <a href='https://shuats.org/webwapp/campus_life.asp'>Click Here</a>"

    # Fee structure queries for specific courses
    if 'fee structure' in user_input:
        if 'b.tech cse' in user_input or 'computer science' in user_input:
            return ("The fee structure for B.Tech CSE:<br>"
                    "1st Year: ₹85,000<br>2nd Year: ₹70,235<br>3rd Year: ₹70,0235<br>4th Year: ₹70,235<br>"
                    "For more details: <a href='https://shuats.org/webwapp/admission2023/fee-structure.asp'>Click Here</a>")
        elif 'b.tech ece' in user_input or 'electronics' in user_input:
            return ("The fee structure for B.Tech ECE:<br>"
                    "1st Year: ₹95,000<br>2nd Year: ₹85,000<br>3rd Year: ₹85,000<br>4th Year: ₹85,000<br>"
                    "For more details: <a href='https://shuats.org/webwapp/admission2023/fee-structure.asp'>Click Here</a>")
        elif 'b.tech mechanical' in user_input:
            return ("The fee structure for B.Tech Mechanical:<br>"
                    "1st Year: ₹1,10,000<br>2nd Year: ₹1,00,000<br>3rd Year: ₹1,00,000<br>4th Year: ₹1,00,000<br>"
                    "For more details: <a href='https://shuats.org/webwapp/admission2023/fee-structure.asp'>Click Here</a>")
        elif 'b.tech civil' in user_input:
            return ("The fee structure for B.Tech Civil Engineering:<br>"
                    "1st Year: ₹1,05,000<br>2nd Year: ₹95,000<br>3rd Year: ₹95,000<br>4th Year: ₹95,000<br>"
                    "For more details: <a href='https://shuats.org/webwapp/admission2023/fee-structure.asp'>Click Here</a>")
        else:
            return ("Please specify the course name (e.g., 'B.Tech CSE fee structure'). "
                    "For general fee details: <a href='https://shuats.org/webwapp/admission2023/fee-structure.asp'>Click Here</a>")


# # Start the chatbot
# while True:
#     user_input = input("You: ")
#     if user_input.lower() == "exit":
#         break
#     response = get_response(user_input)
#     print("Bot:", response)