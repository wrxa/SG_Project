# -*- coding: utf-8 -*-


# direction:0，横向文本，1，纵向文本
class ImageInfo():
    def __init__(self, direction, coordinate, value, valueSize=18):
        self.direction = direction
        self.coordinate = coordinate
        self.value = value
        self.valueSize = valueSize
