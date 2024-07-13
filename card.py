import game_dict

class Card:
    _instances = {}

    def __new__(cls, *args, **kwargs):

        if args[0] in cls._instances.keys():
            return cls._instances[args[0]]
        else:
            instance = super(Card, cls).__new__(cls)
            cls._instances[args[0]] = instance
            return instance

    def __init__(self, diccionario):
        self.dictionary = diccionario

    def __eq__(self, other):
        return self.grp_id == other

    def __str__(self):
        return str(self.grp_id)


    @property
    def instance_id(self):
        return self.dictionary['instanceId']
    @property
    def grp_id(self):
        return self.dictionary['grpId']


    @property
    def owner(self):
        return self.dictionary['ownerSeatId']

    @property
    def zone_id(self):
        return self.dictionary['zoneId']


    @property
    def cost_RGBWBN(self):
        try:
            return sum(coste['count'] for coste in self.dictionary['manaCost'])
        except KeyError:
            return None
        except Exception as e:
            print(f'Error Card cost_RGBWBN: {e}')
            return None
    @property
    def sum_cost(self):
        try:
            return sum(coste['count'] for coste in self.dictionary['manaCost'])
        except KeyError:
            return None
        except Exception as e:
            print(f'Error Card sum_cost: {e}')
            return None
    @property
    def value(self):
        try:
            return self.dictionary['valor']
        except KeyError:
            print('Card value: KeyError')
            return None



    @property
    def power(self):
        try:
            return self.dictionary['power']['value']
        except:
            return 0
    @property
    def toughness(self):
        try:
            if 'value' in self.dictionary['toughness'].keys():
                return self.dictionary['toughness']['value']
            else:
                print('Class Card: no toughness??')
                return 0
        except Exception as e:
            print(f'Excepción property toughness {e}')
    @property
    def stats_4(self):
        if self.first_strike:
            stats =  [self.power, 0 , self.toughness]
        elif self.double_strike:
            stats =  [self.power,self.power,self.toughness]
        else:
            stats =  [0,self.power,self.toughness]

        if self.death_touch:
            return [stats[0], stats[1], stats[2],True]
        else:
            return [stats[0], stats[1], stats[2],False]


    @property
    def creature(self):
        try:
            return True if 'CardType_Creature' in self.dictionary['cardTypes'] else False
        except KeyError:
            print('Card property creature KeyWord')
            return None

    @property
    def land(self):
        try:
            return True if 'CardType_Land' in self.dictionary['cardTypes'] else False
        except KeyError:
            print('Card property land KeyWord')
            return None
    @property
    def planeswalker(self):
        try:
            return True if 'CardType_Planeswalker' in self.dictionary['cardTypes'] else False
        except KeyError:
            print('Card property planeswalker KeyWord')
            return None


    @property
    def tapped(self):
        return True if 'isTapped' in self.dictionary.keys() else False
    @property
    def summoning_sickness(self):
        return True if 'hasSummoningSickness' in self.dictionary.keys() else False
    @property
    def attack_ready(self):
        return True if not self.summoning_sickness and not self.tapped or self.summoning_sickness and self.haste and not self.tapped else False

    @property
    def haste(self):
        try:
            return True if 9 in self.dictionary['abilities'] else False
        except KeyError:
            return None
    @property
    def first_strike(self):
        try:
            return True if 6 in self.dictionary['abilities'] else False
        except KeyError:
            return None
    @property
    def double_strike(self):
        try:
            return True if 3 in self.dictionary['abilities'] else False
        except KeyError:
            return None
    @property
    def death_touch(self):
        try:
            return True if 1 in self.dictionary['abilities'] else False
        except KeyError:
            return None
    @property
    def fly(self):
        try:
            return True if 8 in self.dictionary['abilities'] else False
        except KeyError:
            return None






    @property
    def attack_declared(self):
        try:
            return True if self.dictionary['attackState'] == 'AttackState_Declared' else False
        except KeyError:
            return None
    @property
    def attacking(self):
        try:
            return True if self.dictionary['attackState'] == 'AttackState_Attacking' else False
        except KeyError:
            return None

    @property
    def block_declared(self):
        try:
            return True if self.dictionary['attackState'] == 'BlockState_Declared' else False
        except KeyError:
            return None
    @property
    def blocking(self):
        try:
            return True if self.dictionary['attackState'] == 'BlockState_Blocking' else False
        except KeyError:
            return None
    @property
    def blocked(self):
        try:
            return True if self.dictionary['attackState'] == 'BlockState_Blocked' else False
        except KeyError:
            return None
    @property
    def unblocked(self):
        try:
            return True if self.dictionary['attackState'] == 'BlockState_Unblocked' else False
        except KeyError:
            return None


    @property
    def legendary(self):
        return True if 'superTypes' in self.dictionary.keys() and 'SuperType_Legendary' in self.dictionary['superTypes'] else False

    @property
    def dragon(self):
        return True if 'subtypes' in self.dictionary.keys() and 'SubType_Dragon' in self.dictionary['subtypes'] else False

    @property
    def goblin(self):
        try:
            return True if self.creature and "SubType_Goblin" in self.dictionary['subtypes'] else False
        except KeyError:
            print('Card property creature KeyWord')
            return None

    # @property
    #     mana_cost


if __name__ == '__main__':
    a = Card('hola')
