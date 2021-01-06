import random
from dataclasses import dataclass, field
from datetime import datetime
import uuid
import time


@dataclass
class TemperatureMetric:
    """ Represent a Temperature measurement"""
    value: float
    id: uuid.UUID = field(default_factory=uuid.uuid4)
    create_at: datetime = field(default_factory=datetime.now)


def push_temperature_factory(observer, scheduler):
    """ factory method for testing """
    for i in range(0, 100):
        temp = random.uniform(5.0, 20)
        observer.on_next(TemperatureMetric(temp))
        time.sleep(1.0)

    observer.on_completed()
