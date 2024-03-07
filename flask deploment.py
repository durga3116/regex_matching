from flask import Flask, render_template,request
import re

app = Flask(__name__)

@app.route('/', methods=["GET"])
def home():
    return render_template("index.html")

@app.route('/results', methods=["POST"])
def results():
    test_string = request.form.get("test_string")
    regex_pattern = request.form.get("regex_pattern")
    matched_strings = re.findall(regex_pattern, test_string)
    
    return render_template("results.html", test_string=test_string, regex_pattern=regex_pattern, matched_strings=matched_strings)


@app.route('/validate-email', methods=["GET", "POST"])
def validate_email():
    email = ""
    is_valid = False

    if request.method == "POST":
        email = request.form.get("email")
        email_pattern = r'^[\w\.-]+@[a-zA-Z\d\.-]+\.[a-zA-Z]{2,}$'
        is_valid = re.match(email_pattern, email) is not None
    return render_template("validate_email.html", email=email, is_valid=is_valid)



if __name__ == "__main__":
    app.run( host="0.0.0.0",port =5000,debug=True)