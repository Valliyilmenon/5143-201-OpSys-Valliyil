from sim_components import *

# === Class: StatusList===


class StatusList(object):
    """ The StatusList object lets processes keep track of their own status.
    
    - **add** (job, start_time, com_time):
        -Adds a job to the dictionary. For each entry the process_id is the key, and the value
        is another dictionary, with the following values: arrival_time, run_time, start_time, com_time.
        start_time, com_time default values are None since they aren't relevant in some cases
        
    - **remove** (process_id)
        -Removes a job from the dictionary or prints an error message if the job isn' in the dicitonary.    
    """

    def __init__(self):
        self.list = []
        self.system_clock = Clock()

    def add(self, job, start_time=None, com_time=None):
        if start_time:
            job.start_time = start_time
        if com_time:
            job.com_time = com_time

        self.list.append(job)

    def remove(self):
        if len(self.list) == 0:
            return None
        else:
            del self.list[0]

    def empty(self):
        return len(self.list) == 0

    def first(self):
        if len(self.list) == 0:
            return None
        else:
            return self.list[0]

###################################################################################################


class SystemStatusList(object):


    __shared_state = {}
    def __init__(self):
        self.__dict__ = self.__shared_state
        if len(self.__shared_state.keys()) == 0:
            self.job_scheduling_queue_list = StatusList()
            self.ready_queue_list_lvl1 = StatusList()
            self.ready_queue_list_lvl2 = StatusList()
            self.finished_list = StatusList()
            self.io_wait_queue = StatusList()




