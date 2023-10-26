class Employee:#การสร้างคลาส
    #สร้าง method
    def detail(self,name,salary,department):
        self.name= name
        self.salary=salary
        self.department= department
        print("ชื่อพนักงาน = {}".format(self.name))
        print("เงินเดือน  = {}".format(self.salary))
        print("อาชีพ = {}".format(self.department))
    


opj1 = Employee()#การสร้างวัตถุ
opj1.detail("ก้อง",50000,"นักการเมือง") #การเลียกใช้งาน

opj2= Employee()
opj2.detail("เอ",100000,"โปรเเกรมเมอร์")

opj2.detail()