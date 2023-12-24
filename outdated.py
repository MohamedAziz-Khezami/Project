months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]



month=["1","2","3","4","5","6","7","8","9","10","11","12","01","02","03","04","05","06","07","08","09"]
days=["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31","01","02","03","04","05","06","07","08","09"]

while True:
    date=input("Date: ")
    date=date.strip()
    if date.find(",")!=-1:
        ch,y=date.split(",")
        m,d=ch.split(" ")
        y=y.strip()
        if (m not in months) or (d not in days):
            continue


    else:
        try:
            m,d,y=date.split(" ")
            if m in months or d in months or m not in month or d not in days:
                continue
        except:
            try:
                m,d,y=date.split("/")
                if m in months or d in months or m not in month or d not in days:
                    continue
            except:
                try:
                    m,d,y=date.split("-")
                    if m in months or d in months or m not in month or d not in days:
                        continue
                except:
                    continue

    if(( m  in months) and (d in days)) or ((m in month) and (d  in days)):

        if m not in months:
            print(f"{y}-{int(m):02}-{int(d):02}")
            break
        else:
            print(f"{y}-{months.index(m)+1:02}-{int(d):02}")
            break
    else:




