from datetime import datetime, date, timedelta

users = [
    {"name": "John", "birthday": "1985-07-28"},
    {"name": "Emily", "birthday": "1992-07-29"},
    {"name": "Michael", "birthday": "1978-07-30"},
    {"name": "Sarah", "birthday": "1990-07-31"},
    {"name": "David", "birthday": "1987-08-23"},
    {"name": "Jessica", "birthday": "1983-08-22"},
    {"name": "Daniel", "birthday": "1995-08-03"},
    {"name": "Jennifer", "birthday": "1989-08-04"},
    {"name": "Christopher", "birthday": "1980-08-05"},
    {"name": "Elizabeth", "birthday": "1998-08-6"},
    {"name": "Matthew", "birthday": "1984-07-08"},
    {"name": "Olivia", "birthday": "1993-10-14"},
    {"name": "Andrew", "birthday": "1976-07-13"},
    {"name": "Sophia", "birthday": "1991-09-20"},
    {"name": "William", "birthday": "1982-04-16"},
    {"name": "Ava", "birthday": "1997-11-08"},
    {"name": "Ryan", "birthday": "1986-08-11"},
    {"name": "Natalie", "birthday": "1994-03-05"},
    {"name": "James", "birthday": "1981-07-15"},
    {"name": "Grace", "birthday": "1996-06-23"}
]






def get_birthdays_per_week(users):
    birthdays_dict = {i: [] for i in range(6)}
    datetime_now = date.today() #date(year=2023, month=7, day=31)
    weekday_now = datetime_now.weekday()
    year_now = datetime_now.year
    for item in users:
        item.get('birthday')
        date_birthday = datetime.strptime(item.get('birthday'), '%Y-%m-%d')
        month_birthday = date_birthday.month
        day_birthday = date_birthday.day
        birthday_ = date(year=year_now, month=month_birthday, day=day_birthday)     
        w =  birthday_ - datetime_now
        weekday_birthday = birthday_.weekday()
        if w <= timedelta(days=7)  and w > timedelta(days=0):
            if weekday_birthday == 0:
                birthdays_dict[weekday_birthday].append(item["name"])
            elif weekday_birthday == 1: 
                birthdays_dict[weekday_birthday].append(item["name"])
            elif weekday_birthday == 2: 
                birthdays_dict[weekday_birthday].append(item["name"])
            elif weekday_birthday == 3: 
                birthdays_dict[weekday_birthday].append(item["name"])
            elif weekday_birthday == 4: 
                birthdays_dict[weekday_birthday].append(item["name"])
            elif weekday_birthday == 5: 
                birthdays_dict[weekday_birthday].append(item["name"])
            elif weekday_birthday == 6: 
                birthdays_dict[weekday_birthday].append(item["name"])
        elif w <= timedelta(days=0)  and w >= timedelta(days=-2) and 5<= weekday_now >= 6:   
            if weekday_birthday == 6:
                birthdays_dict[0].append(item["name"])
            elif weekday_birthday == 5:
                birthdays_dict[0].append(item["name"])
            elif weekday_birthday == 0:
                birthdays_dict[0].append(item["name"])
            else:
                continue
        else:
            continue
    return (f"\
Monday: {', '.join(birthdays_dict[0])}\n\
Tuesday: {', '.join(birthdays_dict[1])}\n\
Wednesday: {', '.join(birthdays_dict[2])}\n\
Thursday: {', '.join(birthdays_dict[3])}\n\
Friday: {', '.join(birthdays_dict[4])}\n\
Next_Monday: {', '.join(birthdays_dict[5])}\n")


print(get_birthdays_per_week(users))