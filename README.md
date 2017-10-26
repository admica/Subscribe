# Subscribe
QObject that converts ZeroMQ messages received to emitted signals

Typical usage is to instantiate a Subscribe object for incoming zmq messages and connect the output signal to your own slot to handle messages in whatever way you wish.

```python
@QtCore.pyqtSlot(str)
def processor(msg):
    print msg

s = Subscribe()
s.sig_output.connect(processor)

thread = QtCore.QThread()
s.moveToThread(thread)
thread.started.connect(s.worker)
thread.start()

s.add('tcp://127.0.0.1:1234')
```

Add as many host:port combinations as you wish to listen to with this signal/slot combination or instantiate as many Subscribe objects as you want.
