import subprocess

data = subprocess.check_output(['netsh', 'wlan', 'show',
                                'profiles']).decode('utf-8').split('\n')

print(data)

profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]

for i in profiles:
    results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i,
                                       'key=clear']).decode('utf-8').split('\n')
    results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
    try:
        print("{:<30}|  {:<}".format(i, results[0]))
    except IndexError:
        print("{:<30}|  {:<}".format(i, ""))

input("")

def send_bill():
    msg = EmailMessage()
    msg['Subject'] = 'Your bill '
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = EMAIL_ADDRESS       #receiver email
    global x
    fileref = str(x) + '.txt'
    msg.set_content('This is your Total bill\nyour Reference.No is: Bill' + str(x))
    with open(os.path.join(path, fileref), "rb") as f:
        file_data = f.read()
        file_name = "RestaurentBill"
    msg.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=file_name)
    qsend = messagebox.askyesno("Billing System", "Do you want to send the bill?")
    if qsend > 0:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            smtp.send_message(msg)
        qsmsg = messagebox.showinfo("Information", "Bill send successfully")
    else:
        qnmsg = messagebox.showinfo("Information", "Bill not send")