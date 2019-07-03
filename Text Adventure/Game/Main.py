import SceneMap, Engine


def main():
    map = SceneMap.SceneMap("house")
    game = Engine.Engine(map)
    game.run()


if __name__ == "__main__":
    main()