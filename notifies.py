import time
from plyer import notification
if __name__ == "__main__":
    while True:
        notification.notify(
            title="Drinking water",
            message="you are alerted to drink a glass of water",
            app_icon=r"C:\Users\Administrator\Desktop\python\icon.ico",
            timeout=5
        )
        time.sleep(5)
        break



