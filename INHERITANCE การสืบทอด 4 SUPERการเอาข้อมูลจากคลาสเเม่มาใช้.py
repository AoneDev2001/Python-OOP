
class Employee:#คลาสเเม่
    __Min = 12000 #ปิดPRVATEไว้
    Max = 50000
    Companyname = "AONNE จำกัด"
    def __init__(self,name,salary,department):
        self._name= name
        self._salary=salary
        self._department= department
      
    def _showdata(self):
        print("ชื่อพนักงาน = {}".format(self._name))
        print("เงินเดือน  = {}".format(self._salary))
        print("อาชีพ = {}".format(self._department))


 
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



account._showdata() 
programmer._showdata()
sale._showdata()


