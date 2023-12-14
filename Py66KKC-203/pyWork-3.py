print("*" * 15, "INPUT", "*" * 15)
userid = input("หมายเลขผู้ใช้ไฟฟ้า: ")
username = input("ชื่อผู้ใช้ไฟฟ้า: ")
input_meter_before = float(input("เลขมิเตอร์ไฟฟ้าของเดือนที่แล้ว: "))
input_meter_after = float(input("เลขมิเตอร์ไฟฟ้าของเดือนปัจจุบัน: "))
if input_meter_before < input_meter_after:
    print("*" * 15, "ALERT WARINNG", "*" * 15)
    print("!ERROR!:เลขมิเตอร์ไฟฟ้าครั้งก่อนหน้ามีค่ามากกว่าครั้งหลังเด้อ")
    print("*" * 15, "", "*" * 15)
else:
    use_fire = input_meter_after - input_meter_before
    rate_fire = [5, 10, 15, 20]
    use_fireRes=(use_fire - 50, use_fire - 100, use_fire - 300)
    if use_fire <= 50:
        basic = use_fire * rate_fire[0]
    elif use_fire <= 100:
        basic = 250 + (use_fireRes[0]) * rate_fire[1]
    elif use_fire <= 300:
        basic = 1200 + (use_fireRes[1]) * rate_fire[2]
    else:

        basic = 3500 + (use_fireRes[2]) * rate_fire[3]
    ftPrice = use_fire * 0.50
    vat = (basic +ftPrice)* 0.07
    totalPaid = basic + ftPrice + vat
    print("*" * 15, "OUTPUT", "*" * 15)
    print("หมายเลขผู้ใช้ไฟฟ้า: ", userid)
    print('ชื่อผู้ใช้งาน: ', username)
    print("*" * 3, "{:<50s}{:>10,.2f} หน่วยค่า".format('จำนวนหน่วยไฟฟ้าที่ใช้ไป: ', use_fire), "*" * 15)
    print("{:<50s}{:>10,.2f} หน่วยค่า".format('จำนวนหน่วยไฟฟ้าที่ใช้ไป: ', use_fire))
    print("{:<50s}{:>8,.2f} หน่วยค่า".format('ค่าไฟฟ้าฐาน : ', basic))
    print("{:<50s}{:>9,.2f} หน่วยค่า".format('ค่าไฟฟ้าผันแปร: ', ftPrice))
    print("{:<50s}{:>11,.2f} บาท".format('ภาษีมูลค่าเพิ่ม : ', vat))
    print("{:<50s}{:>12,.2f} บาท".format('ค่าไฟฟ้ารวมทั้งสิ้น : ', totalPaid))
    print("*" * 15, "Goodbye ja", "*" * 15)
