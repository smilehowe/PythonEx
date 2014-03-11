#coding:gbk

from furniture import Furniture

class Bed(Furniture):
    
    def __init__(self):
        self.furniture = Furniture()
    
    def print_define(self):
        self.furniture.print_define()
        print "床是供人躺在上面睡觉的家具。"
    
    def print_classify(self, classify):
        print "床的分类为：%s" % classify
    
    def print_colour(self, colour):
        print "床的颜色是：%s" % colour

        