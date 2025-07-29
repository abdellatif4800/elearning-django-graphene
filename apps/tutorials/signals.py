from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.utils import timezone

from .models import Tutorial, Tutorial_Unit


def _recalc_units_count(tutorial_id: int):
    count = Tutorial_Unit.objects.filter(tutorial_id=tutorial_id).count()
    Tutorial.objects.filter(pk=tutorial_id).update(
        untis_count=count,
    )


@receiver(post_save, sender=Tutorial_Unit)
def tutorial_unit_saved(sender, instance, **kwargs):
    _recalc_units_count(instance.tutorial_id)


@receiver(post_delete, sender=Tutorial_Unit)
def tutorial_unit_deleted(sender, instance, **kwargs):
    _recalc_units_count(instance.tutorial_id)
