studentlist = ['test1', 'test20', 'test3', 'test4', 'test5', 'test6', 'test7']
salesDic = {'emp001': 50000, 'emp002': 50050, 'emp003': 50040, 'emp004': 53000, 'emp005': 50200}
scoreset = (5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60)
print("Students:", studentlist)
for studentz in studentlist:
    print("Student:", studentz)
total = sum(scoreset)
print("Total Score:", total)
average_score = total / len(scoreset)
print("Average Score:", average_score)
for emp_id, sale in salesDic.items():
    print("Employee ID:", emp_id, ", Sale:", sale)
print("Sales Dictionary Items:", salesDic.items())
for key, value in salesDic.items():
    print("Key:", key, ", Value:", value)
