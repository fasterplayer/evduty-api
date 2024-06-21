from evdutyapi.charging_status import ChargingStatus


class Connector:
    def __init__(self, id: int, name: str, status: ChargingStatus):
        self.id = id
        self.name = name
        self.status = status
