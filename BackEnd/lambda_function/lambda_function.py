import json
import smtplib
from email.message import EmailMessage
import boto3
 
def send_email():
    email = "crumb.commander@gmail.com"
    password = "dtzw tuaq ejtm qkqd"
 
    msg = EmailMessage()
    msg['Subject'] = "Immediate Attention Required: Unusual Load on EC2 Instance"
    msg['From'] = email
    msg['To'] = "tsp57081@gmail.com" # My personal email
    body = """Dear Team,

We have detected an unusual load on one of our EC2 instances. While our auto-scaling setup is active and will automatically manage the increased demand by provisioning additional instances, this unexpected spike in usage may lead to higher operational costs.

Action Required:

Immediate Review: Please investigate the source of this unusual load to determine the cause and address any underlying issues.
Cost Management: Monitor the auto-scaling activities closely to understand the impact on our AWS billing. Adjust thresholds and scaling policies if necessary to optimize cost efficiency.
Performance Assurance: Ensure that all additional instances are functioning correctly and maintaining our performance standards during this period of increased load.
Your prompt attention to this matter is crucial to ensure system stability and cost-effective operations. Please provide an update on your findings and any corrective actions taken.

Thank you for your cooperation."""
    msg.set_content(body)
 
    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.login(email, password)
        server.send_message(msg)
        server.quit()
        return {'message': 'Email sent successfully'}
    except Exception as e:
        return {'error': str(e)}
 
def lambda_handler(event, context):
    try:
        response = send_email()
        status_code = 200 if 'message' in response else 500
        return {
            'statusCode': status_code,
            'body': json.dumps(response)
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }