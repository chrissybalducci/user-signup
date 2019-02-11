from flask import Flask, request, redirect, render_template
import jinja2
import cgi

app = Flask(__name__)
app.config['DEBUG'] = True


@app.route("/", methods=['GET','POST'])
def index():
    if request.method == 'GET':
        return render_template("form.html")

    if request.method == 'POST':
        username = str(request.form['username-actual'])
        password = str(request.form['password-actual'])
        verifiedpassword = str(request.form['verifiedpassword-actual'])
        email = str(request.form['email-actual'])

        if username == '' or len(username) < 3 or len(username) > 20 or ' ' in username:
            usererror = "Invalid username."
        else:
            usererror = ""

        if password == '' or len(password) < 3 or len(password) > 20 or ' ' in password:
            passworderror = "Invalid password."
        else:
            passworderror = ""

        if verifiedpassword != password:
            verifiedpassworderror = "Passwords do not match."
        else:
            verifiedpassworderror = ""

        if email == '' or len(email) < 3 or len(email) > 20 or ' ' in email or '@' not in email:
            emailerror = "Your email address is invalid."
        else:
            emailerror = ""

    
        if len(usererror) > 0 or len(passworderror) > 0 or len(verifiedpassworderror) > 0 or len(emailerror) > 0:
            return render_template("form.html",usererror=usererror,
                                passworderror=passworderror,
                                verifiedpassworderror=verifiedpassworderror,
                                emailerror=emailerror,
                                username=username,
                                email=email)
        
        else:  
            return render_template("welcome.html",username=username) 

@app.route("/welcome", methods=['GET'])
def welcome_page():
    return render_template("welcome.html")

app.run()



    