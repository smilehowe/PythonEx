#coding:gbk

from sofa import Sofa
from bed import Bed

sofa = Sofa()
bed = Bed()

sofa.print_define()
sofa.print_classify("低背沙发")
sofa.print_colour("红色")

bed.print_define()
bed.print_classify("平板")
bed.print_colour("白枫")
