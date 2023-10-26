class Employee:#การสร้างคลาส
    def __init__(self,name,salary,department):
        self.name= name
        self.salary=salary
        self.department= department
    
    
    
    def showdata(self):
        print("ชื่อพนักงาน = {}".format(self.name))
        print("เงินเดือน  = {}".format(self.salary))
        print("อาชีพ = {}".format(self.department))
        # method นี้เเสดงข้อมูล


opj1 = Employee("ก้อง",50000,"นักการเมือง")#การสร้างวัตถุ
opj2 = Employee("เอ",100000,"โปรเเกรมเมอร์")





