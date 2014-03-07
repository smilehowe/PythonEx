#coding:gbk

from furniture import Furniture

class Sofa(Furniture):
    
    def print_define(self):
        super(Sofa, self).print_define()
        print "沙发为一种装有软垫的多座位椅子。装有弹簧或厚泡沫塑料等的靠背椅，两边有扶手，是软件家具的一种。"
    
    def print_classify(self, classify):
        print "沙发的分类为：%s" % classify
    
    def print_colour(self, colour):
        print "沙发的颜色是：%s" % colour
