def main():
    timeString = input("What time is it? ").strip()

    time = convert(timeString)

    if 7 <= time <= 8:
        print("breakfast time")
    elif 12 <= time <= 13:
        print("lunch time")
    elif 18 <= time <= 19:
        print("dinner time")

def convert(timeString):

    if timeString.endswith(".m."):
        timeList = timeString.split(":")
        spaceList = timeList[1].split(" ")
        timeList[1] = spaceList[0]
        timeList.append(spaceList[1])

        if timeList[2] == "p.m.":
            hours = float(timeList[0]) + 12
        else:
            hours = float(timeList[0])

    else:
        timeList = timeString.split(":")
        hours = float(timeList[0])

    minutes = float(timeList[1])/60

    return hours + minutes


if __name__ == "__main__":
    main()
