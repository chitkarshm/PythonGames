from tkinter import HIDDEN,NORMAL,Tk,Canvas

def toggle_eyes():
      current_color=c.itemcget(eye_left,'fill')
      new_color=c.body_color if current_color=='white' else 'white'
      current_state=c.itemcget(pupil_left, 'state')
      new_state=NORMAL if current_state==HIDDEN else HIDDEN
      c.itemconfigure(pupil_left, state=new_state)
      c.itemconfigure(pupil_right,state=new_state)
      c.itemconfigure(eye_left, fill=new_color)
      c.itemconfigure(eye_right,fill=new_color)

def blink():
      toggle_eyes()
      root.after(250,toggle_eyes)
      root.after(3000,blink)

def showhappy(event):
      if (20 <= event.x <= 350) and (20 <= event.y <= 350):
            c.itemconfigure(cheek_left, state=NORMAL)
            c.itemconfigure(cheek_right, state=NORMAL)
            c.itemconfigure(mouth_happy, state=NORMAL)
            c.itemconfigure(mouth_normal, state=HIDDEN)
            c.itemconfigure(mouth_sad, state=HIDDEN)
            c.happylevel=10
      return

def hidehappy(event):
      c.itemconfigure(cheek_left, state=HIDDEN)
      c.itemconfigure(cheek_right, state=HIDDEN)
      c.itemconfigure(mouth_happy, state=HIDDEN)
      c.itemconfigure(mouth_normal, state=NORMAL)
      c.itemconfigure(mouth_sad, state=HIDDEN)
      return

def toggletounge():
      if not c.toungeout:
            c.itemconfigure(toungetip,state=NORMAL)
            c.itemconfigure(toungemain,state=NORMAL)
            c.toungeout=True
      else:
            c.itemconfigure(toungetip,state=HIDDEN)
            c.itemconfigure(toungemain,state=HIDDEN)
            c.toungeout=False

def togglepupils():
      if not c.eyescrossed:
            c.move(pupil_left,10,-5)
            c.move(pupil_right,-10,-5)
            c.eyescrossed=True
      else:
            c.move(pupil_left,-10,5)
            c.move(pupil_right,10,5)
            c.eyescrossed=False

def cheeky(event):
      toggletounge()
      togglepupils()
      hidehappy(event)
      root.after(1000,toggletounge)
      root.after(1000,togglepupils)
      return

def sad():
      if c.happylevel==0:
            c.itemconfigure(mouth_happy,state=HIDDEN)
            c.itemconfigure(mouth_normal,state=HIDDEN)
            c.itemconfigure(mouth_sad,state=NORMAL)
      else:
            c.happylevel-=1
      root.after(5000,sad)

root=Tk()
c=Canvas(root,width=400,height=400)
c.configure(bg='dark blue', highlightthickness=0)

c.body_color='teal'
body=c.create_oval(35,20,365,350,outline=c.body_color,fill=c.body_color)
ear_left=c.create_polygon(75,80,75,10,165,70,outline=c.body_color,fill=c.body_color)
ear_right=c.create_polygon(255,45,325,10,320,70,outline=c.body_color,fill=c.body_color)
foot_left=c.create_oval(65,320,145,360,outline=c.body_color,fill=c.body_color)
foot_right=c.create_oval(250,320,330,360,outline=c.body_color,fill=c.body_color)
eye_left=c.create_oval(130,110,160,170,outline='black',fill='white')
pupil_left=c.create_oval(140,145,150,155,outline='black',fill='black')
eye_right=c.create_oval(230,110,260,170,outline='black',fill='white')
pupil_right=c.create_oval(240,145,250,155,outline='black',fill='black')
mouth_normal=c.create_line(170,150,200,272,230,250,smooth=1,width=2,state=NORMAL)
mouth_happy=c.create_line(170,250,200,232,230,250,smooth=1,width=2,state=HIDDEN)
mouth_sad=c.create_line(170,250,200,232,230,250,smooth=1,width=2,state=HIDDEN)
toungemain=c.create_rectangle(170,250,230,290,outline='red',fill='red',state=HIDDEN)
toungetip=c.create_oval(170,285,230,300, outline='red',fill='red', state=HIDDEN)
cheek_left=c.create_oval(70,180,120,230,outline='pink',fill='pink',state=HIDDEN)
cheek_right=c.create_oval(280,180,330,230,outline='pink',fill='pink',state=HIDDEN)

c.pack()

c.bind('<Motion>', showhappy)
c.bind('<Leave>', hidehappy)
c.bind('<Double-1>',cheeky)

c.happylevel=10
c.eyescrossed=False
c.toungeout=False

root.after(1000, blink)
root.after(5000,sad)
root.mainloop
