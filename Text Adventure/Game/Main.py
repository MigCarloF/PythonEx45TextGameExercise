import SceneMap, Engine
from Scenes import Scene


def main():
    tests()


def game_start():
    map = SceneMap.SceneMap("house")
    game = Engine.Engine(map)
    game.run()


def tests():
    in1, in2 = Scene.Scene().index_2d([[0, 0, 1], [0, 0, 0]], 1)
    assert in1 is 0 and in2 is 2

if __name__ == "__main__":
    main()