from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.email import Email

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add_email', methods=['POST'])
def add_email():

    if not Email.validate_email(request.form):
        return redirect('/')

    data = {
        'eaddress' : request.form['eaddress']
    }
    Email.add_email(data)
    return redirect('/')


@app.route('/show_emails')
def show_emails():
    emails = Email.show_emails()
    return render_template('show.html', emails = emails)