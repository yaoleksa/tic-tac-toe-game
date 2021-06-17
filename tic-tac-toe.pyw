import tkinter
import random

class Game(tkinter.Frame):
    def __init__(self, master=None):
        tkinter.Frame.__init__(self, master)
        self.grid()
        self.choose()
        self.board=[1,2,3,4,5,6,7,8,9]
        self.game_board=tkinter.Label()
        self.l=''
        self.comp_sign, self.user_sign="", ""
    def choose(self):
        self.il=tkinter.Label(text="Choose X or O.")
        self.il.grid(row=0, column=0, columnspan=2, padx=20)
        self.chX=tkinter.Button(text="X", command=self.chooseX)
        self.chO=tkinter.Button(text="O", command=self.chooseO)
        self.chX.grid(row=1, column=0, pady=5)
        self.chO.grid(row=1, column=1, pady=5)
    def after_choose(self):
        self.il.destroy()
        self.chX.destroy()
        self.chO.destroy()
        self.display_board()
        self.mainlabel=tkinter.Label(text='Choose cell.')
        self.mainlabel.grid(row=0, column=0, columnspan=3, padx=20)
        self.game_board.grid(row=1, column=0, columnspan=3, padx=20, pady=5)
        self.b1=tkinter.Button(text='1', command=self.select1)
        self.b2=tkinter.Button(text='2', command=self.select2)
        self.b3=tkinter.Button(text='3', command=self.select3)
        self.b4=tkinter.Button(text='4', command=self.select4)
        self.b5=tkinter.Button(text='5', command=self.select5)
        self.b6=tkinter.Button(text='6', command=self.select6)
        self.b7=tkinter.Button(text='7', command=self.select7)
        self.b8=tkinter.Button(text='8', command=self.select8)
        self.b9=tkinter.Button(text='9', command=self.select9)
        self.b1.grid(row=2,column=0)
        self.b2.grid(row=2,column=1)
        self.b3.grid(row=2,column=2)
        self.b4.grid(row=3,column=0)
        self.b5.grid(row=3,column=1)
        self.b6.grid(row=3,column=2)
        self.b7.grid(row=4,column=0)
        self.b8.grid(row=4,column=1)
        self.b9.grid(row=4,column=2)
        self.buttons=[self.b1, self.b2, self.b3, self.b4, self.b5, self.b6,
                      self.b7, self.b8, self.b9]
    def chooseX(self):
        self.after_choose()
        self.user_sign='X'
        self.comp_sign='O'
        if random.choice([0,1])==1:
            self.comp_turn()
    def chooseO(self):
        self.after_choose()
        self.user_sign='O'
        self.comp_sign='X'
        if random.choice([0,1])==1:
            self.comp_turn()
    def display_board(self):
        self.l=''
        for i in range(len(self.board)):
            if (i+1)%3!=0 and (i+1)<7:
                self.l+='_'+str(self.board[i])+'_|'
            elif (i+1)%3==0 and (i+1)<7:
                self.l+='_'+str(self.board[i])+'_\n'
            elif (i+1)%3!=0:
                self.l+=' '+str(self.board[i])+' |'
            else:
                self.l+=' '+str(self.board[i])+' '
        self.game_board['text']=self.l
    def comp_turn(self):
        buf=[]
        for i in self.board:
            if type(i)!=str:
                buf.append(i)
        turn=random.choice(buf)
        self.board[self.board.index(turn)]=self.comp_sign
        self.buttons[turn-1].destroy()
        self.check()
        self.display_board()
    def after_selection(self):
        self.display_board()
        self.check()
        self.comp_turn()
    def select1(self):
        self.board[0]=self.user_sign
        self.buttons[0].destroy()
        self.check()
        self.after_selection()
    def select2(self):
        self.board[1]=self.user_sign
        self.buttons[1].destroy()
        self.check()
        self.after_selection()
    def select3(self):
        self.board[2]=self.user_sign
        self.buttons[2].destroy()
        self.check()
        self.after_selection()
    def select4(self):
        self.board[3]=self.user_sign
        self.buttons[3].destroy()
        self.check()
        self.after_selection()
    def select5(self):
        self.board[4]=self.user_sign
        self.buttons[4].destroy()
        self.check()
        self.after_selection()
    def select6(self):
        self.board[5]=self.user_sign
        self.buttons[5].destroy()
        self.check()
        self.after_selection()
    def select7(self):
        self.board[6]=self.user_sign
        self.buttons[6].destroy()
        self.check()
        self.after_selection()
    def select8(self):
        self.board[7]=self.user_sign
        self.buttons[7].destroy()
        self.check()
        self.after_selection()
    def select9(self):
        self.board[8]=self.user_sign
        self.buttons[8].destroy()
        self.check()
        self.after_selection()
    def check(self):
        for i in range(3):
            if self.board[i]==self.board[i+3]==self.board[i+6]:
                if self.board[i]==self.user_sign:
                    self.mainlabel['text']='My congradulations, you win.'
                else:
                    self.mainlabel['text']='I win.'   
                for i in self.buttons:
                    i.destroy()
                return
        for i in range(0, 9, 3):
            if self.board[i]==self.board[i+1]==self.board[i+2]:
                if self.board[i]==self.user_sign:
                    self.mainlabel['text']='My congradulations, you win.'
                else:
                    self.mainlabel['text']='I win.'   
                for i in self.buttons:
                    i.destroy()
        if self.board[0]==self.board[4]==self.board[8]:
            if self.board[4]==self.user_sign:
                self.mainlabel['text']='My congradulations, you win.'
            else:
                self.mainlabel['text']='I win.'
            for i in self.buttons:
                    i.destroy()
        if self.board[2]==self.board[4]==self.board[6]:
            if self.board[4]==self.user_sign:
                self.mainlabel['text']='My congradulations, you win.'
            else:
                self.mainlabel['text']='I win.'
            for i in self.buttons:
                    i.destroy()
            
        

root=tkinter.Tk()
root.title('Tic-tac-toe game')
app=Game(root)
app.mainloop()
root.destroy()
