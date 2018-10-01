import unittest

from flask import json

from diary_api.api import app, entries


class test_app_api(unittest.TestCase):
    # def setUp(self):
    #     self.client = app.test_client
    # def tearDown(self):
    #     self.entry = None

    def test_post_new_entry(self):
        entry = {"entry_date": "12/09/2018", "details": "this is edna"}
        tester = app.test_client(self)
        response = tester.post(
            '/api/v1/entries', content_type='application/json', data=json.dumps(entry))
        self.assertEqual(response.status_code, 201)

    def test_post_entry_without_detials(self):
        entry = {"entry_date": "30/08/2008", "details": ""}
        tester = app.test_client(self)
        response = tester.post('/api/v1/entries',
                               content_type='application/json', data=json.dumps(entry))
        self.assertEqual(response.json, {
                         "message": "please input details"})

    def test_get_single_entry_that_exists(self):
        entry = {"entry_date": "12/09/2018", "details": "this is edna"}
        tester = app.test_client(self)
        response = tester.post('/api/v1/entries',
                               data=json.dumps(entry),
                               content_type='application/json')

        response = tester.get('/api/v1/entries/1',
                              content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_get_single_entry_that_doesnot_exist(self):
        tester = app.test_client(self)
        response = tester.get('/api/v1/entries/10')
        self.assertEqual(response.status_code, 404)

    def test_modify_an_entry(self):
        tester = app.test_client(self)
        entry = {"entry_date": "12/09/2018", "details": "this is edna"}
        response = tester.post('/api/v1/entries',
                               content_type='application/json', data=json.dumps(entry))
        """ test user can update a diary entry """
        response = tester.put('/api/v1/entries/1',
                              data=json.dumps(entry),
                              content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_modify_an_entry_that_doesnot_exist(self):
        tester = app.test_client(self)
        entry = {"entry_date": "12/09/2018", "details": "this is edna"}
        response = tester.post('/api/v1/entries',
                               content_type='application/json', data=json.dumps(entry))

        response = tester.put('/api/v1/entries/10')
        self.assertEqual(response.status_code, 404)

    def test_get_all_entries(self):
        tester = app.test_client(self)
        entry = {"entry_date": "12/09/2018", "details": "this is edna"}
        response = tester.post('/api/v1/entries',
                               content_type='application/json', data=json.dumps(entry))
        response = tester.get('/api/v1/entries',
                              content_type='application/json')
        self.assertEqual(response.status_code, 200)

    # def test_get_entries_when_list_is_empty(self):
    #     tester = app.test_client(self)
    #     response = tester.get('/api/v1/entries',
    #                           content_type='application/json')

    #     self.assertEqual(response.json, {
    #         'message': 'no entries found'})
    #     self.assertEqual(response.status_code, 400)

        # def test_entry_has_entryId(self):
        #     pass


if __name__ == '__main__':
    unittest.main()
