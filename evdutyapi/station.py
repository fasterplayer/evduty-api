from evdutyapi import Terminal, ChargingStatus


class Station:
    def __init__(self,
                 id: str,
                 name: str,
                 status: ChargingStatus,
                 terminals: list[Terminal],
                 desc: str,
                 ownerId: str,
                 imageUrl: str,
                 thumbUrl: str,
                 latitude: float,
                 longitude: float,
                 isRoot: bool,
                 isOwner: bool,
                 isPartialOwner: bool):
        self.id = id
        self.name = name
        self.status = status
        self.terminals = terminals
        self.desc = desc
        self.ownerId = ownerId
        self.imageUrl = imageUrl
        self.thumbUrl = thumbUrl
        self.latitude = latitude
        self.longitude = longitude
        self.isRoot = isRoot
        self.isOwner = isOwner
        self.isPartialOwner = isPartialOwner
