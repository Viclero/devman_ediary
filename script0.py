
from datacenter.models import Schoolkid, Chastisement, Lesson
from fix_marks import fix_marks 
from remove_chastisements import remove_chastisements

child = Schoolkid.objects.filter(full_name__contains='Фролов Иван')[0]
fix_marks(child)

chestment = Chastisement.objects.filter(schoolkid=child)
chestment.delete()


child2 = Schoolkid.objects.filter(full_name__contains='Голубев Феофан')[0]
remove_chastisements(child2)

math_lesson_child = Lesson.objects.filter(year_of_study=6, group_letter='А',
                                          subject__title='Математика')

Chastisement.objects.create(text='Хвалю!', created=math_lesson_child[0].date,
                            schoolkid=child, subject=math_lesson_child[0].subject,
                            teacher=math_lesson_child[0].teacher)


from create_commendation import create_commendation
create_commendation('Фролов Иван', 'Музыка') 
create_commendation('Фролов Иван', 'Музыка')

from script import main
main('Фролов Иван', 'Музыка')
