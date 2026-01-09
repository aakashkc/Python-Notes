
import smtplib as s
ob=s.SMTP("smtp.gmail.com",587)
# ob.starttls
ob.starttls()
ob.login("akash.kc3745@gmail.com","")
subject="Today is python class"
body="today is the python class for sending an email"
message="Subject:{}\n\n{}".format(subject,body)
listofaddress=["aakashchhetri3745@gmail.com","nischal.nik@gmail.com"]
ob.sendmail("akash.kc3745@gmail.com",listofaddress,message)
print("send sucessfullly")
ob.quit()