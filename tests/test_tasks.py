import sqlite3
import unittest
from task_manager import database, tasks

class TaskManagerTestCase(unittest.TestCase):
    def setUp(self):
        # Use an in-memory SQLite database for testing
        self.conn = sqlite3.connect(":memory:")
        self.conn.row_factory = sqlite3.Row
        database.initialize_db(self.conn)

    def tearDown(self):
        self.conn.close()

    def test_add_and_list_task(self):
        task_id = tasks.add_task("Test Task", "This is a test", "2025-12-31", conn=self.conn)
        self.assertIsNotNone(task_id)

        task_list = tasks.list_tasks(conn=self.conn)
        self.assertEqual(len(task_list), 1)
        task = task_list[0]
        self.assertEqual(task["title"], "Test Task")
        self.assertEqual(task["description"], "This is a test")
        self.assertEqual(task["due_date"], "2025-12-31")
        self.assertEqual(task["done"], 0)

    def test_mark_task_done(self):
        task_id = tasks.add_task("Another Task", conn=self.conn)
        updated = tasks.mark_task_done(task_id, conn=self.conn)
        self.assertEqual(updated, 1)

        task_list = tasks.list_tasks(conn=self.conn)
        self.assertEqual(task_list[0]["done"], 1)

    def test_delete_task(self):
        task_id = tasks.add_task("Task to delete", conn=self.conn)
        deleted = tasks.delete_task(task_id, conn=self.conn)
        self.assertEqual(deleted, 1)

        task_list = tasks.list_tasks(conn=self.conn)
        self.assertEqual(len(task_list), 0)

if __name__ == "__main__":
    unittest.main()
