import unittest
from flask import url_for
from app import create_app, db
from app.models import Journal

class TestRoutes(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.client = self.app.test_client()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_myjournal_route(self):
        response = self.client.get(url_for('views.myjournal'))
        self.assertEqual(response.status_code, 200)
        # Add more assertions here to test the functionality of the route

    def test_create_journal_route(self):
        response = self.client.get(url_for('views.create_journal'))
        self.assertEqual(response.status_code, 200)
        # Add more assertions here to test the functionality of the route

    def test_update_journal_route(self):
        journal = Journal(title='Test Journal', content='Test Content')
        db.session.add(journal)
        db.session.commit()
        response = self.client.get(url_for('views.update_journal', journal_id=journal.id))
        self.assertEqual(response.status_code, 200)
        # Add more assertions here to test the functionality of the route

    def test_delete_journal_route(self):
        journal = Journal(title='Test Journal', content='Test Content')
        db.session.add(journal)
        db.session.commit()
        response = self.client.get(url_for('views.delete_journal', journal_id=journal.id))
        self.assertEqual(response.status_code, 200)
        # Add more assertions here to test the functionality of the route

if __name__ == '__main__':
    unittest.main()