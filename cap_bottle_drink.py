# 4 cap -> 1 new cap + 1 new bottle + 1 drink:)
# 2 bottle -> 1 new cap + 1 new bottle + 1 drink:)
# $2 -> 1 new cap + 1 new bottle + 1 drink:)
# Change them(CAPS_PER_DRINK, BOTTLES_PER_DRINK, PRICE)

import glob as gl

CAPS_PER_DRINK = 4
BOTTLES_PER_DRINK = 2
PRICE = 2
BORROW_FLAG = True

gl.CAP = 0
gl.BOTTLE = 0
gl.FUND = 0
gl.RESULT = 0
while True:
    fund_temp = input("Input your money(input 'q' to quit):\n")
    if fund_temp.isnumeric():
        gl.FUND = int(fund_temp)
        break
    elif fund_temp == "q":
        exit()
    else:
        print("Please input numbers!(or input 'q' to quit)\n")

def get_newdrink(num):
    gl.CAP += num
    gl.BOTTLE += num
    gl.RESULT += num
    print(f'''\tNOW->Cap：{gl.CAP},Bottle:{gl.BOTTLE},Total:{gl.RESULT}\n''')
    
def cap_newdrink():
    cap = gl.CAP
    if cap < CAPS_PER_DRINK:
        return False
    num = cap // CAPS_PER_DRINK
    gl.CAP += -CAPS_PER_DRINK * num
    print(f'''\tCOST->Cap：{CAPS_PER_DRINK * num}\n''')
    get_newdrink(num)
    return True

def bottle_newdrink():
    bottle = gl.BOTTLE
    if bottle < BOTTLES_PER_DRINK:
        return False
    num = bottle // BOTTLES_PER_DRINK
    gl.BOTTLE += -BOTTLES_PER_DRINK * num
    print(f'''\tCOST->Bottle:{BOTTLES_PER_DRINK * num}\n''')
    get_newdrink(num)
    return True

def borrow_newdrink():
    cap = gl.CAP
    bottle = gl.BOTTLE
    if cap >= CAPS_PER_DRINK or bottle >= BOTTLES_PER_DRINK:
        return True
    if ((cap + 3) // CAPS_PER_DRINK >= 1 or (bottle + 3) // BOTTLES_PER_DRINK >= 1 
    and ((cap + 3)/CAPS_PER_DRINK)+((bottle + 3)/BOTTLES_PER_DRINK)) == 3:
        gl.RESULT += 3
        gl.CAP += -((cap + 3)//CAPS_PER_DRINK * CAPS_PER_DRINK) + 3
        gl.BOTTLE += -((bottle + 3)//BOTTLES_PER_DRINK * BOTTLES_PER_DRINK) + 3
        print(f'''\tBorrowed 3!
        NOW->Cap：{gl.CAP},Bottle:{gl.BOTTLE},Total:{gl.RESULT}\n''')
        return True
    elif (cap + 2) // CAPS_PER_DRINK == 1 and (bottle + 2) // BOTTLES_PER_DRINK == 1:
        gl.RESULT += 2
        gl.CAP += 2-CAPS_PER_DRINK
        gl.BOTTLE += 2-BOTTLES_PER_DRINK
        print(f'''\tBorrowed 2!
        NOW->Cap：{gl.CAP},Bottle:{gl.BOTTLE},Total:{gl.RESULT}\n''')
        return True
    elif (cap + 1) // CAPS_PER_DRINK == 1 or (bottle + 1) // BOTTLES_PER_DRINK == 1:
        gl.RESULT +=  ((cap + 1) // CAPS_PER_DRINK) + ((bottle + 1) // BOTTLES_PER_DRINK)
        gl.CAP += 1 - ((cap + 1) // CAPS_PER_DRINK) * CAPS_PER_DRINK
        gl.BOTTLE += 1 - ((bottle + 1)//BOTTLES_PER_DRINK)*BOTTLES_PER_DRINK
        print(f'''\tBorrowed 1!
        NOW->Cap：{gl.CAP},Bottle:{gl.BOTTLE},Total:{gl.RESULT}\n''')
        return True
    return False

# first of all, just buy it!
print("Simulating...\n")
buy_num = gl.FUND // PRICE
print(f"\tBought {buy_num}!\n")
gl.CAP = buy_num
gl.BOTTLE = buy_num
gl.RESULT = buy_num
# math?exchange!
while True:
    if not (cap_newdrink() or bottle_newdrink()):
        if not (borrow_newdrink()) and BORROW_FLAG:
            break

print(f"The result is {gl.RESULT}!")
