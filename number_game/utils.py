from functools import wraps
from flask import session

#
# def check_login(func):
#     @wraps
#     def wrapper(*args, **kwargs):
#         if session.get('logged_in'):
#             return func(*args, **kwargs)
#         return "You need to make login"
#     return wrapper
