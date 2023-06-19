import strawberry
from fastapi import FastAPI
from mongoengine import connect
from strawberry.fastapi import GraphQLRouter

from query import Query
from mutations import Mutations


client = connect("graphql_query_operators", host="mongodb://db:27017/")


app = FastAPI()

schema = strawberry.Schema(
    query=Query,
    mutation=Mutations,
)


graphql_app = GraphQLRouter(schema)
app.include_router(graphql_app, prefix="/graphql")
