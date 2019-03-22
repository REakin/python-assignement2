from Game import Game
from warrior import Warrior
from druid import Druid
from hunter import Hunter


D = Druid('ryan')
W = Warrior('Bob')
H = Hunter('jsd')
D.set_id(1)
W.set_id(2)
H.set_id(3)
RE = Warrior('replace')
RE.set_id(2)
game1 = Game()
game1.add(D)
game1.add(W)
game1.add(H)
print(game1.get(1))
#print(game1.get_all())
#print(game1.get_all_by_type('Druid'))
#game1.update(RE)
#print(game1.get_all())


