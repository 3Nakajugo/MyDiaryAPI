import unittest
from diary_api.api import app
from flask import request, json


class test_app_api(unittest.TestCase):
    # def setUp(self):
    #     self.client = app.test_client

    def test_get_all_entries(self):
        tester = app.test_client(self)
        response = tester.get('/api/v1/entries')
        self.assertEqual(response.status_code, 200)

    def test_get_single_entry_that_doesnot_exist(self):
        tester = app.test_client(self)
        response = tester.get('/api/v1/entries/10')
        self.assertEqual(response.status_code, 404)

    def test_edit_single_entry_that_doesnot_exist(self):
        tester = app.test_client(self)
        response = tester.put('/api/v1/entries/10')
        self.assertEqual(response.status_code, 404)

    def test_get_single_entry_that_exists(self):
        tester = app.test_client(self)
        response = tester.get('/api/v1/entries/1')
        print(response.get_json())
        self.assertEqual(response.status_code, 200)
        # self.assertEqual(response.get_json(),  {'message': 'no entry with that id'}
        #  )

    def test_post_new_entry(self):
        entries = []
        entry = {"entry_date": "12/09/2018", "details": "this is edna"}
        tester = app.test_client(self)
        response = tester.post(
            '/api/v1/entries', content_type='application/json', data=json.dumps(entry))
        entries.append(entry)
        self.assertEqual(response.status_code, 201)

    def test_modify_an_entry(self):
        entry = {"details": "i am a girl"}
        entry2 = {"details": "i am a boy"}
        tester = app.test_client(self)

        """ test user can update a diary entry """
        response = tester.post('/api/v1/entries',
                               data=json.dumps(entry),
                               content_type='application/json')

        response = tester.put('/api/v1/entries/1',
                              data=json.dumps(entry2),
                              content_type='application/json')
        self.assertEqual(response.status_code, 200)

        # with app.test_client as client:
        #     response = client.get()

    def test_modify_an_entry_that_doesnot_exist(self):
        tester = app.test_client(self)
        response = tester.put('/api/v1/entries/2')
        self.assertEqual(response.status_code, 404)

    def test_entry_has_entryId(self):
        pass


if __name__ == '__main__':
    unittest.main()
