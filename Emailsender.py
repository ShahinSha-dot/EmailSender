from tkinter import*
import smtplib
mailid="fredysomy@gmail.com"
password="fredysomykainady"
root=Tk()
root.geometry("400x250")
root.resizable(0,0)
l1=Label(root,text="Email Sender",font="Helvetica 25 bold").place(x=100,y=0)
l2=Label(root,text="To:").place(x=0,y=70)
e1=Entry(root,width="30")
e1.place(x=100,y=70)
l3=Label(root,text="Message:").place(x=0,y=100)
e2=Entry(root,width="40")
e2.place(x=100,y=100)
l4=Label(root)
l4.place(x=0,y=190)
def sendemail():
    try:
        recipnt=str(e1.get())
        msg=str(e2.get())
        server=smtplib.SMTP('smtp.gmail.com',587)
        server.connect("smtp.gmail.com",587)
        server.starttls()
        server.login(mailid,password)
        server.sendmail(mailid,recipnt,msg)
        server.quit()
        l4.configure(text="Email Succesfully send",font="Helvetica 15 bold")
    except:    
        l4.configure(text="Email not send,failed network",font="Helvetica 10 bold")
    
b1=Button(root,text="Send",command=sendemail,width="8").place(x=170,y=150)

root.mainloop()
