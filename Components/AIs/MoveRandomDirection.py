# this is an ai that will move the entity in a random direction
import random


class MoveRandomDirection:
    # AI to move in a random direction
    def take_turn(self):
        # entity takes a turn (this is the basic command for an ai)
        ent = self.owner
        directions = ['north', 'south', 'east', 'west']
        ent.movement.direction = random.choice(directions)
        ent.movement.speed = 100
