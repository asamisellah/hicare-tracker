from app import app
import unittest


class TestRequests(unittest.TestCase):
    request = {"title": "Leaking Pipe",
                   "type": "Repair",
                   "description": "Some description",
                   "category": "Plumbing",
                   "area": "Block A"}

    def setUp(self):
        app.config["TESTING"] = True
        self.client = app.test_client()
        
    def create_request(self, title, type, description, category, area):

        return self.client.post('/users/requests', data=self.request)

    def test_create_request(self):
        res = self.client.post('/users/requests', data=self.request)
        self.assertEqual(res.status_code, 201)

    def test_update_request(self):
        res = self.client.put('/users/requests/1', data=self.request)
        self.assertEqual(res.status_code, 200)

    def test_all_requests(self):
        res = self.client.get('/users/requests')
        self.assertEqual(res.status_code, 200)

    def test_get_request(self):
        res = self.client.get('/users/requests/1')
        self.assertEqual(res.status_code, 200)

    def test_delete_request(self):
        res = self.client.delete('/users/request/1')
        self.assertEqual(res.status_code, 200)


if __name__ == "__main__":
    unittest.main()