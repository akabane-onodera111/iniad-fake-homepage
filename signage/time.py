import datetime
import time

while True:
    now = datetime.datetime.now()
    current_hour = now.current_hour
    
    if 18 <= current_hour < 6:
        greeting = "こんばんは"
    elif 6 <= current_hour < 10:
        greeting = "おはようございます"
    else:
        greeting = "こんにちは"

    html_text = f"<p>{greeting}</p>"

    with open("index.html", "w") as file:
        file.write(html_text)