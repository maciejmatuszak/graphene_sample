import graphene
import graphql
from graphene_django import DjangoObjectType

from people.models import Person, Address


class PersonType(DjangoObjectType):
    # reusing db model
    class Meta:
        model = Person
        fields = ('id', 'name', 'email', 'address')


class AddressType(DjangoObjectType):
    # reusing db model
    class Meta:
        model = Address
        fields = ('id', 'number', 'street', 'city', 'state', 'person')


StateEnum = graphene.Enum.from_enum(Address.StateEnum)


class AddressInput(graphene.InputObjectType):
    number = graphene.Int(required=True)
    street = graphene.String(required=True)
    city = graphene.String(required=True)
    state = StateEnum(required=True)


class PersonInput(graphene.InputObjectType):
    name = graphene.String(required=True)
    email = graphene.String()
    address = graphene.Field(AddressInput)


class CreatePerson(graphene.Mutation):
    person = graphene.Field(PersonType)

    # mutation arguments
    class Arguments:
        person_data = PersonInput(required=True)

    def mutate(self, info: graphql.GraphQLResolveInfo, person_data: PersonInput):
        # Seems Person.objects.create is not capable of taking nested XxxxInput object
        # we have to extract address and create it separately
        # alternatively Person and Address object could be created separately.

        person_data_dict = dict(person_data)
        # remove address to separate object
        address = person_data_dict.pop(Person.address.field.name)

        # if address exists create db object and put it bask to dictionary
        if address:
            address = Address.objects.create(**address)
            person_data_dict[Person.address.field.name] = address

        # create person db object
        person = Person.objects.create(**person_data_dict)

        # return created object using graphene model
        return CreatePerson(person=person)


class PersonMutation(graphene.ObjectType):
    create_person = CreatePerson.Field()


class PersonQuery(graphene.ObjectType):
    people = graphene.List(PersonType)

    def resolve_people(self, info: graphql.GraphQLResolveInfo, **kwargs):
        return Person.objects.all()
