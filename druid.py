from abstract_character import Abstract_Character

class Druid(Abstract_Character):

    def __init__(self,name:str,int,str,dex):
        """creates the object and overides the _class attribute setting it to the class name"""
        super(Druid, self).__init__(name,int,str,dex)
        self._class = 'Druid'

    def _attack(self,target):
        """the basic attack which scales with lvl and the classes primary attribute(intelligence)"""
        damage = self.get_intelligence() * self.get_lvl()
        target.receive_damage(damage)

    def ability_1(self,target):
        """ability that deals damage to the target"""
        damage = (self.get_intelligence()*3)
        target.receive_damage(damage)

    def ability_2(self,ally):
        """ability that heals an ally"""
        heal = 4+self.get_intelligence()
        ally.receive_heal(heal)

    def ability_3(self,target):
        """ability that deals damage to the target"""
        damage1 = self.get_intelligence()+self.get_lvl()
        target.receive_damage(damage1)

    def ability_4(self,target):
        """ability that heals an ally"""
        heal = 10 * self.get_intelligence()
        target.receive_heal(heal)

    def to_dict(self):
         dict = {}
         dict['id'] = self._id
         dict['Name'] = self.get_name()
         dict['Class'] = self.get_class()
         dict['Level'] = self.get_lvl()
         dict['Health'] = self.get_health()
         dict['Strength'] = self.get_strength()
         dict['Dexterity'] = self.get_dexterity()
         dict['Intelligence'] = self.get_intelligence()
         return dict

