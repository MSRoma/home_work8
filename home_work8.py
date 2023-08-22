from datetime import datetime, date, timedelta

users = [
    {"name": "John", "birthday": "1985-08-19"}, #Субота
    {"name": "Emily", "birthday": "1992-08-20"},#Неділя
    {"name": "Michael", "birthday": "1978-08-21"},#понеділок
    {"name": "Sarah", "birthday": "1990-08-22"},#вівторок
    {"name": "David", "birthday": "1987-08-23"},#середа
    {"name": "Jessica", "birthday": "1983-08-24"},#четверг
    {"name": "Daniel", "birthday": "1995-08-25"},# п'ятниця
    {"name": "Jennifer", "birthday": "1989-08-26"},#субота
    {"name": "Christopher", "birthday": "1980-08-27"},#неділя
    {"name": "Elizabeth", "birthday": "1998-08-28"},#понеділок
    {"name": "Matthew", "birthday": "1984-08-07"},#
    {"name": "Olivia", "birthday": "1993-08-30"},#
    {"name": "Andrew", "birthday": "1976-08-09"},#
    {"name": "Sophia", "birthday": "1991-08-10"},
    {"name": "William", "birthday": "1982-04-16"},
    {"name": "Ava", "birthday": "1997-11-08"},
    {"name": "Ryan", "birthday": "1986-08-11"},
    {"name": "Natalie", "birthday": "1994-03-05"},
    {"name": "James", "birthday": "1981-07-15"},
    {"name": "Grace", "birthday": "1996-06-23"}
]

def get_birthdays_per_week(users):
        
        birthdays_dict = {}
        datetime_now = date.today() #date(year=2023, month=8, day=3) 
        year_now = datetime_now.year

        for i in range(7):
            diff = datetime_now + timedelta(days=i)
            if diff.weekday() < 5  :
                birthdays_dict[diff.strftime("%A")] = []
            elif datetime_now.weekday() <= 2 or datetime_now.weekday() == 6 :
                birthdays_dict["Next_Monday"] = []

        for item in users:
            date_birthday = datetime.strptime(item.get('birthday'), '%Y-%m-%d')
            birthday_ = date(year=year_now, month=date_birthday.month, day=date_birthday.day)
            w =  birthday_ - datetime_now
            if w <= timedelta(days=6)  and w >= timedelta(days=0) and datetime_now.weekday() == 0 :
                if birthday_.weekday() < 5:
                    birthdays_dict[birthday_.strftime("%A")].append(item["name"])
                elif birthday_.weekday() >= 5 :
                    birthdays_dict[("Next_Monday")].append(item["name"]) 
            elif w <= timedelta(days=6)  and w >= timedelta(days=0) and  datetime_now.weekday() > 0 and datetime_now.weekday() < 6  :           
                if birthday_.weekday() < 5:
                    birthdays_dict[birthday_.strftime("%A")].append(item["name"])
                elif birthday_.weekday() >= 5:
                    birthdays_dict[("Monday")].append(item["name"])
            elif w <= timedelta(days=-1)  and w >= timedelta(days=-2) and datetime_now.weekday() == 0 :
                if birthday_.weekday() < 5:
                    birthdays_dict[birthday_.strftime("%A")].append(item["name"])
                elif birthday_.weekday() >= 5:
                    birthdays_dict[("Monday")].append(item["name"]) 
            elif w <= timedelta(days=6)  and w >= timedelta(days=0) and datetime_now.weekday() == 6 :
                if birthday_.weekday() < 5:
                    birthdays_dict[birthday_.strftime("%A")].append(item["name"])
                elif birthday_.weekday() == 6:
                    birthdays_dict[("Monday")].append(item["name"])
                elif birthday_.weekday() == 5:
                    birthdays_dict[("Next_Monday")].append(item["name"])               
        result = "" 
        for key,value in birthdays_dict.items():
            if value:
                names = ", ".join(value)
                res = f"{key}: {names}\n"
                result += res

        return print(result)

get_birthdays_per_week(users)