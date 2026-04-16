#***********************STUDENT ATTENDENCE PROJECT****************************

class ClassRoom:
  total_student = 100

  def absentStudent(self,absent):
      print("********ABSENT ATTENDENCE RESULT********")
      print(f"Total Student: {self.total_student}")
      print(f"Absent Student: {absent}")
      self.total_student -= absent
      print(f"Total {self.total_student} student present in classroom")

  def presentStudent(self,present):
      print("********PRESENT ATTENDENCE RESULT********")
      print(f"Total Student: {self.total_student}")
      print(f"Present Student: {present}")
      self.total_student -= present
      print(f"Total {self.total_student} student are absent in classroom")


num = int(input("Enter student range: "))
student = ClassRoom()
student.presentStudent(num)