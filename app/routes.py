from flask import render_template, redirect, url_for, flash, request
from app import app
from datetime import datetime

@app.route('/')
@app.route('/home')
def index():
    return render_template('index.html')

@app.route('/journal', methods=['GET'])
def get_journal():
    return render_template('journal_list.html')

@app.route('/journal', methods =['POST'])
def create_journal():
    return render_template('journal_html')

@app.route('/journal/<id>', method=['PUT'])
def update_journal():
    return render_template('journal_html')

@app.route('journal/<id>', method=['DELETE'])
def delete_journal():
    return render_template('journal.html')