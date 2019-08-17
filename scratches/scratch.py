from tkinter import *
import webbrowser

greeting = ["السلام عليكم","اهلا","مرحبا","كيف حالك","مساء الخير","صباح الخير", "ماهي معسكراتكم"]
response = ["وعليكم السلام =)","أهلاً بك =)","مرحباً بك =)", "بخير، وأتمنى أن تكون كذلك =)","مساء الخير =)","صباح الخير =)","معسكر تطوير المواقع الإلكترونية ،معسكر مبادئ البرمجة بلغة البايثون و قريباً معسكر برمجة تطبيقات الجوال (اندرويد)"]


root = Tk()
user = StringVar()
bot = StringVar()
root.iconbitmap('icon.gif')
root.title("Code for Girls Chatbot")
root.geometry("500x420")
root.configure(background='#352858')
canvas = Canvas(root,width=300, height=250, bg='#352858',highlightcolor='#352858',highlightbackground='#352858', borderwidth=0)
img1 = PhotoImage(file='logo.gif')

canvas.create_image(0, 0, image=img1, anchor=NW)
canvas.grid(row=0,column=1)

l3= Label(root, text=" ",width=35,anchor=NW,background='#352858')
l3.grid(row=1,column=1)
l3= Label(root, text=" ",width=2,anchor=NW,background='#352858')
l3.grid(row=3,column=1)
l1= Label(root, text="المستخدم:",foreground='#F1CF6F',anchor=NW,background='#352858')
l1.grid(row=2,column=1)
l2=Label(root, text="الرد الآلي:",foreground='#F1CF6F',anchor=NW,background='#352858')
l2.grid(row=6,column=1)
E1=Entry(root, textvariable=user,width=47,background='white',foreground='#5773A0')
E1.grid(row=3,column=1)
E2=Entry(root,justify=CENTER,textvariable=bot,width=49,background='#352858',foreground='white',highlightcolor='#352858',highlightbackground='#352858', borderwidth=0)
E2.grid(row=7,column=1)
bot.set("مرحباً بكم في موقعنا، يسعدني خدمتك =)")
photo = PhotoImage(file="sent-512.gif")


def main(event=None):
    question = user.get()
    if question in greeting:
        index=greeting.index(question)
        bot.set(response[index])
    elif "http" in question:
        bot.set("حسناً،يتم الآن فتح الرابط...")
        webbrowser.open_new(r""+ question)
    elif "موقع" in question and "لكتروني" in question:
        bot.set("حسناً، يسعدني مشاركتك موقعنا الإلكتروني =)")
        webbrowser.open_new(r"https://codeforgirls.org/#section-home")
    elif "تويتر" in question :
         bot.set("حسناً، يسعدني مشاركتك حسابنا بتويتر =)")
         webbrowser.open_new(r"https://twitter.com/_codeforgirls")
    elif "معسكر" in question and "قريب" in question:
         bot.set("نعم، سيكون لدينا معسكر مبادئ البرمجة بلغة البايثون في تاريخ ٩ يونيو=)")
    elif "موقع" in question :
         bot.set("هل تقصد موقعنا الإلكتروني أو مكاننا على خرائط قوقل!")
    elif "مكان" in question :
        bot.set("حسناً، يسعدني مشاركتك مكاننا على خرائط قوقل =)")
        webbrowser.open_new(r"https://www.google.com/maps/place/An+Narjis,+Riyadh/@24.8947317,46.5748298,12z/data=!3m1!4b1!4m5!3m4!1s0x3e2efb359ff44d6f:0xe75fa00c795f8cc0!8m2!3d24.834231!4d46.6794995")
    else:
        bot.set("لمزيد من المعلومات تواصل معنا على البريد الإلكتروني: hello@codeforgirls.org")


E1.bind('<Return>', main)
l3= Label(root, text=" ",width=35,anchor=NW,background='#352858')
l3.grid(row=4,column=1)
B1= Button(root, command=main,width=20,image = photo,foreground='#5F8698',font = ('Sans','15','bold'))
B1.grid(row=3,column=0)

mainloop()
