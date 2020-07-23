# game_object.py

GLOBALS = {
    'num_objects': 0
}

#
# Class GameObject
# Exists as base class for all game objects
#

class GameObject:
    name = "unnamed_object_X"
    pos  = (0, 0, 0)

    def __init__(self, name="", pos=(0,0,0)):
        if not name:
            self.name="unnamed_object_"+str(GLOBALS['num_objects'])
        else:
            self.name = name

        GLOBALS['num_objects']+=1
        self.pos = pos

    def set_name(self, name):
        self.name=name

    def set_pos(self, pos):
        self.pos=pos

    def get_name(self):
        return self.name

    def get_pos(self):
        return self.pos
