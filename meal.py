def main():
    input_time = convert(input("What time is it? "))
    if int(input_time) == (7 or 8):
        print("breakfast")
    if int(input_time) == (12 or 13):
        print("lunch")
    if int(input_time) == (18 or 19):
        print("dinner")


def convert(time):
    hour, minutes = time.split(":")
    minutes = float(minutes) * 100 / 60
    hour_min = float(hour) + minutes / 100
    return hour_min

if __name__ == "__main__":
    main()