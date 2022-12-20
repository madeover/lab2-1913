#CSCI 1913 Lab02
#Author: Izra Bereket

import math


def steepest_angle(mountain_range):
    '''Gets the angle in degrees'''
    max = 0
    for i in range(len(mountain_range)-1):
        dy = abs(mountain_range[i] - mountain_range[i+1])
        degrees = (math.degrees(math.atan2(dy, 1)))
        if degrees > max:
            max = degrees
    return max

def total_distance(heightslist):
    '''Distance between the mountain'''
    if len(heightslist) <= 1:
        return 0
    dist = 0
    for i in range(0,len(heightslist)-1):
        dist = dist + math.sqrt((heightslist[i] - heightslist[i + 1]) ** 2 + 1)
    return dist

def longest_sequential_climb(lc):
    '''The longest possible climb when going on the mountain'''
    if len(lc) <= 1:
        return 0
    else:
        start_distance = 0

    distance = 0
    for i in range(0, len(lc)-1):
        if lc[i] <= lc[i+1]:
            distance = distance + math.sqrt((lc[i] - lc[i + 1]) ** 2 + 1)
        else:
            if distance > start_distance:
                start_distance = distance
            distance = 0
    return start_distance

def num_of_peaks_and_valleys(pv):
    '''Shows the number of peaks and valleys when looking at the mountain'''
    if len(pv) <= 2:
        return (0,0)
    peak = 0
    valley = 0
    for i in range(1,len(pv)-1):
        if pv[i] > pv[i+1] and pv[i] > pv[i-1]:
            peak += 1
        elif pv[i] < pv[i+1] and pv[i] < pv[i-1]:
            valley += 1
    return (peak,valley)

def fill_valleys(a, b):
    
    '''Returns a list where all heights below a given minimum have been filled to the given minimum.'''
    update_filled = []
    for i in a:
        update_filled.append(i)
    for h in range(len(update_filled)):
        if update_filled[h] <= b:
            update_filled[h] = b
    return update_filled

def i_need_help(helper):
    
    '''To create a list that shows the highest and lowest peak in a mountain'''
    max_min = []
    for i in range(len(helper)):
        max_min.append(max(i))
        max_min.append(max(i))
    return max_min