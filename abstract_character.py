
class Abstract_Character():

    def __init__(self,player_name:str,int,str,dex):
        self._id = None
        self._class = None
        Abstract_Character.check_user_input('player_name',player_name)
        self._name = player_name
        self._level = 1
        self._max_health = 10 * self.get_lvl()
        self._health = 10 * self.get_lvl()
        self._intelligence = int
        self._strength = str
        self._dexterity = dex


    def set_id(self,id:int):
       """Sets the id attribute of a class to the var provided by the user"""
       Abstract_Character.check_user_input('id',id)
       self._id = id

    def get_id(self):
        """returns the id on the object"""
        return self._id

    def get_name(self):
        """returns the name of the attribute"""
        return self._name

    def get_class(self):
        """returns the class of the object"""
        return self._class

    def get_health(self):
        """returns the current health of the object"""
        return self._health

    def get_intelligence(self):
        """returns the intelligence lvl of the object"""
        return self._intelligence

    def get_strength(self):
        """returns the strength lvl of the object"""
        return self._strength

    def get_dexterity(self):
        """returns the dexterity lvl of the object"""
        return self._dexterity

    def get_lvl(self):
        """returns the lvl of the object"""
        return self._level

    def lvl_up(self):
        """adds one lvl to the object and raises the max health by 5"""
        self._level += 1
        self._max_health += 5

    def receive_heal(self, heal):
        """allows the target to receive healing from abilities"""
        self._health += heal
        if self._health > self._max_health:
            self._health = self._max_health

    def receive_damage(self,damage):
        """allows the target to receive damage/lose health from abilities/attacks"""
        self._health -= damage
        if self._health < 0:
            self._health = 0

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

    def _attack(self):
        raise NotImplementedError('NotImplemented')

    def ability_1(self):
        raise NotImplementedError('NotImplemented')

    def ability_2(self):
        raise NotImplementedError('NotImplemented')

    def ability_3(self):
        raise NotImplementedError('NotImplemented')

    def ability_4(self):
        raise NotImplementedError('NotImplemented')

    @staticmethod
    def check_user_input(varname,input):
        """checks that the inputted value is not empty or None"""
        if input == None:
            raise ValueError(varname+' can not be NoneType')
        if input == '':
            raise ValueError(varname+' can not be empty')