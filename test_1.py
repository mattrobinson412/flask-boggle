from unittest import TestCase
from app import app
from flask import session
from boggle import Boggle

app.config['TESTING'] = True
app.config['DEBUG_TB_HOSTS'] = ['dont-show-debug-toolbar']


class FlaskTests(TestCase):

    # TODO -- write tests for every view function / feature!
    def test_load_game(self):
        with app.test_client() as client:
            with client.session_transaction() as change_session:
                change_session['board'] = []

                resp = client.get('/')
                html = resp.get_data(as_text=True)

                self.assertEqual(resp.status_code, 200)
                self.assertIn('<table></table>', html)
                self.assertNotEqual(session['board'], [])