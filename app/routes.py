from flask import Blueprint, render_template, redirect, url_for, flash, request
from datetime import datetime

views = Blueprint('views', __name__)

@views.route('/')
@views.route('/home')
def home():
    return render_template('home.html')

@views.route('/journals', methods=['GET'])
def get_journal():
    # Fetch all journal entries from the database
    return render_template('journal_list.html')

@views.route('/journal', methods=['POST'])
def create_journal():
    return render_template('journal.html')

@views.route('/journal/<id>', methods=['PUT'])
def update_journal(id):
    return render_template('journal.html')

@views.route('/journal/<id>', methods=['DELETE'])
def delete_journal(id):
    return render_template('journal.html')