from litestar import Controller, get, post, put, delete

class ConversationController(Controller):
    base_path = "/tasks"
    
    @get()
    async def get_conversation(self) -> None:
        pass
    
    @get(path="/{conversation_id:int}")
    async def get_converstaion_id(self) -> None:
        pass
    
    @put(path="/{conversation_id:int}")
    async def create_conversation(self) -> None:
        pass
    
    @post(path="/{conversation_id:int}")
    async def update_conversation(self) -> None:
        pass
    
    @delete(path="/{conversation_id:int}")
    async def delete_conversation(self) -> None:
        pass
    