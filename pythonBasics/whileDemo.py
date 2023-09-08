it = 10
while it > 1:
    # if it != 3:
    #     print(it)  # 3 is not printed
    if it == 9:
        it = it - 1
        continue  # continue: skip current iteration and proceed to the next iteration. 9 is not printed
    if it == 3:
        break  # break: when it equals to 3, it comes out of while. stop printing from 3
    print(it)
    it = it - 1

