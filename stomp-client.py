import time
from datetime import datetime
import sys

import stomp

class MyListener(stomp.ConnectionListener):
    def on_error(self, headers, message):
        print('received an error "%s"' % message)
    def on_message(self, headers, message):
        print('received a message "%s"' % message)

#c = stomp.Connection([('127.0.0.1', 62613)])
conn = stomp.Connection([('127.0.0.1', 61613)])
#conn.set_listener('', MyListener())
conn.start()
conn.connect('user', 'user', wait=True)

#conn.subscribe(destination='/queue/test', id=1, ack='auto')
print('emission "%s"' % datetime.now())
conn.send(body=' '.join(sys.argv[1:]), destination='/queue/test')

#time.sleep(2)
conn.disconnect()
