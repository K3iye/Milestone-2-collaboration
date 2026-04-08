import unittest
from Milestone import Course, Student, University
from Milestone2 import EnrollmentRecord, LinkedQueue

class TestMilestone2(unittest.TestCase):
    # Base start for most of the testing 
    def start(self):
        self.course = Course("CSE2050", "Data Structures", 3, "CSE", 2)
        self.student1 = Student("STU001", "Johnny", [], 4.0)
        self.student2 = Student("STU002", "Ryan", [], 3.7)
        self.student3 = Student("STU003", "Michael", [], 3.2)

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
    def test_enrollcap(self):
        self.course.request_enroll(self.student1, "2026-04-03")
        self.course.request_enroll(self.student2, "2026-04-04")
        self.course.request_enroll(self.student3, "2026-04-05")

        self.assertEqual(len(self.course.enrolled_roster), 2)
        self.assertEqual(len(self.course.waitlist), 1)

    def test_waitlist(self):
        self.course.request_enroll(self.student1, "2026-04-03")
        self.course.request_enroll(self.student2, "2026-04-04")
        self.course.request_enroll(self.student3, "2026-04-05")
        self.course.drop("STU001")
        enrolled_students = []
        for record in self.course.enrolled_roster:
            enrolled_students.append(record.student.student_id)

        self.assertIn("STU001", enrolled_students)
        self.assertNotIn("STU001", enrolled_students)
    
    # Sorting Tests
    def test_rostersorted(self):
        self.course.request_enroll(self.student2, "2026-04-03")
        self.course.request_enroll(self.student1, "2026-04-01")

        self.course.sort_enrolled(by='date', algorithm='selection')
        self.assertEqual(self.course.enrolled_roster[0].enroll_date, "2026-04-01")
        self.assertEqual(self.course.enrolled_roster[1].enroll_date, "2026-04-03")

        self.course.sort_enrolled(by="name", algorithm="selection")
        self.assertEqual(self.course.enrolled_roster[0], "Johnny")
        
        self.course.sort_enrolled(by='id', algorithm='bubble')
        self.assertEqual(self.course.enrolled_roster[0].student.student_id, "STU001")

    # Binary Search Tests
    def test_binarysearch(self):
        self.course = Course("CSE2050", "Data Structures", 3, "CSE", 10)
        self.s1 = Student("STU001", "Johnny", [], 4.0)
        self.s2 = Student("STU002", "Ryan", [], 3.5)
        self.s3 = Student("STU003", "Carl", [], 3.0)
        self.s4 = Student("STU004", "Michael", [], 3.8)
        self.s5 = Student("STU005", "Mobeen", [], 3.9)

        self.course.request_enroll(self.s3, "2026-01-01")
        self.course.request_enroll(self.s1, "2026-01-01")
        self.course.request_enroll(self.s5, "2026-01-01")
        self.course.request_enroll(self.s4, "2026-01-01")
        self.course.request_enroll(self.s2, "2026-01-01")

        self.course.sort_enrolled(by="id", algorithm="selection")
        roster = self.course.enrolled_roster
        high = len(roster) - 1

        index_first = self.course.recursive_binary_search(roster, "STU001", 0, high)
        self.assertEqual(index_first, 0)

        index_mid = self.course.recursive_binary_searcH(roster, "STU003", 0, high)
        self.assertEqual(index_mid, 2)

        index_last = self.course.recursive_binary_search(roster, "STU005", 0, high)
        self.assertEqual(index_last, 4)

        index_unknown = self.course.recursive_binary_search(roster, "STU011", 0, high)
        self.assertEqual(index_unknown, -1)

if __name__ == "__main__":
    unittest.main()