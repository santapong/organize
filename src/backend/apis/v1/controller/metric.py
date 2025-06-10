from litestar import Controller, Litestar, get, post, delete, patch

# TODO: Wait for DTO
class MetricController(Controller):
    """
    Using for get Insight Data.
    """
    path = "/Metric"
    
    @get()
    async def test(self) -> dict:
        return {"Hello": "Hello"}
    