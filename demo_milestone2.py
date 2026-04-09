from Milestone import University

# setup University and course
uni = University()
course = uni.add_course("CSE101", 3, 2)

# Create 
stu1 = uni.add_student("STU00001", "Ryan")
stu2 = uni.add_student("STU00002", "Johnny")
stu3 = uni.add_student("STU00003", "Swamy")

course.request_enroll(stu1, "2026-04-08")
course.request_enroll(stu2, "2026-04-02")
course.request_enroll(stu3, "2026-04-05") # goes to waitlist capacity(2)

print("Enrolled:", course.enrolled)
print("Waitlist size:", len(course.waitlist))

course.sort_enrolled("id", "insertion")
course.drop("STU00001")

print("After drop:")
print("Enrolled:", course.enrolled)
print("Waitlist size:", len(course.waitlist))
