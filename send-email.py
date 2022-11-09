import smtplib, ssl 
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

sender_email = "[GHANGEME]"
receiver_email = "[GHANGEME]"

message = MIMEMultipart("")
message["Subject"] = "[GHANGEME]"
message["FROM"] = sender_email
message["To"] = receiver_email

text = """\
Mesaj
"""

part1 = MIMEText(text, "plain")
message.attach(part1)

filepath = "[GHANGEME]"
part2 = MIMEBase('application',"octet-stream")
part2.set_payload(open(filepath, "rb").read)
encoders.encode_base64(part2)

part2.add_header('Content-Disposition', 'attachment; filename="[GHANGEME]"')

message.attach(part2)

# Create secure connection with server and send email 
context = ssl.create_default_context()
server = smtplib.SMTP("[GHANGEME]",587)
server.starttls()
server.ehlo_or_helo_if_needed()
server.sendmail(
    sender_email, receiver_email, message.as_string()
)