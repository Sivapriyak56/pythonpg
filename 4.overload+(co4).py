
class Time:
    def _init_(self, hour, minute, second):
        self.__hour = hour
        self.__minute = minute
        self.__second = second

    def _add_(self, other):
        second = self._second + other._second
        minute = self._minute + other._minute
        hour = self._hour + other._hour
        if second > 60:
            minute += int(second / 60)
            second = second % 60
        if minute > 60:
            hour += int(minute / 60)
            minute = minute % 60
        time = "{0} Hours: {1} minutes: {2} seconds".format(hour, minute, second)
        return time


h1 = int(input("Enter the Hours of first TIME \t"))
m1 = int(input("Enter the Minutes of first TIME \t"))
s1 = int(input("Enter the Seconds of first TIME \t"))

h2 = int(input("Enter the Hours of second TIME\t"))
m2 = int(input("Enter the Minutes of second TIME\t"))
s2 = int(input("Enter the Seconds of second TIME\t"))
time1 = Time(h1, m1, s1)
time2 = Time(h2, m2, s2)
print("Sum of time:", time1+time2)