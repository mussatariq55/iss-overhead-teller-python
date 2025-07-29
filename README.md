
# 🛰️ ISS Overhead Teller in Python
A real-time ISS tracker built in Python that alerts you via email when the International Space Station is flying over your location **at night**. This project demonstrates the use of APIs, secure email automation, and periodic background execution — a creative blend of space awareness and automation.

<img width="1536" height="1024" alt="c3133634-7eba-4260-bbd7-b6b71f32af45" src="https://github.com/user-attachments/assets/d27e8056-9cfc-4ec6-8e4e-7213e898955e" />


---

## 🚀 Features
- Real-time ISS position tracking using the Open Notify API  
- Nighttime detection using the Sunrise-Sunset API  
- Sends email alerts when the ISS is overhead during nighttime  
- Secure email handling using environment variables (no hardcoded passwords)  
- Auto-runs every 60 seconds and works silently in the background  

---

## 🧠 Built With
- Python 3.7+  
- `requests` for API communication  
- `smtplib` for secure email sending  
- `datetime` for time logic  
- `os` for environment variable handling  
- Free public APIs (no signup required)  

---

## 💻 How It Works
1. The script continuously checks the ISS's current location.
2. It compares the ISS latitude and longitude to your own.
3. Then it checks if it's nighttime at your location.
4. If both are true, it sends you an email alert to look up and spot the ISS!

---

## 🔧 Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/iss-overhead-teller.git
cd iss-overhead-teller
```

### 2. Install Dependencies
```bash
pip install requests
```

### 3. Set Environment Variables

#### On Linux/macOS:
```bash
export MY_EMAIL="your_email@gmail.com"
export MY_PASSWORD="your_gmail_app_password"
```

#### On Windows (CMD):
```cmd
set MY_EMAIL=your_email@gmail.com
set MY_PASSWORD=your_gmail_app_password
```

🛡️ Make sure you use a [Gmail App Password](https://support.google.com/accounts/answer/185833) — not your regular email password.

---

## ▶️ Running the Script
After setting the environment variables, run the script:

```bash
python main.py
```

The script will run indefinitely, checking every 60 seconds and sending you a notification email if the ISS is overhead during night.

---

## 🌐 APIs Used

| API                | Purpose                              |
|--------------------|--------------------------------------|
| Open Notify        | Fetch current ISS location           |
| Sunrise-Sunset.org | Get sunrise and sunset times in UTC  |

---

## 🧠 What You’ll Learn
- How to use external APIs in Python
- How to send secure emails using SMTP
- How to automate tasks with scheduled intervals
- How to use environment variables to protect sensitive data
- Combining astronomy and automation in a meaningful project

---

## 🙌 Credits
- 👨‍💻 **Built by: Mussa Tariq
- LinkedIn: https://www.linkedin.com/in/mussa-tariq-0652712a0/
- 🛰️ Open Notify Team – http://api.open-notify.org  
- 🌅 Sunrise Sunset API – https://sunrise-sunset.org/api  

---

## 📬 Final Note
Next time you get a mail saying "Look Up!", don’t ignore it — go outside and witness one of humanity's greatest engineering marvels silently pass above you.

