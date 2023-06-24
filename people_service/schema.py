from graphene import ObjectType, Schema


class Query(ObjectType):
    pass


schema = Schema(query=Query)
