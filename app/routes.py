from flask import Blueprint, render_template, redirect, url_for, flash, request, jsonify
from flask_login import login_required, current_user
from app.models import Journal
from app import db
import json

views = Blueprint('views', __name__)

@views.route('/all', methods=['GET', 'POST'])
@login_required
def myjournal():
    return render_template('all.html', user=current_user)

@views.route('/create', methods=['GET', 'POST'])
@login_required
def create_journal():
    if request.method == 'POST':
        title = request.form.get('title')
        body = request.form.get('body')
        new_journal = Journal(title=title, body=body, author=current_user, user_id=current_user.id)
        db.session.add(new_journal)
        db.session.commit()
        flash('Journal entry created.', category='success')
        return redirect(url_for('views.myjournal'))
    return render_template('create_journal.html', user=current_user)
@views.route('/update/<uuid:journal_id>', methods=['GET', 'POST'])
@login_required
def update_journal(journal_id):
    journal = Journal.query.get(journal_id)
    if journal and journal.author == current_user:
        if request.method == 'POST':
            journal.title = request.form.get('title')
            journal.body = request.form.get('body')
            db.session.commit()
            flash('Journal entry updated.', category='success')
            return redirect(url_for('views.myjournal', journal_id=journal_id))
        return render_template('update_journal.html', journal=journal, user=current_user)
    else:
        flash('You do not have permission to update this journal entry.', category='error')
        return redirect(url_for('views.myjournal'))

@views.route('/delete/<uuid:journal_id>', methods=['GET', 'POST'])
@login_required
def delete_journal(journal_id):
    journal = Journal.query.get(journal_id)
    if journal and journal.author == current_user:
        db.session.delete(journal)
        db.session.commit()
        flash('Journal entry deleted.', category='success')
        return redirect(url_for('views.myjournal'))
    else:
        flash('You do not have permission to delete this journal entry.', category='error')
        return redirect(url_for('views.myjournal'))
