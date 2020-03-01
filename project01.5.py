import matplotlib.pyplot as plt
import numpy as np


class car:
    
    def __init__(self, initial_speed, initial_distance, yellow_light_duration, intersection_width, positive_acceleration_magnitude, negative_acceleration_magnitude, maximal_speed):

        self.initial_speed = initial_speed
        self.initial_distance = initial_distance
        self.yellow_light_duration = yellow_light_duration
        self.intersection_width = intersection_width
        self.positive_acceleration_magnitude = positive_acceleration_magnitude
        self.negative_acceleration_magnitude = negative_acceleration_magnitude
        self.maximal_speed = maximal_speed

    def car_func(self):
        s = self.initial_distance + self.intersection_width
        x = self.initial_distance
        v_0 = self.initial_speed
        t = self.yellow_light_duration
        a_pos = self.positive_acceleration_magnitude
        a_neg = self.negative_acceleration_magnitude
        v_max = self.maximal_speed
        

        if (s > v_0 * t - (a_neg* t**2) / 2 > x or s > v_0 * t + (a_pos* t**2) / 2 > x) and ((a_pos*t+v_0<v_max)or (-a_neg*t+v_0<v_max)):
            print('You are dead!!!')
        elif (s <= v_0 * t + (a_pos * t**2) / 2) and (a_pos*t+v_0<v_max):
            print("pass!!!")
        elif (x >= v_0 * t - (a_neg * t**2) / 2) and (-a_neg*t+v_0<v_max):
            print("stop!!!")
        else:
            print('You have passed the maximal speed')


print('For some fixed parameters the initial speed v_0 behaves like this')
for i in range(20, 81):
    car1 = car(i, 50, 2, 10, 1, 1,80)
    print(i)
    car1.car_func()
    
print('For some fixed parameters the initial distance x behaves like this')
for x in range(10, 151):
    car1 = car(80, x, 2, 10, 1, 1, 90)
    print(x)
    car1.car_func()

print('For some fixed parameters the intersection width w behaves like this')
for w in range(5, 21):
  car1 = car(30, 50, 2, w, 1, 1,60)
  print(w)
  car1.car_func()

print('For some fixed parameters the yellow light duration_y should behaves like this')
for y in range(2, 6):
   car1 = car(20, 50, y, 10, 1, 1, 60)
   print(y)
   car1.car_func()

print('For some fixed parameters the positive acceleration ap behaves like this')
for ap in range(1,4):
  car1 = car(23, 50, 2, 10, ap, 1, 50)
  print(ap)
  car1.car_func()

print('For some fixed parameters the negative acceleration an behaves like this')
for an in range(1, 4):
   car1 = car(31, 50, 2, 10, 1, an,50)
   print(an)
   car1.car_func()

print('For some fixed parameters the maximal_speed v_max behaves like this')
for vm in range(50, 150):
   car1 = car(20, 80, 2, 10, 1, 2,vm)
   print(vm)
   car1.car_func()
            
         
