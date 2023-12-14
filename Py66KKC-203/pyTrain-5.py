def fCalAllowance(Job_position):
    allowances = {"CEO": 20000, "Manager": 10000, "Supervisor": 5000}
    return allowances.get(Job_position, 0)
def fCalBonus(Job_position, salary, work_exp=1):
    Bonus_refund = (
        5 if work_exp > 10 and Job_position in ["CEO", "MD", "Supervisor"]
        else 4 if work_exp > 10
        else 3 if 6 <= work_exp <= 10
        else 2 if 3 <= work_exp < 5
        else 2 if 2 <= work_exp < 3
        else 0
    )
    return salary * Bonus_refund
print("" * 15, "INPUT", "" * 15)
emp_id = input("รหัสพนักงาน: ")
emp_name = input("ชื่อพนักงาน: ")
emp_salary = float(input("เงินเดือน: "))
Job_position = input("ตำแหน่ง[1=CEO/2=MD/3=Supervisor]: ")
work_exp = int(input("อายุงาน (ปี): "))
allowance = fCalAllowance(Job_position)
emp_bonus = fCalBonus(Job_position, emp_salary, work_exp)
total_salary = emp_salary + allowance + emp_bonus
print("" * 15, "OUTPUT", "" * 15)
print("{0:20s}{1}".format("รหัสพนักงาน", emp_id))
print("{0:20s}{1}".format("ชื่อพนักงาน", emp_name))
print("{0:20s}{1}".format("ตำแหน่ง:", Job_position))
print("{0:20s}{1}".format("อายุงาน", work_exp))
print("{0:20s}{1:9,.2f}".format("เงินเดือน", emp_salary))
print("{0:20s}{1:9,.2f}".format("เงินเดือนประจำตำเเหน่ง", allowance))
print("{0:20s}{1:9,.2f}".format("โบนัสที่ได้ :", emp_bonus))
print("{0:20s}{1:9,.2f}".format("เงินรวม", total_salary))
print("" * 15, "GOOD BYE", "" * 15)
