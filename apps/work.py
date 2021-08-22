from .timer import WorkPeriodTimer
from functools import reduce
from operator import add
from sqlalchemy.orm import relationship

from .base import BaseModel

class WorkPeriod(BaseModel):

    __tablename__ = "work_period"

    timer = WorkPeriodTimer()
    times = list()
    issue = None

    def start(self):
        self.timer.start()
    
    def pause(self):
        self.timer.stop()
        self.times.append(self.timer.time())
        self.timer = WorkPeriodTimer()
    
    def stop(self):
        self.pause()
    
    def time_spent(self):
        duration = 0
        return reduce(add, self.times)


