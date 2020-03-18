import matplotlib.pyplot as plt
import numpy as np


class car:
    
    def __init__(self, initial_speed, initial_distance, yellow_light_duration, intersection_width, positive_acceleration_magnitude, negative_acceleration_magnitude ):

        self.initial_speed = initial_speed
        self.initial_distance = initial_distance
        self.yellow_light_duration = yellow_light_duration
        self.intersection_width = intersection_width
        self.positive_acceleration_magnitude = positive_acceleration_magnitude
        self.negative_acceleration_magnitude = negative_acceleration_magnitude 

    def car_func(self):
        s = self.initial_distance + self.intersection_width
        x = self.initial_distance
        v_0 = self.initial_speed
        t = self.yellow_light_duration
        a_pos = self.positive_acceleration_magnitude
        a_neg = self.negative_acceleration_magnitude

        if s > v_0 * t - (a_neg * t * t) / 2 > x or s > v_0 * t + (a_pos * t * t) / 2 > x:
            print('You are dead!!!')
        elif s <= v_0 * t + (a_pos * t * t) / 2:
            print("pass!!!")
        elif x >= v_0 * t - (a_neg * t * t) / 2:
            print("stop!!!")



print('For some fixed parameters the initial speed v_0 should be 31<=v_0 or v_0<=24')
for i in range(20, 81):
  car1 = car(i, 50, 2, 10, 1, 1)
  print(i)
  car1.car_func()


print('For some fixed parameters the initial distance x should be x<=148')
for x in range(10, 151):
   car1 = car(80, x, 2, 10, 1, 1)
   print(x)
   car1.car_func()

print('For some fixed parameters the intersection width w should be w<=8')
for w in range(5, 21):
    car1 = car(30, 50, 2, w, 1, 1)
    print(w)
    car1.car_func()

print('For some fixed parameters the yellow light duration_y should be either 2 to stop or 4,5 to pass')
for y in range(2, 6):
    car1 = car(20, 50, y, 10, 1, 1)
    print(y)
    car1.car_func()

print('For some fixed parameters the positive acceleration ap should be 1,2 to stop')
for ap in range(1,4):
    car1 = car(23, 50, 2, 10, ap, 1)
    print(ap)
    car1.car_func()

print('For some fixed parameters the negative acceleration an should be 1 to pass')
for an in range(1, 4):
    car1 = car(31, 50, 2, 10, 1, an)
    print(an)
    car1.car_func()


#figure 1 time -distance plot
#some red light duration value
plt.figure(1)

red_t = 10
carn = car(27,50, 2, 10, 1, 1)

plt.xlabel('time')
plt.ylabel('distance')


t = np.linspace(0,14,100)
d1 = (carn.initial_speed*t + (carn.positive_acceleration_magnitude*t**2)/2) # when the car tries to pass
plt.plot(t, d1)

d2 = (carn.initial_speed*t - (carn.negative_acceleration_magnitude*t**2)/2)  # when the car tries to stop
plt.plot(t, d2)


plt.plot((carn.yellow_light_duration,carn.yellow_light_duration), (0, 1000), 'k-')
plt.plot((carn.yellow_light_duration+red_t,carn.yellow_light_duration+red_t), (0, 1000), 'k-')

plt.plot((0,14), (carn.initial_distance,carn.initial_distance ), 'k-')
plt.plot((0,14), (carn.initial_distance + carn.intersection_width,carn.initial_distance + carn.intersection_width ), 'k-')



# All the points in the time-distance graph that are in the black square are not safe. Those are the points where you are at the intersection and it is red light so these values are prohibited

plt.figure(2)

plt.xlabel('distance')
plt.ylabel('speed')


red_t = 10
carn = car(47,90, 2, 10, 1, 1)


v = np.linspace(-47,150,100)
vd = v-carn.initial_speed
d3 = (carn.yellow_light_duration*(3*carn.initial_speed - v)/2)  # when the car tries to pass
plt.plot(d3, vd)

d4 = (carn.yellow_light_duration*(carn.initial_speed + v)/2)    # when the car tries to stop
plt.plot(d4, vd)


plt.plot((0,300), (0, 0), 'k-')


plt.plot((carn.initial_distance,carn.initial_distance ), (0,100), 'k-')
plt.plot((carn.initial_distance + carn.intersection_width,carn.initial_distance + carn.intersection_width ),(0,100) , 'k-')

plt.show()


#If the car is in the middle of the intersection and its speed is 0 then we have a problem. If the yellow or blue graphs cross the horizontal black line and are in the middle of the 2 vertical lines then we are in the middle of
#the intersection with 0 speed (stopped).












