import time
from meters.base_meter import BaseMeter


class Scheduler:
    def __init__(self, meters=[], interval=1):
        """
        Args:
            meters(tuple or list): list of meters to register
            interval(float): seconds to flush
        """
        self.meters = meters.copy()
        self.interval = interval

    def add_meter(self, meter):
        assert isinstance(meter, BaseMeter)
        self.meters.append(meter)

    def remove_meter(self, meter_index):
        return self.meters.pop(meter_index)

    def clear_screen(self):
        print('\033[H\033[J')

    def _wait(self):
        time.sleep(self.interval)

    def _start(self):
        for meter in self.meters:
            meter.start()

    def _end(self):
        for meter in self.meters:
            meter.end()

    def _print_summary(self):
        self.clear_screen()

        for meter in self.meters:
            meter_table = meter.get_meter_table()
            print(meter_table)

    def loop(self):
        while True:
            try:
                self._start()
                self._wait()
                self._end()
                self._print_summary()
            except KeyboardInterrupt:
                exit(0)