import tkinter
from tkinter import *
import random

questions = [
    "Which of these numbers is normally required to verify a transaction, when shopping online using a debit or credit card?",
    "“Nabhah Sparsham Deeptam”, the motto of India Air Force, is taken from which ancient work?",
    "Which of the following is the capital of India ?",
    "In the abbreviation PNR, used while issuing rail or air ticket, what does R stand For?",
    "The Taj Mahal is located in  ?",
    "Within which of these mediums is the speed of the sound fastest ?",
    "Which of the following is not a costal city of india ?",
    "Which of The following is executed in browser(client side) ?",
    "In medicine, which of these is usually denoted by 120/80 for an adult?",
    "Which of these is also known as the festival of sacrifice?",
    "Which objects of everyday use have types called AA, AAA, C and D?",
    "Which of these cities is also known as the “Steel City of Odisha”?",
    " On which of these planets does the sun rise in the west and set in the east?",
    " Which among the following Muslim bodies has decided against filing review petition on Supreme Court’s Ayodhya Verdict?",

]

answers_choice = [
    ["PAN", "PNR", "CVV", "AADHAR", ],
    ["Garuda Purana", "Valmiki Ramayan", "Bhagwad Gita", "Mundaka Upnishad", ],
    ["Mumbai", "Delhi", "Chennai", "Lucknow", ],
    ["Reservation", "Record", "Registration", "Recognition", ],
    ["Patna", "Delhi", "Benaras", "Agra", ],
    ["Vacuum", "Air", "Water", "Steel", ],
    ["Bengluru", "Kochin", "Mumbai", "vishakhapatnam", ],
    ["perl", "css", "python", "java", ],
    ["Normal Pulse", "Normal Hearing", "Normal vision", "Normal Blood Pressure", ],
    ["Eid – ul – Adha", "Eid – ul – Fitr", "Milan- un – Nabi", "Chehlum", ],
    ["SIM Cards", "Memory Cards", "Batteries", "Paper"],
    ["Bokaro", "Bhilai", "Jamesdpur", "Rourkela", ],
    ["Jupiter", "Mars", "Venus", "Mercury", ],
    ["All India Muslim Personal Law Board", "Jamiat Ulama-i-Hind", "Sunni Waqf board", "None of the above", ],
]

answers = [2, 2, 1, 1, 3, 3, 0, 1, 3, 0, 2, 3, 2, 2]

user_answer = []

indexes = []


def gen():
    global indexes
    while (len(indexes) < 10):
        x = random.randint(0, 13)
        if x in indexes:
            continue
        else:
            indexes.append(x)


def showresult(score):
    lblQuestion.destroy()
    r1.destroy()
    r2.destroy()
    r3.destroy()
    r4.destroy()
    global labelimage, labelresulttext, btnReplay
    labelimage = Label(
        root,
        root.config(background="#5a3786"),
        border=0,
    )
    labelimage.pack(pady=(50, 30))
    labelresulttext = Label(
        root,
        width=500,
        font=("Consolas", 22),
        background="#946ec4",
    )
    labelresulttext.pack(pady=10)

    if score >= 80:
        img = PhotoImage(file="great.png")
        labelimage.configure(image=img)
        labelimage.image = img
        labelresulttext.configure(text="You Are Excellent !!" + str(score))
    elif (score >= 50 and score < 80):
        img = PhotoImage(file="ok.png")
        labelimage.configure(image=img)
        labelimage.image = img
        labelresulttext.configure(text="You Can Be Better !!" + str(score))
    else:
        img = PhotoImage(file="bad.png")
        labelimage.configure(image=img)
        labelimage.image = img
        labelresulttext.configure(text="You Should Work Hard !!" + str(score))


def calc():
    global indexes, user_answer, answers
    x = 0
    score = 0
    for i in indexes:
        if user_answer[x] == answers[i]:
            score = score + 10
        x += 1
    print(score)
    showresult(score)


ques = 1


def selected():
    global radiovar, user_answer
    global lblQuestion, r1, r2, r3, r4
    global ques
    x = radiovar.get()
    user_answer.append(x)
    radiovar.set(-1)
    if ques < 10:
        lblQuestion.config(text=questions[indexes[ques]])
        r1['text'] = answers_choice[indexes[ques]][0]
        r2['text'] = answers_choice[indexes[ques]][1]
        r3['text'] = answers_choice[indexes[ques]][2]
        r4['text'] = answers_choice[indexes[ques]][3]
        ques += 1
    else:
        calc()


def startquiz():
    root.config(background="#235e71")
    global lblQuestion, r1, r2, r3, r4
    lblQuestion = Label(
        root,
        text=questions[indexes[0]],
        font=("Consolas", 22),
        width=500,
        justify="center",
        wraplength=400,
        background="#c1e1ec",
    )
    lblQuestion.pack(pady=(100, 30))

    global radiovar
    radiovar = IntVar()
    radiovar.set(-1)

    r1 = Radiobutton(
        root,
        width=500,
        text=answers_choice[indexes[0]][0],
        font=("Consolas", 18),
        value=0,
        variable=radiovar,
        command=selected,
        background="#c1e1ec",
    )
    r1.pack(pady=5)

    r2 = Radiobutton(
        root,
        width=500,
        text=answers_choice[indexes[0]][1],
        font=("Consolas", 18),
        value=1,
        variable=radiovar,
        command=selected,
        background="#c1e1ec",
    )
    r2.pack(pady=5)

    r3 = Radiobutton(
        root,
        width=500,
        text=answers_choice[indexes[0]][2],
        font=("Consolas", 18),
        value=2,
        variable=radiovar,
        command=selected,
        background="#c1e1ec",
    )
    r3.pack(pady=5)

    r4 = Radiobutton(
        root,
        width=500,
        text=answers_choice[indexes[0]][3],
        font=("Consolas", 18),
        value=3,
        variable=radiovar,
        command=selected,
        background="#c1e1ec",
    )
    r4.pack(pady=5)


def startIspressed():
    labelimage.destroy()
    labeltext.destroy()
    lblInstruction.destroy()
    lblRules.destroy()
    btnStart.destroy()
    gen()
    startquiz()


root = tkinter.Tk()
root.title("GK Tester")
root.geometry("700x600")
root.config(background="#ffffff")
root.resizable(0, 0)

img1 = PhotoImage(file="homepage.png")

labelimage = Label(
    root,
    image=img1,
    background="#ffffff",
)
labelimage.pack(pady=(40, 0))

labeltext = Label(
    root,
    text="GK Tester",
    font=("Comic sans MS", 24, "bold"),
    background="#ffffff",
)
labeltext.pack(pady=(5))

img2 = PhotoImage(file="Frame.png")

btnStart = Button(
    root,
    image=img2,
    relief=FLAT,
    border=0,
    command=startIspressed,
)
btnStart.pack()

lblInstruction = Label(
    root,
    text="Read The Rules And\nClick Start Once You Are ready",
    background="#ffffff",
    font=("Consolas", 14),
    justify="center",
)
lblInstruction.pack(pady=(10, 70))

lblRules = Label(
    root,
    text="This quiz contains 10 questions\nOnce you select a radio button that will be a final choice\nHence think before you select",
    width=100,
    font=("Times", 14),
    background="#000000",
    foreground="#FACA2F",
)
lblRules.pack()

root.mainloop()
