name= 'Nawapol Siraphant'
age=19
gender="male"
sale = 25000.50
commission = sale * 0.03
interest=['Java', 'Web Development', 'IOT', 'cat','game', 'sport', 'Dog' ]
education={'vocational':'kwicec ','deploma':'Business Computer',}
print("************ Data form Variables *************")
print("Hello, " + name)
print("Your are ", age, " years old")
print("Your gender are ", gender)
print("Your sale for this month ", sale ,", and get commission : ", commission)
print("Your interest: ", len(interest) ," are : ", interest)
interest.append("Fashion")
print("Your interest after update : ", interest)
print("New your interest are ", interest[7])
print("Your education are : ", education)
education['vocational'] = "Marketing"
education.update({'deploma': 'Finance'})
education['postdoctor'] = 'Digital Tranformation'
print("New your education are : ", education)
print("Your bachelor degree is : " ,education.get('bachelor'))
print("Good Bye.")
print("*********************")