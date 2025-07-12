from backend.apis.v1.controller import AgentController, TaskController, ConversationController, MetricController, HealthController
from litestar import Router

api_v1_router = Router(
    path='/v1',
    route_handlers=[
        AgentController, 
        TaskController,
        ConversationController,
        HealthController,
        ])
