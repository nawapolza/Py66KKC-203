studyList = [
    ["32-406-801-302", "DBAP", 3, "A"],
    ["32-406-801-201", "Com Programming 1", 3, "B+"],
    ["32-406-804-302", "ERP", 2, "C"],
    ["32-406-805-302", "Web Programming", 2, "A"]
]
numGradeDict = {"A": 4, "B+": 3.5, "B": 3, "C+": 2.5, "C": 2, "D+": 1.5, "D": 1, "F": 0}
while True:
    print("***********INPUT*********")
    student_id = input("รหัสนักศึกษา: ")
    student_name = input("ชื่อนักศึกษา: ")
    print("***********OUTPUT*********")
    print("ผลการเรียน (studyList):", studyList)
    for entry in studyList:
        numGrade = numGradeDict.get(entry[3], 0)
        entry.extend([numGrade, entry[2] * numGrade])
        numGradeDict[entry[0]] = entry[3]
    CGX = sum(entry[5] for entry in studyList)
    CCX = sum(entry[2] for entry in studyList)
    GPA = CGX / CCX if CCX != 0 else 0
    print("ผลการเรียนหลังประมวลผล (studyList):", studyList)
    print("รหัสวิชาและเกรด (gradeDic):", numGradeDict)
    print(f"ผลคูณหน่วยกิตกับเกรดสะสม (CGX): {CGX}")
    print(f"หน่วยกิตสะสม (CCX): {CCX}")
    print(f"เกรดเฉลี่ยสะสม (GPA): {GPA:.2f}")
    print("***********GOOD BYE*********")
