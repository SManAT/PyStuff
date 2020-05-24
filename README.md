# PyStuff
some things markable for me to remember

# QT/Notification
This is a QtDialog that simulates a notification on the screen.

## How to use it
In your Main Module you have to do this
```python3
from Notification import Notification_Core, Notification

n = Notification_Core()
notification = Notification(n)
notification.showInformation("MyMessage")
notification.showError("MyMessage")
notification.showWarning("MyMessage")
notification.showSuccess("MyMessage")
```
To get an idea how it looks like
![Screenshot](./img/notifyshot.jpg)


This stuff is provided as it is, gl & hf!
