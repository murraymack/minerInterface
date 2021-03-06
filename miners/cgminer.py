from API.cgminer import CGMinerAPI
from miners import BaseMiner


class CGMiner(BaseMiner):
    def __init__(self, ip: str) -> None:
        api = CGMinerAPI(ip)
        super().__init__(ip, api)

    def __repr__(self) -> str:
        return f"CGMiner: {str(self.ip)}"

    async def send_config(self):
        return None
