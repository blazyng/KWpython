from datetime import date
today = date.today()
wk = today.isocalendar()[1]
k={"KW":wk}
return k
