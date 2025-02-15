import sys
import sendgrid
from sendgrid.helpers.mail import Mail

def main():
    try:
        # Retrieve inputs from command-line arguments
        sendgrid_api_key = sys.argv[1]
        from_email = sys.argv[2]
        to_email = sys.argv[3].split(",")
        subject = sys.argv[4]
        html_content = sys.argv[5]

        # Initialize SendGrid client and send email
        sg = sendgrid.SendGridAPIClient(api_key=sendgrid_api_key)
        message = Mail(
            from_email=from_email,
            to_emails=to_email,
            subject=subject,
            html_content=html_content
        )

        response = sg.send(message)
        print(f"Email sent successfully! Status Code: {response.status_code}")
    except Exception as e:
        print(f"Failed to send email: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
