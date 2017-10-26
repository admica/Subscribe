#!/usr/bin/env python

from PyQt4 import QtCore
import zmq

class Subscribe(QtCore.QObject):

    sig_output = QtCore.pyqtSignal(str)

    def __init__(self, parent=None):
        super(Subscribe, self).__init__(parent)
        self.running = True

        context = zmq.Context()
        self.socket = context.socket(zmq.SUB)
        self.socket.setsockopt_string(zmq.SUBSCRIBE, u'')


    def add(self, addr):
        self.socket.bind(addr)


    def worker(self):
        while self.running:
            msg = self.socket.recv_string()
            print "worker:",
            print msg
            self.sig_output.emit(msg)


if __name__ == '__main__':

    import sys
    from PyQt4 import QtCore
    app = QtCore.QCoreApplication(sys.argv)

    @QtCore.pyqtSlot(str)
    def processor(msg):
        print msg

    s = Subscribe()
    s.sig_output.connect(processor)

    thread = QtCore.QThread()
    s.moveToThread(thread)
    thread.started.connect(s.worker)
    thread.start()

    s.add('tcp://127.0.0.1:14444')

    sys.exit(app.exec_())
    
