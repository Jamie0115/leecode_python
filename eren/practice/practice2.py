print("----------")
"""
*
**
***
****
*****
"""
layer = 5
i = 1
while i <= layer:
    print("*" * i)
    i = i + 1

print("----------")
"""
    *
   **
  ***
 ****
*****
"""
layer = 5
i = 1
while i <= layer:
    print(" "*(layer-i) + "*"*i)
    i = i + 1

print("----------")
"""
*****
****
***
**
*
"""
layer = 5
i = 0
while i < layer:
    print("*"*(layer-i))
    i = i + 1

print("----------")
"""
*****
 ****
  ***
   **
    *
"""
layer = 5
i = 0
while i < layer:
    print(" "*i + "*"*(layer-i))
    i = i + 1
