import numpy as np
import random
import tensorflow as tf
import csv
from ReadLoad import *
import matplotlib.pyplot as plt
from ExtraFunctions import *

input_size = 10 # variables that describe a state
batch_size = 360 
pre_train_steps = 360 
do_experience_replay = True 
method = "DoubleDQN" # available: SimpleDQN, FullDQN, DoubleDQN 
logging = False

# training & testing steps
num_training_steps = 5000 
num_annealing_steps = 5000
annealing = num_annealing_steps/10
num_testing_steps = 2000 


def weight_variable(shape,name="weight"):
    """Create a weight variable with appropriate initialization."""
    initial = tf.truncated_normal(shape, stddev=0.1)
    return tf.Variable(initial,name=name)

def bias_variable(shape,name="bias"):
    """Create a bias variable with appropriate initialization."""
    initial = tf.constant(0.1, shape=shape)
    return tf.Variable(initial,name=name)


class QNetwork(object):
    """docstring for QNetwork"""
    def __init__(self)
    
        if method == "SimpleDQN":
           

        elif method == "DoubleDQN" or method == "FullDQN":
            
# copy of first network to second 
def updateTargetGraph(tfVars,tau):
    

def updateTarget(op_holder,sess):
    




# memory
class Memory():
    def __init__(self, buffer_size = 500):
        self.buffer = []
        self.buffer_size = buffer_size
        self.current_buffer_size = 0

    #add to memory
    def add(self,state,action,reward,new_state, allQ):
        if self.current_buffer_size >= self.buffer_size:
            self.buffer.insert(0,(state, action, reward, new_state, allQ))
            del self.buffer[-1]
        else:
            self.buffer.insert(0,(state, action, reward, new_state, allQ))
            self.current_buffer_size += 1

    #sample apo ti mnimi 
    def sample(self,size):
        return random.sample(self.buffer,size)



def main():
    tf.reset_default_graph()

    if method == "DoubleDQN" or method=="FullDQN":
        mainQ = QNetwork()
        targetQNet = QNetwork()
        trainables = tf.trainable_variables()
        tau = 0.001
        targetOps = updateTargetGraph(trainables,tau)
    else:
        mainQ = QNetwork()

    init = tf.initialize_all_variables()

    



    saver = tf.train.Saver()

    # Set learning parameters
    y = 0.99 # learning rate
    update_freq = 1 #How often to perform a training step.
    e = 1.0
    #num_episodes = 2000
    #create lists to contain total rewards and steps per episode
    jList = []
    rList = []


    path = "models"

    vmList = []
    loadList = []
    # load_model = False # if we have a previous trained model
    experience_buffer = Memory()
    total_reward = 0

    with tf.Session() as sess:
        sess.run(init)
        for i in range(1):
            rAll = 0
            d = False
            j = 0

            # get initial state
            scenario = ReadLoadScenario(num_training_steps,num_testing_steps)
            state = dict_to_state(scenario.get_current_measurements())
        
            #The Q-Network
            while j < num_training_steps+num_testing_steps: 
               

                if j < num_training_steps:
                    if j<=pre_train_steps:
                    else:
                        if method=="FullDQN" or method=="DoubleDQN":
                            
                                if method == "DoubleDQN":
                                    targetQ = reard_batch + y * Q2[range(batch_size),Q1] * end_multiplier


                                elif method == "FullDQN":

                               
                        elif method=="SimpleDQN":
                           
                state=new_state

                if j%annealing == 0 and e!=0: 
                    e = e-0.1

                jList.append(j)
                rList.append(reward)

        # saver.save(sess,path+'/model.cptk', global_step=j-num_testing_steps)

        # return total_reward


        print "Total Reward: ", total_reward

        fig, ax1 = plt.subplots()
        t = np.arange(1, num_testing_steps+2, 1)
        ax1.plot(t, vmList, 'b.')
        ax1.set_xlabel('time (s)')
        # Make the y-axis label, ticks and tick labels match the line color.
        ax1.set_ylabel('vms', color='b')
        ax1.tick_params('y', colors='b')

        ax2 = ax1.twinx()
        ax2.plot(t, loadList, 'r')
        ax2.set_ylabel('load', color='r')
        ax2.tick_params('y', colors='r')

        ax1.text(1.05, -0.13, "total reward= "+str(int(total_reward)),
        verticalalignment='bottom', horizontalalignment='right',
        transform=ax1.transAxes,
        color='blue', fontsize=15)

        fig.tight_layout()
        plt.show()
        return total_reward

if __name__ == '__main__':
    x=main()
    print x
