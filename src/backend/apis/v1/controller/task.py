from litestar import Controller, get, post, put, delete

class TaskController(Controller):
    base_path = "/tasks"
    
    @get()
    async def get_tasks(self) -> None:
        pass
    
    @get(path="/{task_id:int}")
    async def get_tasks_id(self) -> None:
        pass
    
    @put(path="/{task_id:int}")
    async def create_tasks(self) -> None:
        pass
    
    @post(path="/{task_id:int}")
    async def update_task(self) -> None:
        pass
    
    @delete(path="/{task_id:int}")
    async def delete_task(self) -> None:
        pass
    