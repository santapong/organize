from litestar import Controller, get ,post, put, delete
from litestar.contrib.opentelemetry import OpenTelemetryConfig, OpenTelemetryPlugin

# TODO: Learning Opentelemetry.
from pydantic import BaseModel

class Metric(BaseModel):
    pass


class HealthController(Controller):
    base_path = "/healthcheck"

    @get()
    async def service_healthcheck(self) -> None:
        pass
    
    
    @get(path="/{agent_id:int}")
    async def agent_healthcheck(self) -> None:
        pass
    
class MetricController(Controller):
    
    raise NotImplementedError("Not implement yet.")


    