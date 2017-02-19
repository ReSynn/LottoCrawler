import calendar
import datetime
import locale
import requests
import random
import time
import math
import multiprocessing
from multiprocessing import Process, Manager
from bs4 import BeautifulSoup
from bs4 import NavigableString

class cLottoDraw():
    def __init__(self, LottoDrawSoup):
        self.__LottoDrawSoup = LottoDrawSoup
        self.__Draw = "0"
        self.__Day = "0"
        self.__Month = "0"
        self.__Year = "0"
        self.__WeekDay = ""
        self.__WinNumber1 = "0"
        self.__WinNumber2 = "0"
        self.__WinNumber3 = "0"
        self.__WinNumber4 = "0"
        self.__WinNumber5 = "0"
        self.__WinNumber6 = "0"
        self.__WinDraw = "0"
        self.__SuperNumber = "0"

    def getLottoDrawSoup(self):
        return self.__LottoDrawSoup

    def getDraw(self):
        return self.__Draw

    def getDay(self):
        return self.__Day

    def getMonth(self):
        return self.__Month

    def getYear(self):
        return self.__Year

    def getWeekDay(self):
        return self.__WeekDay

    def getWinNumber1(self):
        return self.__WinNumber1

    def getWinNumber2(self):
        return self.__WinNumber2

    def getWinNumber3(self):
        return self.__WinNumber3

    def getWinNumber4(self):
        return self.__WinNumber4

    def getWinNumber5(self):
        return self.__WinNumber5

    def getWinNumber6(self):
        return self.__WinNumber6

    def getWinDraw(self):
        return self.__WinDraw

    def getSuperNumber(self):
        return self.__SuperNumber

    def setDraw(self, Draw):
        self.__Draw = Draw

    def setDay(self, Day):
        self.__Day = Day

    def setMonth(self, Month):
        self.__Month = Month

    def setYear(self, Year):
        self.__Year = Year

    def setWeekDay(self, WeekDay):
        self.__WeekDay = WeekDay

    def setWinNumber1(self, WinNumber1):
        self.__WinNumber1 = WinNumber1

    def setWinNumber2(self, WinNumber2):
        self.__WinNumber2 = WinNumber2

    def setWinNumber3(self, WinNumber3):
        self.__WinNumber3 = WinNumber3

    def setWinNumber4(self, WinNumber4):
        self.__WinNumber4 = WinNumber4

    def setWinNumber5(self, WinNumber5):
        self.__WinNumber5 = WinNumber5

    def setWinNumber6(self, WinNumber6):
        self.__WinNumber6 = WinNumber6

    def setWinDraw(self, WinDraw):
        self.__WinDraw = WinDraw

    def setSuperNumber(self, SuperNumber):
        self.__SuperNumber = SuperNumber

    def findDraw(self):
        Draw = self.__LottoDrawSoup.find("div", {"class": "zahlensuche_nr"})
        Draw = Draw.text
        Draw = int(Draw)
        self.setDraw(Draw)

    def findDate(self):
        Date = self.__LottoDrawSoup.find("div", {"class":"zahlensuche_datum"})
        Date =  Date.text
        for i, Split in enumerate(Date.split(".")):
            if i == 0:
                Day = Split
                self.setDay(Day)
            if i == 1:
                Month = Split
                self.setMonth(Month)
            if i == 2:
                Year = Split
                self.setYear(Year)

        englishDate = Year + " " + Month + " " + Day
        WeekDay = datetime.datetime.strptime(englishDate, "%Y %m %d").strftime("%A")

        if WeekDay == "Monday":
            WeekDay = "Montag"

        if WeekDay == "Tuesday":
            WeekDay = "Dienstag"

        if WeekDay == "Wednesday":
            WeekDay = "Mittwoch"

        if WeekDay == "Thursday":
            WeekDay = "Donnerstag"

        if WeekDay == "Friday":
            WeekDay = "Freitag"

        if WeekDay == "Saturday":
            WeekDay = "Samstag"

        if WeekDay == "Sunday":
            WeekDay = "Sonntag"

        self.setWeekDay(WeekDay)

    def findWinningNumbers(self):
        WinningNumbers = []
        WinDraw = ""
        Numbers = self.__LottoDrawSoup.findAll("div", {"class": "zahlensuche_zahl"})
        for Number in Numbers:
            Number = str(Number.text)
            length = len(str(Number))
            if length == 1:
                Number = "0" + Number

            WinningNumbers.append(Number)
            WinDraw = WinDraw + Number

        self.setWinNumber1(WinningNumbers[0])
        self.setWinNumber2(WinningNumbers[1])
        self.setWinNumber3(WinningNumbers[2])
        self.setWinNumber4(WinningNumbers[3])
        self.setWinNumber5(WinningNumbers[4])
        self.setWinNumber6(WinningNumbers[5])
        self.setWinDraw(WinDraw)

    def findSuperNumber(self):
        SuperNumber = 0
        SuperNumber = self.__LottoDrawSoup.find("div", {"class": "zahlensuche_zz"})
        SuperNumber = SuperNumber.text
        SuperNumber = SuperNumber.replace("\n", "")
        SuperNumber = SuperNumber.replace("\r", "")

        if SuperNumber == "":
            SuperNumber = "nA"

        self.setSuperNumber(SuperNumber)

    def writeToCSVFile(self):
        FileWrite = open(str(self.getYear()) + " - CSVLottoDraws" + ".txt", "a")
        FileWrite.write(str(self.getDraw()) + ', ' +
                        str(self.getYear()) + ', ' +
                        str(self.getMonth()) + ', ' +
                        str(self.getDay()) + ', ' +
                        str(self.getWinNumber1()) + ', ' +
                        str(self.getWinNumber2()) + ', ' +
                        str(self.getWinNumber3()) + ', ' +
                        str(self.getWinNumber4()) + ', ' +
                        str(self.getWinNumber5()) + ', ' +
                        str(self.getWinNumber6()) + ', ' +
                        str(self.getSuperNumber()) + '\n' )
        FileWrite.close()

    def writeToTABFile(self):
        FileWrite = open(str(self.getYear()) + " - TABLottoDraws" + ".txt", "a")
        FileWrite.write(str(self.getDraw()) + '\t' +
                        str(self.getYear()) + '\t' +
                        str(self.getMonth()) + '\t' +
                        str(self.getDay()) + '\t' +
                        str(self.getWinNumber1()) + '\t' +
                        str(self.getWinNumber2()) + '\t' +
                        str(self.getWinNumber3()) + '\t' +
                        str(self.getWinNumber4()) + '\t' +
                        str(self.getWinNumber5()) + '\t' +
                        str(self.getWinNumber6()) + '\t' +
                        str(self.getSuperNumber()) + '\n')
        FileWrite.close()

    def writeToCSVFile2(self, CPU):
        FileWrite = open(str(CPU) + " - CSVLottoDraws" + ".txt", "a")
        FileWrite.write(str(self.getDraw()) + ', ' +
                        str(self.getYear()) + ', ' +
                        str(self.getMonth()) + ', ' +
                        str(self.getDay()) + ', ' +
                        '"' + str(self.getWinNumber1()) + '"' +  ', ' +
                        '"' + str(self.getWinNumber2()) + '"' + ', ' +
                        '"' + str(self.getWinNumber3()) + '"' + ', ' +
                        '"' + str(self.getWinNumber4()) + '"' + ', ' +
                        '"' + str(self.getWinNumber5()) + '"' + ', ' +
                        '"' + str(self.getWinNumber6()) + '"' + ', ' +
                        str(self.getSuperNumber()) + ', ' +
                        '"' + str(self.getWinDraw()) + '"' + ', ' +
                        str(self.getWeekDay()) + '\n')
        FileWrite.close()

    def writeToTABFile2(self, CPU):
        FileWrite = open(str(CPU) + " - TABLottoDraws" + ".txt", "a")
        FileWrite.write(str(self.getDraw()) + '\t' +
                        str(self.getYear()) + '\t' +
                        str(self.getMonth()) + '\t' +
                        str(self.getDay()) + '\t' +
                        '"' + str(self.getWinNumber1()) + '"' + '\t' +
                        '"' + str(self.getWinNumber2()) + '"' + '\t' +
                        '"' + str(self.getWinNumber3()) + '"' + '\t' +
                        '"' + str(self.getWinNumber4()) + '"' + '\t' +
                        '"' + str(self.getWinNumber5()) + '"' + '\t' +
                        '"' + str(self.getWinNumber6()) + '"' + '\t' +
                        str(self.getSuperNumber()) + '\t' +
                        '"' + str(self.getWinDraw()) + '"' + '\t' +
                        str(self.getWeekDay()) + '\n')
        FileWrite.close()

def MakeSoup(CPU, URL):
    heads = [
        {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"},
        {"User-Agent": "Lynx/2.8.4rel.1 libwww-FM/2.14 SSL-MM/1.4.1 OpenSSL/0.9.6c"},
        {"User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 5_0 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9A334 Safari/7534.48.3"},
        {"User-Agent": "Mozilla/5.0 (Linux; Android 5.1.1; SM-G928X Build/LMY47X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.83 Mobile Safari/537.36"},
        {"User-Agent": "Mozilla/5.0 (Linux; Android 5.0.2; LG-V410/V41020c Build/LRX22G) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/34.0.1847.118 Safari/537.36"},
        {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9"},
        {"User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:15.0) Gecko/20100101 Firefox/15.0.1"},
        {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.111 Safari/537.36"}
    ]

    try:
        Bot = True
        i = 0
        while Bot:
            IntHeader = random.randint(0, int(len(heads)))
            if IntHeader == 8:
                IntHeader = IntHeader - 1
            headers = heads[IntHeader]

            sleep = 0
            if (i >= 0) and (i < 5):
                sleep = round(random.uniform(2.1, 5.0), 2)
            if (i >= 5) and (i < 10) and (sleep == 0):
                sleep = round(random.uniform(4.1, 7.0), 2)
            if (i >= 10) and (i < 50) and (sleep == 0):
                sleep = round(random.uniform(8.1, 11.0), 2)
            if (i >= 50) and (sleep == 0):
                sleep = round(random.uniform(12.1, 14.0), 2)
            time.sleep(sleep)
            i += 1
            Bot = False

            page = requests.get(URL, headers=headers)
            pagePlainText = page.content
            pageSoup = BeautifulSoup(pagePlainText, "html.parser")

            '''
            SoupTitle = str(pageSoup.title.text)
            SoupTitle = SoupTitle.replace("\n", "")
            SoupTitle = SoupTitle.lstrip()
            SoupTitle = SoupTitle.rstrip()
            if (SoupTitle == "Bot Check") or (SoupTitle == "Tut uns Leid!"):
                print("(" + str(CPU) + ")" + " " + "Blocked: " + str(i) + " Try" + " (Sleep " + str(sleep) + ")")
                Bot = True
            '''

        return pageSoup

    except:
        print("")

    return pageSoup

def getLottoDrawYearURLs():
    allLottoDrawYearURL = []
    baseLink = "http://www.lottozahlenonline.de/statistik/beide-spieltage/lottozahlen-archiv.php?j="
    Year = 1955

    while(Year != 2018):
        LottoDrawYearURL = ""
        LottoDrawYearURL = baseLink + str(Year)
        allLottoDrawYearURL.append(LottoDrawYearURL)
        Year = Year + 1

    return allLottoDrawYearURL

def getDraws(CPU, allLottoDrawYearURLs, start, end):
    LottoDrawYearURLs = allLottoDrawYearURLs[int(start):int(end)]
    allLottoDraws = []

    for i, LottoDrawYearURL in enumerate(LottoDrawYearURLs):
        #LottoDrawYearURL = "http://www.lottozahlenonline.de/statistik/beide-spieltage/lottozahlen-archiv.php?j=1992"
        print("\n(" + str(CPU) + ")" + " " + str(LottoDrawYearURL))
        Year = LottoDrawYearURL[-4:]

        try:
            LottoDrawYearURLSoup = MakeSoup(CPU, LottoDrawYearURL)
            allDraws = LottoDrawYearURLSoup.findAll("div", {"class": "zahlensuche_rahmen"})

            for Draw in allDraws:
                NewLottoDraw = cLottoDraw(Draw)
                NewLottoDraw.findDraw()
                NewLottoDraw.findDate()
                NewLottoDraw.findWinningNumbers()
                NewLottoDraw.findSuperNumber()
                #NewLottoDraw.writeToCSVFile()
                #NewLottoDraw.writeToTABFile()
                allLottoDraws.append(NewLottoDraw)

                print("(" + str(CPU) + ")" + " " + str(Year) + " - " + str(NewLottoDraw.getDraw()) + "/" + str(len(allDraws)))

        except:
            FileWrite = open(Year + " - #CND LottoDraws.txt", "a")
            FileWrite.write(str(LottoDrawYearURL) + "\n")
            FileWrite.close()

    for LottoDraw in allLottoDraws:
        LottoDraw.writeToCSVFile2(CPU)
        LottoDraw.writeToTABFile2(CPU)


if __name__ == "__main__":
    startTime = time.time()
    print("\n### Started ###\n")

    allLottoDrawYearURLs = getLottoDrawYearURLs()
    lenghtLottoDrawYearURLs = len(allLottoDrawYearURLs)
    numberOfCPUs = multiprocessing.cpu_count()

    manager = Manager()
    ManagedLottoDrawYearURLs = manager.list(allLottoDrawYearURLs)
    Intervall = math.floor(lenghtLottoDrawYearURLs / numberOfCPUs)

    Processes = []

    #getDraws(1, allLottoDrawYearURLs, 0, 7)

    for v in range(numberOfCPUs):
        start = Intervall * v
        end = (Intervall * (v + 1))

        if v < numberOfCPUs - 1:
            p = Process(target=getDraws,
                        args=(v + 1, ManagedLottoDrawYearURLs, start, end))
        else:
            p = Process(target=getDraws,
                        args=(v + 1, ManagedLottoDrawYearURLs, start, lenghtLottoDrawYearURLs))
        p.start()
        Processes.append(p)

    for p in Processes:
        p.join()

    print("\n### Finished ###\n")
    elapsedTime = time.time() - startTime
    print(elapsedTime)










