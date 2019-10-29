from event import Event
from time import sleep

STATUS = [
    'En Reposo',
    'Pausada',
    'Imprimiendo'
]

class Printer:
    def __init__(self, code, name):
        self._code = code
        self._name = name
        self._status = STATUS[0]
        self._queue = list()

        print('Created printer {}-{}'.format(code, name))

    def get_code(self):
        return self._code

    def get_name(self):
        return self._name

    def get_job_queue(self):
        return len(self._queue)

    def pause(self):
        if (self._status == STATUS[2]):
            self._status = STATUS[1]

        return self._status == STATUS[1]

    def proceed(self):
        if (self._status == STATUS[1]):
            self._status = STATUS[2]
        
        return self.printing()
    
    def printing(self):
        return self._status == STATUS[2]

    def get_job_from_queue(self):
        if (len(self._queue) > 0):
            job = self._queue[0]
            self._queue.remove(job)

            return job
        
        return None

    def add_job(self, job):
        print('{}-{}: Adding {} to the queue'.format(self._code, self._name, job))
        self._queue.append(job)

    def print_job(self, job):
        self._status = STATUS[2]
        print('{}-{} printing: {}'.format(self._code, self._name, job))
        for i in range(1, job.pages + 1):
            print('\tPrinting page {}: '.format(i), end='')
            sleep(1)
            print('done')
        self._status = STATUS[0]

        return self.get_job_queue()

    def print_next(self):
        job = self.get_job_from_queue()
        
        if (job != None):
            return self.print_job(job)

        return 0

    def event_handler(self, event):
        if (event == Event.PAUSE):
            return self.pause()
        elif (event == Event.PROCEED):
            return self.proceed()
        elif (event == Event.PRINT):
            return self.print_next()