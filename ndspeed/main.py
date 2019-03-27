from meters.net_meter import NetMeter
from scheduler import Scheduler


def main():
    scheduler = Scheduler(interval=1)

    net_meter = NetMeter(nic=['enp3s0'])
    scheduler.add_meter(net_meter)

    scheduler.loop()

main()