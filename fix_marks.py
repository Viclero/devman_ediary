from datacenter.models import Mark


def fix_marks(schoolkid):

    bad_marks = Mark.objects.filter(schoolkid=schoolkid, points__in=[2, 3])
    id_fix = [id for id in bad_marks]   
    for fix_point in bad_marks:
    #for i in range(bad_marks.count()-1):
    #    fix_point = Mark.objects.get(id=id_fix[i].id)
        fix_point.points = 5
        fix_point.save()