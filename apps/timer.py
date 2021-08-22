import logging, time


logger = logging.getLogger(__name__)


class WorkPeriodTimerError(Exception):
    """
    A custom exception used to report errors in use of Timer class.
    """


class WorkPeriodTimer():
    """
    Times workperiods.
    """

    time_start = None
    time_end = None

    def start(self):
        if self.time_start is not None:
            raise WorkPeriodTimerError("A workperiod was already started." +
                " Stop the current period before starting another.")
        self.time_start = time.time()
        logger.info("Started a job at %H:%M:%S", self.time_start)
    
    def stop(self):
        if self.time_start is None:
            raise WorkPeriodTimerError("Can't stop a workperiod that wasn't" +
                " started first. Start a new period before stopping it.")
        self.time_end = time.time()
        logger.info("Stopped a job at %H:%M:%S", self.time_end)
    
    def time(self):
        if self.time_start is None or self.time_end is None:
            raise WorkPeriodTimerError("Not enough data available to report" +
                " the time spent. Did you start and stop a work period ?")
        elapsed_time = self.time_end - self.time_start
        logger.info("Worked for %H:%M:%S on a job", elapsed_time)
        return elapsed_time

