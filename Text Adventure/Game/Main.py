import SceneMap, Engine


def main():
    tests()


def game_start():
    map = SceneMap.SceneMap("house")
    game = Engine.Engine(map)
    game.run()


def tests():
    x = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]

    print x.index(1)


if __name__ == "__main__":
    main()