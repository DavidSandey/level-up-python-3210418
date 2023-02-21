import smtplib

SENDER_EMAIL = "davidsandey@outlook.com"
SENDER_PASSWORD = "bmroghvugezegtoo"
SMTP_SERVER = "smtp-mail.outlook.com"
SMTP_PORT = 587


def send_email(receiver_email, subject, body):
    print("Entering send_email()")
    message = f"Subject:{subject}\n\n{body}"
    print(f"Prepared message {message}")
    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as smtp:
        print("opened SMTP session")
        smtp.starttls()
        print("Started TLS")
        smtp.login(SENDER_EMAIL, SENDER_PASSWORD)
        print("Logged in")
        smtp.sendmail(SENDER_EMAIL, receiver_email, message)
        print("message sent")


if __name__ == "__main__":
    send_email("david_sandey@wvi.org", "Hello", "Hello David from David")
