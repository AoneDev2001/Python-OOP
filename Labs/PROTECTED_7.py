class Employee:#การสร้างคลาส
    def __init__(self,name,salary,department):
        
        #protected attribute ด้วยการเติม_ลงไป
        self._name= name
        self._salary=salary
        self._department= department
    
    
    #protected methodด้วยการเติม_ลงไป
    def _showdata(self):
        print("ชื่อพนักงาน = {}".format(self._name))
        print("เงินเดือน  = {}".format(self._salary))
        print("อาชีพ = {}".format(self._department))
        # method นี้เเสดงข้อมูล


obj1 = Employee("ก้อง",50000,"นักการเมือง")#การสร้างวัตถุ
obj2 = Employee("เอ",100000,"โปรเเกรมเมอร์")

obj1._salary=500000000
obj1._showdata()


