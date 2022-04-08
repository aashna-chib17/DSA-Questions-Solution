# An avid hiker keeps meticulous records of their hikes. During the last hike that took exactly steps, 
# for every step it was noted if it was an uphill, , or a downhill, step. Hikes always start and end at sea level, 
# and each step up or down represents a unit change in altitude. We define the following terms:
# A mountain is a sequence of consecutive steps above sea level, starting with a step up from sea level and ending with a step down to sea level.
# A valley is a sequence of consecutive steps below sea level, starting with a step down from sea level and ending with a step up to sea level.
# Given the sequence of up and down steps during a hike, find and print the number of valleys and mountains walked through.

str = input()
mountain = 0
valley = 0
level = 0
for i in range(len(str)):
    if str[i] == "U":
        level+=1
    else:
        level-=1 
    if level == 0 and str[i]=='D':
        mountain += 1 
    elif level == 0 and str[i]=='U':
        valley += 1
print('Mountain',mountain)
print('Valley',valley) 


