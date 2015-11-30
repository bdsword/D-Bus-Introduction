import gobject
import dbus
import dbus.service
from dbus.mainloop.glib import DBusGMainLoop

class DemoSignalService(dbus.service.Object):
    def __init__(self):
        bus_name = dbus.service.BusName('org.twbbs.bdsword.DemoSignalService', bus=dbus.SessionBus())
        dbus.service.Object.__init__(self, bus_name, '/org/twbbs/bdsword/DemoSignalServiceObject')

    @dbus.service.signal(dbus_interface='org.twbbs.bdsword.DemoSignalInterface',
                         signature='s')
    def device_inject_signal(self, device):
        print 'Device %s hook up!' % (device)

    @dbus.service.method(dbus_interface='org.twbbs.bdsword.DemoSignalInterface', in_signature='s')
    def inject(self, device):
        self.device_inject_signal(device)

    @dbus.service.method('org.twbbs.bdsword.DemoSignalInterface')
    def exit(self):
        loop.quit()

DBusGMainLoop(set_as_default=True)
demo_service = DemoSignalService()
loop = gobject.MainLoop()
loop.run()

