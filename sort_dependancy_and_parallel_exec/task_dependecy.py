#!/usr/bin/python
import threading, argparse, time
 
'''
Created on Mar 31, 2014

@author: swapnesh
'''

def sort_by_dependencies(graph_unsorted, node):
    
    # This is the list we'll return, Initialized with the node
    graph_sorted = [node]
   
    # Convert the unsorted graph into a hash table. This will give
    # constant-time lookup for checking if edges are dependent, and
    # for removing nodes from the unsorted graph.
   
    tasks_hash = dict(graph_unsorted)
    
    # initialize the stack with all the dependencies of the node. 
    Stack=tasks_hash[node]

    # we will pop all the elements in the stack on to sorted_graph until stack is empty
    #while putting in sorted_graph making sure that same task is not repeated
    while Stack:
        node=Stack.pop()
        if graph_sorted.count(node) == 0:   #make sure the task is not already present
            graph_sorted.append(node)       
            Stack=Stack+tasks_hash[node]    #Copy over all the dependencies of the popped node
        
    # while accessing the graph_sorted we must make sure that it's accessed as a stack data structure using pop 
    # and we'll get the sequence of executing the tasks
    return graph_sorted


# worker thread class
class myThread (threading.Thread):
    def __init__(self, threadID, lock,condition):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.task=0                 # task the thread is executing at the moment 0 means no task
        self.condition=condition    #conditional variable for a given thread
        
    def run(self):
        global tasks_hash
        global taskscondition
        
        print "Starting " + self.name
        while 1:
            self.condition.acquire()    #acquire lock over it's conditional variable, this variable is shared 
                                        #with the main thread as the self.task is shared also it used to notify worker
                                        #threads that there is work to do.  
            self.condition.wait()       #wait at the start
            print "thread %s is running task %s" %(self.threadID,self.task)
            taskscondition.acquire()    #lock is necessary as the main thread reads tasks and task_hash data structures
            
            # after executing the task removes the entry of the task from hash tables so that the dependency is now removed
            #this for and if loop structure checks of the task that was executed by the thread is present in any other task's
            # dependency list in other words, it tries to remove the dependency of the current task as the task has now completed. 
            for task in tasks_hash:
                if self.task in tasks_hash[task]:
                    tasks_hash[task].remove(self.task)
            taskscondition.notify()       #If main thread is waiting then it will be notified that the one of the worker has 
                                            #finished the job and is now free     
            taskscondition.release()
            self.task=0                   #mark self has free for assigning new work
            self.condition.release()    
        
        print "Exiting %s" %(self.threadID)
        

tasks_hash=[]           #hash table for graph lookup
taskscondition=threading.Condition() #conditional variable for tasks data structure which holds the sequence of execution  

def main():
    global tasks_hash
    global taskscondition
    parser = argparse.ArgumentParser(description='parser')
    # accept from user no. of threads to have default is 2
    parser.add_argument("--threads",'-s',help="Enter the number of threads",default=2)
    args = parser.parse_args()
    
    threads=[]    
        # Create new threads
    for j in range(0,args.threads):
        thread = myThread(j,threading.Lock(), threading.Condition())
        thread.start()
        threads.append(thread)
    
    #graph with given set of dependencies
    graph_unsorted = [(2, []), (5, [11]),(11, [2, 9, 10]),(7, [11, 8]),(9, []),(10, []),(8, [9]),(3, [10, 2, 8]), (1,[2])]
    
   
    tasks=sort_by_dependencies(graph_unsorted, 3)   #find sequence of task execution
    tasks_hash=dict(graph_unsorted)                     #create the hash table of the graph
        #lock hash table as it is shared with worker threads
    print "correct order of executing task %s is " %(3)
    print "%s\n"%(tasks[::-1])     
    
    taskscondition.acquire()
     
    while tasks:
        task=tasks.pop()    #pop the element form the stack, to get them in correct sequence 
        append=1
        if not tasks_hash[task]:    #if no dependency, execute
            
            for j in range(0,args.threads):  # try and find a free thread and notify it.             
                if not threads[j].task:
                    threads[j].condition.acquire()
                    threads[j].task=task
                    threads[j].condition.notify()
                    threads[j].condition.release()
                    append=0
                    break    
        if append:                          #if thread is not free or if no independent task is present 
            tasks.append(task)              #push element back on the stack                            
            taskscondition.wait()           #wait until one of the worker's wakes main thread up.
    
    time.sleep(1)                               #wait for the threads to finish then exit the program
    for j in range(0,args.threads):  
        if threads[j].isAlive():
            try:
                threads[j]._Thread__stop()
            except:
                print(str(threads[j].threadID) + ' could not be terminated')
                      
if __name__ == '__main__':
    main()