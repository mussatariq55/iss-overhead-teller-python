# ISS Overhead Notifier
# This script checks if the International Space Station (ISS) is currently overhead and sends an email notification if it is night time.

from datetime import datetime
from smtplib import SMTP
import requests
import time
import os

# ------------------ USER CONFIGURATION ------------------
MY_LAT = 31.5204      # Your latitude (e.g., Lahore, Pakistan)
MY_LONG = 74.3587     # Your longitude
MY_EMAIL = os.getenv("MY_EMAIL")         # Use environment variables for security
MY_PASSWORD = os.getenv("MY_PASSWORD")   # NEVER hardcode passwords in code!
# --------------------------------------------------------

def is_iss_overhead():
    """Check if the ISS is currently within ~5 degrees of the user's location."""
    try:
        response = requests.get(url="http://api.open-notify.org/iss-now.json")
        response.raise_for_status()
        data = response.json()

        iss_lat = float(data["iss_position"]["latitude"])
        iss_long = float(data["iss_position"]["longitude"])

        # Check if ISS is close to your position
        return (MY_LAT - 5) <= iss_lat <= (MY_LAT + 5) and (MY_LONG - 5) <= iss_long <= (MY_LONG + 5)

    except requests.RequestException as e:
        print(f"Error fetching ISS data: {e}")
        return False

def is_night():
    """Determine whether it is currently night at the user's location."""
    try:
        parameters = {
            "lat": MY_LAT,
            "lng": MY_LONG,
            "formatted": 0
        }

        response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
        response.raise_for_status()
        data = response.json()

        sunrise_hour = int(data["results"]["sunrise"].split('T')[1].split(":")[0])
        sunset_hour = int(data["results"]["sunset"].split('T')[1].split(":")[0])
        current_hour = datetime.utcnow().hour  # Use UTC because sunrise API returns UTC

        return current_hour < sunrise_hour or current_hour > sunset_hour

    except requests.RequestException as e:
        print(f"Error fetching sunrise/sunset data: {e}")
        return False

def send_notification():
    """Send an email notification if the ISS is overhead and it’s nighttime."""
    try:
        with SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=MY_EMAIL,
                msg="Subject: Look Up!!\n\nThe ISS is currently overhead. Go outside and look up!"
            )
        print("📨 Email sent: ISS is overhead and it's night.")
    except Exception as e:
        print(f"Failed to send email: {e}")

# Run loop every 60 seconds
while True:
    time.sleep(60)
    if is_iss_overhead() and is_night():
        send_notification()
