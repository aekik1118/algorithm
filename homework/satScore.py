
# 학생성적정보 클래스 : 수험번호, 이름, 성별, 출신고, 탐구선택과목, 국어점수, 영어점수, 수학점수, 탐구1점수, 탐구2점수를 저장한다
class StudentScores:
    def __init__(self, studentNumber, name, gender, highschool, subjectList, korean, english, math, subject1, subject2):
        self.studentNumber = studentNumber
        self.name = name
        self.gender = gender
        self.highschool = highschool
        self.subjectList = subjectList
        self.korean = korean
        self.english = english
        self.math = math
        self.subject1 = subject1
        self.subject2 = subject2


#모든 학생들의 성적정보를 저장해두는 리스트
StudentScoresList = []


#StudentScoresList에 더미 성적 데이터를 넣어주는 함수
def init():
    StudentScoresList.append(StudentScores('1',"더미1","남","충북고",["화학1", "생물1"],75,80,75,40,28))
    StudentScoresList.append(StudentScores('2',"더미2","남","충북고",["화학1", "생물1"],74,88,92,40,23))
    StudentScoresList.append(StudentScores('3',"더미3","남","충북고",["물리1", "생물1"],16,83,89,16,18))
    StudentScoresList.append(StudentScores('4',"더미4","남","충북고",["물리1", "생물1"],75,80,24,40,30))
    StudentScoresList.append(StudentScores('5',"더미5","남","충북고",["생물1","화학1"],70,85,55,16,33))
    StudentScoresList.append(StudentScores('6',"더미6","여","충북여고",["화학1", "생물1"],90,56,43,41,36))
    StudentScoresList.append(StudentScores('7',"더미7","여","충북여고",["화학1", "생물1"],100,80,12,42,15))
    StudentScoresList.append(StudentScores('8',"더미8","여","충북여고",["화학1", "생물1"],24,100,90,43,50))
    StudentScoresList.append(StudentScores('9',"더미9","여","충북여고",["화학1", "생물1"],77,80,90,43,40))
    StudentScoresList.append(StudentScores('10',"더미10","여","충북여고",["화학1", "지구과학1"],42,77,42,45,32))


#성적 데이터를 직접 입력하는 경우
def inputScore():
    studentNumber = input("수험번호 입력 : ")
    name = input("이름 입력 : ")
    gender = input("성별 입력 : ")
    highschool = input("출신고등학교 입력 : ")

    print("탐구선택과목은 물리1, 화학1, 생물1, 지구과학1이 존재합니다")
    subject1Name = input("첫번째 탐구 과목 이름 입력 : ")
    subject2Name = input("두번째 탐구 과목 이름 입력 : ")
    subjectList = [subject1Name,subject2Name]

    korean = int(input("국어 원점수 입력 : "))
    english = int(input("영어 원점수 입력 : "))
    math = int(input("수학 원점수 입력 : "))
    subject1 = int(input("탐구 과목1 원점수 입력 : "))
    subject2 = int(input("탐구 과목2 원점수 입력 : "))

    StudentScoresList.append(StudentScores(studentNumber, name, gender, highschool, subjectList, korean, english, math, subject1, subject2))
    print("입력이 완료되었습니다")
    print()


#성적을 입력하면 절대등급을 반환해주는 함수
def ratingByScore(score):
    if score >= 90:
        return 1
    if score >= 80:
        return 2
    if score >= 70:
        return 3
    if score >= 60:
        return 4
    if score >= 50:
        return 5
    if score >= 40:
        return 6
    if score >= 30:
        return 7
    if score >= 20:
        return 8
    return 9

#탐구영역 성적을 입력하면 절대등급을 반환해주는 함수
def subjectRatingByScore(score):
    if score >= 45:
        return 1
    if score >= 40:
        return 2
    if score >= 35:
        return 3
    if score >= 30:
        return 4
    if score >= 25:
        return 5
    if score >= 20:
        return 6
    if score >= 15:
        return 7
    if score >= 10:
        return 8
    return 9


#subjectName 과목의 score 점수의 백분위를 반환해주는 함수
def getPercentage(subjectName, score):

    #score보다 낮은 사람들의 수
    lowerScoreCnt = 0

    #score와 동점인 사람들의 수
    equleScoreCnt = 0

    for i in StudentScoresList:
        cmpScore = -1
        if subjectName == "국어":
            cmpScore = i.korean
        if subjectName == "영어":
            cmpScore = i.english
        if subjectName == "수학":
            cmpScore = i.math
        if subjectName == i.subjectList[0]:
            cmpScore = i.subject1
        if subjectName == i.subjectList[1]:
            cmpScore = i.subject2

        if score > -1:
            if cmpScore == score:
                equleScoreCnt += 1
            if cmpScore < score:
                lowerScoreCnt += 1

    return (((lowerScoreCnt) + (equleScoreCnt/2))/len(StudentScoresList))*100

#studentNumber 수험번호의 성적표 출력 함수
def printGradeCard(studentNumber):
    for i in StudentScoresList:
        if i.studentNumber == studentNumber:
            print()
            print("============================================================")
            print(i.name+"의 성적표 입니다")
            print("출신학교: ", i.highschool)
            print("성별: ", i.gender)
            print("국어 등급:", ratingByScore(i.korean))
            print("국어 백분율:", getPercentage("국어", i.korean))
            print("영어 등급:", ratingByScore(i.english))
            print("영어 백분율:", getPercentage("영어", i.english))
            print("수학 등급:", ratingByScore(i.math))
            print("수학 백분율:", getPercentage("수학", i.math))
            print(i.subjectList[0],"등급:", subjectRatingByScore(i.subject1))
            print(i.subjectList[0],"백분율:", getPercentage(i.subjectList[0], i.subject1))
            print(i.subjectList[1],"등급:", subjectRatingByScore(i.subject2))
            print(i.subjectList[1],"백분율:", getPercentage(i.subjectList[1], i.subject2))
            print("============================================================")
            print()


#현재 입력되어있는 학생들의 수험번호와 이름 출력 함수
def printStudents():
    for i in StudentScoresList:
        print("수험번호 :", i.studentNumber,"이름 :",i.name )


#main 실행 부분
init()

while True:
    print("----------------------------------")
    print("수능성적 처리 프로그램입니다.")
    print("명령을 입력해주세요")
    print("1. 현재 등록된 학생의 리스트 출력")
    print("2. 새로운 학생 등록하기")
    print("3. 성적표 조회")
    print("9. 프로그램 종료")
    print("----------------------------------")
    e = input("명령을 입력하세요 :")

    if e == '1':
        printStudents()
    if e == '2':
        inputScore()
    if e == '3':
        studentNumber = input("확인하고 싶은 학생의 수험번호 입력 : ")
        printGradeCard(studentNumber)
    if e == '9':
        break
