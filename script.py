
from datacenter.models import Schoolkid, Chastisement, Lesson, Subject, Mark
import random 


def fix_marks(schoolkid):
    Mark.objects.filter(schoolkid=schoolkid, points__in=[2, 3]).update(points=5)


def remove_chastisements(schoolkid):
    Chastisement.objects.filter(schoolkid=schoolkid).delete()


def create_chastisement(schoolkid, subject):
    commendations = ['Молодец!', 'Отлично!', 'Хорошо!', 'Гораздо лучше, чем я ожидал!', 'Ты меня приятно удивил!',
                     'Великолепно!', 'Прекрасно!', 'Ты меня очень обрадовал!', 'Именно этого я давно ждал от тебя!',
                     'Сказано здорово – просто и ясно!', 'Ты, как всегда, точен!', 'Очень хороший ответ!', 'Талантливо!',
                     'Ты сегодня прыгнул выше головы!', 'Я поражен!', 'Уже существенно лучше!', 'Потрясающе!',
                     'Замечательно!', 'Прекрасное начало!', 'Так держать!', 'Ты на верном пути!', 'Здорово!',
                     'Это как раз то, что нужно!', 'Я тобой горжусь!', 'С каждым разом у тебя получается всё лучше!',
                     'Мы с тобой не зря поработали!', 'Я вижу, как ты стараешься!', 'Ты растешь над собой!',
                     'Ты многое сделал, я это вижу!', 'Теперь у тебя точно все получится!']
    commendation = random.choice(commendations)
    lesson = Lesson.objects.filter(year_of_study=schoolkid.year_of_study,
                                   group_letter=schoolkid.group_letter,
                                   subject=subject).order_by('-date').first()
      
    while lesson and Chastisement.objects.filter(created=lesson.date, subject=subject):
        lesson = Lesson.objects.filter(year_of_study=schoolkid.year_of_study,
                                       group_letter=schoolkid.group_letter,
                                       subject=subject, date__lt=lesson.date
                                       ).order_by('-date').first()

    Chastisement.objects.create(text=commendation, created=lesson.date,
                                schoolkid=schoolkid, subject=subject,
                                teacher=lesson.teacher)


def main(child_name, subject_name):
    try: 
        child = Schoolkid.objects.get(full_name__contains=child_name)
        subject = Subject.objects.get(title=subject_name.capitalize(),
                                      year_of_study=child.year_of_study)
        fix_marks(child)
        remove_chastisements(child)
        create_chastisement(child, subject)
    
    except Schoolkid.DoesNotExist:
        print("Введите корректные Фамилия Имя")
    except Schoolkid.MultipleObjectsReturned:
        print("Указаны не полные данные. Введите корректные Фамилия Имя")
    except Subject.DoesNotExist:
        print("Введите правильно название предмета")

if __name__ == '__main__':
    main(child_name, subject_name)