import game_object

g = game_object.GameObject()
g.set_pos((2,2,2))

print(g.get_name())
print(g.get_pos())
print(game_object.GAME_OBJECT_GLOBALS['num_objects'])
