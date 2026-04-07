import unittest
from Milestone2 import EnrollmentRecord, LinkedQueue

class TestMilestone2(unittest.TestCase):
    # Linked Queue Tests
    def test_FIFO(self):
        new_queue = LinkedQueue()
        new_queue.enqueue("A")
        new_queue.enqueue("B")
        self.assertEqual(new_queue.dequeue(), "A")
        self.assertEqual(new_queue.dequeue(), "B")

    def test_dequeue(self):
        new_queue = LinkedQueue()
        with self.assertRaises(ValueError):
            new_queue.dequeue()
    
    def test_len(self):
        new_queue = LinkedQueue()
        new_queue.enqueue("A")
        new_queue.enqueue("B")
        self.assertEqual(len(new_queue), 2)
        new_queue.dequeue()
        self.assertEqual(len(new_queue), 1)

    # Enrollment Tests
unittest.main()