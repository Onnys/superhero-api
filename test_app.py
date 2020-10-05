import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy 
from app import create_app
from Models import setup_db, superheros  


class QuotesTestCase(unittest.TestCase):
    
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = 'superhero'
        self.database_path = "postgres://{}:{}@{}/{}".format('superhero','hero','localhost:5432', self.database_name)

        setup_db(self.app, self.database_path)

        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            self.db.create_all()
    
    def tearDown(self):
        pass

    def test_404_get_superheros(self):
        #superheros.query.delete()
        response = self.client().get('/superheros')
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 404)
        self.assertEqual(data['success'], False)

    
if __name__ == '__main__':
    unittest.main()