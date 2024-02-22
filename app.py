# import base64
# import streamlit as st

# st.header('BookVerse', divider='rainbow')
# st.text('Where Every Page Tells a Story')

# def get_img_as_base64(file):
#     with open(file, "rb") as f:
#         data = f.read()
#     return base64.b64encode(data).decode()

# img = get_img_as_base64("photo5.jpg")

# selected_tab = st.sidebar.radio("MENU", ["Home", "Bookstore", "AboutUs", "Contact", "Login"])

# if selected_tab == "Home":
#     page_bg_img = f"""
#     <style>
#     [data-testid="stAppViewContainer"] > .main {{
#         background-image: url("data:image/png;base64,{img}");
#         background-size: cover;
#         background-position: center;
#         background-repeat: no-repeat;
#     }}
#     </style>
#     """

#     st.markdown(page_bg_img, unsafe_allow_html=True)

# # Container to show/hide content based on the selected tab
# container = st.container()

# # Render content based on the selected tab
# with container:
#     if selected_tab == "Home":
#         # Form
#         with st.form("search_form"):
#             # Form Fields
#             col1, col2 = st.columns(2)

#             with col1:
#                 st.text_input("Book Title", key="ad_title", placeholder="What Are You Looking For...")

#             with col2:
#                 st.selectbox("Select Category", options=[
#                     "Select Category", "Accountancy", "Arts", "Automobile", "Bollywood/Hollywood", "Business & Law",
#                     "Business Management", "CAT|GATE|GRE", "Civil", "Comics", "Commerce", "Competitive Exam",
#                     "Computer/Information Technology", "Economics", "Education", "Electrical", "Electronics", "Engineering",
#                     "Engineering Exams", "Fiction", "Finance", "Homeopathy", "Human Resource Management", "IBPS PO",
#                     "Lifestyle", "Magazines", "Management", "Management Books", "Marketing", "MBBS", "Mechanical", "Medical",
#                     "Medical", "Medicine", "NDA", "News", "Non-Fiction", "Nursing", "Operation Management", "Others", "Others",
#                     "Others", "Others", "Others", "Others", "Others", "Physiology", "Physiotherapy", "School Books", "Science",
#                     "STD 1-10th", "Stories", "UPSC"
#                 ], key="cat_id", index=0)

#             # Location
#             st.text_input("Book Author", key="author", placeholder="Author...")

#             # Submit Button
#             st.form_submit_button("Search")

#     elif selected_tab == "AboutUs":
#         st.header("AboutUs")
#         st.write("Welcome to our digital atelier, where we sculpt bestsellers with the precision of code and the artistry of insight.")
#         st.write("Here, the future of book sales isn't foretold; it's crafted with the finesse of data-driven imagination.")
    
#     elif selected_tab == "Contact":
#         st.header("ContactUs")
#         st.write("Feel free to contact us for any inquiries or feedback.")
#         # Contact Form
#         with st.form("contact_form"):
#             st.text_input("Your Name", key="contact_name", placeholder="Enter your name...")
#             st.text_input("Your Email", key="contact_email", placeholder="Enter your email...")
#             st.text_area("Your Message", key="contact_message", placeholder="Type your message here...")
#             st.form_submit_button("Submit")

#     elif selected_tab == "Login":
#         st.header("Login")
#         # Login Form
#         with st.form("login_form"):
#             st.text_input("Username", key="username", placeholder="Enter your username...")
#             st.text_input("Password", key="password", type="password", placeholder="Enter your password...")
#             login_button = st.form_submit_button("Login")

#         # Register Link
#         st.write("Don't have an account? [Register here](http://localhost:8000/registration.html)")


#     # Footer
#     st.markdown("""
#         --- 
#         *Bookie - Your Gateway to Literary Insights* 
#         [Privacy Policy](#) | [Terms of Service](#) | © 2023 Bookie Inc.
#     """)


# import base64
# import streamlit as st

# st.header('BookVerse', divider='rainbow')
# st.text('Where Every Page Tells a Story')

# def get_img_as_base64(file):
#     with open(file, "rb") as f:
#         data = f.read()
#     return base64.b64encode(data).decode()

# img = get_img_as_base64("photo5.jpg")

# selected_tab = st.sidebar.radio("MENU", ["Home", "Bookstore", "AboutUs", "Contact", "Login", "Register"])

# if selected_tab == "Home":
#     page_bg_img = f"""
#     <style>
#     [data-testid="stAppViewContainer"] > .main {{
#         background-image: url("data:image/png;base64,{img}");
#         background-size: cover;
#         background-position: center;
#         background-repeat: no-repeat;
#     }}
#     </style>
#     """

#     st.markdown(page_bg_img, unsafe_allow_html=True)

# # Container to show/hide content based on the selected tab
# container = st.container()

# # Render content based on the selected tab
# with container:
#     if selected_tab == "Home":
#         # Form
#         with st.form("search_form"):
#             # Form Fields
#             col1, col2 = st.columns(2)

#             with col1:
#                 st.text_input("Book Title", key="ad_title", placeholder="What Are You Looking For...")

#             with col2:
#                 st.selectbox("Select Category", options=[
#                     "Select Category", "Accountancy", "Arts", "Automobile", "Bollywood/Hollywood", "Business & Law",
#                     "Business Management", "CAT|GATE|GRE", "Civil", "Comics", "Commerce", "Competitive Exam",
#                     "Computer/Information Technology", "Economics", "Education", "Electrical", "Electronics", "Engineering",
#                     "Engineering Exams", "Fiction", "Finance", "Homeopathy", "Human Resource Management", "IBPS PO",
#                     "Lifestyle", "Magazines", "Management", "Management Books", "Marketing", "MBBS", "Mechanical", "Medical",
#                     "Medical", "Medicine", "NDA", "News", "Non-Fiction", "Nursing", "Operation Management", "Others", "Others",
#                     "Others", "Others", "Others", "Others", "Others", "Physiology", "Physiotherapy", "School Books", "Science",
#                     "STD 1-10th", "Stories", "UPSC"
#                 ], key="cat_id", index=0)

#             # Location
#             st.text_input("Book Author", key="author", placeholder="Author...")

#             # Submit Button
#             st.form_submit_button("Search")

#     elif selected_tab == "AboutUs":
#         st.header("AboutUs")
#         st.write("Welcome to our digital atelier, where we sculpt bestsellers with the precision of code and the artistry of insight.")
#         st.write("Here, the future of book sales isn't foretold; it's crafted with the finesse of data-driven imagination.")
    
#     elif selected_tab == "Contact":
#         st.header("ContactUs")
#         st.write("Feel free to contact us for any inquiries or feedback.")
#         # Contact Form
#         with st.form("contact_form"):
#             st.text_input("Your Name", key="contact_name", placeholder="Enter your name...")
#             st.text_input("Your Email", key="contact_email", placeholder="Enter your email...")
#             st.text_area("Your Message", key="contact_message", placeholder="Type your message here...")
#             st.form_submit_button("Submit")

#     elif selected_tab == "Login":
#         st.header("Login")
#     # Login Form
#         with st.form("login_form"):
#             username = st.text_input("Username", key="username", placeholder="Enter your username...")
#             password = st.text_input("Password", key="password", type="password", placeholder="Enter your password...")
#             login_button = st.form_submit_button("Login")

#         if login_button:
#             if password == '12345':  # Checking the password (example password: '12345')
#                 st.success("Logged In as {}".format(username))
#             else:
#                 st.warning("Incorrect Password")


#       # Register Button
#         if st.write("Don't have an account?  Register"):
#             selected_tab = "Register"

#     elif selected_tab == "Register":
#         st.header("Register")
#         # Registration Form
#         with st.form("register_form"):
#             email = st.text_input("Email:", key="reg_email", placeholder="Enter your email...")
#             password = st.text_input("Password:", key="reg_password", type="password", placeholder="Enter your password...")
#             confirm_password = st.text_input("Confirm Password:", key="confirm_password", type="password", placeholder="Confirm your password...")
#             register_button = st.form_submit_button("Register")

#         # Simulate registration process and redirect to login page
#         if register_button:
#             if email and password and password == confirm_password:
#                 st.success("Registration successful! Please login.")
#                 selected_tab = "Login"
#             else:
#                 st.error("Registration failed. Please check your inputs.")
#     # Footer
#     st.markdown("""
#         --- 
#         *Bookie - Your Gateway to Literary Insights* 
#         [Privacy Policy](#) | [Terms of Service](#) | © 2023 Bookie Inc.
#     """)





# import base64
# import streamlit as st

# # Dummy data for registered users
# registered_users = {
#     "shreyahippa@gmail.com": "shreya@123",
#     "shifaliujire@gmail.com": "shifali@123",
#     "tanvip@123.com": "tanvi@123"
# }


# st.header('BookVerse', divider='rainbow')
# st.text('Where Every Page Tells a Story')

# def get_img_as_base64(file):
#     with open(file, "rb") as f:
#         data = f.read()
#     return base64.b64encode(data).decode()

# img = get_img_as_base64("photo5.jpg")

# selected_tab = st.sidebar.radio("MENU", ["Home", "Bookstore", "AboutUs", "Contact", "Login", "Register"])

# if selected_tab == "Home":
#     page_bg_img = f"""
#     <style>
#     [data-testid="stAppViewContainer"] > .main {{
#         background-image: url("data:image/png;base64,{img}");
#         background-size: cover;
#         background-position: center;
#         background-repeat: no-repeat;
#     }}
#     </style>
#     """

#     st.markdown(page_bg_img, unsafe_allow_html=True)

# # Container to show/hide content based on the selected tab
# container = st.container()

# # Render content based on the selected tab
# with container:
#     if selected_tab == "Home":
#         # Form
#         with st.form("search_form"):
#             # Form Fields
#             col1, col2 = st.columns(2)

#             with col1:
#                 st.text_input("Book Title", key="ad_title", placeholder="What Are You Looking For...")

#             with col2:
#                 st.selectbox("Select Category", options=[
#                     "Select Category", "Accountancy", "Arts", "Automobile", "Bollywood/Hollywood", "Business & Law",
#                     "Business Management", "CAT|GATE|GRE", "Civil", "Comics", "Commerce", "Competitive Exam",
#                     "Computer/Information Technology", "Economics", "Education", "Electrical", "Electronics", "Engineering",
#                     "Engineering Exams", "Fiction", "Finance", "Homeopathy", "Human Resource Management", "IBPS PO",
#                     "Lifestyle", "Magazines", "Management", "Management Books", "Marketing", "MBBS", "Mechanical", "Medical",
#                     "Medical", "Medicine", "NDA", "News", "Non-Fiction", "Nursing", "Operation Management", "Others", "Others",
#                     "Others", "Others", "Others", "Others", "Others", "Physiology", "Physiotherapy", "School Books", "Science",
#                     "STD 1-10th", "Stories", "UPSC"
#                 ], key="cat_id", index=0)

#             # Location
#             st.text_input("Book Author", key="author", placeholder="Author...")

#             # Submit Button
#             st.form_submit_button("Search")

#     elif selected_tab == "AboutUs":
#         st.header("AboutUs")
#         st.write("Welcome to our digital atelier, where we sculpt bestsellers with the precision of code and the artistry of insight.")
#         st.write("Here, the future of book sales isn't foretold; it's crafted with the finesse of data-driven imagination.")
    
#     elif selected_tab == "Contact":
#         st.header("ContactUs")
#         st.write("Feel free to contact us for any inquiries or feedback.")
#         # Contact Form
#         with st.form("contact_form"):
#             st.text_input("Your Name", key="contact_name", placeholder="Enter your name...")
#             st.text_input("Your Email", key="contact_email", placeholder="Enter your email...")
#             st.text_area("Your Message", key="contact_message", placeholder="Type your message here...")
#             st.form_submit_button("Submit")

#     elif selected_tab == "Login":
#         st.header("Login")
#         # Login Form
#         with st.form("login_form"):
#             email = st.text_input("Email", key="login_email", placeholder="Enter your email...")
#             password = st.text_input("Password", key="login_password", type="password", placeholder="Enter your password...")
#             login_button = st.form_submit_button("Login")

#         if login_button:
#             if email in registered_users and registered_users[email] == password:
#                 st.success("Logged In successfully!")
#             else:
#                 st.error("Invalid email or password")

#     elif selected_tab == "Register":
#         st.header("Register")
#         # Registration Form
#         with st.form("register_form"):
#             email = st.text_input("Email", key="reg_email", placeholder="Enter your email...")
#             password = st.text_input("Password", key="reg_password", type="password", placeholder="Enter your password...")
#             confirm_password = st.text_input("Confirm Password", key="confirm_password", type="password", placeholder="Confirm your password...")
#             register_button = st.form_submit_button("Register")

#         # Simulate registration process and redirect to login page
#         if register_button:
#             if email and password and password == confirm_password:
#                 st.success("Registration successful! Please login.")
#                 selected_tab = "Login"
#             else:
#                 st.error("Registration failed. Please check your inputs.")

# # Footer
# st.markdown("""
#     --- 
#     *Bookie - Your Gateway to Literary Insights* 
#     [Privacy Policy](#) | [Terms of Service](#) | © 2023 Bookie Inc.
# """)



import base64
import streamlit as st
import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash

st.header('BookVerse', divider='rainbow')
st.text('Where Every Page Tells a Story')

# Function to create a database connection
def create_connection():
    conn = sqlite3.connect('use_database.db')
    return conn

# Function to create a user table if it doesn't exist
def create_user_table(conn):
    try:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                email TEXT UNIQUE,
                password TEXT
            )
        ''')
        conn.commit()
    except sqlite3.Error as e:
        st.error(f'Error creating user table: {e}')

# Function to register a new user
def register_user(email, password):
    try:
        conn = create_connection()
        cursor = conn.cursor()
        hashed_password = generate_password_hash(password)
        cursor.execute('INSERT INTO users (email, password) VALUES (?, ?)', (email, hashed_password))
        conn.commit()
        st.success('Registration successful!')
    except sqlite3.IntegrityError:
        st.error('Email already exists. Please choose a different email.')
    except sqlite3.Error as e:
        st.error(f'Error registering user: {e}')
    finally:
        conn.close()

# Function to authenticate a user
def authenticate_user(email, password):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users WHERE email = ?', (email,))
    user = cursor.fetchone()
    conn.close()
    if user and check_password_hash(user[2], password):
        return True
    else:
        return False

# Create the users table if it doesn't exist
create_user_table(create_connection())

selected_tab = st.sidebar.radio("MENU", ["Home", "Bookstore", "AboutUs", "Contact", "Login", "Register"])

if selected_tab == "Home":
    # Your existing Home tab content here...
    with st.form("search_form"):
            # Form Fields
            col1, col2 = st.columns(2)

            with col1:
                st.text_input("Book Title", key="ad_title", placeholder="What Are You Looking For...")

            with col2:
                st.selectbox("Select Category", options=[
                    "Select Category", "Accountancy", "Arts", "Automobile", "Bollywood/Hollywood", "Business & Law",
                    "Business Management", "CAT|GATE|GRE", "Civil", "Comics", "Commerce", "Competitive Exam",
                    "Computer/Information Technology", "Economics", "Education", "Electrical", "Electronics", "Engineering",
                    "Engineering Exams", "Fiction", "Finance", "Homeopathy", "Human Resource Management", "IBPS PO",
                    "Lifestyle", "Magazines", "Management", "Management Books", "Marketing", "MBBS", "Mechanical", "Medical",
                    "Medical", "Medicine", "NDA", "News", "Non-Fiction", "Nursing", "Operation Management", "Others", "Others",
                    "Others", "Others", "Others", "Others", "Others", "Physiology", "Physiotherapy", "School Books", "Science",
                    "STD 1-10th", "Stories", "UPSC"
                ], key="cat_id", index=0)

            # Location
            st.text_input("Book Author", key="author", placeholder="Author...")

            # Submit Button
            st.form_submit_button("Search")
    pass

elif selected_tab == "AboutUs":
    # Your existing AboutUs tab content here...
    st.header("AboutUs")
    st.write("Welcome to our digital atelier, where we sculpt bestsellers with the precision of code and the artistry of insight.")
    st.write("Here, the future of book sales isn't foretold; it's crafted with the finesse of data-driven imagination.")
    pass
    
elif selected_tab == "Contact":
    # Your existing Contact tab content here...
    st.header("ContactUs")
    st.write("Feel free to contact us for any inquiries or feedback.")
        # Contact Form
    with st.form("contact_form"):
        st.text_input("Your Name", key="contact_name", placeholder="Enter your name...")
        st.text_input("Your Email", key="contact_email", placeholder="Enter your email...")
        st.text_area("Your Message", key="contact_message", placeholder="Type your message here...")
        st.form_submit_button("Submit")
    pass

elif selected_tab == "Login":
    st.header("Login")
    # Login Form
    with st.form("login_form"):
        email = st.text_input("Email", key="login_email", placeholder="Enter your email...")
        password = st.text_input("Password", key="login_password", type="password", placeholder="Enter your password...")
        login_button = st.form_submit_button("Login")

    if login_button:
        if authenticate_user(email, password):
            st.success("Login successful!")
            # Redirect or perform actions after successful login
        else:
            st.error("Invalid email or password")

elif selected_tab == "Register":
    st.header("Register")
    # Registration Form
    with st.form("register_form"):
        email = st.text_input("Email", key="register_email", placeholder="Enter your email...")
        password = st.text_input("Password", key="register_password", type="password",placeholder="Enter your password...")
        confirm_password = st.text_input("Confirm Password", key="confirm_password", type="password",placeholder="Confirm your password...")
        register_button = st.form_submit_button("Register")

    if register_button:
        if password == confirm_password:
            register_user(email, password)
        else:
            st.error("Passwords do not match")

# Footer
st.markdown("""
    --- 
    *Bookie - Your Gateway to Literary Insights* 
    [Privacy Policy](#) | [Terms of Service](#) | © 2023 Bookie Inc.
""")

















# import base64
# import streamlit as st
# import sqlite3
# from werkzeug.security import generate_password_hash, check_password_hash
# import smtplib
# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText


# st.header('BookVerse', divider='rainbow')
# st.text('Where Every Page Tells a Story')

# # Function to create a database connection
# def create_connection():
#     conn = sqlite3.connect('use_database.db')
#     return conn

# def create_user_table(conn):
#     try:
#         cursor = conn.cursor()
#         cursor.execute('DROP TABLE IF EXISTS users')
#         cursor.execute('''
#             CREATE TABLE users (
#                 id INTEGER PRIMARY KEY AUTOINCREMENT,
#                 email TEXT UNIQUE,
#                 password TEXT
#             )
#         ''')
#         conn.commit()
#     except sqlite3.Error as e:
#         st.error(f'Error creating user table: {e}')


# # Function to register a new user and send a confirmation email
# def register_user(email, password):
#     try:
#         conn = create_connection()
#         cursor = conn.cursor()
#         hashed_password = generate_password_hash(password)
#         cursor.execute('INSERT INTO users (email, password) VALUES (?, ?)', (email, hashed_password))
#         conn.commit()
#         st.success('Registration successful!')
#         send_confirmation_email(email)  # Send confirmation email
#     except sqlite3.IntegrityError:
#         st.error('Email already exists. Please choose a different email.')
#     except sqlite3.Error as e:
#         st.error(f'Error registering user: {e}')
#     finally:
#         conn.close()

# # Function to send a confirmation email
# def send_confirmation_email(email):
#     # Configure the SMTP server
#     smtp_server = "smtp.gmail.com"  # Update with your SMTP server address
#     smtp_port = 587  # Update with your SMTP port
#     sender_email = "shreyahippa@gmail.com"  # Update with your email address
#     sender_password = "shreya"  # Update with your email password
    
#     # Create a multipart message
#     message = MIMEMultipart()
#     message["From"] = sender_email
#     message["To"] = email
#     message["Subject"] = "Registration Confirmation"
    
#     # Add body to email
#     body = "Thank you for registering with BookVerse!"
#     message.attach(MIMEText(body, "plain"))
    
#     # Connect to the SMTP server and send the email
#     with smtplib.SMTP(smtp_server, smtp_port) as server:
#         server.starttls()
#         server.login(sender_email, sender_password)
#         server.sendmail(sender_email, email, message.as_string())

# # Function to authenticate a user
# def authenticate_user(email, password):
#     conn = create_connection()
#     cursor = conn.cursor()
#     cursor.execute('SELECT * FROM users WHERE email = ?', (email,))
#     user = cursor.fetchone()
#     conn.close()
#     if user and check_password_hash(user[2], password):
#         return True
#     else:
#         return False

# # Create the users table if it doesn't exist
# create_user_table(create_connection())

# selected_tab = st.sidebar.radio("MENU", ["Home", "Bookstore", "AboutUs", "Contact", "Login", "Register"])

# if selected_tab == "Home":
#     # Your existing Home tab content here...
#     with st.form("search_form"):
#             # Form Fields
#             col1, col2 = st.columns(2)

#             with col1:
#                 st.text_input("Book Title", key="ad_title", placeholder="What Are You Looking For...")

#             with col2:
#                 st.selectbox("Select Category", options=[
#                     "Select Category", "Accountancy", "Arts", "Automobile", "Bollywood/Hollywood", "Business & Law",
#                     "Business Management", "CAT|GATE|GRE", "Civil", "Comics", "Commerce", "Competitive Exam",
#                     "Computer/Information Technology", "Economics", "Education", "Electrical", "Electronics", "Engineering",
#                     "Engineering Exams", "Fiction", "Finance", "Homeopathy", "Human Resource Management", "IBPS PO",
#                     "Lifestyle", "Magazines", "Management", "Management Books", "Marketing", "MBBS", "Mechanical", "Medical",
#                     "Medical", "Medicine", "NDA", "News", "Non-Fiction", "Nursing", "Operation Management", "Others", "Others",
#                     "Others", "Others", "Others", "Others", "Others", "Physiology", "Physiotherapy", "School Books", "Science",
#                     "STD 1-10th", "Stories", "UPSC"
#                 ], key="cat_id", index=0)

#             # Location
#             st.text_input("Book Author", key="author", placeholder="Author...")

#             # Submit Button
#             st.form_submit_button("Search")
#     pass

# elif selected_tab == "AboutUs":
#     # Your existing AboutUs tab content here...
#     st.header("AboutUs")
#     st.write("Welcome to our digital atelier, where we sculpt bestsellers with the precision of code and the artistry of insight.")
#     st.write("Here, the future of book sales isn't foretold; it's crafted with the finesse of data-driven imagination.")
#     pass
    
# elif selected_tab == "Contact":
#     # Your existing Contact tab content here...
#     st.header("ContactUs")
#     st.write("Feel free to contact us for any inquiries or feedback.")
#         # Contact Form
#     with st.form("contact_form"):
#         st.text_input("Your Name", key="contact_name", placeholder="Enter your name...")
#         st.text_input("Your Email", key="contact_email", placeholder="Enter your email...")
#         st.text_area("Your Message", key="contact_message", placeholder="Type your message here...")
#         st.form_submit_button("Submit")
#     pass

# elif selected_tab == "Login":
#     st.header("Login")
#     # Login Form
#     with st.form("login_form"):
#         email = st.text_input("Email", key="login_email", placeholder="Enter your email...")
#         password = st.text_input("Password", key="login_password", type="password", placeholder="Enter your password...")
#         login_button = st.form_submit_button("Login")

#     if login_button:
#         if authenticate_user(email, password):
#             st.success("Login successful!")
#             # Redirect or perform actions after successful login
#         else:
#             st.error("Invalid email or password")

# elif selected_tab == "Register":
#     st.header("Register")
#     # Registration Form
#     with st.form("register_form"):
#         email = st.text_input("Email", key="register_email", placeholder="Enter your email...")
#         password = st.text_input("Password", key="register_password", type="password",placeholder="Enter your password...")
#         confirm_password = st.text_input("Confirm Password", key="confirm_password", type="password",placeholder="Confirm your password...")
#         register_button = st.form_submit_button("Register")

#     if register_button:
#         if password == confirm_password:
#             register_user(email, password)
#         else:
#             st.error("Passwords do not match")

# # Footer
# st.markdown("""
#     --- 
#     *Bookie - Your Gateway to Literary Insights* 
#     [Privacy Policy](#) | [Terms of Service](#) | © 2023 Bookie Inc.
# """)

