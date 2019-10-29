from event import Event

class System:
    def __init__(self):
        self._printers = dict()
        print('Iniciando sistema')

    def attach(self, printer, callback = None):
        if callback == None:
            callback = getattr(printer, 'event_handler')

        print('Attaching printer {}-{}'.format(printer.get_code(), printer.get_name()))
        
        self._printers[printer] = callback

    def detach(self, printer):
        print('Detaching printer {}-{}'.format(printer.get_code(), printer.get_name()))
        del self._printers[printer]

    def pause_printers(self, but = None):
        for printer, callback in self._printers.items():
            if (printer in but):
                continue

            callback(Event.PAUSE)

    def start_print(self):
        print('Starting prints')
        while (True):
            jobs = []
            for printer, callback in self._printers.items():
                self.pause_printers(but = [printer])
                remaining_jobs = callback(Event.PRINT)
                jobs.append(remaining_jobs)

            if (sum(jobs) == 0):
                print('Jobs Queue empty')
                break

        print('Exiting')
