#This is sodoku gui project, an amazing logger project for python geeks.
from tkinter import *
from tkinter import messagebox
import random

counter=-1
time_taken=0

def play_again(new_Master,master):
    global counter,time_taken
    counter=-1
    time_taken=0
    new_Master.destroy()
    master.destroy()
    main()

def quit_game(new_Master,master):
    new_Master.destroy()
    master.destroy()

def set_timer(time):
    def count():
        global counter
        if counter==-1:
            display="Starting..."
        else:
            display=str(counter)
        time.delete(0,'end')
        time.insert(0,display)
        #print("hii")
        time.after(1000, count)
        counter += 1
    count()

def tell_score(a,b):
    fl=1
    sc=1000
    for i in range(0,6):
        for j in range(0,6):
            if len(a[i][j].get())==0 or str(b[i][j]) != a[i][j].get():
                sc=0
                break
        if sc==0:
            break
    if sc!=0:
        sc=(sc-time_taken)/sc*1000
        fl=0
    if sc<=0 and fl==0:
        sc=10
    return sc
    
def check_sudoku(a,b,time,status,score,master):
    global time_taken
    time.config(state=DISABLED)
    time_taken=int(time.get())
    sc=tell_score(a,b)
    if sc!=0:
        status.insert(0,"Congo! You win")
        score.insert(0,sc)
    else:
        status.insert(0,"Oops! You lose")
        score.insert(0,"0")
    new_Master=Tk()
    b1=Button(new_Master,text='PLAY AGAIN',bg='green',command=lambda:play_again(new_Master,master))
    b2=Button(new_Master,text='QUIT',bg='green',command=lambda:quit_game(new_Master,master))
    b1.pack()
    b2.pack()

def correct(inp):
    if inp in ['1','2','3','4','5','6']:
        return True
    elif inp is "":
        return True
    else:
        messagebox.showinfo("WRONG","ONLY digits from 1-6 are allowed")
        return False
    
def main():
    master=Tk()
    master.title('6X6 Easy Sudoku Game')
    listi=[]
    for i in range(0,6):
        listi.append([])
        for j in range(0,6):
            listi[i].append(Entry(master,width=5))

    reg=master.register(correct)
        
    Label(master,text='TIME').grid(row=1,column=7)
    Label(master,text='STATUS').grid(row=2,column=7)
    Label(master,text='SCORE').grid(row=3,column=7)

    time=Entry(master)
    status=Entry(master)
    score=Entry(master)

    quit_button=Button(master,text='QUIT',bg='green',command=lambda:master.destroy())
    quit_button.place(x=245,y=90)

    submit_button=Button(master,text='SUBMIT',bg='green',command=lambda:check_sudoku(listi,solution,time,status,score,master))
    submit_button.place(x=285,y=90)

    #count=0
    for i in range(0,6):
        for j in range(0,6):
            listi[i][j].grid(row=i,column=j+1)
            listi[i][j].config(validate="key",validatecommand=(reg,'%P'))

    time.grid(row=1,column=10)
    status.grid(row=2,column=10)
    score.grid(row=3,column=10)

    trial=0
    while(trial==0):
        row=[]
        col=[]
        dia=[]
        for i in range(6):
            row.append([])
            col.append([])
            dia.append([])
        solution=[[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]]
        for r in range(0,6):
            for j in range(0,6):
                flag=1
                while(flag==1):
                    c=random.randint(0,5)
                    if solution[r][c]==0:
                        flag=0
                if c>2:
                    dg=(r-r%2)+1
                else:
                    dg=r-r%2
                res=0
                unsafe=[]
                notsafe=1
                while(res==0):
                    if len(unsafe)==6:
                        notsafe=0
                        break
                    n=random.randint(1,6)
                    if n not in unsafe:
                        unsafe.append(n)
                    if n not in row[r] and n not in col[c] and n not in dia[dg]:
                        solution[r][c]=n
                        row[r].append(n)
                        col[c].append(n)
                        dia[dg].append(n) 
                        res=1
                if notsafe==0:
                    break
            if notsafe==0:
                break
        if notsafe==1:
            trial=1

    rand_list=[]
    for i in range(0,18):
        r=random.randint(0,5)
        c=random.randint(0,5)
        while([r,c] in rand_list):
            r=random.randint(0,5)
            c=random.randint(0,5)
        else:
            rand_list.append([r,c])
            listi[r][c].insert(0,solution[r][c])
            listi[r][c].config(state=DISABLED)

    set_timer(time)        
    mainloop()

if __name__=="__main__":
    main()


