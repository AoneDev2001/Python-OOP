class Employee:#การสร้างคลาส
    #สร้าง method
    def detail(self):
        self.name= "เอวัน"
        self.salary=50000
        print("ชื่อพนักงาน = {}".format(self.name))
        print("เงินเดือน  = {}".format(self.salary))
    


emp1 = Employee()#การสร้างวัตถุ

emp1.detail() #การเลียกใช้งาน