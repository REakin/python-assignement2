from unittest import TestCase
from druid import Druid

class TestDruid(TestCase):

    def setUp(self):
        """creates test characters"""
        self.test = Druid('Test')
        self.receiver = Druid('receiver')
        self.injured = Druid('injured')
        self.injured.receive_damage(8)

    def tearDown(self):
        """deletes the objects"""
        del self.test
        del self.receiver
        del self.injured

    def test_set_id(self):
        """sets the id of a object and """
        self.test.set_id(12)
        self.assertEqual(self.test.get_id(), 12)

    def test_get_id(self):
        self.test.set_id(12)
        self.assertEqual(self.test.get_id(), 12)

    def test_get_name(self):
        self.assertEqual(self.test.get_name(), 'Test')

    def test_get_class(self):
        self.assertEqual(self.test.get_class(), 'Druid')

    def test_get_health(self):
        self.assertEqual(self.test.get_health(), 10)

    def test_get_intelligence(self):
        self.assertEqual(self.test.get_intelligence(), 1)

    def test_get_strength(self):
        self.assertEqual(self.test.get_strength(), 1)

    def test_get_dexterity(self):
        self.assertEqual(self.test.get_dexterity(), 1)

    def test_get_lvl(self):
        self.assertEqual(self.test.get_lvl(), 1)

    def test_lvl_up(self):
        self.test.lvl_up()
        self.assertEqual(self.test.get_lvl(), 2)

    def test_receive_heal(self):
        self.test.receive_damage(7)
        self.test.receive_heal(5)
        self.assertEqual(self.test.get_health(), 8)

    def test_receive_damage(self):
        self.test.receive_damage(7)
        self.assertEqual(self.test.get_health(), 3)

    def test__attack(self):
        self.test._attack(self.receiver)
        self.assertEqual(self.receiver.get_health(), 9)

    def test_ability_1(self):
        self.test.ability_1(self.receiver)
        self.assertEqual(self.receiver.get_health(), 7)

    def test_ability_2(self):
        self.test.ability_2(self.injured)
        self.assertEqual(self.injured.get_health(), 7)

    def test_ability_3(self):
        self.test.ability_3(self.receiver)
        self.assertEqual(self.receiver.get_health(), 8)

    def test_ability_4(self):
        self.test.ability_4(self.injured)
        self.assertEqual(self.injured.get_health(), 10)