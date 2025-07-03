import unittest
import json
from app import app

class TaskTrackerTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_get_tasks_empty(self):
        response = self.app.get('/tasks')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.data), [])

    def test_create_task_success(self):
        response = self.app.post('/tasks', json={'title': 'Test Task'})
        self.assertEqual(response.status_code, 201)
        data = json.loads(response.data)
        self.assertEqual(data['title'], 'Test Task')
        self.assertFalse(data['completed'])

    def test_create_task_no_title(self):
        response = self.app.post('/tasks', json={})
        self.assertEqual(response.status_code, 400)

    def test_update_task_success(self):
        # Create a task first
        post_response = self.app.post('/tasks', json={'title': 'Update Me'})
        task_id = json.loads(post_response.data)['id']

        # Update the task
        put_response = self.app.put(f'/tasks/{task_id}', json={'title': 'Updated', 'completed': True})
        self.assertEqual(put_response.status_code, 200)
        data = json.loads(put_response.data)
        self.assertEqual(data['title'], 'Updated')
        self.assertTrue(data['completed'])

    def test_update_task_invalid_completed(self):
        post_response = self.app.post('/tasks', json={'title': 'Invalid Completed'})
        task_id = json.loads(post_response.data)['id']

        put_response = self.app.put(f'/tasks/{task_id}', json={'completed': 'yes'})
        self.assertEqual(put_response.status_code, 400)

    def test_delete_task_success(self):
        post_response = self.app.post('/tasks', json={'title': 'Delete Me'})
        task_id = json.loads(post_response.data)['id']

        delete_response = self.app.delete(f'/tasks/{task_id}')
        self.assertEqual(delete_response.status_code, 204)

    def test_delete_task_not_found(self):
        delete_response = self.app.delete('/tasks/9999')
        self.assertEqual(delete_response.status_code, 404)

if __name__ == '__main__':
    unittest.main()
