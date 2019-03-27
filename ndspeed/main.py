import os
import sys


app_home_dir = os.path.dirname(os.path.realpath(__file__))
sys.path.append(app_home_dir)


from meters.net_meter import NetMeter
from scheduler import Scheduler


def main():
    scheduler = Scheduler(interval=1)

    net_meter = NetMeter(nic=['enp3s0'])
    scheduler.add_meter(net_meter)

    scheduler.loop()


if __name__=='__main__':
    main()