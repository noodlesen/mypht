
"""step1"""

import datetime
import os
from django.core.management.base import BaseCommand
from foodapp.models import Person, Meal, Intake, Product


class Command(BaseCommand):
    """A Django command."""

    def handle(self, *args, **options):
        """A Django command body."""

        # Product.objects.all().delete()
        # Meal.objects.all().delete()
        # Intake.objects.all().delete()

        def parse_line(s):
            qblocks = []
            block = ''
            q = False
            for ch in s:
                if ch == '"':
                    q = not q
                elif ch == ',':
                    if q:
                        block += ch
                    else:
                        qblocks.append(block)
                        block = ''
                else:
                    block += ch

            res = []
            res.append(qblocks[0].strip())
            for b in qblocks[1:]:
                if b == '':
                    res.append(None)
                else:
                    res.append(float(b.replace(',', '.')))
            return (res)

        def parse_weight(s):
            tokens = s.strip().split(' ')
            num = float(tokens[0])
            if '1/2' in s:
                num += 0.5
            if tokens[-1] == 'г' or tokens[-1] == 'мл':
                return(num)
            elif tokens[-1] == 'хлебец':
                return(6)

        person_name = 'klapshov'
        person = Person.objects.get(name=person_name)
        print(person)
        folder = os.path.join('incoming', 'fs', person_name)
        fnames = [
            os.path.join(folder, fn) for fn in os.listdir(folder) if fn.endswith('.csv')
        ]
        months = ['января', 'февраля', 'марта', 'апреля', 'мая', 'июня', 'июля', 'августа', 'сентября', 'октября', 'ноября', 'декабря']
        meal_names = [' Завтрак,', ' Обед,', ' Ужин,', ' Перекус/Другое,']
        for fn in fnames:
            with open(fn, 'r', encoding='utf-8') as f:
                lines = f.read().split('\n')
                skip = True
                current_date = None
                current_meal = None
                current_meal_no = None
                skip_line = False
                for ln in range(len(lines)-2):
                    l = lines[ln]

                    if not skip:
                        if not skip_line:
                            if l == '':  # if next line is date line
                                nl = lines[ln+1]
                                text_date = nl.split('"')[1].split(',')
                                month_day = text_date[1].split(' ')
                                month = month_day[1]
                                day = int(month_day[2])
                                year = int(text_date[2])
                                month_number = None
                                for i, m in enumerate(months):
                                    if m == month:
                                        month_number = i+1
                                current_date = datetime.date(
                                    year=year, day=day, month=month_number
                                )
                                print(current_date)
                                skip_line = True
                            else:
                                meal_line = False
                                for i, mn in enumerate(meal_names):
                                    if l.startswith(mn):
                                        current_meal_no = i
                                        meal_line = True
                                        print('meal ', i)
                                        # if current_meal is None:
                                        try:
                                            current_meal = Meal.objects.get(
                                                person=person, date=current_date, meal_number=current_meal_no
                                            )
                                        except Meal.DoesNotExist:
                                            current_meal = Meal()
                                            current_meal.person = person
                                            current_meal.meal_number = current_meal_no
                                            current_meal.date = current_date
                                            current_meal.save()

                                if not meal_line:
                                    p = parse_line(l)
                                    w = parse_weight(lines[ln+1])
                                    wk = w/100
                                    try:
                                        pr = Product.objects.get(name=p[0])
                                    except Product.DoesNotExist:
                                        pr = Product()
                                        # Кал ( ккал),Жир( г),Н/жир( г),Углев( г),Клетч( г),Сахар( г),Белк( г),Натри( мг),Холес( мг),Калий( мг)
                                        # REWRITE
                                        pr.name = p[0]
                                        if p[1] is not None:
                                            pr.kkal = round(p[1]/wk, 1)
                                        if p[2] is not None:
                                            pr.fat = round(p[2]/wk, 1)
                                        if p[3] is not None:
                                            pr.nfat = round(p[3]/wk, 1)
                                        if p[4] is not None:
                                            pr.carb = round(p[4]/wk, 1)
                                        if p[5] is not None:
                                            pr.fiber = round(p[5]/wk, 1)
                                        if p[6] is not None:
                                            pr.sugar = round(p[6]/wk, 1)
                                        if p[7] is not None:
                                            pr.prot = round(p[7]/wk, 1)
                                        if p[8] is not None:
                                            pr.natr = round(p[8]/wk, 1)
                                        if p[9] is not None:
                                            pr.holes = round(p[9]/wk, 1)
                                        try:
                                            if p[10] is not None:
                                                pr.kali = round(p[10]/wk, 1)
                                        except:
                                            pass
                                        pr.source = 'FS_RU'
                                        pr.is_meta = False
                                        pr.save()

                                    try:
                                        i = Intake.objects.get(meal=current_meal, product=pr)
                                    except Intake.DoesNotExist:
                                        i = Intake()
                                        i.product = pr
                                        i.weight = w
                                        i.person = person
                                        i.meal = current_meal
                                        i.save()

                                    skip_line = True

                        else:
                            skip_line = False

                    if l.startswith('Дата,'):
                        skip = False
                #current_meal.save()