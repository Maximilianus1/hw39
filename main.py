import numpy as np
import random
products = np.array([random.randint(0,1000000) for i in range(100)])
print(products)
min= np.min(products)
max =  np.max(products)
mean = np.mean(products)
average = np.average(products)
median=np.median(products)
summ =np.sum(products)
pos_to_pos_range = np.ptp(products)
print("max: ",max,"min: ",min,"mean: ",mean,"average: ",average,"median: ",median,"sum: ",summ,"range: ",pos_to_pos_range)