from datetime import datetime


def handle_like_reaction():
    current_time = datetime.now().strftime('%H:%M:%S')
    return f"Current time: {current_time}"

def handle_poo_reaction():
    current_date = datetime.now().strftime('%Y-%m-%d')
    return f"Current_date: {current_date}"

def handle_ok_hand_reaction():
    return "You have set 👌"

def handle_rolling_on_the_floor_laughing_reaction():
    return "You have set 🤣"
