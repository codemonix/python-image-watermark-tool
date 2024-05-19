
class ListMover:
    def __init__(self, list) :
        self.list = list
        self.index = 0
        self.element = self.list[self.index]

    def next_element(self):
        if self.index < len(self.list):
            self.index += 1
            self.element = self.list[self.index]
            return self.element
        
    def previous_element(self):
        if self.index > 0:
            self.index -= 1
            self.element = self.list[self.index]
            return self.element