from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.controllers import emails
from flask import flash
import re	# the regex module
# create a regular expression object that we'll use later   
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

class Email:
    def __init__(self, data):
        self.id = data['id']
        self.address = data['address']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    @staticmethod
    def validate_email( email ):
        is_valid = True
        if not EMAIL_REGEX.match(email['eaddress']):
            flash('Invalid email address!!!')
            is_valid = False
        return is_valid    
    @classmethod
    def add_email(cls, data):
        query = 'INSERT INTO email_addresses (address, created_at, updated_at) VALUES (%(eaddress)s, NOW(), NOW());'
        return connectToMySQL('emails').query_db(query, data)
    @classmethod
    def show_emails(cls):
        query = 'SELECT * FROM email_addresses'
        results = connectToMySQL('emails').query_db(query)
        emails = []
        for email in results:
            emails.append( cls(email) )
        return emails