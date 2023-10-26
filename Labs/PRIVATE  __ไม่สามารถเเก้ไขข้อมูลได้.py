class Employee:#การสร้างคลาส
    def __init__(self,name,salary,department):
        
        #private attribute ด้วยการเติม__ลงไป2ตัว
        self.__name= name
        self.__salary=salary
        self.__department= department
    
    
    #private methodด้วยการเติม__ลงไป2ตัว
    def _showdata(self):
        print("ชื่อพนักงาน = {}".format(self.__name))
        print("เงินเดือน  = {}".format(self.__salary))
        print("อาชีพ = {}".format(self.__department))
        # method นี้เเสดงข้อมูล


obj1 = Employee("ก้อง",50000,"นักการเมือง")#การสร้างวัตถุ
obj2 = Employee("เอ",100000,"โปรเเกรมเมอร์")

obj1.__salary=40000 #เเก้ไม่ได้
obj1.__department="นักบิน" #เเก้ไม่ได้
obj1._showdata()


