
# -*- coding: utf-8 -*-
# Created by ChiaSang on 2017-12-08 19:31
# 鸡兔同笼问题
numHeads = 35
numLegs = 94
for numChickens in range(0, numHeads + 1):
    numRabbits = numHeads - numChickens
    if (2 * numChickens + 4 * numRabbits == numLegs):
        print('numChickens:', numChickens)
        print('numChickens:', numRabbits)
