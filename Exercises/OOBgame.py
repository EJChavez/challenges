class User():
    def sign_in(self):
        print('logged in')
    def fireball(self):
        print('you dont know this idiot')
class Wizard(User): # now this wizard just inherited some properties of the User class
    def __init__(self,name, hp, mana):
        self.name = name
        self.hp = hp
        self.mana = mana

    def fireball(self): # we can have multiple classes use fireball due to polymorphism
        User.fireball(self)
        if self.mana >= 50:
            print(f'fireball uses 50 mana, you have {self.mana - 50} mana left')
            self.mana = self.mana - 50
        else:
            print('not enough mana!')

class Cleric(User):
    def __init__(self, name, hp, mana):
        self.name = name
        self.hp = hp
        self.mana = mana

    def heal(self):
        print(f'heal uses {self.mana} mana')


wizard1 = Wizard('keith', 80,90)
wizard1.sign_in() #we can use this within the wizard class because we inherited it by calling through
wizard1.fireball()

# print(isinstance(wizard1, object))
# #multiple inheritance
#
# class User(object):
# 	def sign_in(self):
# 		print('logged in')
#
# class Wizard(User):
# 	def __init__(self, name, power):
# 		self.name = name
# 		self.power = power
# 	def attack(self):
# 		print(f'attacking with power of {self.power}')
#
# class Archer(User):
# 	def __init__(self, name, arrows):
# 		self.name = name
# 		self.arrows = arrows
# 	def check_arrows(self):
# 		print(f'{self.arrows} remaining')
# 	def attack(self):
# 		if self.arrows > 1:
# 			self.arrows = self.arrows - 1
# 			print(f'you have {self.arrows} arrows left')
# 		else:
# 			print('No arrows left!')
# 	def run(self):
# 		print('ran really fast')
#
#
# class HybridBorg(Wizard, Archer): #you can inherit from multiple classes:
# 	def __init__(self, name, power, arrows):
# 		Archer.__init__(self, name, arrows)
# 		Wizard.__init__(self,name,power)
#
# hb1 = HybridBorg('Lurtz', 50, 100)
# wizard1 = Wizard('Merlin', 60)
# archer1 = Archer('Robin Hood', 10)
# hb1.check_arrows()
# hb1.attack()
# # wizard1.attack()
# # archer1.check_arrows()
# # archer1.attack()