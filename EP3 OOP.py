class Employee:#การสร้างคลาส
    
    def detail(self,name,salary,department):#สร้าง method
        self.name= name
        self.salary=salary
        self.department= department
        # method นี้กำหนดข้อมูลให้กับ opject
    
    def showdata(self):
        print("ชื่อพนักงาน = {}".format(self.name))
        print("เงินเดือน  = {}".format(self.salary))
        print("อาชีพ = {}".format(self.department))
        # method นี้เเสดงข้อมูล


opj1 = Employee()#การสร้างวัตถุ
opj1.detail("ก้อง",50000,"นักการเมือง") #ส่งข้อมูลไป

opj2 = Employee()
opj2.detail("เอ",100000,"โปรเเกรมเมอร์")

opj1.showdata()#เลียกใช้งาน
opj2.showdata()


