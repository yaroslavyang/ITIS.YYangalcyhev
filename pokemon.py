import timekill = 20class Pokemon:    def __init__(self):        self.health = 100        self.satiety = 100        self.t = time.time()    def check_health(self):        self.satiety = int(self.satiety - (time.time() - self.t) * kill)        if self.satiety <= 0:            self.health = int(self.health + self.satiety)            self.satiety = 0            if self.health <= 0:                return "You died"            self.t = time.time()            return "Health: " + str(self.health)        else:            self.t = time.time()            return "Health: " + str(self.health)    def check_satiety(self):        self.satiety = int(self.satiety - (time.time() - self.t) * kill)        if self.satiety <= 0:            self.health = int(self.health + self.satiety)            self.satiety = 0            if self.health <= 0:                return "You died"        self.t = time.time()        return "Satiety: " + str(self.satiety)    def feed(self):        self.satiety = int(self.satiety - (time.time() - self.t) * kill)        if self.satiety <= 0:            self.health = int(self.health - (time.time() - self.t) * kill)            if self.health <= 0:                return "You died"        self.t = time.time()        self.satiety = 100        return "Health: " + str(self.health), "Satiety: " + str(self.satiety)player = Pokemon()time.sleep(1)print(player.check_satiety())time.sleep(2)print(player.check_health())print(player.check_satiety())time.sleep(3)print(player.check_satiety())print(player.check_health())time.sleep(4)print(player.check_satiety())time.sleep(5)print(player.check_health())print(player.check_satiety())