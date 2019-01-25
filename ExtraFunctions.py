import numpy as np

# State modelized as input vector
def dict_to_state(dic):
    state = np.zeros((1,10))
    state[0,0] = (float(dic['%_free_RAM']) - 0.4)/(0.8-0.4)
    # state[0,1] = 0 #(float(dic['storage_capacity'])-10.0)/30.0

    if dic['storage_capacity'] == 10:
        state[0,1] = 0
    else:
        state[0,1] = 1

    state[0,2] = (float(dic['%_read_load'])-0.5)/(1.0-0.5)
    state[0,3] = (float(dic['number_of_VMs']) - 1.0) / (20.0-1.0)

    if dic['number_of_CPUs'] == 2:
        state[0,4] = 0
    else:
        state[0,4] = 1

    if dic['RAM_size'] == 1024:
        state[0,5] = 0
    else:
        state[0,5] = 1
    
    state[0,6] = (float(dic['I/O_per_sec'])-1000.0)/(1800.0-1000.0)
    state[0,7] = (float(dic['%_CPU_usage']) - 0.6)/(0.9-0.6)
    state[0,8] = float(dic['total_load'])/100.0
    state[0,9] = dic['total_latency']
    return state


def dict_to_state_tmp(dic):
    state = np.zeros((1,3))
    state[0,0] = (float(dic['%_read_load'])-0.5)/(1.0-0.5)
    state[0,1] = (float(dic['number_of_VMs']) - 1.0) / (20.0-1.0)
    state[0,2] = (dic['total_load'])/100
    return state

def add_to_log(state_dic, state1_dic, action, allQ):
   log_file.write(state, " ", state1, " ", action, " ", allQ)    
