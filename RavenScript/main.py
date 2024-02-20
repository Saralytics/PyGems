import smtplib

email = "saralytics@gmail.com"
password = "oahf jzsk wlhw tapi"
connection = smtplib.SMTP("smtp.gmail.com", port=587) # host provider
connection.starttls()   # securing connection
connection.login(user=email, password=password)
connection.sendmail(
    from_addr=email,
    to_addrs="zhaoxue.li@alumni.ie.edu",
    msg="Subject: Did you do your reading today!\n\n Read, check what's new in the hood and write something down")
connection.close()
