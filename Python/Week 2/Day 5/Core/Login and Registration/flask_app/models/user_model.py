from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask import flash
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

class User:
    def __init__(self,data):
        self.id=data["id"]
        self.first_name=data["first_name"]
        self.last_name=data["last_name"]
        self.email=data["email"]
        self.password=data["password"]
    
    @classmethod
    def create(cls,data):
        query="""INSERT INTO users 
                            (first_name,last_name,email,password)
                            VALUES (%(first_name)s,%(last_name)s,%(email)s,%(password)s)"""
        return connectToMySQL(DATABASE).query_db(query,data)
    @classmethod
    def get_by_id(cls,data):
        query="""SELECT * FROM users WHERE id=%(id)s"""
        result=connectToMySQL(DATABASE).query_db(query,data)
        if result:
            return cls(result[0])
        return None
    @classmethod
    def get_by_email(cls,data):
        query="""SELECT * FROM users WHERE email=%(email)s"""
        result=connectToMySQL(DATABASE).query_db(query,data)
        if result:
            return cls(result[0])
        return False
    @staticmethod
    def validate(data):
        is_valid=True

        #                              ******Full-Name Section******
        # Flash if first_name/last_name less than 2 char.
        if len(data["first_name"])<2:
            is_valid=False
            flash("First name must contains at least 2 characters. ","register")
        if len(data["last_name"])<2:
            is_valid=False
            flash("Last name must contains at least 2 characters. ","register")


        #                              ******Email Section******
        # Flash if Email unvalid/REGEX.
        if not EMAIL_REGEX.match(data['email']):
            flash("Invalid email address.","register")
            is_valid=False
        # Unused Email.
        if User.get_by_email({'email':data['email']}):
            flash("Email already been used.","register")
            is_valid=False


        #                              ******Password Section******

        # Flash if pw less than 6 char.
        if len(data["password"])<6:
            flash("Password is too short","register")
            is_valid=False
        # Flash if pw doesn't match.
        elif data["password"]!=data["confirm_pw"]:
            flash("Password must match","register")
            is_valid=False
        return is_valid