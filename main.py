from flask import Flask, request, redirect, render_template
import re 

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/", methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route("/validate", methods=['POST'])
def validate_form():
    username = request.form['username']
    password = request.form['password']
    confirm_password = request.form['confirm_password']
    user_email = request.form['user_email']

    username_error = ''
    password_error = ''
    confirm_error = ''
    email_error = ''
    form_error = ''

    #-- ACCOUNT FOR EMPTY SPACES AND FIELDS--
    #username
    if username == '':
        username_error = "Please enter a username."
    elif ' ' in username:
        username_error = "Username may not contain any spaces."
        username = ''
    elif len(username) <= 3 or len(username)>= 20: 
        username_error = "Please enter a username between 3 and 20 characters."
        username = ''
        
    #password
    if password == '':
        passord_error = "Please enter a password."
    elif len(password) <= 3 or len(password)>= 20:
        password_error = "Please enter a password between 3 and 20 characters"

    #confirm
    if confirm_password == '':
        confirm_error = "Please confirm your password."
    elif password != confirm_password:
        confirm_error = "Passwords do not match."
    #email
    if user_email != '':
        if not re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", user_email):
            email_error = "Please enter a valid E-mail."
            user_email = ''

    #-- VERIFY LENGTH OF USERNAME AND PASSWORD <3  AND >20 --
    
    #-- VERIFY PASSWORD AND PASSWORD CONFIRMATION MATCH --
    
    #-- IF NO ERRORS, RENDER WELCOME PAGE --
    if not username_error and not password_error and not confirm_error and not email_error:
        return render_template('welcome.html', username=username)
    else:
        return render_template('index.html', username=username, 
                        password=password, 
                        user_email=user_email, username_error=username_error,
                        password_error=password_error, email_error=email_error 
                        )
 

app.run()