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
        
    #setter คือการเข้าไปปรับค่าที่เป็น private
    def setName(self,newname):
        self.__name =newname
    
    def setSalary(self,newsalary):
        self.__salary=newsalary
        
    def setDepastment(self,newdepartment):
        self.__department =newdepartment
    
    #getterคือการส่งค่าออกไปเพราะมันเป็นเเบบPRIVATE
    def getName(self):
        return self.__name
    def getSalary(self):
        return self.__salary
    def getDepartment(self):
        return self.__department

        

        


obj1 = Employee("ก้อง",50000,"นักการเมือง")#การสร้างวัตถุ
obj2 = Employee("เอ",100000,"โปรเเกรมเมอร์")

#เลียกใช้getter
print(obj1.getName())
print(obj1.getSalary())
print(obj1.getDepartment())




