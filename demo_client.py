import dbus

bus = dbus.SessionBus()
demo_service = bus.get_object('org.twbbs.bdsword.DemoService', '/org/twbbs/bdsword/DemoServiceObject')
hello = demo_service.get_dbus_method('hello', dbus_interface='org.twbbs.bdsword.DemoInterface')

demo_service_iface = dbus.Interface(demo_service, 'org.twbbs.bdsword.DemoInterface')
demo_service_iface2 = dbus.Interface(demo_service, 'org.twbbs.bdsword.DemoInterface2')

print demo_service_iface.hello('tes')
print hello('tes2')

demo_service_iface2.exit()
