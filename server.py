from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)

# @app.route("/")
# def hello_world():
#     return "<p>Welcome to python web, Uche!</p>"

@app.route("/")  #VARIABLES
def my_home():
    return render_template('index.html')


#JUST added to reduce my stress
@app.route("/<string:page_name>")
def index(page_name):
    return render_template(page_name)


# def write_to_file(data):
#     with open('database.txt', mode='a') as  database:
#         email = data['email']
#         subject = data['subject']
#         message = data['message']
#         file = database.write(f'\n--------------\nEmail: {email}\nSubject: {subject}\nMessage: {message}')


def write_to_csv(data):
    with open('database.csv', mode='a', newline='') as  database2:
        fieldnames = ['email', 'subject', 'message']
        writer = csv.DictWriter(database2, fieldnames=fieldnames)
        writer.writerow(data)

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
           #name = request.form['name']
           data = request.form.to_dict() #GET THE DATA INTO A DICTIONARY
           #print(data)
           #write_to_file(data)
           write_to_csv(data)
           return redirect('./thankyou.html') #'<h3>Form submitted successfully.</h3>'
        except:
            return "You data could not be saved."

    else:
        return "Something went wrong, try gain."
#
# @app.route("/about.html")
# def about():
#     return render_template('about.html')
#
# @app.route("/work.html")
# def work():
#     return render_template('about')
#
# @app.route("/works.html")
# def works():
#     return render_template('works.html')
#
# @app.route("/components.html")
# def components():
#     return render_template('components.html')
#
# @app.route("/contact.html")
# def contact():
#     return render_template('contact.html')
#
# @app.route("/thankyou.html")
# def thankyou():
#     return render_template('thankyou.html')
#
# @app.route("/blog")
# def blog():
#     return "<p>This is our blog post</p>"
#
# @app.route("/blog/2020/dog")
# def blog2():
#     return "<p>I don't have a dog yet</p>"