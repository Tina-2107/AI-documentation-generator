import os
import math
from datetime import datetime

PI = 3.14159
APP_NAME = "Documentation Generator"
DEBUG = True

class User:
    """Represents a user."""

    def __init__(self, username, email):
        self.username = username
        self.email = email

    def login(self, password):
        """Login the user."""
        return True


class Calculator:
    def add(self, a, b):
        """Add two numbers."""
        return a + b

    def subtract(self, a, b):
        return a - b


def greet(name):
    """Greet a user."""
    return f"Hello {name}"


def square(number):
    return number * number