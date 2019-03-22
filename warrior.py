from abstract_character import Abstract_Character

class Warrior(Abstract_Character):

    def __init__(self,name:str,int,str,dex):
        """creates the object and overides the _class attribute setting it to the class name"""
        super(Warrior, self).__init__(name,int,str,dex)
        self._class = 'Warrior'

    def _attack(self,target):
        """the basic attack which scales with lvl and the classes primary attribute(Strength)"""
        damage = self.get_strength() * self.get_lvl()
        target.receive_damage(damage)

    def ability_1(self,target):
        """ability that deals damage to the target"""
        damage = (self.get_strength()+2)
        target.receive_damage(damage)

    def ability_2(self,target):
        """ability that deals damage to the target"""
        damage1 = (self.get_lvl()+self.get_strength())
        target.receive_damage(damage1)

    def ability_3(self,target):
        """ability that deals damage to the target"""
        damage = (self.get_dexterity()+self.get_strength())
        target.receive_damage(damage)

    def ability_4(self,target):
        """ability that deals damage to the target"""
        damage = (self.get_strength()*3)
        target.receive_damage(damage)
