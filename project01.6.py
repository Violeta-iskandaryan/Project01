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



def advice(car1, car2, d):
    s = car1.initial_distance + car1.intersection_width
    x = car1.initial_distance
    t = car1.yellow_light_duration
    v_0_1 = car1.initial_speed
    a_pos_1 = car1.positive_acceleration_magnitude
    a_neg_1 = car1.negative_acceleration_magnitude
    v_0_2 = car2.initial_speed
    a_pos_2 = car2.positive_acceleration_magnitude
    a_neg_2 = car2.negative_acceleration_magnitude

    if s > v_0_1 * t - (a_neg_1 * t * t) / 2 > x or s > v_0_1 * t + (a_pos_1 * t * t) / 2 > x:
         if x+d >= v_0_2 * t - (a_neg_2 * t * t) / 2:
             print('first is dead, second should stop')
         else:
            print('Both are dead')        # the first one can't pass or stop and the second one cannot stop so it will join the first one with a crash or be crashed with another car at the intersection   
    elif s <= v_0_1 * t + (a_pos_1 * t * t) / 2:
         if s+d <= v_0_2 * t + (a_pos_2 * t * t) / 2:
             print('Both cars can pass')
         elif x+d >= v_0_2 * t - (a_neg_2 * t * t) / 2:
             print('first can pass, second should stop')
    elif x >= v_0_1 * t - (a_neg_1 * t * t) / 2:
           print('Both cars need to stop') # because if the first needs to stop then the second has to
            

print('example 1')
d = 10
t = 4
car1 = car(80, 100, t, 7, 2, 1)
car2 = car(60, 100 + d, t, 7, 2, 1  )

advice(car1, car2, d)


print('example 2')
d2 = 2
car3 = car(20, 100, t, 7, 2, 1)
car4 = car(80, 100 + d2, t, 7, 2, 1  )

advice(car3, car4, d2)


print('example 3')
d3 = 1
car5 = car(20, 70, t, 7, 2, 1)
car6 = car(80, 70 + d2, t, 7, 2, 1)

advice(car5, car6, d2)


print('example 4')
d4 = 1
car7 = car(20, 70, t, 7, 2, 1)
car8 = car(20, 70 + d2, t, 7, 2, 1)

advice(car7, car8, d2)


