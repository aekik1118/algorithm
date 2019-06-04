from tkinter import *
from tkinter import ttk
import tkinter


#모든 학생들의 성적정보를 저장해두는 리스트
StudentScoresList = []

# 파일 저장버튼, 학생 추가 버튼, 수정 버튼, 삭제 버튼, 검색 창(수험번호), 전체리스트 확인

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





window = tkinter.Tk()
window.title("수능 성적처리 프로그램")
window.geometry("1280x480+100+100")
window.resizable(False, False)

# 성적을 입력하면 절대등급을 반환해주는 함수
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

# 탐구영역 성적을 입력하면 절대등급을 반환해주는 함수
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

# subjectName 과목의 score 점수의 백분위를 반환해주는 함수
def getPercentage(subjectName, score):
    # score보다 낮은 사람들의 수
    lowerScoreCnt = 0
    # score와 동점인 사람들의 수
    equleScoreCnt = 0
    for i in StudentScoresList:
        cmpScore = -1
        if subjectName == "국어":
            cmpScore = int(i.korean)
        if subjectName == "영어":
            cmpScore = int(i.english)
        if subjectName == "수학":
            cmpScore = int(i.math)
        if subjectName == i.subjectList[0]:
            cmpScore = int(i.subject1)
        if subjectName == i.subjectList[1]:
            cmpScore = int(i.subject2)
        if score > -1:
            if cmpScore == score:
                equleScoreCnt += 1
            if cmpScore < score:
                lowerScoreCnt += 1
    return (((lowerScoreCnt) + (equleScoreCnt / 2)) / len(StudentScoresList)) * 100

def addBtnCallback():
    toplevel = tkinter.Toplevel()

    tkinter.Label(toplevel, text="수험번호").grid(row=0)
    tkinter.Label(toplevel, text="이름").grid(row=1)
    tkinter.Label(toplevel, text="성별").grid(row=2)
    tkinter.Label(toplevel, text="출신 고등학교").grid(row=3)
    tkinter.Label(toplevel, text="탐구과목1 이름").grid(row=4)
    tkinter.Label(toplevel, text="탐구과목2 이름").grid(row=5)
    tkinter.Label(toplevel, text="국어 점수").grid(row=6)
    tkinter.Label(toplevel, text="영어 점수").grid(row=7)
    tkinter.Label(toplevel, text="수학 점수").grid(row=8)
    tkinter.Label(toplevel, text="탐구과목1 점수").grid(row=9)
    tkinter.Label(toplevel, text="탐구과목2 점수").grid(row=10)

    student_number_entry = tkinter.Entry(toplevel)
    student_name_entry = tkinter.Entry(toplevel)
    student_gender_entry = tkinter.Entry(toplevel)
    student_highschool_entry = tkinter.Entry(toplevel)
    student_subject1_name_entry = tkinter.Entry(toplevel)
    student_subject2_name_entry = tkinter.Entry(toplevel)
    student_korean_entry = tkinter.Entry(toplevel)
    student_english_entry = tkinter.Entry(toplevel)
    student_math_entry = tkinter.Entry(toplevel)
    student_subject1_entry = tkinter.Entry(toplevel)
    student_subject2_entry = tkinter.Entry(toplevel)

    student_number_entry.grid(row=0, column=1)
    student_name_entry.grid(row=1, column=1)
    student_gender_entry.grid(row=2, column=1)
    student_highschool_entry.grid(row=3, column=1)
    student_subject1_name_entry.grid(row=4, column=1)
    student_subject2_name_entry.grid(row=5, column=1)
    student_korean_entry.grid(row=6, column=1)
    student_english_entry.grid(row=7, column=1)
    student_math_entry.grid(row=8, column=1)
    student_subject1_entry.grid(row=9, column=1)
    student_subject2_entry.grid(row=10, column=1)

    def save_btn_callback():
        newStudent = StudentScores(student_number_entry.get(),
                                   student_name_entry.get(),
                                   student_gender_entry.get(),
                                   student_highschool_entry.get(),
                                   [student_subject1_name_entry.get(),
                                   student_subject2_name_entry.get()],
                                   student_korean_entry.get(),
                                   student_english_entry.get(),
                                   student_math_entry.get(),
                                   student_subject1_entry.get(),
                                   student_subject2_entry.get()
                                   )

        StudentScoresList.append(newStudent)
        studentRepository.saveDB()
        show_all_info()
        toplevel.quit()
        toplevel.destroy()

    tkinter.Button(toplevel, text="학생 정보 추가", command=save_btn_callback).grid(row=11)
    toplevel.mainloop()


def search_btn_callback():
    for i in treeview.get_children():
        treeview.delete(i)

    for i in StudentScoresList:
        if i.getStudentNumber() == search_entry.get():
            treeview.insert('', 'end', text=i.getStudentNumber(), values=(
            i.getName(), i.getGender(), i.getHighschool(), i.getSubjectList()[0], i.getSubjectList()[1], i.getKorean(),
            i.getEnglish(), i.getMath(), i.getSubject1(), i.getSubject2()))


def show_all_info():
    for i in treeview.get_children():
        treeview.delete(i)

    for i in StudentScoresList:
        treeview.insert('', 'end', text=i.getStudentNumber(), values=(
        i.getName(), i.getGender(), i.getHighschool(), i.getSubjectList()[0], i.getSubjectList()[1], i.getKorean(),
        i.getEnglish(), i.getMath(), i.getSubject1(), i.getSubject2()))


def delete_studentinfo(studentNumber):
    for index, i in enumerate(StudentScoresList):
        if i.getStudentNumber() == studentNumber:
            del StudentScoresList[index]
            return
    studentRepository.saveDB()


def treeview_callback(event):
    item = treeview.selection()[0]
    item_values = treeview.item(item, "values")

    print(treeview.item(item, "text"))
    print(item_values)
    print("you clicked on", treeview.item(item, "text"))

    toplevel = tkinter.Toplevel()

    tkinter.Label(toplevel, text="수험번호").grid(row=0)
    tkinter.Label(toplevel, text="이름").grid(row=1)
    tkinter.Label(toplevel, text="성별").grid(row=2)
    tkinter.Label(toplevel, text="출신 고등학교").grid(row=3)
    tkinter.Label(toplevel, text="탐구과목1 이름").grid(row=4)
    tkinter.Label(toplevel, text="탐구과목2 이름").grid(row=5)
    tkinter.Label(toplevel, text="국어 점수").grid(row=6)
    tkinter.Label(toplevel, text="영어 점수").grid(row=7)
    tkinter.Label(toplevel, text="수학 점수").grid(row=8)
    tkinter.Label(toplevel, text="탐구과목1 점수").grid(row=9)
    tkinter.Label(toplevel, text="탐구과목2 점수").grid(row=10)

    student_number_label = tkinter.Label(toplevel, text=str(treeview.item(item, "text")))
    student_name_entry = tkinter.Entry(toplevel)
    student_gender_entry = tkinter.Entry(toplevel)
    student_highschool_entry = tkinter.Entry(toplevel)
    student_subject1_name_entry = tkinter.Entry(toplevel)
    student_subject2_name_entry = tkinter.Entry(toplevel)
    student_korean_entry = tkinter.Entry(toplevel)
    student_english_entry = tkinter.Entry(toplevel)
    student_math_entry = tkinter.Entry(toplevel)
    student_subject1_entry = tkinter.Entry(toplevel)
    student_subject2_entry = tkinter.Entry(toplevel)

    student_number_label.grid(row=0, column=1)
    student_name_entry.grid(row=1, column=1)
    student_gender_entry.grid(row=2, column=1)
    student_highschool_entry.grid(row=3, column=1)
    student_subject1_name_entry.grid(row=4, column=1)
    student_subject2_name_entry.grid(row=5, column=1)
    student_korean_entry.grid(row=6, column=1)
    student_english_entry.grid(row=7, column=1)
    student_math_entry.grid(row=8, column=1)
    student_subject1_entry.grid(row=9, column=1)
    student_subject2_entry.grid(row=10, column=1)

    student_name_entry.insert(0,item_values[0])
    student_gender_entry.insert(0,item_values[1])
    student_highschool_entry.insert(0,item_values[2])
    student_subject1_name_entry.insert(0,item_values[3])
    student_subject2_name_entry.insert(0,item_values[4])
    student_korean_entry.insert(0,item_values[5])
    student_english_entry.insert(0,item_values[6])
    student_math_entry.insert(0,item_values[7])
    student_subject1_entry.insert(0,item_values[8])
    student_subject2_entry.insert(0,item_values[9])

    def create_file_btn_callback():
        #todo 성적표 파일 생성 처리

        f = open(student_number_label['text']+"번 수능 성적표.csv", "wt", encoding="UTF=8")

        data1 = "{0},{1},{2},{3}".format(
            student_number_label['text'],
            student_name_entry.get(),
            student_gender_entry.get(),
            student_highschool_entry.get()
            )

        f.writelines("수험번호, 이름, 성별, 출신고\n")
        f.writelines(data1 + "\n")

        f.writelines("/ ,국어, 영어, 수학, ")
        f.writelines(student_subject1_name_entry.get()+","+student_subject2_name_entry.get()+"\n")

        f.writelines("원점수, ")

        data2 = "{0},{1},{2},{3},{4}".format(
            student_korean_entry.get(),
            student_english_entry.get(),
            student_math_entry.get(),
            student_subject1_entry.get(),
            student_subject2_entry.get()
        )
        f.writelines(data2+"\n")

        f.writelines("등급, ")

        data3 = "{0},{1},{2},{3},{4}".format(
            ratingByScore(int(student_korean_entry.get())),
            ratingByScore(int(student_english_entry.get())),
            ratingByScore(int(student_math_entry.get())),
            subjectRatingByScore(int(student_subject1_entry.get())),
            subjectRatingByScore(int(student_subject2_entry.get()))
        )
        f.writelines(data3 + "\n")

        f.writelines("백분율, ")
        data4 = "{0},{1},{2},{3},{4}".format(
            getPercentage("국어", int(student_korean_entry.get())),
            getPercentage("영어", int(student_english_entry.get())),
            getPercentage("수학", int(student_math_entry.get())),
            getPercentage(student_subject1_name_entry.get(), int(student_subject1_entry.get())),
            getPercentage(student_subject2_name_entry.get(), int(student_subject2_entry.get()))
        )
        f.writelines(data4 + "\n")

        print("성적표 파일 생성 완료")

        toplevel.quit()
        toplevel.destroy()

    def delete_btn_callback():
        delete_studentinfo(student_number_label['text'])
        studentRepository.saveDB()
        print("삭제 완료")

        show_all_info()
        toplevel.quit()
        toplevel.destroy()

    def update_btn_callback():
        delete_studentinfo(student_number_label['text'])
        newStudent = StudentScores(student_number_label['text'],
                                   student_name_entry.get(),
                                   student_gender_entry.get(),
                                   student_highschool_entry.get(),
                                   [student_subject1_name_entry.get(),
                                    student_subject2_name_entry.get()],
                                   student_korean_entry.get(),
                                   student_english_entry.get(),
                                   student_math_entry.get(),
                                   student_subject1_entry.get(),
                                   student_subject2_entry.get()
                                   )

        StudentScoresList.append(newStudent)
        studentRepository.saveDB()

        print("수정 완료")

        show_all_info()
        toplevel.quit()
        toplevel.destroy()

    tkinter.Button(toplevel, text="수정", command=update_btn_callback).grid(row=11)
    tkinter.Button(toplevel, text="삭제", command=delete_btn_callback).grid(row=12)
    tkinter.Button(toplevel, text="성적표 파일 생성", command=create_file_btn_callback).grid(row=13)
    toplevel.mainloop()


#main
studentRepository = StudentRepository(StudentScoresList, "studentDB.csv")
studentRepository.loadDB()

frame1=tkinter.Frame(window, relief="solid")

frame1.grid(row=0)

Button(frame1, text="학생 추가", command=addBtnCallback).grid(row=0, column=0)
Button(frame1, text="전체 학생 출력", command= show_all_info).grid(row=0, column=1)
search_entry = tkinter.Entry(frame1)
search_entry.grid(row=0, column=2)
Button(frame1, text="수험 번호 검색", command= search_btn_callback).grid(row=0, column=3)

Label(window, text="수정, 삭제, 성적표 파일 생성을 하려면 리스트의 항목을 더블클릭 하세요").grid(row=1)

treeview = tkinter.ttk.Treeview(window, selectmode="extended", columns=("0","1","2","1","1","1","1","1","1","1"))

treeview.column("#0", width=70)
treeview.column("#1", width=50)
treeview.column("#2", width=50)
treeview.column("#3", width=100)
treeview.column("#4", width=100)
treeview.column("#5", width=100)
treeview.column("#6", width=100)
treeview.column("#7", width=100)
treeview.column("#8", width=100)
treeview.column("#9", width=120)
treeview.column("#10", width=120)

treeview.heading("#0", text="수험번호")
treeview.heading("#1", text="이름")
treeview.heading("#2", text="성별")
treeview.heading("#3", text="출신 고등학교")
treeview.heading("#4", text="탐구과목1")
treeview.heading("#5", text="탐구과목2")
treeview.heading("#6", text="국어 원점수")
treeview.heading("#7", text="영어 원점수")
treeview.heading("#8", text="수학 원점수")
treeview.heading("#9", text="탐구과목1 원점수")
treeview.heading("#10", text="탐구과목2 원점수")

treeview.bind("<Double-1>", treeview_callback)

vsb = ttk.Scrollbar(window, orient="vertical", command=treeview.yview)
vsb.place(x=1015, y=50, height=200+20)

treeview.configure(yscrollcommand=vsb.set)

treeview.grid(row=2)
window.mainloop()