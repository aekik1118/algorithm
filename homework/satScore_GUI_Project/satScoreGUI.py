from tkinter import *
from tkinter import ttk


# 파일 저장버튼, 학생 추가 버튼, 수정 버튼, 삭제 버튼, 검색 창(수험번호), 전체리스트 확인, 더미데이터 추가 버튼

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

    def getStudentNumber(self):
        return self.studentNumber

    def getName(self):
        return self.name

    def getGender(self):
        return self.gender

    def getHighschool(self):
        return self.highschool

    def getSubjectList(self):
        return self.subjectList

    def getKorean(self):
        return self.korean

    def getEnglish(self):
        return self.english

    def getMath(self):
        return self.math

    def getSubject1(self):
        return self.subject1

    def getSubject2(self):
        return self.subject2

    def setStudnetNumber(self, studentNumber):
        self.studentNumber = studentNumber

    def setName(self, name):
        self.name = name

    def setGender(self, gender):
        self.gender = gender

    def setHighschool(self, highschool):
        self.highschool = highschool

    def setSubjectList(self, subjectList):
        self.subjectList = subjectList

    def setKorean(self, korean):
        self.korean = korean

    def setEnglish(self, english):
        self.english = english

    def setMath(self, math):
        self.math = math

    def setSubject1(self, subject1):
        self.subject1 = subject1

    def setSubject2(self, subject2):
        self.subject2 = subject2


class StudentRepository:
    def __init__(self, dbList ,dbFilename):
        self.__dbList = dbList
        self.__dbFilename = dbFilename

    def loadDB(self):
        f = open(self.__dbFilename ,"rt", encoding="UTF=8")
        lines = f.readlines()

        for line in lines:
            StuArgsList = line.strip().split(",")
            self.__dbList.append(StudentScores(StuArgsList[0],
                                               StuArgsList[1],
                                               StuArgsList[2],
                                               StuArgsList[3],
                                               [StuArgsList[4], StuArgsList[5]],
                                               StuArgsList[6],
                                               StuArgsList[7],
                                               StuArgsList[8],
                                               StuArgsList[9],
                                               StuArgsList[10]))

    def saveDB(self):
        f = open(self.__dbFilename ,"wt", encoding="UTF=8")
        for i in self.__dbList:
            data = "{0},{1},{2},{3},{4},{5},{6},{7},{8},{9},{10},".format(
                i.getStudentNumber(),
                i.getName(),
                i.getGender(),
                i.getHighschool(),
                i.getSubjectList()[0],
                i.getSubjectList()[1],
                i.getKorean(),
                i.getEnglish(),
                i.getMath(),
                i.getSubject1(),
                i.getSubject2())

            f.writelines(data+"\n")


#모든 학생들의 성적정보를 저장해두는 리스트
StudentScoresList = []

studentRepository = StudentRepository(StudentScoresList, "studentDB.csv")
studentRepository.loadDB()

StudentScoresList[0].setName("test")

studentRepository.saveDB()