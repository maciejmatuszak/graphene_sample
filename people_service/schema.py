import graphene

import people.schema


class Query(people.schema.PersonQuery, graphene.ObjectType):
    pass


class Mutation(people.schema.PersonMutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
