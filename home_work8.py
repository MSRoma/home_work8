from datetime import datetime, date, timedelta

users = [
    {"name": "John", "birthday": "1985-07-28"},
    {"name": "Emily", "birthday": "1992-07-29"},
    {"name": "Michael", "birthday": "1978-07-30"},
    {"name": "Sarah", "birthday": "1990-07-31"},
    {"name": "David", "birthday": "1987-08-01"},
    {"name": "Jessica", "birthday": "1983-08-22"},
    {"name": "Daniel", "birthday": "1995-08-03"},
    {"name": "Jennifer", "birthday": "1989-08-04"},
    {"name": "Christopher", "birthday": "1980-08-05"},
    {"name": "Elizabeth", "birthday": "1998-08-06"},
    {"name": "Matthew", "birthday": "1984-08-07"},
    {"name": "Olivia", "birthday": "1993-08-08"},
    {"name": "Andrew", "birthday": "1976-08-09"},
    {"name": "Sophia", "birthday": "1991-08-10"},
    {"name": "William", "birthday": "1982-04-16"},
    {"name": "Ava", "birthday": "1997-11-08"},
    {"name": "Ryan", "birthday": "1986-08-11"},
    {"name": "Natalie", "birthday": "1994-03-05"},
    {"name": "James", "birthday": "1981-07-15"},
    {"name": "Grace", "birthday": "1996-06-23"}
]

def get_birthdays_per_week(users):
    birthdays_dict = {i: [] for i in range(7)}
    datetime_now = date.today() #date(year=2023, month=8, day=3) 
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
        if w <= timedelta(days=6)  and w >= timedelta(days=0) and 0<= weekday_now <= 4:
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
                birthdays_dict[0].append(item["name"])
            elif weekday_birthday == 6: 
                birthdays_dict[0].append(item["name"])
        elif w < timedelta(days=0)  and w >= timedelta(days=-2) and 5<= weekday_now <= 6:   
            if weekday_birthday == 6:
                birthdays_dict[0].append(item["name"])
            elif weekday_birthday == 5:
                birthdays_dict[0].append(item["name"])
            else:
                continue
        else:
            continue 
    result = ""
    count = 0
    for i in range(weekday_now,7):
        day_naw = datetime_now + timedelta(days=(count))
        count += 1
        day_name = day_naw.strftime('%A')  
        result += (f"{day_name}: {', '.join(birthdays_dict[i])}\n")
    for  i in range(0,weekday_now):
        day_naw = datetime_now + timedelta(days=(count))
        count += 1
        day_name = day_naw.strftime('%A')  
        result += (f"{day_name}: {', '.join(birthdays_dict[i])}\n")
    return result

print(get_birthdays_per_week(users))
