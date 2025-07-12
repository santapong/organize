import typing as T
from litestar.controller import Controller
from litestar.handlers import get, put, delete, post, patch

class AgentController(Controller):
    base_path="/agents"
    
    @get()
    async def get_agents(self) -> None:
        pass
    
    @get(path="/{agent_id:int}")
    async def get_agent_id(self) -> None:
        pass
    
    @get(path="/{agent_id:int}/cards")
    async def get_cards(self) -> None:
        pass
    
    @get(path="/{agent_id:int}/cards/{card_id:int}")
    async def get_card_id(self) -> None:
        pass
    
    @put(path="/{agent_id:int}")
    async def create_agent(self) -> None:
        pass
    
    @put(path="/{agent_id:int}/cards")
    async def create_cards(self) -> None :
        pass
    
    @put(path="/{agent_id:int}/card/{card_id:int}")
    async def create_card_id(self) -> None :
        pass
    
    @post(path="/{agent_id:int}")
    async def update_agent(self) -> None :
        pass

    @post(path="/{agent_id:int}/cards")
    async def update_cards(self) -> None :
        pass
    
    @post(path="/{agent_id:int}/cards/{card_id:int}")
    async def update_cards_id(self) -> None :
        pass
    
    @delete(path="/{agent_id:int}")
    async def delete_agent(self) -> None :
        pass
    
    @delete(path="/{agent_id:int}/cards")
    async def delete_cards(self) -> None :
        pass
    
    @delete(path="/{agent_id:int}/cards/{card_id:int}")
    async def delete_card(self) -> None :
        pass