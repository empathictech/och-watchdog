import smtplib, ssl

# sends a message to and from the emails defined in the credentials.env file
def send_message(message):
  with open("env_files/credentials.env", "r") as env_file:
    creds = env_file.read().strip().split()
    recipient = creds[0]
    sender = creds[1]
    password = creds[2]

  # default smtp port for GMail
  port = 465
  context = ssl.create_default_context()

  with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
    server.login(sender, password)
    server.sendmail(sender, recipient, message)
