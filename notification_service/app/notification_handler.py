import asyncio
from asyncio.log import logger
import json
import aio_pika import connect_robust, IncomingMessage
import smtplib
from email.mime.text import MIMEText
from app.utils.validators import validate_email, validate_phone_number




async def process_message(message: IncomingMessage):
       async with message.process():
        try:
            print(f"Received message: {message.body.decode()}")
            # Simulate notification sending
            success = await send_notification(message.body.decode())
            if not success:
                raise Exception("Notification failed")
            print(f"Notification sent successfully for: {message.body.decode()}")
        except Exception as e:
            print(f"Error processing message: {e}")
            # Retry logic (simple implementation with 3 retries)
            for attempt in range(3):
                try:
                    print(f"Retrying ({attempt + 1}/3)...")
                    success = await send_notification(message.body.decode())
                    if success:
                        print(f"Notification sent successfully on retry {attempt + 1}")
                        break
                except Exception as retry_exception:
                    print(f"Retry {attempt + 1} failed: {retry_exception}")
            else:
                print("Failed to send notification after 3 attempts")

async def consume():
    connection = await connect_robust("amqp://guest:guest@localhost/")
    channel = await connection.channel()
    queue = await channel.declare_queue("appointments", durable=True)

    print(" [*] Waiting for messages. To exit press CTRL+C")

    await queue.consume(process_message)




async def send_notification(notification_data: dict):
    """
    Simulate sending a notification via email or SMS.
    Replace this with actual integrations.
    
    Args:
    - notification_data (dict): Contains target, type, and message.
        Example:
        {
            "type": "email",
            "target": "user@example.com",
            "message": "Your appointment is confirmed."
        }
    
    Returns:
    - bool: True if the notification is sent successfully, False otherwise.
    """
    
    notification_type = notification_data.get("type")
    target = notification_data.get("target")
    message = notification_data.get("message")

    if notification_type == "email":
        if not validate_email(target):
            logger.error(f"Invalid email address: {target}")
            return False
        return await send_email(target, message)

    elif notification_type == "sms":
        if not validate_phone_number(target):
            logger.error(f"Invalid phone number: {target}")
            return False
        return await send_sms(target, message)

    else:
        logger.error(f"Unsupported notification type: {notification_type}")
        return False


async def send_email(target, message):
    """
    Simulate sending an email using SMTP.
    Replace this with real SMTP server configuration.
    """
    try:
        # Placeholder SMTP configuration (for local testing)
        smtp_server = "localhost"
        smtp_port = 1025
        sender_email = "noreply@example.com"

        mime_message = MIMEText(message, "plain")
        mime_message["Subject"] = "Healthcare Notification"
        mime_message["From"] = sender_email
        mime_message["To"] = target

        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.sendmail(sender_email, target, mime_message.as_string())

        logger.info(f"Email sent successfully to {target}")
        return True
    except Exception as e:
        logger.error(f"Failed to send email to {target}: {e}")
        return False