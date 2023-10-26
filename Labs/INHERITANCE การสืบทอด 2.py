class Employee:#คลาสเเม่
    Min = 12000
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


 #คลาสลูกสืบทอดมาจากเเม่เข้าถึงขอมูลเเม่ได้ยอเว้นprvateต้องไม่ปิด 
class Accounting(Employee):#คลาสลูก
    def __init__(self): #NONe คำสั่งไม่มีอะไรเลยถ้าไม่ใส่อินเฮอลิเเทนมันจะดึงของเเม่มา
        pass
    
class Programmer(Employee):#คลาสลูก
    def __init__(self):
        pass
    
class Sale(Employee):#คลาสลูก
    def __init__(self):
        pass


account = Accounting() #สร้างออฟเจคคลาสลูก
programmer=Programmer()#สร้างออฟเจคคลาสลูก
sale=Sale()#สร้างออฟเจคคลาสลูก
    
print(account.Companyname) #เลียกใช้account เอาข้อมูลเเม่มา




