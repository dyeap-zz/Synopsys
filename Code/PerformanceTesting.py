# Below is performance testing for three different implementation of solution
# The code generates a graph of code speed with respect to increasing sample input size

import time
import random
import matplotlib.pyplot as plt
from FindNeighbors import easily_understood,fewest_lines,fewest_memory

# parameters to set for graph
min_input_size = 1
max_intput_size = 10000
interval_size = 1000
rep = 100

# genereates a list of random integers
def gen_nums(size):
    res = []
    for _ in range(size):
        res.append(random.randint(-10000,10000))
    return res

# times the function passed for x number of repetitions
def time_function(nums,func,rep):
    tot = 0
    for _ in range(rep):
        start = time.time()
        func(nums[:])
        end = time.time()
        tot += (end-start)
    return tot/rep

# main function to time all functions
def time_all_implementations(min_size,max_size,interval_size,rep):
    sizes,times_a,times_b,times_c = [] ,[] , [], []

    for size in range(min_size,max_size,interval_size+1):
        # generate random num based on input size
        sizes.append(size)
        nums = gen_nums(size)

        # time all different implementation
        times_a.append(time_function(nums, easily_understood,rep))
        times_b.append(time_function(nums, fewest_lines,rep))
        times_c.append(time_function(nums, fewest_memory,rep))

    # plot graph
    ax = plt.gca()
    ax.scatter(sizes, times_a, color="b",label = "A. Easily Understood")
    ax.scatter(sizes,times_b,color = "r",label = "B. Fewest Lines")
    ax.scatter(sizes,times_c,color = "g",label = "C. Lowest Memory")

    # set plot labels,limits, and title
    plt.xlabel("Size of input (list)")
    plt.ylabel("Time (sec.)")
    plt.xlim(0,max_size)
    plt.ylim(0)
    plt.title("Performance plot of three different code implementations\n"
              " with list size interval = " + str(interval_size) +
              " and each input repeated " + str(rep) + "x.\n")
    plt.legend()
    plt.show()

time_all_implementations(min_input_size,max_intput_size,interval_size,rep)