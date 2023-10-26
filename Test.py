class Employee:
    def __init__(self,name,salary,department):
        self.__name =name
        self.__salary=salary
        self.__department=department
        
    def showdata(self):
        print(" ชื่อพนักงาน ={}".format(self.__name))
        print(" เงินเดือน   ={}".format(self.__salary))
        print(" อาชีพ     ={}".format(self.__department))
    


    
class Account(Employee):
    __departmentname = "เเผนกบันชี"
    def __init__(self,name,salary,age):
        super().__init__(name,salary,self.__departmentname)
        self.__age=age
    
    def showdata(self):
        super().showdata()
        print("อายุ = {}".format(self.__age))
        print("############################")
        
        
    
        
class Programmer(Employee):
    __departmentname = "เเผนกโปรเเกรมเมอร์"
    __name="เอวัน"
    def __init__(self,name,salary,experience,skill):
        super().__init__(self.__name,salary,self.__departmentname)
        self.__experience=experience
        self.__skill=skill
    def showdata(self):
        super().showdata()
        print("ประสบการทำงาน ={}".format(self.__experience))
        print("ความสามารถ ={}".format(self.__skill))
        print("############################")
    


        
class Sale(Employee):
    __departmentname = "เเผนกฝ่ายขาย"
    def __init__(self,name,salary,area):
        super().__init__(name,salary,self.__departmentname)
        self.__area=area
        
    def showdata(self):
        super().showdata()
        print("สถานที่ทำงาน ={}".format(self.__area))
        print("############################")


ac = Account("โก้ๆ",50000,21)
pro= Programmer(None,50000,12,"สร้างเกม")
sale = Sale("นัท",120000,"กทม")

pro.showdata()
