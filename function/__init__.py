from datetime import datetime, timedelta
from session import create_session

months = (
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "Augustus",
    "September",
    "October",
    "November",
    "December",
)

api = create_session()


def update_name():
    d = datetime.now()
    # timezone gmt +7
    d_gmt_plus_7 = d + timedelta(hours=7)

    d_dd_month_yyyy = d_gmt_plus_7.strftime("%d %B %Y")

    d_indonesia = d_dd_month_yyyy.replace(
        d_gmt_plus_7.strftime("%B"),
        months[int(d_gmt_plus_7.strftime("%m")) - 1],
    )

    # twitter_icon = ""
    calendar_emoticon = "🗓️"

    name = calendar_emoticon + " " + d_indonesia
    api.update_profile(name=name)


def update_banner():
    days = (
        "sunday",
        "monday",
        "tuesday",
        "wednesday",
        "thursday",
        "friday",
        "saturday",
    )
    now = datetime.now()

    now_my_time = now + timedelta(hours=7)

    # if gmt -7
    # now_my_time = now - timedelta(hours=7)

    # get day
    day = days[now_my_time.weekday()]
    print("Day: ", day)
    api.update_profile_banner(f"banner/{day}.jpg")
