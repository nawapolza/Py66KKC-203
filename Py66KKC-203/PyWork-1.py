print("**************INPUT*************")
employee = "ชื่อพนักงาน"
status = "ตําแหน่ง"
department = "เเผนก"
salary = float(input("เงินเดือน: "))
allowance = float(input("เงินประจำตำแหน่ง: "))
bonus = salary * 3
incomes =(salary + allowance) * 12 + bonus
tax = incomes * 0.05
print("**************OUTPUT*************")
print("ชื่อพนักงาน:", employee)
print("ตำแหน่ง:", status)
print("แผนก:", department)
print("เงินเดือน:", salary)
print("เงินประจำตำแหน่ง:", allowance)
print("เงินโบนัส:", bonus)
print("รายได้ทั้งปี:", incomes)
print("ภาษีที่ต้องชำระ:", tax)
print("**************END*************")