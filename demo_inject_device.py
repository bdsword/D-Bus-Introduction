import dbus

bus = dbus.SessionBus()
demo_service = bus.get_object('org.twbbs.bdsword.DemoSignalService', '/org/twbbs/bdsword/DemoSignalServiceObject')

demo_service_iface = dbus.Interface(demo_service, 'org.twbbs.bdsword.DemoSignalInterface')

demo_service_iface.inject('bluetooth')

