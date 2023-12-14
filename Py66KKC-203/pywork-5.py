def getAllowance(position):
    allowances = {"CEO": 20000, "MD": 10000, "Supervisor": 5000}
    return allowances.get(position, 0)
def getBonus(position, salary, work_exp=1):
    bonus_refund = 2 if position in ["CEO", "MD", "Supervisor"] else 1
    if work_exp < 3:
        return salary
    elif  work_exp < 5:
        return salary * 2
    elif  work_exp <= 10:
        return salary * 3
    else:
        return salary * 4
print(" " * 15, "INPUTก", " " * 15)
emp_id = input("รหัสพนักงาน: ")
emp_name = input("ชื่อพนักงาน: ")
emp_salary = float(input("เงินเดือน: "))
position = input("ตำแหน่ง: ")
work_exp = int(input("อายุงาน (ปี): "))
allowance = getAllowance(position)
bonus = getBonus(position, emp_salary, work_exp)
total_salary = emp_salary + allowance + bonus
print(" " * 15, "OUTPUT", " " * 15)
print("{0:20s}{1}".format("รหัสพนักงาน", emp_id))
print("{0:20s}{1}".format("ชื่อพนักงาน", emp_name))
print("{0:20s}{1}".format("ตำแหน่ง:", position))
print("{0:20s}{1}".format("อายุงาน", work_exp))
print("{0:20s}{1:9,.2f}".format("เงินเดือน", emp_salary))
print("{0:20s}{1:9,.2f}".format("เงินประจำตำแหน่ง", allowance))
print("{0:20s}{1:9,.2f}".format("เงินโบนัส", bonus))
print("{0:20s}{1:9,.2f}".format("เงินรวม", total_salary))
print(" " * 15, "GOOD BYE", " " * 15)
