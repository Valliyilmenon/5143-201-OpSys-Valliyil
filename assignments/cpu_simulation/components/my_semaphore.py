
from sim_components import *

# === Class: Semaphore===


class MySemaphore(object):
    """A class to simulate a semaphore.
    - **Methods**:
        - acquire() : Attempt to acquire copy of semaphore
        - release() : Relinquish semaphore

    - **Attributes**:
        - value     : Current value of semaphore
    """
    def __init__(self):
        self.acquired_dict = {}
        self.value = 1
        self.waiting_queue = Fifo()

    def acquire(self, job):
        status = None
        if self.value > 0:  # There are available copies
            self.acquired_dict[job.process_id] = job
            status = True
        else:
            self.waiting_queue.add(job)

        self.value -= 1
        return status

    def release(self, job_id):
        """
        
        :param job_id: 
        :return: process_id to be moved to the appropriate waiting_queue or 'None' if irrelevant 
        """
        status = None
        self.value += 1
        if job_id in self.acquired_dict:
            del self.acquired_dict[job_id]
        if not self.waiting_queue.empty():  # If there are jobs waiting for that semaphore
            self.acquired_dict[self.waiting_queue.first().process_id] = self.waiting_queue.first()
            status = self.waiting_queue.first()
            self.waiting_queue.remove()
        return status


        # if self.waiting_queue.empty():  # No jobs in waiting queue for that semaphore
        #     self.value += 1  # Increment number of available slots
        # else:  # Waiting queue is not empty
        #     self.acquired_dict[self.waiting_queue.first().process_id] = self.waiting_queue.first()
        #     ## MOVE THE JOB TO THE APPROPRIATE WAITING QUEUE
        #     status = self.waiting_queue.first()
        # return status



# === Class: MySemaphorePool===

class MySemaphorePool(object):
    __shared_state = {}

    def __init__(self, num_sems=5):
        self.__dict__ = self.__shared_state

        if len(self.__shared_state.keys()) == 0:
            self.sem_dict = {}
            # self.sem_owner = []
            for i in range(num_sems):
                self.sem_dict[i] = MySemaphore()
                # self.sem_owner.append(None)

    def acquire(self, sem_num, job):
        status = None
        sem_num = int(sem_num)
        # if self.sem_dict[sem_num].acquire(job) is None:  # No available semaphore
        #     self.sem_dict[sem_num].waiting_queue.add(job)  # job added to waiting queue
        # else:  # semaphore acquired successfully
        #     status = True
        # return status

        if self.sem_dict[sem_num].acquire(job):
            status = True
        return status

    def release(self, process_id, sem_num=None):
        # sem = None
        job_to_move = None
        if sem_num is None:  # semaphore released because a job was terminated and removed from the cpu
            for i in self.sem_dict:
                if process_id in self.sem_dict[i].acquired_dict:
                    self.sem_dict[i].release(process_id)

        else:  # semaphore released because of external input
            job_to_move = self.sem_dict[int(sem_num)].release(process_id)
        return job_to_move  # A job from the semaphore waiting queue has acquired the semaphore




