from litestar import Controller, get, post, delete, put

# TODO: Wait for DTO
class TaskController(Controller):
    path = "/Task"
    
    @get()
    async def list_task(self):
        return {}