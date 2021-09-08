# Typewriter

import time

# print
def typewrite(text, gap):
    length = len(text)
    for i in range(0, length):
        print(text[i], end = "")
        time.sleep(gap)
    print("")
    
# input
def question(text, gap):
    length = len(text)
    for i in range(0, length - 1):
        print(text[i], end = "")
        time.sleep(gap)
    answer = input(text[-1])
    return answer

gap = 0.05

##############################################
# Main Logic

deployed = [] # 배치된 오브젝트 리스트

class Block:
    # 배치
    def __init__(self, type, location, radius):
        self.type = type
        self.location = location
        self.radius = radius

        if deployed == []:
            typewrite("System : " +self.type+ "이 " +str(self.location)+ " 에 배치되었습니다.", gap)
            deployed.append([self.type,self.location, self.radius])
        else:
            flag = True # flag 알고리즘
            for obj in deployed: # 블록끼리 겹치지 않게 하기
                if abs(self.location[0] - obj[1][0]) >= obj[2] + self.radius\
                    or abs(self.location[1] - obj[1][1]) >= obj[2] + self.radius\
                    or abs(self.location[2] - obj[1][2]) >= obj[2] + self.radius:
                    continue
                else:
                    flag = False
                    break

            if flag == True:
                typewrite("System : " +self.type+ "이 " +str(self.location)+ " 에 배치되었습니다.", gap)
                deployed.append([self.type, self.location, self.radius])
            elif flag == False:
                typewrite("System : 블록을 배치하려는 공간이 다른 블록과 겹쳐져 있습니다.\
                     위치나 크기를 재설정하십시오.", gap)

    # 삭제
    def remove(self):
        ex_location = deployed.index([self.type, self.location, self.radius])
        deployed.pop(ex_location)
        typewrite("System : "+self.type+"이 삭제되었습니다.", gap)

    #재배치 = 삭제 + 배치
    def relocation(self, new_location):
        ex_location = deployed.index([self.type, self.location, self.radius])
        deployed.pop(ex_location) # 기존 블록 삭제
        self.location = new_location

        if deployed == []:
            typewrite("System : " +self.type+ "이 " +str(self.location)+ " 로 재배치되었습니다.", gap)
            deployed.append([self.type,self.location, self.radius])
        else:
            flag = True # flag 알고리즘
            for obj in deployed: # 블록끼리 겹치지 않게 하기
                if abs(self.location[0] - obj[1][0]) >= obj[2] + self.radius\
                    or abs(self.location[1] - obj[1][1]) >= obj[2] + self.radius\
                    or abs(self.location[2] - obj[1][2]) >= obj[2] + self.radius:
                    continue
                else:
                    flag = False
                    break

            if flag == True:
                typewrite("System : " +self.type+ "이 " +str(self.location)+ " 로 재배치되었습니다.", gap)
                deployed.append([self.type, self.location, self.radius])
            elif flag == False:
                typewrite("System : 블록을 재배치하려는 공간이 다른 블록과 겹쳐져 있습니다.\
                     위치나 크기를 재설정하십시오.", gap)

##############################################
# Control
# typewrite("Block", 0.5)
# time.sleep(1)
while True:
    menu_answer = question("\n1.생성\t2.삭제\t3.배치\t4.종료 ", 0.1)
    if menu_answer == str(1):
        self = question("블록의 영어이름을 입력하시오. ", 0.1)
        type = question("블록의 이름을 입력하시오. ", 0.1)
        location = question("블록의 위치를 입력하시오.(리스트) ", 0.1)
        scale = question("블록 한 변의 길이를 입력하시오. ", 0.1)
        self = Block(type, list(location), float(scale/2))






# 실행문

nether_wart_block = Block("네더 와트 블록", [9,9,9], 1/40)

nether_wart_block.relocation([13,1,3])
print(deployed)
nether_wart_block.remove()
print(deployed)

import time

print("\n안녕하세요? ^^")
time.sleep(2)
print("\n이 프로그램은 고객님의 키와 성별을 통해 표준 체중을 구해드립니다.")
time.sleep(4)
print("\n그리고 모든 기록은 서버에 \"영구저장\" 됨을 유의하시기 바랍니다. ^^")
time.sleep(2)

# 키
while True:
   height = input("\n고객님의 키는? ")
   time.sleep(1)
   try:
      height = float(height)
   except ValueError:
      print("\n숫자만 입력하세요. 凸ಠ益ಠ)凸")
      time.sleep(1)
   else:
      print("\n입력 완료!!")
      time.sleep(2)
      break

# 성별
while True:
   gender = input("\n남성이라면 1, 여성이라면 2, 중성이라면 3을 누르세요. ")
   time.sleep(1)
   if gender == "1" or gender == "2":
      print("\n입력 완료!!")
      time.sleep(2)
      break
   elif gender == "3":
      print("\nWTF")
      time.sleep(0.5)
   else:
      print("\nWTF")
      time.sleep(0.5)

# 표준체중 함수
def std_weight(height, gender):
   if gender == "1":
      need_to_be_this_heavy = round(((height / 100) ** 2 * 22) * 100) / 100
      gender2 = "남자"
   elif gender == "2":
      need_to_be_this_heavy = round(((height / 100) ** 2 * 21) * 100) / 100
      gender2 = "여자"
   print("\n키 {0}cm {1}의 표준 체중은 {2}kg 입니다.".format(height, gender2, need_to_be_this_heavy))

std_weight(height, gender)
time.sleep(1)
print("\n살 좀 빼셔야겠어요. ^^")

import time

text = "hidfasdaf"
dead_time = 0.3

def autotype(text, dead_time):
    length = len(text)
    for i in range(0, length):
        print(text[i], end = "")
        time.sleep(dead_time)

autotype(text, dead_time)

# text = "WTF"
# print(text[0], end = "")
# time.sleep(1)
# print(text[1], end = "")
# time.sleep(1)
# print(text[2], end = "")

# Typewriter

import time

GAP = 0.05

# print
def typewrite(text, GAP):
    length = len(text)
    for i in range(0, length):
        print(text[i], end = "")
        time.sleep(GAP)
    print("")
    
# input
def question(text, GAP):
    length = len(text)
    for i in range(0, length - 1):
        print(text[i], end = "")
        time.sleep(GAP)
    answer = input(text[-1])
    return answer

##################################################

# Control

typewrite("Block", 0.1)
time.sleep(1)

deployed = []
while True:
    menu_answer = question("\n1.배치\t2.삭제\t3.재배치\t4.종료 ", GAP)
    print("")
    # 배치
    if menu_answer == "1":
        name = question("블록의 이름 : ", GAP)
        x = int(question("블록의 x 좌표(정수) : ", GAP))
        y = int(question("블록의 y 좌표(정수) : ", GAP))
        z = int(question("블록의 z 좌표(정수) : ", GAP))
        location = [x, y, z]
        radius = int(question("블록 한 변의 길이(정수) : ", GAP)) / 2

        flag = True # flag 알고리즘
        for obj in deployed: # 블록끼리 겹치지 않게 하기
            if abs(location[0] - obj[1][0]) >= obj[2] + radius\
                or abs(location[1] - obj[1][1]) >= obj[2] + radius\
                or abs(location[2] - obj[1][2]) >= obj[2] + radius:
                continue
            else:
                flag = False
                break

        if flag == True:
            typewrite("\nSystem : " + name + "이 " + str(location) + " 에 배치되었습니다.", GAP)
            deployed.append([name, location, radius])
            print("[이름, [x, y, z], 반지름] : {0}".format(deployed))
        elif flag == False:
            typewrite("\nSystem : 블록을 배치하려는 공간이 다른 블록과 겹쳐져 있습니다. 위치나 크기를 재설정하십시오.", GAP)
            print("[이름, [x, y, z], 반지름] : {0}".format(deployed))

    # 삭제
    elif menu_answer == "2":
        typewrite("몇 번째 블록을 지우시겠습니까?", GAP)
        will_be_deleted = int(input("[이름, [x, y, z], 반지름] : {0} ".format(deployed))) - 1
        deployed.pop(will_be_deleted)
        typewrite("\nSystem : " + name + "이 삭제되었습니다.", GAP)
        print("[이름, [x, y, z], 반지름] : {0}".format(deployed))

    # 재배치
    elif menu_answer == "3":
        typewrite("몇 번째 블록을 재배치하시겠습니까?", GAP)
        will_be_relocated = int(input("[이름, [x, y, z], 반지름] : {0} ".format(deployed))) - 1
        name = deployed[will_be_relocated][0]
        x = int(question("재배치될 x 좌표(정수) : ", GAP))
        y = int(question("재배치될 y 좌표(정수) : ", GAP))
        z = int(question("재배치될 z 좌표(정수) : ", GAP))
        location = [x, y, z]
        radius = deployed[will_be_relocated][2]
        deployed.pop(will_be_relocated)

        flag = True # flag 알고리즘
        for obj in deployed: # 블록끼리 겹치지 않게 하기
            if abs(location[0] - obj[1][0]) >= obj[2] + radius\
                or abs(location[1] - obj[1][1]) >= obj[2] + radius\
                or abs(location[2] - obj[1][2]) >= obj[2] + radius:
                continue
            else:
                flag = False
                break

        if flag == True:
            typewrite("\nSystem : " + name + "이 " + str(location) + " 로 재배치되었습니다.", GAP)
            deployed.append([name, location, radius])
            print("[이름, [x, y, z], 반지름] : {0}".format(deployed))
        elif flag == False:
            typewrite("\nSystem : 블록을 재배치하려는 공간이 다른 블록과 겹쳐져 있습니다. 위치나 크기를 재설정하십시오.", GAP)

    # 종료
    elif menu_answer == "4":
        typewrite("System : Block 을 이용해주셔서 감사합니다.", GAP)
        time.sleep(1)
        break