
class Employee:#คลาสเเม่
    __Min = 12000 #ปิดPRVATEไว้
    Max = 50000
    Companyname = "AONNE จำกัด"
    def __init__(self,name,salary,department):
        self._name= name
        self._salary=salary
        self._department= department
     #เเสดงลายละเอียด 
    def _showdata(self):
        print("ชื่อพนักงาน = {}".format(self._name))
        print("เงินเดือน  = {}".format(self._salary))
        print("อาชีพ = {}".format(self._department))
       
     #รายได้ต่ออปี  
    def _getincome(self):
        return self._salary*12
    
    def __str__(self):#เเปลงobject เป็นstring
        return ("ชื่อพนักงาน ={} ,เเผนก = {} , เงินเดือน = {} ,รายได้ต่อปี = {}".format(self._name,self._department,self._salary,self._getincome()))
        


       #คลาสลูก
class Accounting(Employee):
    __depastmentName = "เเผนกบันชี"
    def __init__(self,name,salary):
        super().__init__(name,salary,self.__depastmentName)
        #superคือการดึงขอมูลจากคลาสเเม่มา
        
    
class Programmer(Employee):
    __depastmentName = "เเผนกพัฒนาระบบ"
    def __init__(self,name,salary):
        super().__init__(name,salary,self.__depastmentName)
        #superคือการดึงขอมูลจากคลาสเเม่มา
      
    
class Sale(Employee):
    __depastmentName = "ฝ่ายขายสินค้า"
    def __init__(self,name,salary):
        super().__init__(name,salary,self.__depastmentName)
        #superคือการดึงขอมูลจากคลาสเเม่มา
       
        


account = Accounting("ก้อง",12000) #สร้างออฟเจคคลาสลูก
programmer=Programmer("เอวัน",50000)#สร้างออฟเจคคลาสลูก
sale=Sale("นัท",120000)#สร้างออฟเจคคลาสลูก

print(account.__str__()) #การเลียกใช้ str 
print(programmer.__str__())
print(sale.__str__())






