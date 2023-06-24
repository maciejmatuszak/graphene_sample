import graphene
import graphql
from graphene_django import DjangoObjectType

from people.models import Person, Address


class PersonType(DjangoObjectType):
    # reusing db model
    class Meta:
        model = Person


class AddressType(DjangoObjectType):
    # reusing db model
    class Meta:
        model = Address


class CreatePerson(graphene.Mutation):
    id = graphene.BigInt()
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


StateEnum = graphene.Enum.from_enum(Address.StateEnum)


class CreateAddress(graphene.Mutation):
    id = graphene.BigInt()
    number = graphene.Int()
    street = graphene.String()
    city = graphene.String()
    state = StateEnum(required=True)

    # mutation arguments
    class Arguments:
        number = graphene.Int()
        street = graphene.String()
        city = graphene.String()
        state = StateEnum(required=True)

    def mutate(self, info: graphql.GraphQLResolveInfo, number: int, street: str, city: str, state: Address.StateEnum):
        address = Address(
            number=number,
            street=street,
            city=city,
            state=state
        )
        address.save()

        return CreateAddress(
            id=address.id,
            number=address.number,
            street=address.street,
            city=address.city,
            state=address.state
        )


class PersonMutation(graphene.ObjectType):
    create_person = CreatePerson.Field()
    create_address = CreateAddress.Field()


class PersonQuery(graphene.ObjectType):
    people = graphene.List(PersonType)
    addresses = graphene.List(AddressType)

    def resolve_people(self, info: graphql.GraphQLResolveInfo, **kwargs):
        return Person.objects.all()

    def resolve_addresses(self, info: graphql.GraphQLResolveInfo, **kwargs):
        return Address.objects.all()
