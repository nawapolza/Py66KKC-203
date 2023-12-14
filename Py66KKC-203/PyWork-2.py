id = "65342110020-3"
name = "Nawapol Siraphant"
print("************INPUT YOU FROM DATA  NA EIEI*************")
price = float(input("ราคาสินค้าที่ซื้อ: "))
quantity = int(input("จำนวนที่ซื้อ: "))
print("**********ทำเเยก***********")
insertfood =input("อาหารที่จะสั่งซื้อ: ")
print("**********OUTPUT***********")
total =price*quantity
discount =0.2*total
net =total-discount
myFavoritesRelax = ["SONG:นั่งนับเงินเเสนเเลัวก็เดินควงเเขนเธอ", "SONG:บักคนชั่ว", "SONG:PANIC", "MOVIE:WHOAMI", "SONG:เธอคงไม่อินกับอะไรเดิมๆ"]
menus = {"กระเพราหมูกรอบ": 60,"ก๋วยเตี๋ยว":80,"ไข่ดาว":20,"ข้าวผัด":70,"หมูกระทะ":189}
sales = {"กระเพราหมูกรอบ": 0.1,"ก๋วยเตี๋ยว":0.2,"ไข่ดาว":0.3,"ข้าวผัด":0.4," หมูกระทะ":0.5}
scores = {"Nawapol":85,"Siraphant":40,"Tu":78,"PYTHONKUNG":60,"PHPKUNG":20,"REACT.JSKUNG":60}
name1 = "Nawapol"
name2 = "Siraphant"
name3 = "Tu"
name4 = "PYTHONKUNG"
name5 = "PHPKUNG"
name6 = "JSKUNG"
name7 = "REACT.JSKUNG"
certificate = (name1,name2,name3,name4,name5,name6,name7)
certicate1 = ["Nawapol","Siraphant","Tu","test4","PYTHONKUNG","PHPKUNG","REACT.JSKUNG"]
if insertfood not in sales: #อันนี้ทำเพิ่มอยากทำนะ
  print("ไม่สามารถคำนวณราคาได้เด้อ",insertfood)
else:
   vax = price * sales[insertfood]
resualtprice=price-vax
print("รหัสลูกค้า:", id)
print("ชื่อลูกค้า:", name)
print("ยอดซื้อก่อนหักส่วนลด:", total)
print("ส่วนลด 20%:", discount)
print("ยอดเงินที่ต้องชำระหลังหักส่วนลด:", net)
print("เเสดงรายชื่่อ:", certicate1)
print("แสดงรายการในตัวแปร List myFavoriteRelax ที่สร้างขึ้นใน 2.3 เฉพาะรายการที่ 3:", myFavoritesRelax[2])
print("แสดงรายการในตัวแปร Dictionary ที่สร้างขึ้นใน 2.4 เฉพาะรายการที่ 2 ถึง 5",list(menus.items())[2:5])
myFavoritesRelax.append("BACKCLOVER")
menus["ตัวที่เพิ่มรายการ1ตัว :->หมาล่า"] = 160
print("เพิ่มรายการเข้าไปใน List และ Dictionary อย่างละ 1 รายการ:", myFavoritesRelax)
print("แสดงผลข้อมูลตัวแปร List และ Dictionary หลังการเพิ่มรายการ:", menus)
print("**********END***********")
print("************ทำเเยก(เปิด)*************")
print("เเสดงรายชื่อ2:",certificate)
print("เเสดงอาหารที่สั่ง:",insertfood)
print("ส่วนลดจากการสั่งอาหาร:",vax)
print("ราคาสินค้าหลังการหักส่วนลด:",resualtprice)
print("************ทำเเยก(ปิด)*************")

