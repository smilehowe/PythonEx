#coding:gbk

from furniture import Furniture

class Sofa(Furniture):
    
    def print_define(self):
        super(Sofa, self).print_define()
        print "ɳ��Ϊһ��װ�����Ķ���λ���ӡ�װ�е��ɻ����ĭ���ϵȵĿ����Σ������з��֣�������Ҿߵ�һ�֡�"
    
    def print_classify(self, classify):
        print "ɳ���ķ���Ϊ��%s" % classify
    
    def print_colour(self, colour):
        print "ɳ������ɫ�ǣ�%s" % colour
