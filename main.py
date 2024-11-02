import uvicorn
import strawberry
from fastapi import FastAPI
from contextlib import asynccontextmanager
from config import db
from strawberry.fastapi import GraphQLRouter

from Graphql.query import Query
from Graphql.mutation import Mutation


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup logic
    await db.create_all()
    yield
    # Shutdown logic
    await db.close()

def init_app():
    apps = FastAPI(
        title="Lorem Ipsum",
        description="Fast API",
        version="1.0.0",
        lifespan=lifespan
    )

    @apps.get('/')
    def home():
        return "Welcome to home!"

    # add graphql endpoint
    schema = strawberry.Schema(query=Query, mutation=Mutation)
    graphql_app = GraphQLRouter(schema)

    apps.include_router(graphql_app, prefix='/graphql')
    
    return apps


app = init_app()


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)