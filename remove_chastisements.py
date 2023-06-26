from datacenter.models import Chastisement


def remove_chastisements(schoolkid):

    chestments = Chastisement.objects.filter(schoolkid=schoolkid)
    chestments.delete()