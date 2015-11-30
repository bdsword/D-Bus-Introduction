import dbus
import gobject
from dbus.mainloop.glib import DBusGMainLoop

def handler(device=None):
    print "got signal from %s" % device

DBusGMainLoop(set_as_default=True)

bus = dbus.SessionBus()
demo_service = bus.get_object('org.twbbs.bdsword.DemoSignalService', '/org/twbbs/bdsword/DemoSignalServiceObject')

demo_service_iface = dbus.Interface(demo_service, 'org.twbbs.bdsword.DemoSignalInterface')

demo_service_iface.connect_to_signal('device_inject_signal', handler,
                                     dbus_interface='org.twbbs.bdsword.DemoSignalInterface')

loop = gobject.MainLoop()
loop.run()

