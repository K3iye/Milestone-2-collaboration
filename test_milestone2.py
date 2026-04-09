import unittest
from Milestone import University, load_courses
from Milestone2 import LinkedQueue, binary_search_helper

class TestMilestone2(unittest.TestCase):

    # CSV testing for reading course catalog with capacity
    def test_csv(self):
        uni = University()
    
        load_courses("course_catalog_CSE10_with_capacity.csv", uni)

        s1 = uni.add_student("STU00001", "A")
        s2 = uni.add_student("STU00002", "B")

        course = uni.get_course("CSE1010")

        course.request_enroll(s1, "2026-04-01")
        course.request_enroll(s2, "2026-04-02")

        self.assertEqual(len(course.enrolled), 2)

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
        uni = University()
        course = uni.add_course("CSE2050", 3, 2)
        student1 = uni.add_student("STU00001", "Johnny")
        student2 = uni.add_student("STU00002", "Ryan")
        student3 = uni.add_student("STU00003", "Michael")
        course.request_enroll(student1, "2026-04-03")
        course.request_enroll(student2, "2026-04-04")
        course.request_enroll(student3, "2026-04-05")

        self.assertEqual(len(course.enrolled), 2)
        self.assertEqual(len(course.waitlist), 1)

    def test_waitlist(self):
        uni = University()
        course = uni.add_course("CSE2050", 3, 2)

        student1 = uni.add_student("STU00001", "Johnny")
        student2 = uni.add_student("STU00002", "Ryan")
        student3 = uni.add_student("STU00003", "Michael")

        course.request_enroll(student1, "2026-04-03")
        course.request_enroll(student2, "2026-04-04")
        course.request_enroll(student3, "2026-04-05")

        self.assertEqual(1, len(course.waitlist))
        self.assertEqual("STU00001", course.enrolled[0].student.student_id)

        course.sort_enrolled("id", "insertion")
        course.drop("STU00001")
        self.assertEqual(0, len(course.waitlist))
    
    # Sorting Tests
    def test_rostersorted(self):
        uni = University()
        course = uni.add_course("CSE2050", 3, 10)
        student1 = uni.add_student("STU00001", "Johnny")
        student2 = uni.add_student("STU00002", "Ryan")
        course.request_enroll(student2, "2026-04-03")
        course.request_enroll(student1, "2026-04-01")

        course.sort_enrolled('date', 'selection')
        self.assertEqual(course.enrolled[0].enroll_date, "2026-04-01")
        self.assertEqual(course.enrolled[1].enroll_date, "2026-04-03")

        course.sort_enrolled("name", "selection")
        self.assertEqual(course.enrolled[0].student.name, "Johnny")
        
        course.sort_enrolled('id', 'insertion')
        self.assertEqual(course.enrolled[0].student.student_id, "STU00001")

    # Binary Search Tests
    def test_binarysearch(self):
        uni = University()
        course = uni.add_course("CSE2050", 3, 10)
        s1 = uni.add_student("STU00001", "Johnny")
        s2 = uni.add_student("STU00002", "Ryan")
        s3 = uni.add_student("STU00003", "Carl")
        s4 = uni.add_student("STU00004", "Michael")
        s5 = uni.add_student("STU00005", "Mobeen")

        course.request_enroll(s3, "2026-01-01")
        course.request_enroll(s1, "2026-01-01")
        course.request_enroll(s5, "2026-01-01")
        course.request_enroll(s4, "2026-01-01")
        course.request_enroll(s2, "2026-01-01")

        course.sort_enrolled("id", "selection")
        roster = course.enrolled

        index_first = binary_search_helper(roster, "STU00001")
        self.assertEqual(index_first, 0)

        index_mid = binary_search_helper(roster, "STU00003")
        self.assertEqual(index_mid, 2)

        index_last = binary_search_helper(roster, "STU00005")
        self.assertEqual(index_last, 4)

        index_unknown = binary_search_helper(roster, "STU00011")
        self.assertEqual(index_unknown, -1)

if __name__ == "__main__":
    unittest.main()