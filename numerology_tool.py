import datetime
import subprocess
import tkinter
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image

###GUI 
root = Tk()
root.title('Nhân số học tool')
root.iconbitmap('C:\\Python Project\\Numerology Tool\\icon\\fortune_teller_4425.ico')
root.geometry("455x300")
# root.focus_force()


img = ImageTk.PhotoImage(Image.open(r'C:\\Python Project\\Numerology Tool\\icon\\numerology_background.jpg'))
bkg = Label(root, image=img)
bkg.place(x=0, y=0)

name_label= Label(root,text="Nhập Tên của bạn!", font= ('TkDefaultFont', 10)) 
name_label.place(x=30, y=30)

name_entry = Entry(root, font= ('Arial bold', 12))  
name_entry.place(x = 30, y = 60, width=80, height=25)

bd_label= Label(root,text="Nhập sinh nhật của bạn! (DD/MM/YYYY)", font= ('TkDefaultFont', 10))
bd_label.place(x=30, y=110)

day_entry = Entry(root, font= ('Arial bold', 12))  
day_entry.place(x = 30, y = 140, width=35, height=25)
month_entry = Entry(root, font= ('Arial bold', 12))  
month_entry.place(x = 80, y = 140, width=35, height=25)
year_entry = Entry(root, font= ('Arial bold', 12))  
year_entry.place(x = 130, y = 140, width=75, height=25)


var_name = ""
var_day = 0
var_month = 0
var_year = 0

def func_name():
    global var_name
    var_name = name_entry.get()
def func_day():
    global var_day
    var_day = day_entry.get()
def func_month():
    global var_month
    var_month = month_entry.get()
def func_year():
    global var_year
    var_year = year_entry.get()


def show_result():
    
    func_name()
    func_day()
    func_month()
    func_year()
    
    ###########Calculate_Ruling_Number############
    numsequence_str = str(var_day) + str(var_month) + str(var_year)
    print('Chuỗi ngày sinh nhật: ' + numsequence_str)
    
    sumnum = 0
    i = 0
    while i < len(numsequence_str):
        sumnum += int(numsequence_str[i])
        i += 1
    # print('SUM Day/Month/Year of Birth: ' + str(sumnum))

    ruling_num = sumnum
    if sumnum > 11 and sumnum != 22:
        tempnum = int(str(sumnum)[0]) + int(str(sumnum)[1])
        ruling_num = tempnum
        if tempnum > 11:
            tempnum = int(str(tempnum)[0]) + int(str(tempnum)[1])
            ruling_num = tempnum

    kq_ruling_num = "Con số chủ đạo của bạn là: " + str(ruling_num)
    print(kq_ruling_num)

    ###########Calculate_Day_Number############
    day_num = int(var_day)
    if day_num > 11 and day_num != 22:
        day_num = int(str(var_day)[0]) + int(str(var_day)[1])
    
    kq_day_num = "Con số ngày sinh của bạn là: " + str(day_num)
    print(kq_day_num)
    
    #########Calculate_Four_Peak_Years########
    sub_ruling = ruling_num
    if ruling_num == 22:
        sub_ruling = 4 
    
    peak_year = [0,0,0,0,0]
    k = 0
    while k < 4:
        peak_year[k+1] = (36 - sub_ruling) + 9*k
        print('Năm đỉnh cao '+ str(k+1) + ':   ' + str(peak_year[k+1]) + ' tuổi')
        k+=1
    # print(peak_year)
    kq_peak_year = "Bốn năm đỉnh cao của bạn là: "+"\n"+str(peak_year[1])+" tuổi, "+str(peak_year[2])+" tuổi, "+str(peak_year[3])+" tuổi, "+str(peak_year[4])+" tuổi"

    #######Calculate_PYN######
    WYN = datetime.datetime.now().year
    # print(WYN)
    # print(type(WYN))
    WYN_DM_str = str(WYN) + str(var_day) + str(var_month)
    # print(WYN_DM_str)

    sumWYN_DM = 0
    n = 0
    while n < len(WYN_DM_str):
        sumWYN_DM += int(WYN_DM_str[n])
        n += 1
    # print('SUM WYN_DM: ' + str(sumWYN_DM))

    PYN = sumWYN_DM
    if sumWYN_DM > 9:
        temp_WYN_DM = int(str(sumWYN_DM)[0]) + int(str(sumWYN_DM)[1])
        PYN = temp_WYN_DM
        if temp_WYN_DM > 9:
            temp_WYN_DM = int(str(temp_WYN_DM)[0]) + int(str(temp_WYN_DM)[1])
            PYN = temp_WYN_DM

    kq_PYN = "Năm cá nhân của bạn là: " + str(PYN)
    print(kq_PYN)

    ########Name_Power###########
    alphabet = "ajsbktcludmvenwfoxgpyhqzir"
    alphabet_value = "11122233344455566677788899"

    name_value_arr = [0]*len(var_name)

    m1 = 0
    while m1 < len(alphabet):
        n1 = 0
        while n1 < len(var_name):
            if var_name[n1].find(alphabet[m1]) != -1:
                name_value_arr[n1] = alphabet_value[m1]
            n1 += 1
        m1 += 1
    name_value_str = "".join(map(str, name_value_arr))

    # print(name_value_str)
    
    #########Name_Soul#########
    alphabet_soul = "aeiouy"
    alphabet_soul_value = "159637"
    
    name_soul_value_arr = [0]*len(var_name)

    m2 = 0
    while m2 < len(alphabet_soul):
        n2 = 0
        while n2 < len(var_name):
            if var_name[n2].find(alphabet_soul[m2]) != -1:
                name_soul_value_arr[n2] = alphabet_soul_value[m2]
            n2 += 1
        m2 += 1
    name_soul_value_str = "".join(map(str, name_soul_value_arr))

    # print(name_soul_value_str)

     ###########Calculate_Name_Soul###########
    sumnum_soul = 0
    i_soul = 0
    while i_soul < len(name_soul_value_str):
        sumnum_soul += int(name_soul_value_str[i_soul])
        i_soul += 1
    
    soul_value = sumnum_soul
    if sumnum_soul > 11:
        tempnum_soul = int(str(sumnum_soul)[0]) + int(str(sumnum_soul)[1])
        soul_value = tempnum_soul
        if tempnum_soul > 11:
            tempnum_soul = int(str(tempnum_soul)[0]) + int(str(tempnum_soul)[1])
            soul_value = tempnum_soul

    kq_soul_value = "Con số linh hồn của tên bạn là: " + str(soul_value)
    print(kq_soul_value)


    #########Name_Outer#########
    alphabet_outer = "jsbktcldmvnwfxgphqzr"
    alphabet_outer_value = "11222334445566778889"
    
    name_outer_value_arr = [0]*len(var_name)

    m3 = 0
    while m3 < len(alphabet_outer):
        n3 = 0
        while n3 < len(var_name):
            if var_name[n3].find(alphabet_outer[m3]) != -1:
                name_outer_value_arr[n3] = alphabet_outer_value[m3]
            n3 += 1
        m3 += 1
    name_outer_value_str = "".join(map(str, name_outer_value_arr))

    # print(name_outer_value_str)

    ###########Calculate_Name_Outer###########
    sumnum_outer = 0
    i_outer = 0
    while i_outer < len(name_outer_value_str):
        sumnum_outer += int(name_outer_value_str[i_outer])
        i_outer += 1
    
    outer_value = sumnum_outer
    if sumnum_outer > 11 and sumnum_outer != 22:
        tempnum_outer = int(str(sumnum_outer)[0]) + int(str(sumnum_outer)[1])
        outer_value = tempnum_outer
        if tempnum_outer > 11:
            tempnum_outer = int(str(tempnum_outer)[0]) + int(str(tempnum_outer)[1])
            outer_value = tempnum_outer

    kq_outer_value = "Con số biểu đạt của tên bạn là: " + str(outer_value)
    print(kq_outer_value)

    ###############Calculate_Arrow############
    arrow_str = name_value_str + numsequence_str
    print(arrow_str)

    q = 0
    n1=n2=n3=n4=n5=n6=n7=n8=n9 = 0
    arr123=2
    while q<len(arrow_str):
        if int(arrow_str[q]) == 1:
            n1=1
        elif int(arrow_str[q]) == 2:
            n2=1
        elif int(arrow_str[q]) == 3:
            n3=1
        elif int(arrow_str[q]) == 4:
            n4=1
        elif int(arrow_str[q]) == 5:
            n5=1
        elif int(arrow_str[q]) == 6:
            n6=1
        elif int(arrow_str[q]) == 7:
            n7=1
        elif int(arrow_str[q]) == 8:
            n8=1
        elif int(arrow_str[q]) == 9:
            n9=1
        q+=1

    arrow = ""
    if n1==1 and n2==1 and n3==1:
        arrow += "123, "
        subprocess.Popen("Arrow123.pdf",shell=True)
    if n4==1 and n5==1 and n6==1:
        arrow += "456, "
        subprocess.Popen("Arrow456.pdf",shell=True)
    if n7==1 and n8==1 and n9==1:
        arrow += "789, "
        subprocess.Popen("Arrow789.pdf",shell=True)
    if n1==1 and n4==1 and n7==1:
        arrow += "147, "
        subprocess.Popen("Arrow147.pdf",shell=True)
    if n2==1 and n5==1 and n8==1:
        arrow += "258, "
        subprocess.Popen("Arrow258.pdf",shell=True)
    if n3==1 and n6==1 and n9==1:
        arrow += "369, "
        subprocess.Popen("Arrow369.pdf",shell=True)
    if n1==1 and n5==1 and n9==1:
        arrow += "159, "
        subprocess.Popen("Arrow159.pdf",shell=True)
    if n3==1 and n5==1 and n7==1:
        arrow += "357"
        subprocess.Popen("Arrow357.pdf",shell=True)

    if len(arrow) > 0:
        kq_arrow = "Bạn có mũi tên: " + arrow
    else:
        kq_arrow = "Bạn không có mũi tên nào"
    print(kq_arrow)

    no_arrow = ""
    if n4==0 and n5==0 and n6==0:
        no_arrow += "456, "
        subprocess.Popen("NoArrow456.pdf",shell=True)
    if n7==0 and n8==0 and n9==0:
        no_arrow += "789, "
        subprocess.Popen("NoArrow789.pdf",shell=True)
    if n1==0 and n4==0 and n7==0:
        no_arrow += "147, "
        subprocess.Popen("NoArrow147.pdf",shell=True)
    if n2==0 and n5==0 and n8==0:
        no_arrow += "258, "
        subprocess.Popen("NoArrow258.pdf",shell=True)
    if n3==0 and n6==0 and n9==0:
        no_arrow += "369, "
        subprocess.Popen("NoArrow369.pdf",shell=True)
    if n1==0 and n5==0 and n9==0:
        no_arrow += "159, "
        subprocess.Popen("NoArrow159.pdf",shell=True)
    if n3==0 and n5==0 and n7==0:
        no_arrow += "357"
        subprocess.Popen("NoArrow357.pdf",shell=True)

    if len(no_arrow) > 0:
        kq_no_arrow = "Bạn có mũi tên trống: " + no_arrow
    else:
        kq_no_arrow = "Bạn không có mũi tên trống nào"
    print(kq_no_arrow)

    add_name = ""
    if n1==0:
        add_name += "[A,J,S]-"
    if n2==0:
        add_name += "[B,K,T]-"
    if n3==0:
        add_name += "[C,L,U]-"
    if n4==0:
        add_name += "[D,M,V]-"
    if n5==0:
        add_name += "[E,N,W]-"
    if n6==0:
        add_name += "[F,O,X]-"
    if n7==0:
        add_name += "[G,P,Y]-"
    if n8==0:
        add_name += "[H,Q,Z]-"
    if n9==0:
        add_name += "[I,R]"

    if len(add_name)>0:
        kq_add_name = "Bạn nên đặt tên bổ sung chứa các ký tự: "+"\n"+add_name
    else:
        kq_add_name = "Bạn không cần đặt thêm tên bổ sung"
    print(kq_add_name)


    ############OpenPDF_files################
    subprocess.Popen("RulingNum"+str(ruling_num)+".pdf",shell=True)
    subprocess.Popen("DayNum"+str(day_num)+".pdf",shell=True)
    subprocess.Popen("PYN"+str(PYN)+".pdf",shell=True)
    subprocess.Popen("SoulNum"+str(soul_value)+".pdf",shell=True)
    subprocess.Popen("OuterNum"+str(outer_value)+".pdf",shell=True)

    # print(var_name)
    # print(var_day)
    # print(var_month)
    # print(var_year)


    ###############Result_Window####################
    result_window = Toplevel(root)
    result_window.title("KẾT QUẢ")
    result_window.iconbitmap('C:\\Python Project\\Numerology Tool\\icon\\result_icon1.ico')
    result_window.geometry("550x610")
    result_window.focus_force()

    rs_img = ImageTk.PhotoImage(Image.open(r'C:\\Python Project\\Numerology Tool\\icon\\result_border1.jpg'))
    rs_bkg = Label(result_window, image=rs_img)
    rs_bkg.place(x=0, y=0)
    
    intro_label = Label(result_window,text= "Chào " + var_name.upper() + "! " + "Dưới đây là kết quả của bạn:", font= ('TkDefaultFont', 12)).pack()
    
    rs_txt = kq_ruling_num + "\n\n" + kq_day_num + "\n\n" + kq_peak_year + "\n\n" + kq_PYN +"\n\n"+ kq_soul_value +"\n\n"+ kq_outer_value +"\n\n"+kq_arrow+"\n\n"+kq_no_arrow+"\n\n"+kq_add_name
    rs_label = Label(result_window,text=rs_txt, font= ('TkDefaultFont', 12)).place(x = 100, y = 100, width=350, height=400)
    
    ps_label = Label(result_window,text= var_name.upper() + " xem các file vừa mở để biết ý nghĩa của các con số nhé!", font= ('TkDefaultFont', 12)).pack()
    
    # button_OK = Button(result_window,text='OK',bg='silver',relief=RAISED, font=('Lucida Sans italic', 12), command=result_window.quit).place(x=250, y=450)
    result_window.mainloop()

button = Button(root,text='Xác nhận',bg='silver',relief=RAISED, font=('Lucida Sans italic', 12), command=show_result)
button.place(x=180, y=230)

# root.bind('<Return>', show_result)
# root.bind("<Return>", lambda e: root.destroy())
root.mainloop()