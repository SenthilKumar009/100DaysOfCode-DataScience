class Polygon:
    __width = None
    __height = None

    def set_values(self, height, width):
        self.__width = width
        self.__height = height
    
    def get_width(self):
        return self.__width

    def get_height(self):
        return self.__height