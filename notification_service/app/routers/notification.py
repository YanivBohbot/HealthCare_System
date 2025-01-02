from fastapi import APIRouter

router = APIRouter()

@router.get("/health", summary="Check service health")
async def health_check():
    """Returns the health status of the notification service."""
    return {"status": "Notification Service is running"}

@router.post("/test-notification", summary="Send a test notification")
async def send_test_notification(target: str, message: str):
    """
    Send a test notification to a given target (e.g., email or phone number).
    For simplicity, this function logs the notification.
    """
    # Simulate sending a notification
    print(f"Sending test notification to {target}: {message}")
    return {"status": "Test notification sent", "target": target, "message": message}
