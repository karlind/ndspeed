import os
import sys
import argparse


app_home_dir = os.path.dirname(os.path.realpath(__file__))
sys.path.append(app_home_dir)


from meters.net_meter import NetMeter
from scheduler import Scheduler


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--interval', help='interval second to flush', default=1.0, type=float)
    parser.add_argument('-c', '--card', action='append', help='network card names to display', choices=NetMeter.get_all_nic())
    args = parser.parse_args()
    return args


def main():
    args = parse_args()
    scheduler = Scheduler(interval=args.interval)

    net_meter = NetMeter(nic_list=args.card if args.card else [])
    scheduler.add_meter(net_meter)

    scheduler.loop()


if __name__=='__main__':
    main()