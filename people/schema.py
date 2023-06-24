import graphene
import graphql
from graphene_django import DjangoObjectType

from people.models import Person


class PersonType(DjangoObjectType):
    # reusing db model
    class Meta:
        model = Person


class CreatePerson(graphene.Mutation):
    id = graphene.Int()
    name = graphene.String()
    email = graphene.String()

    # mutation arguments
    class Arguments:
        name = graphene.String()
        email = graphene.String()

    def mutate(self, info: graphql.GraphQLResolveInfo, name: str, email: str):
        person = Person(
            name=name,
            email=email
        )
        person.save()

        return CreatePerson(
            id=person.id,
            name=person.name,
            email=person.email
        )


class PersonMutation(graphene.ObjectType):
    create_person = CreatePerson.Field()


class PersonQuery(graphene.ObjectType):
    people = graphene.List(PersonType)

    def resolve_people(self, info: graphql.GraphQLResolveInfo, **kwargs):
        return Person.objects.all()
