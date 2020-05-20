# PyStuff
some things markable for me to remember

## Notification
This is a QtDialog that simulates a notification on the screen.

## How to use it
In your Main Module u have to do this
```python3
startNotification_Signal = pyqtSignal(Notification)
endNotification_Signal = pyqtSignal(Notification)

def _showNotification(self, n):
    """ shows the notification n """
    n.show()

def _hideNotification(self, n):
    """ hides the notification n """
    n.hide()

def showInformation(self, msg):
    """ shows a notification within a thread """
    t = threading.Thread(target=self.showInformationNotification, args=[msg])
    t.daemon = True
    t.start()

def _showInformationNotification(self, msg):
    """ shows a Information Notification """
    notification = Notification()
    notification.setHeader("Information")
    notification.setMessage(msg)

    self.startNotification_Signal.connect(self.showNotification)
    self.endNotification_Signal.connect(self.hideNotification)

    # signal the Thread to start Notification
    self.startNotification_Signal.emit(notification)

    # display time
    time.sleep(notification.getTimeout())

    # signal the Thread to stop Notification
    self.endNotification_Signal.emit(notification)
```
after that you can show an Notification with `self.showInformation("My Message")`
