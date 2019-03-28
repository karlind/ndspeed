import time
import psutil
from terminaltables import AsciiTable
from meters.base_meter import BaseMeter


class NetMeter(BaseMeter):
    def __init__(self, name=None, nic_list=[]):
        super().__init__()
        self.meter_name = name if name else self.__class__.__name__

        all_nic_list = self.get_all_nic()
        if nic_list is None or len(nic_list)==0:
            self.nic_list = all_nic_list
        else:
            self.nic_list = []
            for net_name in nic_list:
                assert net_name in all_nic_list
                self.nic_list.append(net_name)

    @staticmethod
    def get_all_nic():
        counter = psutil.net_io_counters(pernic=True)
        nic_list = sorted(counter.keys())
        return nic_list

    def start(self):
        self.start_time = time.time()
        self.counter1 = psutil.net_io_counters(pernic=True)

    def end(self):
        self.counter2 = psutil.net_io_counters(pernic=True)
        self.end_time = time.time()

    def get_meter_table(self):
        result_dict = self._get_meter_result()
        table_data = [['NIC', 'Download', 'Upload']]

        for net_name in self.nic_list:
            net_info = result_dict[net_name]
            download_speed = f'{net_info["formated_recv"]:6.1f} {net_info["formated_recv_unit"]:2}/s'
            upload_speed = f'{net_info["formated_sent"]:6.1f} {net_info["formated_sent_unit"]:2}/s'
            row = [net_name, download_speed, upload_speed]
            table_data.append(row)
        table = AsciiTable(table_data, title=self.meter_name)
        table.justify_columns[1] = 'center'
        table.justify_columns[2] = 'center'
        return table.table

    def _get_meter_result(self):
        time_delta = self.end_time - self.start_time
        net_speed_dict = self._calc_speed(self.counter1, self.counter2, time_delta=time_delta)
        result_dict = self._format_speed(net_speed_dict)
        return result_dict

    def _calc_speed(self, counter1, counter2, time_delta):
        net_speed = dict()

        for net_name in counter1.keys():
            info1 = counter1[net_name]
            info2 = counter2[net_name]
            recv_delta = abs(info2.bytes_recv - info1.bytes_recv)
            recv_speed = recv_delta / time_delta
            sent_delta = abs(info2.bytes_sent - info1.bytes_sent)
            sent_speed = sent_delta / time_delta
            net_speed[net_name] = dict(sent_delta=sent_delta, recv_delta=recv_delta,
                                       sent_speed=sent_speed, recv_speed=recv_speed,
                                       time_delta=time_delta)
        return net_speed

    def _format_byte(self, n_bytes):
        n = n_bytes
        if n < 1024:  # byte
            return n, 'B'
        if n < 1024 * 1024:  # KB
            return n / 1024, 'KB'
        if n < 1024 * 1024 * 1024:  # MB
            return n / 1024 / 1024, 'MB'

    def _format_speed(self, speed_dict):
        speed_dict = speed_dict.copy()
        for net_name, speed_info in speed_dict.items():
            recv_speed = speed_dict[net_name]['recv_speed']
            sent_speed = speed_dict[net_name]['sent_speed']

            speed_info['formated_recv'], speed_info['formated_recv_unit'] = self._format_byte(recv_speed)
            speed_info['formated_sent'], speed_info['formated_sent_unit'] = self._format_byte(sent_speed)
        return speed_dict