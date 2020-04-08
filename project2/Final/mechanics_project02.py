def coordinates (time_force, m1, m2, m3, mu1, mu2, mu3, x01, y01, x02, y02, x03, y03):
    t0 = 0
    v01 = 0
    v02 = 0
    v03x = 0
    v03y = 0

    ret_array = []
    x1s=[];x2s=[]; x3s=[];y1s=[];y2s=[];y3s = []

    rl = x01-x02+y01-y03
    for t in time_force:
        f = time_force[t]


        g = 10
        a1 = ((m3+m2)*(f-mu1*(m1+m2)*g)-m2*m3*g*(1-mu2)*(1-mu1))/((m1+m3)*(m3+m2)+(1-mu1)*(2*mu3*m3+m3)*m2)
        T = (m2*m3*g+(2*mu3*m3+m3)*a1*m2-mu2*m2*m3*g)/(m3+m2)
        a2 = (T-m3*g-2*mu3*m3*a1-m3*a1)/(-m3)
        a3y = a1-a2
        a3x = a1
        

        v1 = v01 + a1*(t-t0)
        v2 = v02 + a2*(t-t0)
        v3x = v03x + a3x*(t-t0)
        v3y = v03y + a3y*(t-t0)

        x1 = x01 + v01*(t-t0) + a1*(t-t0)*(t-t0)/2
        y1 = y01

        x2 = x02 + v02*(t-t0) + a2*(t-t0)*(t-t0)/2
        y2 = y02

        x3 = x03 + v03x*(t-t0) + a3x*(t-t0)*(t-t0)/2
        y3 = y03 + v03y*(t-t0) + a3y*(t-t0)*(t-t0)/2

        v01 = v1
        v02 = v2
        v03x = v3x
        v03y = v3y

        if y3 > y1:  # if m3 tries to escape the hole or go lower than the floor of m1
            y03 = y1
        elif y1-y3 > rl:
             y03 = y1 - rl
        else:
            y03 = y3    
            
        if (rl) < x1-x2: # if m2 tries to fall in the left side of m1 or go too much right
            x02 = x1-(rl)
        elif x2 > x1:
            x02 = x1
        else:
            x02 = x2    




        x01 = x1
        y01 = y1
        y02 = y2
        x03 = x3

        x1s.append(x01)
        x2s.append(x02)
        x3s.append(x03)
        y1s.append(y01)
        y2s.append(y02)
        y3s.append(y03)

        ret_array.append(x1s)
        ret_array.append(x2s)
        ret_array.append(x3s)
        ret_array.append(y1s)
        ret_array.append(y2s)
        ret_array.append(y3s)


        t0 = t
        
        

    return ret_array       

         

        

#below are some of the cases I noticed

# I tried to keep the coordinates of m1 stable in a few ways:
# 1. we choose a big mass for m1
# 2. we choose a small mass for m3 and a bigger mass for m2 compared to m3
# 3. we input big value for mu2(so m2 hardly moves)

# Note that here having only force F = 0 all the time will not help because there are other forces that 
# influence m1's movement (those forces are posed by the motion of m3 and m2) but if we choose the above 
# parameters in a right way that motion will be unnoticable and it will give so little acceleration to m1 that
# m1's coordinates will almost not change



# in this case we see some movments
print("CASE 1 (before the mentioned improvements)")
time_force = {0:0,1:0, 2:0, 3:0, 4:0}
ret_array = coordinates(time_force, 6, 1, 3, 0, 0, 0, 10, 15, 4, 15, 12, 10)


from tabulate import tabulate
headers = ['time moment', 'Force', 'x1', 'y1', 'x2', 'y2', 'x3', 'y3']    

time_moments = time_force.keys()
forces = time_force.values()
x1s = ret_array[0]
x2s = ret_array[1]
x3s = ret_array[2]
y1s = ret_array[3]
y2s = ret_array[4]
y3s = ret_array[5]

table = zip(time_moments, forces, x1s, y1s, x2s, y2s, x3s, y3s)
print(tabulate(table, headers=headers, floatfmt=".4f"))

# in this case there is no movement
print("CASE 2", "(after the mentioned improvements)")
time_force = {0:0,1:0, 2:0, 3:0, 4:0}
ret_array = coordinates(time_force, 10, 0.1, 0.00001, 0, 0.5, 0, 10, 15, 4, 15, 12, 10)


from tabulate import tabulate
headers = ['time moment', 'Force', 'x1', 'y1', 'x2', 'y2', 'x3', 'y3']    

time_moments = time_force.keys()
forces = time_force.values()
x1s = ret_array[0]
x2s = ret_array[1]
x3s = ret_array[2]
y1s = ret_array[3]
y2s = ret_array[4]
y3s = ret_array[5]

table = zip(time_moments, forces, x1s, y1s, x2s, y2s, x3s, y3s)
print(tabulate(table, headers=headers, floatfmt=".4f"))

# I also tried forces with different directions
# we can see that even though we push m1 back with the same force it does not end up in the same place
# I assume it is because it has some initial velocity when we use the force f2
print("CASE 3")
time_force = {0:0,1:30, 2:-30}
ret_array = coordinates(time_force, 6, 3, 1, 0, 0, 0, 10, 15, 4, 15, 12, 10)


from tabulate import tabulate
headers = ['time moment', 'Force', 'x1', 'y1', 'x2', 'y2', 'x3', 'y3']    

time_moments = time_force.keys()
forces = time_force.values()
x1s = ret_array[0]
x2s = ret_array[1]
x3s = ret_array[2]
y1s = ret_array[3]
y2s = ret_array[4]
y3s = ret_array[5]

table = zip(time_moments, forces, x1s, y1s, x2s, y2s, x3s, y3s)
print(tabulate(table, headers=headers, floatfmt=".4f"))


# in this case we  choose m3 with really big mass and m1 with small mass, which results to a small tension and small N0
# hence m1 does not significantly move
print("CASE 4")
time_force = {0:0,1:0, 2:0}
ret_array = coordinates(time_force, 10, 0.001, 10, 0, 0, 0, 10, 15, 4, 15, 12, 10)


from tabulate import tabulate
headers = ['time moment', 'Force', 'x1', 'y1', 'x2', 'y2', 'x3', 'y3']    

time_moments = time_force.keys()
forces = time_force.values()
x1s = ret_array[0]
x2s = ret_array[1]
x3s = ret_array[2]
y1s = ret_array[3]
y2s = ret_array[4]
y3s = ret_array[5]

table = zip(time_moments, forces, x1s, y1s, x2s, y2s, x3s, y3s)
print(tabulate(table, headers=headers, floatfmt=".4f"))


# in this case I chose m1's mass really small and it moved significantly
print("CASE 5")
time_force = {0:0,1:0, 2:0}
ret_array = coordinates(time_force, 0.1, 10, 10, 0, 0, 0, 10, 15, 4, 15, 12, 10)


from tabulate import tabulate
headers = ['time moment', 'Force', 'x1', 'y1', 'x2', 'y2', 'x3', 'y3']    

time_moments = time_force.keys()
forces = time_force.values()
x1s = ret_array[0]
x2s = ret_array[1]
x3s = ret_array[2]
y1s = ret_array[3]
y2s = ret_array[4]
y3s = ret_array[5]

table = zip(time_moments, forces, x1s, y1s, x2s, y2s, x3s, y3s)
print(tabulate(table, headers=headers, floatfmt=".4f"))


# and then I increased mu2 and mu3 to help stop their motion and hence m1's motion. we see a great 
# difference between this and 5th cases
print("CASE 6")
time_force = {0:0,1:0, 2:0}
ret_array = coordinates(time_force, 0.1, 10, 10, 0, 0.5, 0.5, 10, 15, 4, 15, 12, 10)


from tabulate import tabulate
headers = ['time moment', 'Force', 'x1', 'y1', 'x2', 'y2', 'x3', 'y3']    

time_moments = time_force.keys()
forces = time_force.values()
x1s = ret_array[0]
x2s = ret_array[1]
x3s = ret_array[2]
y1s = ret_array[3]
y2s = ret_array[4]
y3s = ret_array[5]

table = zip(time_moments, forces, x1s, y1s, x2s, y2s, x3s, y3s)
print(tabulate(table, headers=headers, floatfmt=".4f"))

# Now let's try maximum force on m1
print("CASE 7")
time_force = {0:0,1:300}
ret_array = coordinates(time_force, 0.1, 10, 10, 0, 0.5, 0.5, 10, 15, 4, 15, 12, 10)


from tabulate import tabulate
headers = ['time moment', 'Force', 'x1', 'y1', 'x2', 'y2', 'x3', 'y3']    

time_moments = time_force.keys()
forces = time_force.values()
x1s = ret_array[0]
x2s = ret_array[1]
x3s = ret_array[2]
y1s = ret_array[3]
y2s = ret_array[4]
y3s = ret_array[5]

table = zip(time_moments, forces, x1s, y1s, x2s, y2s, x3s, y3s)
print(tabulate(table, headers=headers, floatfmt=".4f"))


#let's use 30 N force and then 15 and after that 15
print("CASE 8")
time_force = {0:0,1:30}
ret_array = coordinates(time_force, 0.1, 10, 10, 0, 0.5, 0.5, 10, 15, 4, 15, 12, 10)


from tabulate import tabulate
headers = ['time moment', 'Force', 'x1', 'y1', 'x2', 'y2', 'x3', 'y3']    

time_moments = time_force.keys()
forces = time_force.values()
x1s = ret_array[0]
x2s = ret_array[1]
x3s = ret_array[2]
y1s = ret_array[3]
y2s = ret_array[4]
y3s = ret_array[5]

table = zip(time_moments, forces, x1s, y1s, x2s, y2s, x3s, y3s)
print(tabulate(table, headers=headers, floatfmt=".4f"))



print("CASE 9")
time_force = {0:0,0.5:15,1:15}
ret_array = coordinates(time_force, 0.1, 10, 10, 0, 0.5, 0.5, 10, 15, 4, 15, 12, 10)


from tabulate import tabulate
headers = ['time moment', 'Force', 'x1', 'y1', 'x2', 'y2', 'x3', 'y3']    

time_moments = time_force.keys()
forces = time_force.values()
x1s = ret_array[0]
x2s = ret_array[1]
x3s = ret_array[2]
y1s = ret_array[3]
y2s = ret_array[4]
y3s = ret_array[5]

table = zip(time_moments, forces, x1s, y1s, x2s, y2s, x3s, y3s)
print(tabulate(table, headers=headers, floatfmt=".4f"))

# in the last 2 cases we get different coordinates in the end because in the first case the initial velocity 
# is 0, but in the second case when we use 15 N force the second time it already has a initial velocity

