class UndergroundSystem:

    def __init__(self):
        self.checkin = dict()
        self.avgTime = dict()

    def checkIn(self, id, stationName, t):
        if id not in self.checkin:
            self.checkin[id] = (stationName, t)
        return None

    def checkOut(self, id, stationName, t):
        if id in self.checkin:
            station, time = self.checkin.get(id)
            if station + '-' + stationName not in self.avgTime:
                self.avgTime[station + '-' + stationName] = (abs(t - time), 1)
            else:
                oldtime, itr = str(self.avgTime[station + '-' + stationName]).split(',')
                oldtime = float(oldtime.strip('('))
                itr = int(itr.strip(')'))
                self.avgTime[station + '-' + stationName] = (abs(oldtime + (t - time)), itr + 1)
            self.checkin.pop(id)
        return None

    def getAverageTime(self, startStation, endStation):
        if startStation + '-' + endStation in self.avgTime:
            time, num = str(self.avgTime[startStation + '-' + endStation]).split(',')
            time = float(time.strip('('))
            num = int(num.strip(')'))
            return time / num

undergroundSystem = UndergroundSystem()
instationName = 'Leyton'
outstationName = 'Waterloo'

undergroundSystem.checkIn(45, "Leyton", 3)
undergroundSystem.checkIn(32, "Paradise", 8)
undergroundSystem.checkIn(27, "Leyton", 10)
undergroundSystem.checkOut(45, "Waterloo", 15)
undergroundSystem.checkOut(27, "Waterloo", 20)
undergroundSystem.checkOut(32, "Cambridge", 22)
print(undergroundSystem.getAverageTime("Paradise", "Cambridge"))
print(undergroundSystem.getAverageTime("Leyton", "Waterloo"))
undergroundSystem.checkIn(10,"Leyton",24),
print(undergroundSystem.getAverageTime("Leyton","Waterloo"))
undergroundSystem.checkOut(10,"Waterloo",38)
print(undergroundSystem.getAverageTime("Leyton","Waterloo"))


["UndergroundSystem","checkIn","checkIn","checkIn","checkOut","checkOut","checkOut","getAverageTime","getAverageTime","checkIn","getAverageTime","checkOut","getAverageTime"]
[[],[45,"Leyton",3],[32,"Paradise",8],[27,"Leyton",10],[45,"Waterloo",15],[27,"Waterloo",20],[32,"Cambridge",22],["Paradise","Cambridge"],["Leyton","Waterloo"],[10,"Leyton",24],["Leyton","Waterloo"],[10,"Waterloo",38],["Leyton","Waterloo"]]