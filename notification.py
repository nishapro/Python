import time
from plyer import notification
if __name__=="__main__":
        notification.notify(
            title="**Please Drink Water",
            message = "The U.S. National Academies of Sciences, Engineering, andMedicine determinedthat an adequate daily fluid intake is:About 15.5 cups (3.7 liters) of fluids a day for men. About 11.5cups (2.7 liters) of fluids a day for women.",
            timeout=10
        )
        time.sleep(6)
