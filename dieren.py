class Dier():
    def __init__(self, poten, ogen):
        self.poten = poten
        self.ogen = ogen
    
    def voorplanting():
        pass


class Zoogdier(Dier):
    def __init__(self, maanden, poten, ogen):
        self.maanden = maanden
        super().__init__(poten, ogen)

    def voorplanting():
        pass

class Vis(Dier):
    def __init__(self, poten, ogen):
        super().__init__(poten, ogen)

poes = Zoogdier(2, 4, 2)