# int & float
# .format的好處是字符串格式化的一種方法，它允許你通過佔位符將變量插入到字符串中。
import math
from math import exp, log, sqrt

x = 9 ; y = 10
print("Output #1: {1}".format(x, y))
print("Output #2: {0}".format(3**4))
print("Output #3: {0}".format(int(8.3)/int(2.7)))
print("Output #4: {0:.3f}".format(8.3/2.7))
y = 2.5*4.8
print("Output #5: {0:.5f}".format(y))
r = 8/float(3)
print("Output #6: {0:.5f}".format(r))
print("Output #7: {0:.4f}".format(0.8/3))
print("Output #8: {0:.5f}".format(exp(3)))
print("Output #9: {0:.5f}".format(log(exp(3))))
print("Output #10: {0:.1f}".format(sqrt(81)))

# 練習題
name = "Jamie"
age = "25"
sentence_1 = "Hi, my name is {}, I'm {} years old.".format(name, age)
print("Practice #1: {0}".format(sentence_1))
sentence_2 = "Hi, my name is {0}, I'm {1} years old.".format(name, age)
print("Practice #2: {0}".format(sentence_2))
x = math.pi
sentence_3 = "Pi is approximately {0:.20f}".format(x)
print("Practice #3: {0}".format(sentence_3))
sentence_4 = "{0:<10} | {0:^10} | {0:>10}".format("left", "center", "right")
print("Practice #4: {0}".format(sentence_4))
number = 1234.5678
sentence_5 = "The number is {0:.2f} and in scientific notation it's {0:e}".format(number)
print("Practice #5: {0}".format(sentence_5))
