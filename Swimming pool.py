from connection import*

xp, yp, zp = mc.player.getPos()

def heram_create(my_file, start_x, start_y, start_z):
    my_file = open(my_file)
    for line in my_file:
        nums = line.strip().split(" ")
        print(nums)
        x = int(nums[0]) + start_x
        y = int(nums[1]) + start_y
        z = int(nums[2]) + start_z
        b = int(nums[3])
        mc.setBlock(x, y, z, b)

for i in range(10):
    heram_create("unknown.txt", xp + i * 20 , yp, zp)

