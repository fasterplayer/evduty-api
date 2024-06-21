from evdutyapi import ChargingSession, ChargingStatus, NetworkInfo
from evdutyapi.connector import Connector


class Terminal:
    def __init__(self,
    id: str,
    name: str,
    status: ChargingStatus,
    chargeBoxIdentity: str,
    firmwareVersion: str,
    session: ChargingSession,
    stationId: str,
    ownerId: str,
    connectors: list[Connector],
    type: str,
    level: int,
    amperage: int,
    voltage: int,
    accessMode: str,
    access: str,
    costLocal: float,
    isRoot: bool,
    isOwner: bool,
    network_info: NetworkInfo = None
    ):
        self.id = id
        self.name = name
        self.status = status
        self.chargeBoxIdentity = chargeBoxIdentity
        self.firmwareVersion = firmwareVersion
        self.session = session
        self.network_info = network_info
        self.stationId = stationId
        self.ownerId = ownerId
        self.connectors = connectors
        self.type = type
        self.leve = level
        self.amperage = amperage
        self.voltage = voltage
        self.accessMode = accessMode
        self.access = access
        self.costLocal = costLocal
        self.isRoot = isRoot
        self.isOwner = isOwner