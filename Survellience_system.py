import psutil
import sys
import os
import time
import schedule
import smtplib
from email.message import EmailMessage



def ProcessScan():

    process_data = []

    
    for proc in psutil.process_iter():
        try:
            proc.cpu_percent(None)
        except:
            pass

    time.sleep(0.2)

    for proc in psutil.process_iter():
        try:
            info = {}

            info["pid"] = proc.pid
            info["name"] = proc.name()
            info["cpu"] = round(proc.cpu_percent(None) / psutil.cpu_count(), 2)
            info["memory_percent"] = round(proc.memory_percent(), 2)
            info["threads"] = proc.num_threads()

            process_data.append(info)

        except (psutil.NoSuchProcess,
                psutil.AccessDenied,
                psutil.ZombieProcess):
            pass

    return process_data



# ---------------------------------------------------------
# Function: CreateLog
# ---------------------------------------------------------
def CreateLog(FolderName):

    Border = "-" * 50

    # Create folder if not exists
    if not os.path.exists(FolderName):
        os.mkdir(FolderName)
        print("Directory for log files gets created successfully")

    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
    FileName = os.path.join(FolderName, "Marvellous_%s.log" % timestamp)

    fobj = open(FileName, "w")

    fobj.write(Border + "\n")
    fobj.write("---- Marvellous Platform Surveillance System -----\n")
    fobj.write("Log created at : " + time.ctime() + "\n")
    fobj.write(Border + "\n\n")

    data = ProcessScan()

    for process in data:

        # Current timestamp for each process
        current_time = time.ctime()

        fobj.write("Timestamp    : %s\n" % current_time)
        fobj.write("Process Name : %s\n" % process["name"])
        fobj.write("PID          : %s\n" % process["pid"])
        fobj.write("CPU %%       : %s\n" % process["cpu"])
        fobj.write("Memory %%    : %s\n" % process["memory_percent"])
        fobj.write("Threads      : %s\n" % process["threads"])
        fobj.write("-" * 40 + "\n")

    fobj.close()

    print("Log file created successfully")



def main():
    print("Platform Surveillance System Started")
    CreateLog("MarvellousLogs")

def send_mail(sender, app_password, receiver, subject, body):

    # Step 1 : Create Email object
    msg = EmailMessage()

    # Step 2 : Set mail headers
    msg["From"] = sender
    msg["To"] = receiver
    msg["Subject"] = subject

    # Step 3 : Add mail body
    msg.set_content(body)

    # Step 4 : Create SMTP SSL connection
    smtp = smtplib.SMTP_SSL("smtp.gmail.com", 465)

    # Step 5 : Login using Gmail + App password
    smtp.login(sender, app_password)

    # Step 6 : Send the email
    smtp.send_message(msg)

    # Step 7 : Close connection
    smtp.quit()


# ------------------------------------------------
# Function : main
# ------------------------------------------------
def main():

    # Use your Gmail here
    sender_email = "your_python.test@gmail.com"

    # 16-digit App Password
    app_password = "xxxxxxxxxxxxxxxx"

    # Receiver email
    receiver_email = "yourpersonalemail@gmail.com"

    subject = "Test Mail from Python Script"

    body = """Jay Ganesh,

This is a test email sent using Python.

Regards,
Marvellous Infosystems
"""

    send_mail(sender_email, app_password, receiver_email, subject, body)

    print("Marvellous Mail Sent Successfully")




if __name__ == "__main__":
    main()
