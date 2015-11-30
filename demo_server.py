#!/bin/env python2.7

import gobject
import dbus
import dbus.service
from dbus.mainloop.glib import DBusGMainLoop

class DemoService(dbus.service.Object):
    def __init__(self):
        bus_name = dbus.service.BusName('org.twbbs.bdsword.DemoService', bus=dbus.SessionBus())
        dbus.service.Object.__init__(self, bus_name, '/org/twbbs/bdsword/DemoServiceObject')

    @dbus.service.method('org.twbbs.bdsword.DemoInterface',
                         in_signature='s', out_signature='s')
    def hello(self, msg):
        return "Hello,World!" + msg

    @dbus.service.method('org.twbbs.bdsword.DemoInterface2')
    def exit(self):
        loop.quit()

DBusGMainLoop(set_as_default=True)
demo_service = DemoService()
loop = gobject.MainLoop()
loop.run()
