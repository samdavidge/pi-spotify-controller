import operator


class Device():

    def __init__(self, id: str, active: bool, name: str, volume: int, shuffle: bool):
        self.id = id
        self.active = active
        self.name = name
        self.volume = volume
        self.shuffle = shuffle

    def increaseVolume(self):
        self.volume = (self.volume + 10) if (self.volume + 10) <= 100 else 100
        return self.volume

    def decreaseVolume(self):
        self.volume = (self.volume - 10) if (self.volume - 10) >= 0 else 0
        return self.volume

    def toggleShuffle(self):
        self.shuffle = operator.not_(self.shuffle)
        return self.shuffle
