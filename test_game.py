from unittest import TestCase
from Game import Game
from warrior import Warrior
from druid import Druid
from hunter import Hunter

class TestGame(TestCase):

    def setUp(self):
        self.game1 = Game()
        self.game2 = Game()
        W = Warrior('warrior')
        H = Hunter('hunter')
        D = Druid('druid')
        W.set_id(1)
        H.set_id(2)
        D.set_id(3)
        self.game2.add(W)
        self.game2.add(H)
        self.game2.add(D)

    def tearDown(self):
        del self.game1
        del self.game2

    def test_add(self):
        self.game1.add(Druid('test2'))
        self.assertEqual(len(self.game1.players), 1)

    def test_get(self):
        self.assertEqual(type(self.game2.get(1)),Warrior)
        self.assertEqual(type(self.game2.get(2)),Hunter)
        self.assertEqual(type(self.game2.get(3)),Druid)

    def test_get_all(self):
        self.assertEqual(type(self.game2.get_all()),list)

    def test_get_all_by_type(self):
        self.game2.add(Warrior('test2'))
        self.assertEqual(len(self.game2.get_all_by_type('Warrior')),2)
        self.assertEqual(type(self.game2.get_all_by_type('Warrior')),list)

    def test_update(self):
        Replace = Warrior('replace')
        Replace.set_id(2)
        self.game2.update(Replace)
        self.assertEqual(type(self.game2.get(2)),Warrior)

    def test_update_raise_error(self):
        Replace = Warrior('replace')
        Replace.set_id(5)
        self.assertRaisesRegex(LookupError,'Player ID not found',self.game2.update,Replace)

    def test_delete(self):
        self.game2.delete(2)
        self.assertEqual(len(self.game2.get_all()),2)
