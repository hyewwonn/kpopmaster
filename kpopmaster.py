print("""

██╗  ██╗██████╗  ██████╗ ██████╗ 
██║ ██╔╝██╔══██╗██╔═══██╗██╔══██╗
█████╔╝ ██████╔╝██║   ██║██████╔╝
██╔═██╗ ██╔═══╝ ██║   ██║██╔═══╝ 
██║  ██╗██║     ╚██████╔╝██║     
╚═╝  ╚═╝╚═╝      ╚═════╝ ╚═╝    
███╗   ███╗ █████╗ ███████╗████████╗███████╗██████╗ 
████╗ ████║██╔══██╗██╔════╝╚══██╔══╝██╔════╝██╔══██╗
██╔████╔██║███████║███████╗   ██║   █████╗  ██████╔╝
██║╚██╔╝██║██╔══██║╚════██║   ██║   ██╔══╝  ██╔══██╗
██║ ╚═╝ ██║██║  ██║███████║   ██║   ███████╗██║  ██║
╚═╝     ╚═╝╚═╝  ╚═╝╚══════╝   ╚═╝   ╚══════╝╚═╝  ╚═╝                     
                            
=========================================
|     1. QUIZ   2. BINGO   3. 종료      |
=========================================           

        """)
qb = 0
while qb != 1 and qb != 2 and qb != 3:
    qb = int(input("선택 : "))
    if qb != 1 and qb != 2 and qb != 3:
        print("잘못된 입력입니다.")

if qb == 1:
    print("\nQUIZ")
    qdifficulty = 0
    qnumber = 0
    while qdifficulty != 1 and qdifficulty !=2 and qdifficulty != 3:
        qdifficulty = int(input("\n문제 난이도 선택\n상- 1  중- 2  하- 3 : "))
    while qnumber != 1 and qnumber !=2 and qnumber != 3:
        qnumber = int(input("\n문제 개수 선택\n10개- 1  20개- 2  30개- 3 : "))
    qnumber *= 10

    qcorrect = 0
    for i in range (1, qnumber+1):
        print("문제", i)
        print("정답 입력 : ")

elif qb == 2:
    print("\nBINGO")
    byear = 0
    bindex = 0
    banswer = ""
    banswercount = 0
    bingocount = 0
    banswerlist = [["▢","▢","▢","▢","▢","▢","▢"],
    ["▢","▢","▢","▢","▢","▢","▢"],
    ["▢","▢","▢","▢","▢","▢","▢"],
    ["▢","▢","▢","▢","▢","▢","▢"],
    ["▢","▢","▢","▢","▢","▢","▢"],
    ["▢","▢","▢","▢","▢","▢","▢"],
    ["▢","▢","▢","▢","▢","▢","▢"]]
    bqlist10 = ["다시 만난 세계","애상","오락실","No.1","Tell Me","누난 너무 예뻐","아틀란티스 소녀",
    "왜 불러","U R Man","캔디","비밀번호 486","Nobody","로꾸거!!","나혼자",
    "토요일밤에","Electric Shock","좋은 날","Bubble Pop!","사랑비","A","잘자요 굿나잇",
    "Lucifer","Sorry, Sorry","난리나","Sign","왜","행복","검은 고양이",
    "커플","주문","내꺼하자","Gee","외톨이야","후유증","내 귀에 캔디",
    "Shy Boy","U-Go-Girl","10점 만점에 10점","Bo Peep Bo Peep","사랑앓이","Mr.Simple","미스터",
    "Kissing You","비밀","내 남자친구에게","태양을 피하는 방법","영원한 사랑","Pretty girl","내 머리가 나빠서"]
    balist10 = ["소녀시대","쿨","한스밴드","보아","원더걸스","샤이니","보아",
    "디바","더블에스오공일","에이치오티","윤하","원더걸스","슈퍼주니어","씨스타",
    "손담비","에프엑스","아이유","현아","김태우","레인보우","비원에이포",
    "샤이니","슈퍼주니어","블락비","브라운아이드걸스","동방신기","에이치오티","터보",
    "젝스키스","동방신기","인피니트","소녀시대","씨엔블루","제국의아이들","백지영",
    "시크릿","이효리","투피엠","티아라","에프티아일랜드","슈퍼주니어","카라",
    "소녀시대","비투비","핑클","비","핑클","카라","더블에스오공일"]
    while byear != 1 and byear !=2 and byear != 3:
        byear = int(input("\n연도 선택\n~2012년- 1  ~2016년- 2  ~2022년- 3 : "))    

        print("""


                  ____   ___  _ ____    ____ ___ _   _  ____  ___  
                 |___ \ / _ \/ |___ \  | __ )_ _| \ | |/ ___|/ _ \ 
                   __) | | | | | __) | |  _ \| ||  \| | |  _| | | |
                  / __/| |_| | |/ __/  | |_) | || |\  | |_| | |_| |
                 |_____|\___/|_|_____| |____/___|_| \_|\____|\___/ 
          
            _______________________________________________________
            |       |       |       |       |       |       |       |
            |다시만 | 애상  |오락실 | No.1  |Tell Me|누난 너|아틀란 |
            |   1   |   2   |   3   |   4   |   5   |   6   |   7   |
            |-------|-------|-------|-------|-------|-------|-------|
            |왜 불러|U R Man| 캔디  |비밀번 |Nobody |로꾸거!|나혼자 |
            |   8   |   9   |  10   |  11   |  12   |  13   |  14   |
            |-------|-------|-------|-------|-------|-------|-------|
            |토요일 |Electri|좋은 날|Bubble |사랑비 |   A   |잘자요 |
            |  15   |  16   |  17   |  18   |  19   |  20   |  21   |
            |-------|-------|-------|-------|-------|-------|-------|
            |Lucifer|Sorry, |난리나 |  Sign |  왜   | 행복  |검은 고|
            |  22   |  23   |  24   |  25   |  26   |  27   |  28   |
            |-------|-------|-------|-------|-------|-------|-------|
            | 커플  | 주문  |내꺼하 |  Gee  |외톨이 |후유증 |내 귀에|
            |  29   |  30   |  31   |  32   |  33   |  34   |  35   |
            |-------|-------|-------|-------|-------|-------|-------|
            |Shy Boy|U Go Gi|10점 만|Bo Peep|사랑앓 |Mr.Simp|미스터 |
            |  36   |  37   |  38   |  39   |  40   |  41   |  42   |
            |-------|-------|-------|-------|-------|-------|-------|
            |Kissing| 비밀  |내 남자|태양을 |영원한 |Pretty |내 머리|
            |  43   |  44   |  45   |  46   |  47   |  48   |  49   |
            |_______|_______|_______|_______|_______|_______|_______|

            

        """)
        while bindex != -1:
            for i in range(0,7):
                for j in range(0,7):
                    print(banswerlist[i][j], end=" ")
                print("\n")

            # while bindex != 1 and bindex != 2 and bindex != 3:
            bindex = int(input("\n칸 선택(종료- -1 빙고판 보기- 50) : "))
            if bindex == -1:
                break
            elif bindex == 50:
                print("""


                 ____   ___  _ ____    ____ ___ _   _  ____  ___  
                |___ \ / _ \/ |___ \  | __ )_ _| \ | |/ ___|/ _ \ 
                  __) | | | | | __) | |  _ \| ||  \| | |  _| | | |
                 / __/| |_| | |/ __/  | |_) | || |\  | |_| | |_| |
                |_____|\___/|_|_____| |____/___|_| \_|\____|\___/ 
        
            _______________________________________________________
            |       |       |       |       |       |       |       |
            |다시만 | 애상  |오락실 | No.1  |Tell Me|누난 너|아틀란 |
            |   1   |   2   |   3   |   4   |   5   |   6   |   7   |
            |-------|-------|-------|-------|-------|-------|-------|
            |왜 불러|U R Man| 캔디  |비밀번 |Nobody |로꾸거!|나혼자 |
            |   8   |   9   |  10   |  11   |  12   |  13   |  14   |
            |-------|-------|-------|-------|-------|-------|-------|
            |토요일 |Electri|좋은 날|Bubble |사랑비 |   A   |잘자요 |
            |  15   |  16   |  17   |  18   |  19   |  20   |  21   |
            |-------|-------|-------|-------|-------|-------|-------|
            |Lucifer|Sorry, |난리나 |  Sign |  왜   | 행복  |검은 고|
            |  22   |  23   |  24   |  25   |  26   |  27   |  28   |
            |-------|-------|-------|-------|-------|-------|-------|
            | 커플  | 주문  |내꺼하 |  Gee  |외톨이 |후유증 |내 귀에|
            |  29   |  30   |  31   |  32   |  33   |  34   |  35   |
            |-------|-------|-------|-------|-------|-------|-------|
            |Shy Boy|U Go Gi|10점 만|Bo Peep|사랑앓 |Mr.Simp|미스터 |
            |  36   |  37   |  38   |  39   |  40   |  41   |  42   |
            |-------|-------|-------|-------|-------|-------|-------|
            |Kissing| 비밀  |내 남자|태양을 |영원한 |Pretty |내 머리|
            |  43   |  44   |  45   |  46   |  47   |  48   |  49   |
            |_______|_______|_______|_______|_______|_______|_______|

            

                """)
                bindex = int(input("\n칸 선택 (종료- -1) : "))
                if bindex == -1 :
                    break
            elif bindex<0 or bindex>50:
                print("잘못된 입력입니다.")

            print(f"\n{bindex}번 - {bqlist10[bindex-1]} 의 가수는?")
            banswer = input("한글로 입력, 유닛명 생략 : ")
            if banswer == balist10[bindex-1]:
                print("\n정답!")
                banswerlist[(bindex-1) // 7][((bindex) % 7)-1] = "■"
            else:
                print("\n땡!")

            banswercount = 0
            for i in range(0,7):
                for j in range(0,7):
                    if banswerlist[i][j] == "■":
                        banswercount += 1

            if banswercount == 49:
                break


        if banswerlist[0][0] == "■" and banswerlist[0][1] == "■" and banswerlist[0][2] == "■" and banswerlist[0][3] == "■" and banswerlist[0][4] == "■" and banswerlist[0][5] == "■" and banswerlist[0][6] == "■":
            bingocount+=1
        if banswerlist[1][0] == "■" and banswerlist[1][1] == "■" and banswerlist[1][2] == "■" and banswerlist[1][3] == "■" and banswerlist[1][4] == "■" and banswerlist[1][5] == "■" and banswerlist[1][6] == "■":
            bingocount+=1
        if banswerlist[2][0] == "■" and banswerlist[2][1] == "■" and banswerlist[2][2] == "■" and banswerlist[2][3] == "■" and banswerlist[2][4] == "■" and banswerlist[2][5] == "■" and banswerlist[2][6] == "■":
            bingocount+=1
        if banswerlist[3][0] == "■" and banswerlist[3][1] == "■" and banswerlist[3][2] == "■" and banswerlist[3][3] == "■" and banswerlist[3][4] == "■" and banswerlist[3][5] == "■" and banswerlist[3][6] == "■":
            bingocount+=1
        if banswerlist[4][0] == "■" and banswerlist[4][1] == "■" and banswerlist[4][2] == "■" and banswerlist[4][3] == "■" and banswerlist[4][4] == "■" and banswerlist[4][5] == "■" and banswerlist[4][6] == "■":
            bingocount+=1
        if banswerlist[5][0] == "■" and banswerlist[5][1] == "■" and banswerlist[5][2] == "■" and banswerlist[5][3] == "■" and banswerlist[5][4] == "■" and banswerlist[5][5] == "■" and banswerlist[5][6] == "■":
            bingocount+=1
        if banswerlist[6][0] == "■" and banswerlist[6][1] == "■" and banswerlist[6][2] == "■" and banswerlist[6][3] == "■" and banswerlist[6][4] == "■" and banswerlist[6][5] == "■" and banswerlist[6][6] == "■":
            bingocount+=1

        if banswerlist[0][0] == "■" and banswerlist[1][0] == "■" and banswerlist[2][0] == "■" and banswerlist[3][0] == "■" and banswerlist[4][0] == "■" and banswerlist[5][0] == "■" and banswerlist[6][0] == "■":
            bingocount+=1
        if banswerlist[0][1] == "■" and banswerlist[1][1] == "■" and banswerlist[2][1] == "■" and banswerlist[3][1] == "■" and banswerlist[4][1] == "■" and banswerlist[5][1] == "■" and banswerlist[6][1] == "■":
            bingocount+=1
        if banswerlist[0][2] == "■" and banswerlist[1][2] == "■" and banswerlist[2][2] == "■" and banswerlist[3][2] == "■" and banswerlist[4][2] == "■" and banswerlist[5][2] == "■" and banswerlist[6][2] == "■":
            bingocount+=1
        if banswerlist[0][3] == "■" and banswerlist[1][3] == "■" and banswerlist[2][3] == "■" and banswerlist[3][3] == "■" and banswerlist[4][3] == "■" and banswerlist[5][3] == "■" and banswerlist[6][3] == "■":
            bingocount+=1
        if banswerlist[0][4] == "■" and banswerlist[1][4] == "■" and banswerlist[2][4] == "■" and banswerlist[3][4] == "■" and banswerlist[4][4] == "■" and banswerlist[5][4] == "■" and banswerlist[6][4] == "■":
            bingocount+=1
        if banswerlist[0][5] == "■" and banswerlist[1][5] == "■" and banswerlist[2][5] == "■" and banswerlist[3][5] == "■" and banswerlist[4][5] == "■" and banswerlist[5][5] == "■" and banswerlist[6][5] == "■":
            bingocount+=1
        if banswerlist[0][6] == "■" and banswerlist[1][6] == "■" and banswerlist[2][6] == "■" and banswerlist[3][6] == "■" and banswerlist[4][6] == "■" and banswerlist[5][6] == "■" and banswerlist[6][6] == "■":
            bingocount+=1

        if banswerlist[0][0] == "■" and banswerlist[1][1] == "■" and banswerlist[2][2] == "■" and banswerlist[3][3] == "■" and banswerlist[4][4] == "■" and banswerlist[5][5] == "■" and banswerlist[6][6] == "■":
            bingocount+=1
        if banswerlist[0][6] == "■" and banswerlist[1][5] == "■" and banswerlist[2][4] == "■" and banswerlist[3][3] == "■" and banswerlist[4][2] == "■" and banswerlist[5][1] == "■" and banswerlist[6][0] == "■":
            bingocount+=1

        if bingocount == 16:
            print("""
                 __        _   _ 
  _ __  ___ _ _ / _|___ __| |_| |
 | '_ \/ -_) '_|  _/ -_) _|  _|_|
 | .__/\___|_| |_| \___\__|\__(_)
 |_|                 
            """)
    print(bingocount, "빙고")

    if byear == 2:
        print("""
                 ____   ___  _  __     ____ ___ _   _  ____  ___  
                |___ \ / _ \/ |/ /_   | __ )_ _| \ | |/ ___|/ _ \ 
                  __) | | | | | '_ \  |  _ \| ||  \| | |  _| | | |
                 / __/| |_| | | (_) | | |_) | || |\  | |_| | |_| |
                |_____|\___/|_|\___/  |____/___|_| \_|\____|\___/ 
          
            _______________________________________________________
            |       |       |       |       |       |       |       |
            |       |       |       |       |       |       |       |
            |   1   |   2   |   3   |   4   |   5   |   6   |   7   |
            |-------|-------|-------|-------|-------|-------|-------|
            |       |       |       |       |       |       |       |
            |   8   |   9   |  10   |  11   |  12   |  13   |  14   |
            |-------|-------|-------|-------|-------|-------|-------|
            |       |       |       |       |       |       |       |
            |  15   |  16   |  17   |  18   |  19   |  20   |  21   |
            |-------|-------|-------|-------|-------|-------|-------|
            |       |       |       |       |       |       |       |
            |  22   |  23   |  24   |  25   |  26   |  27   |  28   |
            |-------|-------|-------|-------|-------|-------|-------|
            |       |       |       |       |       |       |       |
            |  29   |  30   |  31   |  32   |  33   |  34   |  35   |
            |-------|-------|-------|-------|-------|-------|-------|
            |       |       |       |       |       |       |       |
            |  36   |  37   |  38   |  39   |  40   |  41   |  42   |
            |-------|-------|-------|-------|-------|-------|-------|
            |       |       |       |       |       |       |       |
            |  43   |  44   |  45   |  46   |  47   |  48   |  49   |
            |_______|_______|_______|_______|_______|_______|_______|

        """)
    if byear == 3:
        print("""
               ____   ___ ____  ____    ____ ___ _   _  ____  ___  
              |___ \ / _ \___ \|___ \  | __ )_ _| \ | |/ ___|/ _ \ 
                __) | | | |__) | __) | |  _ \| ||  \| | |  _| | | |
               / __/| |_| / __/ / __/  | |_) | || |\  | |_| | |_| |
              |_____|\___/_____|_____| |____/___|_| \_|\____|\___/ 
          
            _______________________________________________________
            |       |       |       |       |       |       |       |
            |       |       |       |       |       |       |       |
            |       |       |       |       |       |       |       |
            |-------|-------|-------|-------|-------|-------|-------|
            |       |       |       |       |       |       |       |
            |       |       |       |       |       |       |       |
            |-------|-------|-------|-------|-------|-------|-------|
            |       |       |       |       |       |       |       |
            |       |       |       |       |       |       |       |
            |-------|-------|-------|-------|-------|-------|-------|
            |       |       |       |       |       |       |       |
            |       |       |       |       |       |       |       |
            |-------|-------|-------|-------|-------|-------|-------|
            |       |       |       |       |       |       |       |
            |       |       |       |       |       |       |       |
            |-------|-------|-------|-------|-------|-------|-------|
            |       |       |       |       |       |       |       |
            |       |       |       |       |       |       |       |
            |-------|-------|-------|-------|-------|-------|-------|
            |       |       |       |       |       |       |       |
            |       |       |       |       |       |       |       |
            |_______|_______|_______|_______|_______|_______|_______|

        """)
        

elif qb == 3:
    print("종료합니다.")
