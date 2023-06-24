from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.
class Person(models.Model):
    name = models.TextField()
    email = models.EmailField()


class Address(models.Model):
    class StateEnum(models.TextChoices):
        ACT = "ACT", _("Australian Capital Territory")
        NSW = "NSW", _("New South Wales")
        NT = "NT", _("Northern Territory")
        QLD = "QLD", _("Queensland")
        SA = "SA", _("South Australia")
        TAS = "TAS", _("Tasmania")
        VIC = "VIC", _("Victoria")
        WA = "WA", _("Western Australia")

    number = models.IntegerField()
    street = models.TextField()
    city = models.TextField()
    state = models.CharField(max_length=3, choices=StateEnum.choices, default=StateEnum.TAS)
    person = models.ForeignKey('people.Person', related_name='address', on_delete=models.CASCADE)

