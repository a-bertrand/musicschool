import datetime
from datetime import date, timedelta
from dateutil.relativedelta import relativedelta
"""
    cours :
        choisir un eleve 
        lui dire tous les lundi 
        ajouter tous les lundi de l'année 
        
        
    eleve 
        
    class Cours
        Label
        Date 
        User 

    
    def create(jour):
        for each lundi dans l'année 
            self.addTimeStamp(date)

    class TimestampModel()
        date_meet = DateTimeField()
"""
class Lessons(models.Model):
    dates = models.ManyToManyField()
    user = models.ForeignKey("app.Model", verbose_name=_(""), on_delete=models.CASCADE)

    DAY_OF_THE_WEEK = {
        '1' : 'Monday',
        '2' : 'Tuesday',
        '3' : 'Wednesday',
        '4' : 'Thursday',
        '5' : 'Friday',
        '6' : 'Saturday', 
        '7' : 'Sunday',
    }

    # asked the date of the first lesson
    def create_year_school(self, date_of_the_first_lesson)
        next_date_year = date_of_the_first_lesson + timedelta(days=365)
        add_day = 7
        index = 1
        while date_of_the_first_lesson < next_date_year:
            add_day = index * add_day
            date_to_add = date_of_the_first_lesson + timedelta(days=add_day))
            print(date_to_add.weekdays(), date_to_add.day, date_to_add.month ,date_to_add.year)
            if add_day > 100:
                break;
            index = index + 1;

        if now_date == date_of_the_first_lesson:
            #its ok 
            pass 
            

        date += timedelta(days =  - now_date.weekday()) 
        # Get first weekday_asked 
        # loops and add one day 
        while d.year == year:
            yield d
            d += timedelta(days = 7)

        for d in allsundays(now_date.):

'''
en premier trouver le chiffre du jour 
boucler pour arriver au premier chiffre 
puis fait time_delta de une semaine jusqu'a  
arriver à la même date avec un timedelta d'un an de plus
'''