ItemsInCart = 0
# 2 items will be added to cart

if ItemsInCart != 2:
#     raise Exception("Products Cart count not matching")s
    pass

assert (ItemsInCart == 0)

try:
    with open('test1.txt', 'r') as reader:
        reader.read()
except:
    print("open file failure")

try:
    with open('test1.txt', 'r') as reader:
        reader.read()
except Exception as e:  # python failure info passed to e
    print(e)
finally:
    print("cleaning up records")