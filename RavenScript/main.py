import smtplib

email = "saralytics@gmail.com"
password = ""

connection = smtplib.SMTP("smtp.gmail.com", port=587) # host provider
connection.starttls()   # securing connection
connection.login(user=email, password=password)
connection.sendmail(
    from_addr=email,
    to_addrs="zhaoxue.li@outlook.com",
    msg="Subject: Your morning coffee delivery is here!\n\n This is my body of the cup")
connection.close()
