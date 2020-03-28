from polygon import Polygon

class Triangle(Polygon):
    def get_area(self):
        return self.get_width() * self.get_height() / 2