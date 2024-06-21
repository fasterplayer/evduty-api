from typing import Dict, Any
from evdutyapi.api_response.terminal_response import TerminalResponse
from evdutyapi.charging_status import ChargingStatus


class SessionStartResponse:
    def __init__(self,
                id: str,
                connectingTimeRemaining: float,
                targetPercentage: int,
                targetDuration: int
                ):
        self.id = id
        self.connectingTimeRemaining = connectingTimeRemaining
        self.targetPercentage = targetPercentage
        self.targetDuration = targetDuration
