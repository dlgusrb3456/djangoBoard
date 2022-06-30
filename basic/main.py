import copy
import sys
from collections import deque

def iceToWater(waterList):  # 물과 만나있는 얼음 체크 후 물로 변화
    returnList = copy.deepcopy(waterList)  # waterList에서 값을 체크하고 returnLIst의 값을 변화시켜서 returnLIst를 반환한다
    for i in range(len(waterList)):
        for j in range(len(waterList[i])):
            if waterList[i][j] == 'X':

                if i > 0 and waterList[i - 1][j] == '.':
                    #print(1)
                    returnList[i][j] = '.'
                    continue

                if i < len(waterList) - 1 and waterList[i + 1][j] == '.':
                    #print(2)
                    returnList[i][j] = '.'
                    continue

                if j > 0 and waterList[i][j - 1] == '.':
                    #print(3)
                    returnList[i][j] = '.'
                    continue

                if j < len(waterList[i]) - 1 and waterList[i][j + 1] == '.':
                    #print(4)
                    returnList[i][j] = '.'
                    continue

    return returnList


def checkConnect(waterList,LposX,LposY):  # 물이 녹고 난 후 두 백조가 만나는지 탐색
    returnList = copy.deepcopy(waterList)

    for i in range(len(returnList)):
        for j in range(len(returnList[i])):
            if returnList[i][j]=='X':
                returnList[i][j]=0
        # temp = i.replace('X',0) #가지 못하는 부분을 0으로 바꿈
        # returnList.append(temp)

    queue = deque()
    queue.append([LposX,LposY])

    # queue=[]
    # queue.append([LposX,LposY])

    while len(queue) > 0:
        checkPos = queue.pop()
        xPos = checkPos[0]
        yPos = checkPos[1]
    ##################여기부터!

        if waterList[xPos][yPos]=='L' and (xPos != LposX or yPos != LposY):
            return True

        if xPos > 0 and waterList[xPos - 1][yPos] != 'X' and returnList[xPos - 1][yPos] != 0: # 0이면 못가니까, 여기서 ., L 둘다 들어감
            # print(1)
            returnList[xPos - 1][yPos] = 0 #이미 간 곳이니 0으로 변환
            queue.append([xPos-1,yPos])

        if xPos < len(waterList) - 1 and waterList[xPos + 1][yPos] != 'X' and returnList[xPos + 1][yPos] != 0:
            # print(2)
            returnList[xPos + 1][yPos] = 0  # 이미 간 곳이니 0으로 변환
            queue.append([xPos + 1, yPos])

        if yPos > 0 and waterList[xPos][yPos - 1] != 'X' and returnList[xPos][yPos-1] != 0:
            # print(3)
            returnList[xPos][yPos-1] = 0  # 이미 간 곳이니 0으로 변환
            queue.append([xPos, yPos-1])

        if yPos < len(waterList[xPos]) - 1 and waterList[xPos][yPos + 1] != 'X' and returnList[xPos][yPos+1] != 0:
            # print(4)
            returnList[xPos][yPos + 1] = 0  # 이미 간 곳이니 0으로 변환
            queue.append([xPos, yPos + 1])

    return False



days = 0
x, y = map(int, input().split())

waterList = []
LposX = 0
LposY = 0
for i in range(x):
    babyList = list(sys.stdin.readline().rstrip())
    if 'L' in babyList:
        LposX = i
        LposY = babyList.index('L')
    waterList.append(babyList)

while True:
    days = days+1
    waterList = iceToWater(waterList)
    if checkConnect(waterList,LposX,LposY):
        break;



print(days)