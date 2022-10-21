

import random
# Soldier
class Soldier:
    def __init__(self, health= 0, strength= 0):           
    
        #atributos
        self.health= health
        self.strength= strength
    
    #métodos
    def attack(self):
    
        return (self.strength)
    
    def receiveDamage(self, damage):
        self.health= self.health - damage
        
        return

# Viking
class Viking(Soldier):
    def __init__(self, name= "", health= 0, strength= 0): 
        
        #atributos
        Soldier.__init__(self)
        self.health= health
        self.strength= strength
        self.name= name
        
        #Métodos
              
    def receiveDamage(self, damage):
                   
        self.health= self.health - damage
        if self.health > 0:
            return(f'{self.name} has received {damage} points of damage')
        else:
            return(f'{self.name} has died in act of combat')
    def battleCry(self):
        return('Odin Owns You All!')      

# Saxon
class Saxon(Soldier):
    def __init__(self, health= 0, strength= 0): 
        
        #atributos
        Soldier.__init__(self)
        self.health= health
        self.strength= strength
        
        
         #Métodos
    def receiveDamage(self, damage):                           
        self.health= self.health - damage
        if self.health > 0:
            return(f'A Saxon has received {damage} points of damage')
        else:
            return('A Saxon has died in combat')
            
        

# War
class War:
    def __init__(self):
        
        #atributo
        self.vikingArmy= vikingArmy= []
        self.saxonArmy= saxonArmy=[]
                
        #Métodos
    def addViking(self, viking):
        self.vikingArmy.append(viking)
               
    
    def addSaxon(self, saxon):
        self.saxonArmy.append(saxon)
                    
    
    def vikingAttack(self):
        s=random.choice(self.saxonArmy)
        v=random.choice(self.vikingArmy)
        result= s.receiveDamage(v.strength)
        if s.health <= 0:
            self.saxonArmy.remove(s)
        return(result)
        
    def saxonAttack(self):
        s=random.choice(self.saxonArmy)
        v=random.choice(self.vikingArmy)
        result= v.receiveDamage(s.strength)
        if v.health <= 0:
            self.vikingArmy.remove(v)
        return(result)
    
    def showStatus(self):
        lista_vacia=[]
        if self.vikingArmy == lista_vacia:
            return('Saxons have fought for their lives and survive another day...')
        elif self.saxonArmy == lista_vacia:
            return ('Vikings have won the war of the century!')
          
        else:
            return "Vikings and Saxons are still in the thick of battle."
    
