from django.db import models
from django.utils.translation import gettext_lazy as _


# Django database models

class Address(models.Model):
    class StateEnum(models.TextChoices):
        """ see https://docs.djangoproject.com/en/4.2/ref/models/fields/#enumeration-types """
        ACT = "ACT", _("Australian Capital Territory")
        NSW = "NSW", _("New South Wales")
        NT = "NT", _("Northern Territory")
        QLD = "QLD", _("Queensland")
        SA = "SA", _("South Australia")
        TAS = "TAS", _("Tasmania")
        VIC = "VIC", _("Victoria")
        WA = "WA", _("Western Australia")

        # we must have Iowa... for James :)
        IA = "IA", _("Iowa")

    # allow string as number i.e. "221/3"
    number = models.CharField(max_length=64, null=False, blank=False)
    street = models.CharField(max_length=128, null=False, blank=False)
    city = models.CharField(max_length=128, null=False, blank=False)
    state = models.CharField(max_length=3, choices=StateEnum.choices, default=StateEnum.TAS, null=False, blank=False)


class Person(models.Model):
    name = models.CharField(max_length=128, null=False, blank=False)
    email = models.EmailField(max_length=128)
    address = models.ForeignKey(Address, blank=True, null=True, related_name='person', on_delete=models.CASCADE)
