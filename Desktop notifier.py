from Notification import notification
import time
import winsound
from urllib import request
if __name__ == '__main__':
    while True:
        x = notification.notify(title="Pls drink water",
                                message=f"Please! Take rest from you pc.",
                                app_icon="icon.ico",
                                toast=True,
                                timeout=5
        )
        timeout = 10
        winsound.MessageBeep(winsound.MB_OK)
        time.sleep(30*60)
        print(x)


