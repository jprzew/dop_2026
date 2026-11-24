"""Module with definitions of considered species"""
import random


class Probability:

    def __get__(self, obj, objtype=None):
        return getattr(obj, self.private_name)

    def __set__(self, obj, value):
        # Makes sure that 0 <= value <= 1
        value = min(1.0, max(0.0, value))

        setattr(obj, self.private_name, value)

    def __set_name__(self, owner, name):
        self.private_name = '_' + name


class Creature:

    alive: bool = True
    p_death = Probability()
    p_reproduce = Probability()

    def __init__(self, p_death: float, p_reproduce: float):
        self.p_death = p_death
        self.p_reproduce = p_reproduce

    def kill(self):
        """Kills (i.e. alive=False) the creature with probability p_death"""
        if random.random() < self.p_death:
            self.alive = False

    def reproduce(self):
        """Returns new instance of Creature with probability p_reproduce (otherwise None)"""

        if self.alive and (random.random() < self.p_reproduce):

            # 1. Consider changing p_death, p_reproduce to have instances different from the parent
            return self.__class__(p_death=self.p_death, p_reproduce=self.p_reproduce)

        return None


class Prey(Creature):

    def __init__(self, p_death: float, p_reproduce: float, p_hunt: float):
        super().__init__(p_death, p_reproduce)
        self.p_hunt = min(1.0, max(0.0, p_hunt))

    def reproduce(self):
        if self.alive and random.random() < self.p_reproduce:
            return Prey(
                p_death=self.p_death,
                p_reproduce=self.p_reproduce,
                p_hunt=self.p_hunt
            )

        return None


class Predator(Creature):

    p_death_hungry = 0.9

    def __init__(self, p_death: float, p_reproduce: float, hungry: bool = True):
        super().__init__(p_death, p_reproduce)
        self.hungry = hungry

    def hunt(self, prey: Prey):
        if self.alive and prey.alive:
            if random.random() < prey.p_hunt:
                prey.alive = False
                self.hungry = False
                return True

        return False

    def kill(self):
        if self.hungry:
            probability = self.p_death_hungry
        else:
            probability = self.p_death

        if random.random() < probability:
            self.alive = False
