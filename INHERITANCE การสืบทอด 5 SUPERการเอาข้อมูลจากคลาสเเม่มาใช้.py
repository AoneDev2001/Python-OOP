
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


       #คลาสลูก
class Accounting(Employee):
    __depastmentName = "เเผนกบันชี"
    def __init__(self,name,salary):
        super().__init__(name,salary,self.__depastmentName)
        #superคือการดึงขอมูลจากคลาสเเม่มา
        super()._showdata() #หรือให้เเสดงขอมูลเลยก็ได้เเบบไม่ต้องประกาศ คลาสเเม่เลียกใช้ผ่าน Super ถ้าเป็นลูกจะเลียกใช้ด้านล้าง
        
    
class Programmer(Employee):
    __depastmentName = "เเผนกพัฒนาระบบ"
    def __init__(self,name,salary):
        super().__init__(name,salary,self.__depastmentName)
        #superคือการดึงขอมูลจากคลาสเเม่มา
        super()._showdata() #หรือให้เเสดงขอมูลเลยก็ได้เเบบไม่ต้องประกาศ
    
class Sale(Employee):
    __depastmentName = "ฝ่ายขายสินค้า"
    def __init__(self,name,salary):
        super().__init__(name,salary,self.__depastmentName)
        #superคือการดึงขอมูลจากคลาสเเม่มา
        super()._showdata() #หรือให้เเสดงขอมูลเลยก็ได้เเบบไม่ต้องประกาศ
        


account = Accounting("ก้อง",12000) #สร้างออฟเจคคลาสลูก
programmer=Programmer("เอวัน",50000)#สร้างออฟเจคคลาสลูก
sale=Sale("นัท",120000)#สร้างออฟเจคคลาสลูก






