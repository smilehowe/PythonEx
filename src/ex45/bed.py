#coding:gbk

from furniture import Furniture

class Bed(Furniture):
    
    def __init__(self):
        self.furniture = Furniture()
    
    def print_define(self):
        self.furniture.print_define()
        print "���ǹ�����������˯���ļҾߡ�"
    
    def print_classify(self, classify):
        print "���ķ���Ϊ��%s" % classify
    
    def print_colour(self, colour):
        print "������ɫ�ǣ�%s" % colour

        