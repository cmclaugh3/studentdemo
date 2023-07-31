from student import Student
import unittest

class EnrollInTestCase(unittest.TestCase): 
    
    def test_is_incremented_correctly(self):
        # test if enrollInCourse() method successfully increments the
        # num_courses attribute of the Student object 

        # Create student instance, adding some courses
        student1 = Student('Katherine', ['DS 5100'])
        student1.enroll_in_course("CS 5050")
        student1.enroll_in_course("CS 5777")
        print(student1.courses)
        print(student1.num_courses)
        
        # Test
        expected = 3
        # unittest.TestCase brings in the assertEqual() method
        self.assertEqual(student1.num_courses, expected)
    
    def test_1(self):
        student_1 = Student('Will', ['DS 5100','DS5101'])
        student_1.unenroll_in_course('DS5101')
        
        expected = "Expected False since student should no longer be in course"
        
        self.assertFalse('DS5101' in student_1.courses)
        
    def test_2(self):
        student_2 = Student('Conor', ['DS 5100','DS5101'])
        student_2.unenroll_in_course('DS6001')
        self.assertEquals(student_2.num_courses, 2)
        
if __name__ == '__main__':
    unittest.main(verbosity=2)