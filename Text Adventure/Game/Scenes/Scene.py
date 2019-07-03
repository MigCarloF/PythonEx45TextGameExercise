class Scene(object):
    def __init__(self):
        pass

    def play(self, area_map):
        pass

    # searches a 2d array for an item
    # returns the indexes
    def index_2d(self, array, item):

        for i in range(0, len(array)):
            try:
                index2 = array[i].index(item)
            except ValueError:
                index2 = -1
            if index2 != -1:
                index1 = i
                break

        if index2 is -1:
            index1 = -1
        return index1, index2
