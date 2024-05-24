from flask import Blueprint, render_template, redirect, url_for, flash, request, jsonify
from flask_login import login_required, current_user
from app.models import Journal
from app import db
import json

views = Blueprint('views', __name__)

@views.route('/home', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
        title = request.form.get('title')
        body = request.form.get('body')
        new_journal = Journal(title=title, body=body, author=current_user, user_id=current_user.id)
        db.session.add(new_journal)
        db.session.commit()
        flash('Journal entry created.', category='success')
        return redirect(url_for('views.home'))
    return render_template('home.html', user=current_user)

@views.route('/update_journals', methods=['GET'])
def get_journal():
    # Fetch all journal entries from the database
    return render_template('journal_list.html', user=current_user)

@views.route('/journal', methods=['POST'])
def create_journal():
    return render_template('journal.html')
@views.route('/journal_list/<uuid:journal_id>', methods=['POST'])
@login_required
def update_journal(journal_id):
    journal = Journal.query.get(journal_id)
    if journal and journal.author == current_user:
        journal.title = request.form.get('title')
        journal.body = request.form.get('body')
        db.session.commit()
        flash('Journal entry updated.', category='success')
        return redirect(url_for('views.get_journal'))
    else:
        flash('You do not have permission to update this journal entry.', category='error')
        return redirect(url_for('views.home'))


@views.route('/delete_journal/<uuid:journal_id>', methods=['POST'])
@login_required
def delete_journal(journal_id):
    journal = Journal.query.get(journal_id)
    if journal and journal.author == current_user:
        db.session.delete(journal)
        db.session.commit()
        flash('Journal entry deleted.', category='success')
        return redirect(url_for('views.get_journal'))
    else:
        flash('You do not have permission to delete this journal entry.', category='error')
        return redirect(url_for('views.journal_list'))
