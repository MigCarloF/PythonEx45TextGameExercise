from Scenes import HouseScene, LabScene, MallScene, WinScene, DeathScene

class SceneMap(object):
    scene_map = {
        'house': HouseScene.HouseScene(),
        'mall': MallScene.MallScene(),
        'lab': LabScene.LabScene(),
        'win': WinScene.WinScene(),
        'death': DeathScene.DeathScene()
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        return SceneMap.scene_map.get(scene_name)

    def opening_scene(self):
        return self.next_scene(self.start_scene)
