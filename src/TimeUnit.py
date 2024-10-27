from datetime import timedelta

# Give the Unit part

class Give_unit:
    def __init__(self, hours = "heure", minutes = "minute", seconds = "seconde"):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
    

    def Unit(self, delta: str):
        heures, reste = divmod(delta.total_seconds(), 3600)
        minutes, secondes = divmod(reste, 60)

        if heures > 0:
            text_time = f"{int(heures)}:{int(minutes):02}:{int(secondes):02}"
        elif minutes > 0:
            text_time = f"{int(minutes)}:{int(secondes):02}"
        else:
            text_time = f"{int(secondes)}"
        
        return text_time