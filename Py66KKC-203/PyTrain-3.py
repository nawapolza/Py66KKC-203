eid = input("ป้อนหมายเลขผู้ใช้ไฟฟ้า: ")
ename = input("ป้อนชื่อผู้ใช้ไฟฟ้า: ")
lastUnit = float(input("ป้อนเลขมิเตอร์ไฟฟ้าของเดือนที่แล้ว: "))
currentUnit = float(input("ป้อนเลขมิเตอร์ไฟฟ้าของเดือนปัจจุบัน: "))
if lastUnit > currentUnit:
    print("ข้อผิดพลาด: เลขมิเตอร์ไฟฟ้าเดือนที่แล้วมากกว่าเดือนปัจจุบัน")
    exit()
usedUnit = currentUnit - lastUnit
if usedUnit <= 50:
    basePrice = usedUnit * 5
elif usedUnit <= 150:
    basePrice = 250 + (usedUnit - 50) * 10
elif usedUnit <= 300:
    basePrice = 1250 + (usedUnit - 150) * 15
else:
    basePrice = 3500 + (usedUnit - 300) * 20
ftPrice = usedUnit * 0.5
vat = (basePrice + ftPrice) * 0.07
totalPaid = basePrice + ftPrice + vat
print("\nผลลัพธ์")
print(f"จำนวนหน่วยไฟฟ้าที่ใช้: {usedUnit:.2f} หน่วย")
print(f"ค่าไฟฟ้าฐาน: {basePrice:,.2f} บาท")
print(f"ค่าไฟฟ้าผันแปร: {ftPrice:,.2f} บาท")
print(f"ภาษีมูลค่าเพิ่ม: {vat:,.2f} บาท")
print(f"ค่าไฟฟ้ารวมทั้งสิ้น: {totalPaid:,.2f} บาท")
