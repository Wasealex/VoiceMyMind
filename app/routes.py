from flask import render_template, redirect, url_for, flash, request
from app import app, db
from app.models import Journal
from datetime import datetime

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/journal', methods=['GET', 'POST'])
def journal():
    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        journal = journal(title=title, body=body, timestamp=datetime.utcnow())
        db.session.add(journal)
        db.session.commit()
        flash('Journal entry created!', 'success')
        return redirect(url_for('journal_list'))
    return render_template('journal.html')