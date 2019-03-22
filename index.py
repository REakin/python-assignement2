from druid import Druid
from warrior import Warrior
from hunter import Hunter



war = Warrior('eff')
print(war.get_name())
print(war.get_class())

hun = Hunter('Victor')
hun.set_id(1)
print(hun.get_id())
print(hun.get_name())
print(hun.get_class())

dru = Druid('Ryan')
print(dru.get_name())
dru.lvl_up()
print(dru.get_class())
dru.set_id(1)
print(dru.get_id())