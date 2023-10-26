
class Employee:#คลาสเเม่
    __Min = 12000 #ปิดPRVATEไว้
    Max = 50000
    Companyname = "AONNE จำกัด"
    def __init__(self,name,salary,department):
        self.__name= name
        self.__salary=salary
        self.__department= department
     #เเสดงลายละเอียด 
    def _showdata(self):
        print("ชื่อพนักงาน = {}".format(self.__name))
        print("เงินเดือน  = {}".format(self.__salary))
        print("อาชีพ = {}".format(self.__department))
       
     #รายได้ต่ออปี  
    def _getincome(self):
        return self._salary*12
    
    def __str__(self):#เเปลงobject เป็นstring
        return ("ชื่อพนักงาน ={} ,เเผนก = {} , เงินเดือน = {} ,รายได้ต่อปี = {}".format(self._name,self._department,self._salary,self._getincome()))
        


       #คลาสลูก
class Accounting(Employee):
    __depastmentName = "เเผนกบันชี"
    def __init__(self,name,salary,age):
        super().__init__(name,salary,self.__depastmentName)
        #superคือการดึงขอมูลจากคลาสเเม่มา
        self.__age=age
        
    def _showdata(self):
        super()._showdata()
        print("อายุ = {}".format(self.__age))
        print("#################")
    
class Programmer(Employee):
    __depastmentName = "เเผนกพัฒนาระบบ"
    def __init__(self,name,salary,experience,skill):
        super().__init__(name,salary,self.__depastmentName)
        #superคือการดึงขอมูลจากคลาสเเม่มา
        self.__exp =experience
        self.__skill = skill
        
    def _showdata(self):
        super()._showdata()
        print("ประสบการ = {}".format(self.__exp))
        print("ความสามารถ = {}".format(self.__skill))
        print("#################")
      
    
class Sale(Employee):
    __depastmentName = "ฝ่ายขายสินค้า"
    def __init__(self,name,salary,area):
        super().__init__(name,salary,self.__depastmentName)
        #superคือการดึงขอมูลจากคลาสเเม่มา
        self.__area=area
     
    def _showdata(self):
        super()._showdata()
        print("สถานที่ = {}".format(self.__area))
        print("#################")
    
       
        


account = Accounting("ก้อง",12000,30) #สร้างออฟเจคคลาสลูก
programmer=Programmer("เอวัน",50000,2,"พัฒนาเกมได้")#สร้างออฟเจคคลาสลูก
sale=Sale("นัท",120000,"เชียงใหม่")#สร้างออฟเจคคลาสลูก

account._showdata()
programmer._showdata()
sale._showdata()




