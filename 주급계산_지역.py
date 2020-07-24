"""
리스트를 갖고 다니면 힘들다
dict 타입이 무난하고 편하다
이름, 근무시간, 시간당급여액, 총액, 수당, 세금
"""
dataList = list()   #전역변수로 사용

#함수는 입력-계산-출력

def append(dataList):
    #아래 global dataList 줄을 없애고 전역변수를 사용하지 않고 전역변수로 사용하던 dataList를 함수의 Argument에 넣어준다.
    #global dataList #전역변수를 함수 내에서 사용 - 함수간에 공유 메모리
    while True:
            
        temp = dict()
        temp['name']=input("이름 :")
        temp['worktime']=int(input("근무시간 :"))
        temp['perpay']=int(input("시간당급여액 :"))

        dataList.append(temp)
        again = input("계속? (1:yes / 2:no) :")
        if again!="1":
            break
        # break는 조건식을 종료하는 것이고
        # return은 함수를 종료하는 것이다. 여기서는 둘다 동일한 효과 

def output(dataList):
    #아래 global dataList 줄을 없애고 전역변수를 사용하지 않고 전역변수로 사용하던 dataList를 함수의 Argument에 넣어준다.
    #global dataList
    for data in dataList:
        print(data['name'], end='\t')
        print(data['worktime'], end='\t')
        print(data['perpay'],end='\t')
        print(data['pay'],end='\n')

def process(dataList):
    #아래 global dataList 줄을 없애고 전역변수를 사용하지 않고 전역변수로 사용하던 dataList를 함수의 Argument에 넣어준다.
    #global dataList
    for data in dataList:
        data['pay']= data['worktime'] * data['perpay']

def start(dataList):
    while True:
        print("1:추가 / 2:출력 / 0:종료")
        menu = input("선택: ")
        if menu=="1":
            append(dataList)
        elif menu=="2":
            process(dataList)
            output(dataList)
        elif menu=="0":
            return
        else:
            print("1:추가 / 2:출력 / 0:종료  <=== 메뉴에서 선택하세요")
            return
start(dataList)
# 전역변수를 사용하지 않는 대신 argument로 넣어서 사용하게 된다.

# 제일 먼저 입력받아 값을 담는 함수 append()를 작성하고, 입력받아 담은 값들이 원하는대로 되는지 보기 위해 임시 output() 함수를 작성한다
# 원하는 값들이 입력받아지고 저장된 값들을 출력할 수 있으면 process() 함수를 작성하여 계산을 한 값들이 반영되도록 한다.
# 입력-처리된 값들이 최종적으로 출력될 수 있도록 output() 함수를 수정 적용하여 마무리한다