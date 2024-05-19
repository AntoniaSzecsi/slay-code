from flask import Flask, render_template, request, Blueprint, redirect, url_for, session
from .repository import *
from .utils import *

problems = Blueprint('problems', __name__)

@problems.route('/')
def index():
    problems = get_problems_with_categories_and_difficulty()

    if len(problems) == 0:
        add_initial_data()
        problems = get_all_problems_with_categories()

    if 'loggedin' in session:
        return render_template('index.html', problems=problems, username=session['username'])
    return render_template('index.html', problems=problems)
