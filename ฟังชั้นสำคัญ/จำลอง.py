class Employee:#การสร้างคลาส
    _MIN=15000
    _MAX=50000
    _Salary="ZXC จำกัด"
    
    def __init__(self,name,salary,department):
        
        
        self.__name= name
        self.__salary=salary
        self.__department= department
    
    
    
    def _showdata(self):
        print("ชื่อพนักงาน = {}".format(self.__name))
        print("เงินเดือน  = {}".format(self.__salary))
        print("อาชีพ = {}".format(self.__department))
       
        
obj1 = Employee("ก้อง",50000,"นักการเมือง")
obj2 = Employee("เอ",100000,"โปรเเกรมเมอร์")

print("จำนวนเงินมากสุด =",str(Employee._MAX))



