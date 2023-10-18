class Student:
  def __init__(self, name, roll_number, cgpa):
      self.name = name
      self.roll_number = roll_number
      self.cgpa = cgpa

def sort_students(student_list):
  # Sort the student list based on CGPA in descending order
  sorted_students = sorted(student_list, key=lambda student: student.cgpa, reverse=True)
  return sorted_students

# Test the function with different input lists of students
if __name__ == "__main":
  # Create a list of student objects
  students = [
      Student("Alice", "A001", 3.8),
      Student("Bob", "B002", 3.5),
      Student("Charlie", "C003", 4.0),
      Student("David", "D004", 3.9),
  ]

  # Sort and print the list of students
  sorted_students = sort_students(students)
  for student in sorted_students:
      print(f"Name: {student.name}, Roll Number: {student.roll_number}, CGPA: {student.cgpa}")

