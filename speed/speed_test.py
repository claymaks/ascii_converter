from ascii_pic_optimize import run



black_sum = 0
for i in range(0,4):
    black_sum += run("test.jpg", 1)
print(black_sum/4)

