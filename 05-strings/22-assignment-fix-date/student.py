def fix_date(date):
    month = date[0:2]
    day = date[3:5]
    year = date[6:]

    return year + "/" + month + "/" + day