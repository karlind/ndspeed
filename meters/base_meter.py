class BaseMeter:
    def __init__(self):
        pass

    def start(self):
        raise NotImplemented

    def end(self):
        raise NotImplemented

    def get_meter_table(self):
        raise NotImplemented