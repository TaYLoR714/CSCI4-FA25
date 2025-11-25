#python
import array as array


def f(x,y,z):
    if (z==0):
        print("sum", x+y)
    elif (z==1):
        print("difference", abs(x-y))
    else:
        print("z =/= {0,1}")

f(1,1,0) #guess sum 3
f(1,2,1) #guess difference 1
f(1,2,5) #guess string in the else statement


x = 5  #x represents left right
y = 6  #y represnets down up
# index 0 represnes x coord, index 1 represents y coord
point = [x,y]

point_dict = {'x': 5, 'y': 6}

print("point at 0:", point[0])
print("point_dict at 'x':", point_dict['x'])