from polygon import Polygon

class Rectangle(Polygon):
    def get_area(self):
        return self.get_width() * self.get_height()