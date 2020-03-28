from polygon import Polygon
from color_shape import Colors

class Rectangle(Polygon, Colors):
    def get_area(self):
        return self.get_width() * self.get_height()