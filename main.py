import csv
from mailer import Mailer
import time

# --- User Input Zone ---

fileNameCsv = "Automate test email- Python.csv"
emailAddress = "example@gmail.com"
emailPassword = "examplePassword1234"

# -----------------------

if emailPassword == '' or emailAddress == '':
    print("--!--  You forgot to add your email credentials in the \"Your_Email_Details\" file!   --!--")
    print("--!--                             Program closing in:                               --!--")
    for i in reversed(range(3)):
        print("--!--                                       %s                                       --!--" % (i + 1))
        time.sleep(1)
    exit(0)

count = len(open(fileNameCsv).readlines())
emails = [[0 for x in range(6)] for y in range(count)]
with open(fileNameCsv) as csvFile:
    csv_reader = csv.reader(csvFile, delimiter=',')
    index = 0
    for row in csv_reader:
        emails[index][0] = row[0]
        emails[index][1] = row[1]
        emails[index][2] = row[2]
        emails[index][3] = row[3]
        emails[index][4] = row[4]
        emails[index][5] = row[5]
        index = index + 1

mail = Mailer(email=emailAddress, password=emailPassword)

for emailIndex in range(count):
    subject = "(Account Code: %s) Accessorial Increase" % (emails[emailIndex][0])

    body = "Hello (Sales Name: %s), this account is currently up for M&A and we will be increasing their ELS " \
           "to (ELS: %s) and Discount (Discount: %s)" % \
           (emails[emailIndex][1], emails[emailIndex][2], emails[emailIndex][3])

    mail.send(receiver=emails[emailIndex][4], cc=emails[emailIndex][5], subject=subject, message=body)

    print("Sent email number #%s for %s at %s with cc at %s" % (emailIndex, emails[emailIndex][1],
                                                                emails[emailIndex][4], emails[emailIndex][5]))

print("\nDone!\n")
print("Sent %s Emails!" % count)
