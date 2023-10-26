class Employee:#คลาสเเม่
    Min = 12000
    Max = 50000
    Companyname = "AONNE จำกัด"
    


 #คลาสลูกสืบทอดมาจากเเม่เข้าถึงขอมูลเเม่ได้ยอเว้นprvateต้องไม่ปิด 
class Accounting(Employee):#คลาสลูก
    pass
    
class Programmer(Employee):#คลาสลูก
    pass
    
class Sale(Employee):#คลาสลูก
    pass


account = Accounting() #สร้างออฟเจคคลาสลูก
programmer=Programmer()#สร้างออฟเจคคลาสลูก
sale=Sale()#สร้างออฟเจคคลาสลูก
    
print(account.Companyname)




