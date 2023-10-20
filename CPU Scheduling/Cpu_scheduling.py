from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox

process_count = 0
Burst_time = []
Arrival_time = []
Priority = []
p_labels = []
ContextSwitch = []

def create_frame(window, width, height, x, y):
    frame = Frame(window, width=width, height=height)
    frame.pack()
    frame.place(x=x, y=y)
    return frame

def create_label(window, text, font, font_color, change_color, color, x, y):
    if change_color:
        label = Label(window, text=text, font=font, foreground=font_color, bg=color)
    else:
        label = Label(window, text=text, font=font, foreground=font_color)
    label.pack()
    label.place(x=x, y=y)
    return label

def create_entry(window, relief, width, x, y, show):
    entry = Entry(window, relief=relief, width=width, font=7, show=show)
    entry.pack()
    entry.place(x=x, y=y)
    return entry

def create_button(window, text, font, command, relief, height, width, button_color, font_color, x, y, state):
    button = Button(window, text=text, font=font, command=command, relief=relief, height=height,
                    width=width, bg=button_color, fg=font_color, state=state)
    button.pack()
    button.place(x=x, y=y)
    return button

def add_process(win1):
    global process_count
    global Burst_time
    global Arrival_time
    global Priority
    global p_labels
    if process_count < 8:
        process_count += 1
        txt = "P" + str(process_count)
        plabel = create_label(window=win1, text=txt, font='Helvetica 14 bold', font_color="Black",
                    change_color=False, color="White",x=350, y=80+(process_count*30))
        p_labels.append(plabel)
        """    Create Entry    """
        new_burst_time = create_entry(window=win1, relief="flat", width=10, x=475, y=80+(process_count*30), show="")
        new_arrival_time = create_entry(window=win1, relief="flat", width=10, x=600, y=80+(process_count*30), show="")
        new_priority = create_entry(window=win1, relief="flat", width=10, x=740, y=80+(process_count*30), show="")
        Burst_time.append(new_burst_time)
        Arrival_time.append(new_arrival_time)
        Priority.append(new_priority)

def remove_process():
    global process_count
    global Burst_time
    global Arrival_time
    global Priority
    global p_labels
    if process_count > 0:
        Burst_time.pop().destroy()
        Arrival_time.pop().destroy()
        Priority.pop().destroy()
        p_labels.pop().destroy()
        process_count -= 1

def back_menu(win):
    global process_count
    global Burst_time
    global Arrival_time
    global Priority
    process_count = 0
    Burst_time.clear()
    Arrival_time.clear()
    Priority.clear()
    win.destroy()

def write():
    global Burst_time
    print(Burst_time[0].get())

def create_process_export_page(win):
    prc_export_Win = Toplevel(win)
    prc_export_Win.overrideredirect(True)
    prc_export_Win.geometry("900x550+318+157")
    
    """    Create Canvas   """
    canvas = Canvas(prc_export_Win, width=300, height=550)
    canvas.place(x=0, y=0)
    background_image = ImageTk.PhotoImage(Image.open("D:\Programming\Python\PythonCode\OS\images\Linear-Gradient3.png"))
    canvas.create_image(0, 0, anchor=NW, image=background_image) 

    """    Create Button    """
    back_to_proc_mng = create_button(window=prc_export_Win, text='Back To Process Mangement', font='Helvetica 9 bold',
                                command=lambda: prc_export_Win.destroy(),
                                relief="flat", height=2, width=25, button_color='Purple',
                                font_color='White', x=50, y=445, state=NORMAL) 

    prc_export_Win.wm_attributes('-alpha', 1)
    prc_export_Win.mainloop() 

def find_min(mylist):
    inedx = 0
    count = -1
    ter = mylist[0]
    for temp in mylist:
        count += 1
        if temp < ter:
            ter = temp
            index = count
    return inedx, ter

def min_index(mylist):
    mini = min(mylist)
    counter = -1
    for temp in mylist:
        counter += 1
        if mini == temp:
            return counter

def find_process_start_time(namelist, timelist, p):
    for temp in range(len(namelist)):
        if p == namelist[temp]:
            return timelist[temp]
    return -1

def find_process_end_time(namelist, timelist, p):
    for temp in range(len(namelist)):
        if p == namelist[temp]:
            return timelist[temp + 1]
    return -1

def FCFS(win):
    prc_export_Win = Toplevel(win)
    prc_export_Win.overrideredirect(True)
    prc_export_Win.geometry("900x550+318+157")
    
    """    Create Canvas   """
    canvas = Canvas(prc_export_Win, width=300, height=550)
    canvas.place(x=0, y=0)
    background_image = ImageTk.PhotoImage(Image.open("D:\Programming\Python\PythonCode\OS\images\Linear-Gradient3.png"))
    canvas.create_image(0, 0, anchor=NW, image=background_image) 

    """    Create Button    """
    back_to_proc_mng = create_button(window=prc_export_Win, text='Back To Process Mangement', font='Helvetica 9 bold',
                                command=lambda: prc_export_Win.destroy(),
                                relief="flat", height=2, width=25, button_color='Purple',
                                font_color='White', x=50, y=445, state=NORMAL) 

    """    algo    """
    global process_count
    burst = []
    arrival = []
    proc = []
    new_burst = []
    new_arrival = []
    new_proc = []
    name = []
    time = []
    for temp in range (process_count):
        burst.append(int(Burst_time[temp].get()))
    for temp2 in range (process_count):
        arrival.append(int(Arrival_time[temp2].get()))
    for temp3 in range (process_count):
        proc.append(temp3 + 1)
    a = 0
    b = 0
    for temp4 in range(process_count):
        a, b = find_min(arrival)
        inx = min_index(arrival)
        new_arrival.append(arrival[inx])
        new_burst.append(burst[inx])
        new_proc.append(proc[inx])
        arrival.pop(inx)
        burst.pop(inx)
        proc.pop(inx)
        

    time.append(new_arrival[0])
    time.append(new_arrival[0]+new_burst[0])
    name.append(new_proc[0])
    for temp5 in range(process_count - 1):
        if time[-1] < new_arrival[temp5 + 1]:
            time.append(new_arrival[temp5 + 1])
            time.append(new_arrival[temp5 + 1] + new_burst[temp5 + 1])
            name.append(0)
            name.append(new_proc[temp5 + 1])
        else:
            time.append(time[-1] + new_burst[temp5 + 1])
            name.append(new_proc[temp5 + 1])

    """    avg wait time    """
    start_time = []
    sumy = 0
    avg_time = 0.0
    for i in range(process_count):
        start_time.append(find_process_start_time(name, time, i + 1))
        sumy = sumy + start_time[i] - new_arrival[i]
    avg_time = sumy / process_count
    create_label(window=prc_export_Win, text="Avrage Wait Time :", font='Helvetica 15 bold', font_color="Black",
                change_color=False, color="Green",x=350, y=400)
    create_label(window=prc_export_Win, text=avg_time, font='Helvetica 15 bold', font_color="Black",
                change_color=False, color="Green",x=550, y=400)

    """    turn around time    """
    end_time = []
    sumt = 0
    turn_ar_time = 0.0
    for j in range(process_count):
        end_time.append(find_process_end_time(name,time, j + 1))
        sumt = sumt + end_time[j] - new_arrival[j]
    turn_ar_time = sumt / process_count
    create_label(window=prc_export_Win, text="Turn Around Time :", font='Helvetica 15 bold', font_color="Black",
                change_color=False, color="Green",x=350, y=450)
    create_label(window=prc_export_Win, text=turn_ar_time, font='Helvetica 15 bold', font_color="Black",
                change_color=False, color="Green",x=550, y=450)

    """    show    """
    colorlist = ['Red', 'Orange', 'Yellow', 'green yellow', 'Green', 'Blue', 'Purple', 'Pink']
    alllen = 30*len(name)
    startx = ((600 - alllen)/2) + 300
    for temp6 in range(len(name)):
        if name[temp6] == 0:
            create_label(window=prc_export_Win, text=" L  ", font='Helvetica 12 bold', font_color="Black",
                        change_color=True, color="Gray",x=startx + (temp6 *30), y=250)
        else:
            newname = " " + "P" + str(name[temp6]) + " "
            create_label(window=prc_export_Win, text=newname, font='Helvetica 12 bold', font_color="Black",
                        change_color=True, color=colorlist[name[temp6] - 1],x=startx + (temp6 *30), y=250)

    for temp7 in range(len(time)):
        create_label(window=prc_export_Win, text=time[temp7], font='Helvetica 10 bold', font_color="Black",
                    change_color=False, color="Gray",x=startx + (temp7 *30) - 10, y=280)        


    """    end    """
    prc_export_Win.wm_attributes('-alpha', 1)
    prc_export_Win.mainloop() 

def SJF(win):
    prc_export_Win = Toplevel(win)
    prc_export_Win.overrideredirect(True)
    prc_export_Win.geometry("900x550+318+157")
    
    """    Create Canvas   """
    canvas = Canvas(prc_export_Win, width=300, height=550)
    canvas.place(x=0, y=0)
    background_image = ImageTk.PhotoImage(Image.open("D:\Programming\Python\PythonCode\OS\images\Linear-Gradient3.png"))
    canvas.create_image(0, 0, anchor=NW, image=background_image) 

    """    Create Button    """
    back_to_proc_mng = create_button(window=prc_export_Win, text='Back To Process Mangement', font='Helvetica 9 bold',
                                command=lambda: prc_export_Win.destroy(),
                                relief="flat", height=2, width=25, button_color='Purple',
                                font_color='White', x=50, y=445, state=NORMAL) 

    """    algo    """
    global process_count
    burst = []
    arrival = []
    proc = []
    new_burst = []
    new_arrival = []
    new_proc = []
    name = []
    time = []
    for temp in range (process_count):
        burst.append(int(Burst_time[temp].get()))
    for temp2 in range (process_count):
        arrival.append(int(Arrival_time[temp2].get()))
    for temp3 in range (process_count):
        proc.append(temp3 + 1)
    a = 0
    b = 0
    for temp4 in range(process_count):
        a, b = find_min(arrival)
        inx = min_index(arrival)
        new_arrival.append(arrival[inx])
        new_burst.append(burst[inx])
        new_proc.append(proc[inx])
        arrival.pop(inx)
        burst.pop(inx)
        proc.pop(inx)

    new_arrival0 = new_arrival.copy()
    new_burst3 = []
    new_arrival3 = []
    new_proc3 = []
    lenr = len(new_arrival)
    now = new_arrival[0]
    indx = 0
    first = True
    for temp6 in range(lenr):

        for temp5 in range(len(new_arrival)):
            if new_arrival[temp5] <= now:
                new_arrival3.append(new_arrival[temp5])
                new_burst3.append(new_burst[temp5])
                new_proc3.append(new_proc[temp5])
                indx = min_index(new_burst3)
        if first:
            time.append(new_arrival[indx])
            time.append(time[temp6] + new_burst[indx])
            name.append(new_proc[indx])
            first = False
        else:
            if time[-1] < new_arrival[indx]:
                time.append(new_arrival[indx])
                time.append(new_arrival[indx] + new_burst[indx])
                name.append(0)
                name.append(new_proc[indx])
            else:
                time.append(time[-1] + new_burst[indx])
                name.append(new_proc[indx])

        new_arrival.pop(indx)
        new_burst.pop(indx)
        new_proc.pop(indx)
        new_arrival3.clear()
        new_burst3.clear()
        new_proc3.clear()
        now = time[-1]

    """    avg wait time    """
    start_time = []
    sumy = 0
    avg_time = 0.0
    for i in range(process_count):
        start_time.append(find_process_start_time(name, time, i + 1))
        sumy = sumy + start_time[i] - new_arrival0[i]
    avg_time = sumy / process_count
    create_label(window=prc_export_Win, text="Avrage Wait Time :", font='Helvetica 15 bold', font_color="Black",
                change_color=False, color="Green",x=350, y=400)
    create_label(window=prc_export_Win, text=avg_time, font='Helvetica 15 bold', font_color="Black",
                change_color=False, color="Green",x=550, y=400)

    """    turn around time    """
    end_time = []
    sumt = 0
    turn_ar_time = 0.0
    for j in range(process_count):
        end_time.append(find_process_end_time(name,time, j + 1))
        sumt = sumt + end_time[j] - new_arrival0[j]
    turn_ar_time = sumt / process_count
    create_label(window=prc_export_Win, text="Turn Around Time :", font='Helvetica 15 bold', font_color="Black",
                change_color=False, color="Green",x=350, y=450)
    create_label(window=prc_export_Win, text=turn_ar_time, font='Helvetica 15 bold', font_color="Black",
                change_color=False, color="Green",x=550, y=450)

    """    show    """
    colorlist = ['Red', 'Orange', 'Yellow', 'green yellow', 'Green', 'Blue', 'Purple', 'Pink']
    alllen = 30*len(name)
    startx = ((600 - alllen)/2) + 300
    for temp6 in range(len(name)):
        if name[temp6] == 0:
            create_label(window=prc_export_Win, text=" L  ", font='Helvetica 12 bold', font_color="Black",
                        change_color=True, color="Gray",x=startx + (temp6 *30), y=250)
        else:
            newname = " " + "P" + str(name[temp6]) + " "
            create_label(window=prc_export_Win, text=newname, font='Helvetica 12 bold', font_color="Black",
                        change_color=True, color=colorlist[name[temp7] - 1],x=startx + (temp6 *30), y=250)

    for temp7 in range(len(time)):
        create_label(window=prc_export_Win, text=time[temp7], font='Helvetica 10 bold', font_color="Black",
                    change_color=False, color="Gray",x=startx + (temp7 *30) - 10, y=280)        


    """    end    """
    prc_export_Win.wm_attributes('-alpha', 1)
    prc_export_Win.mainloop() 

def Priority_c(win):
    prc_export_Win = Toplevel(win)
    prc_export_Win.overrideredirect(True)
    prc_export_Win.geometry("900x550+318+157")
    
    """    Create Canvas   """
    canvas = Canvas(prc_export_Win, width=300, height=550)
    canvas.place(x=0, y=0)
    background_image = ImageTk.PhotoImage(Image.open("D:\Programming\Python\PythonCode\OS\images\Linear-Gradient3.png"))
    canvas.create_image(0, 0, anchor=NW, image=background_image) 

    """    Create Button    """
    back_to_proc_mng = create_button(window=prc_export_Win, text='Back To Process Mangement', font='Helvetica 9 bold',
                                command=lambda: prc_export_Win.destroy(),
                                relief="flat", height=2, width=25, button_color='Purple',
                                font_color='White', x=50, y=445, state=NORMAL) 

    """    algo    """
    global process_count
    burst = []
    arrival = []
    pri = []
    proc = []

    new_burst = []
    new_arrival = []
    new_pri = []
    new_proc = []
    name = []
    time = []
    for temp in range (process_count):
        burst.append(int(Burst_time[temp].get()))
    for temp2 in range (process_count):
        arrival.append(int(Arrival_time[temp2].get()))
    for temp3 in range (process_count):
        pri.append(int(Priority[temp3].get()))
    for temp4 in range (process_count):
        proc.append(temp4 + 1)
    a = 0
    b = 0
    for temp5 in range(process_count):
        a, b = find_min(arrival)
        inx = min_index(arrival)
        new_arrival.append(arrival[inx])
        new_burst.append(burst[inx])
        new_pri.append(pri[inx])
        new_proc.append(proc[inx])
        arrival.pop(inx)
        burst.pop(inx)
        proc.pop(inx)
        pri.pop(inx)

    new_arrival0 = new_arrival.copy()
    new_burst3 = []
    new_arrival3 = []
    new_pri3 = []
    new_proc3 = []
    lenr = len(new_arrival)
    now = new_arrival[0]
    indx = 0
    first = True
    for temp6 in range(lenr):

        for temp5 in range(len(new_arrival)):
            if new_arrival[temp5] <= now:
                new_arrival3.append(new_arrival[temp5])
                new_burst3.append(new_burst[temp5])
                new_pri3.append(new_pri[temp5])
                new_proc3.append(new_proc[temp5])
                indx = min_index(new_pri3)
        if first:
            time.append(new_arrival[indx])
            time.append(time[temp6] + new_burst[indx])
            name.append(new_proc[indx])
            first = False
        else:
            if time[-1] < new_arrival[indx]:
                time.append(new_arrival[indx])
                time.append(new_arrival[indx] + new_burst[indx])
                name.append(0)
                name.append(new_proc[indx])
            else:
                time.append(time[-1] + new_burst[indx])
                name.append(new_proc[indx])

        new_arrival.pop(indx)
        new_burst.pop(indx)
        new_pri.pop(indx)
        new_proc.pop(indx)
        new_arrival3.clear()
        new_burst3.clear()
        new_pri3.clear()
        new_proc3.clear()
        now = time[-1]

    """    avg wait time    """
    start_time = []
    sumy = 0
    avg_time = 0.0
    for i in range(process_count):
        start_time.append(find_process_start_time(name, time, i + 1))
        sumy = sumy + start_time[i] - new_arrival0[i]
    avg_time = sumy / process_count
    create_label(window=prc_export_Win, text="Avrage Wait Time :", font='Helvetica 15 bold', font_color="Black",
                change_color=False, color="Green",x=350, y=400)
    create_label(window=prc_export_Win, text=avg_time, font='Helvetica 15 bold', font_color="Black",
                change_color=False, color="Green",x=550, y=400)

    """    turn around time    """
    end_time = []
    sumt = 0
    turn_ar_time = 0.0
    for j in range(process_count):
        end_time.append(find_process_end_time(name,time, j + 1))
        sumt = sumt + end_time[j] - new_arrival0[j]
    turn_ar_time = sumt / process_count
    create_label(window=prc_export_Win, text="Turn Around Time :", font='Helvetica 15 bold', font_color="Black",
                change_color=False, color="Green",x=350, y=450)
    create_label(window=prc_export_Win, text=turn_ar_time, font='Helvetica 15 bold', font_color="Black",
                change_color=False, color="Green",x=550, y=450)

    """    show    """
    colorlist = ['Red', 'Orange', 'Yellow', 'green yellow', 'Green', 'Blue', 'Purple', 'Pink']
    alllen = 30*len(name)
    startx = ((600 - alllen)/2) + 300
    for temp6 in range(len(name)):
        if name[temp6] == 0:
            create_label(window=prc_export_Win, text=" L  ", font='Helvetica 12 bold', font_color="Black",
                        change_color=True, color="Gray",x=startx + (temp6 *30), y=250)
        else:
            newname = " " + "P" + str(name[temp6]) + " "
            create_label(window=prc_export_Win, text=newname, font='Helvetica 12 bold', font_color="Black",
                        change_color=True, color=colorlist[name[temp6] - 1],x=startx + (temp6 *30), y=250)

    for temp7 in range(len(time)):
        create_label(window=prc_export_Win, text=time[temp7], font='Helvetica 10 bold', font_color="Black",
                    change_color=False, color="Gray",x=startx + (temp7 *30) - 10, y=280)  

    """    end    """
    prc_export_Win.wm_attributes('-alpha', 1)
    prc_export_Win.mainloop() 

def next_arrive(arrive, arrivelist):
    for temp in arrivelist:
        if arrive < temp:
            return temp
    return -1

def update_list(index, element, mylist):
    mylist.remove(mylist[index])
    mylist.insert(index, element)
    return mylist

def SRT(win):
    prc_export_Win = Toplevel(win)
    prc_export_Win.overrideredirect(True)
    prc_export_Win.geometry("900x550+318+157")
    
    """    Create Canvas   """
    canvas = Canvas(prc_export_Win, width=300, height=550)
    canvas.place(x=0, y=0)
    background_image = ImageTk.PhotoImage(Image.open("D:\Programming\Python\PythonCode\OS\images\Linear-Gradient3.png"))
    canvas.create_image(0, 0, anchor=NW, image=background_image) 

    """    Create Button    """
    back_to_proc_mng = create_button(window=prc_export_Win, text='Back To Process Mangement', font='Helvetica 9 bold',
                                command=lambda: prc_export_Win.destroy(),
                                relief="flat", height=2, width=25, button_color='Purple',
                                font_color='White', x=50, y=445, state=NORMAL) 

    """    algo    """
    global process_count
    burst = []
    arrival = []
    proc = []
    new_burst = []
    new_arrival = []
    new_proc = []
    name = []
    time = []
    for temp in range (process_count):
        burst.append(int(Burst_time[temp].get()))
    for temp2 in range (process_count):
        arrival.append(int(Arrival_time[temp2].get()))
    for temp3 in range (process_count):
        proc.append(temp3 + 1)
    a = 0
    b = 0
    for temp4 in range(process_count):
        a, b = find_min(arrival)
        inx = min_index(arrival)
        new_arrival.append(arrival[inx])
        new_burst.append(burst[inx])
        new_proc.append(proc[inx])
        arrival.pop(inx)
        burst.pop(inx)
        proc.pop(inx)

    new_arrival0 = new_arrival.copy()
    new_burst3 = []
    new_arrival3 = []
    new_proc3 = []
    lenr = len(new_arrival)
    now = new_arrival[0]
    indx = 0
    first = True
    temp6 = -1
    while new_arrival != []:
        temp6 += 1
        for temp5 in range(len(new_arrival)):
            if new_arrival[temp5] <= now:
                new_arrival3.append(new_arrival[temp5])
                new_burst3.append(new_burst[temp5])
                new_proc3.append(new_proc[temp5])
                indx = min_index(new_burst3)
        if first:
            time.append(new_arrival[indx])
            if  next_arrive(new_arrival[indx], new_arrival) != -1:
                if next_arrive(new_arrival[indx], new_arrival) >= new_burst[indx]:
                    time.append(time[temp6] + new_burst[indx])
                    update_list(indx, 0, new_burst)
                else:
                    time.append(next_arrive(new_arrival[indx], new_arrival))
                    update_list(indx, new_burst[indx] + next_arrive(new_arrival[indx], new_arrival) - new_arrival[indx], new_burst)
            else:
                time.append(time[temp6] + new_burst[indx])
                update_list(indx, 0, new_burst)
            name.append(new_proc[indx])
            first = False
        else:
            if time[-1] < new_arrival[indx]:
                time.append(new_arrival[indx])
                if  next_arrive(new_arrival[indx], new_arrival) != -1:
                    if next_arrive(new_arrival[indx], new_arrival)-new_arrival[indx] >= new_burst[indx]:                    
                        time.append(new_arrival[indx] + new_burst[indx])
                        update_list(indx, 0, new_burst)
                    else:
                        time.append(next_arrive(new_arrival[indx], new_arrival))
                        update_list(indx, new_burst[indx] + next_arrive(new_arrival[indx], new_arrival) - new_arrival[indx], new_burst)
                else:
                    time.append(new_arrival[indx] + new_burst[indx])
                    update_list(indx, 0, new_burst)
                name.append(0)
                name.append(new_proc[indx])
            else:
                if  next_arrive(new_arrival[indx], new_arrival) != -1:
                    if next_arrive(new_arrival[indx], new_arrival)-time[-1] >= new_burst[indx]:
                        time.append(time[-1] + new_burst[indx])
                        update_list(indx, 0, new_burst)
                    else:
                        time.append(next_arrive(new_arrival[indx], new_arrival))
                        update_list(indx, new_burst[indx] + next_arrive(new_arrival[indx], new_arrival) - new_arrival[indx], new_burst)
                else:
                    time.append(time[-1] + new_burst[indx])
                    update_list(indx, 0, new_burst)
                name.append(new_proc[indx])

        if new_burst[indx] == 0:
            new_arrival.pop(indx)
            new_burst.pop(indx)
            new_proc.pop(indx)
        new_arrival3.clear()
        new_burst3.clear()
        new_proc3.clear()
        now = time[-1]
        print(name)
        print(time)

    """    end    """
    prc_export_Win.wm_attributes('-alpha', 1)
    prc_export_Win.mainloop()

def process_start_time(namelist, timelist, p):
    s = -1
    for temp in range(len(namelist)):
        if p == namelist[temp]:
            s = timelist[temp]
    return s

def process_end_time(namelist, timelist, p):
    s = -1
    for temp in range(len(namelist)):
        if p == namelist[temp]:
            s = timelist[temp + 1]
    return s



def MLFQ():
    prc_export_Win = Toplevel(win)
    prc_export_Win.overrideredirect(True)
    prc_export_Win.geometry("900x550+318+157")
    
    """    Create Canvas   """
    canvas = Canvas(prc_export_Win, width=300, height=550)
    canvas.place(x=0, y=0)
    background_image = ImageTk.PhotoImage(Image.open("D:\Programming\Python\PythonCode\OS\images\Linear-Gradient3.png"))
    canvas.create_image(0, 0, anchor=NW, image=background_image) 

    """    Create Button    """
    back_to_proc_mng = create_button(window=prc_export_Win, text='Back To Process Mangement', font='Helvetica 9 bold',
                                command=lambda: prc_export_Win.destroy(),
                                relief="flat", height=2, width=25, button_color='Purple',
                                font_color='White', x=50, y=445, state=NORMAL) 

    """    algo    """                                
    global process_count
    burst = []
    arrival = []
    proc = []
    name = []
    time = []
    cntxswt = 0
    if ContextSwitch[0].get() != '':
        cntxswt = int(ContextSwitch[0].get())
    for temp in range (process_count):
        burst.append(int(Burst_time[temp].get()))
    for temp2 in range (process_count):
        arrival.append(0)    
    for temp3 in range (process_count):
        proc.append(temp3 + 1)
    burst0 = []
    burst0 = burst.copy()

    """    for first Q    """
    endlist = []
    time.append(0)
    for temp4 in range(process_count):
        if burst[temp4] <= 4:
            time.append(burst[temp4] + time[-1])
            name.append(proc[temp4])
            endlist.append(temp4)
        else:
            time.append(4 + time[-1])
            name.append(proc[temp4])
            update_list(temp4, burst[temp4] - 4, burst)
        if cntxswt > 0:
            time.append(time[-1] + cntxswt)
            name.append(0)
    for temp4 in endlist:
        burst.pop(temp4)
        proc.pop(temp4)
    endlist.clear()

    """    for Second Q    """
    for temp4 in range(len(burst)):
        if burst[temp4] <= 8:
            time.append(burst[temp4] + time[-1])
            name.append(proc[temp4])
            endlist.append(temp4)
        else:
            time.append(8 + time[-1])
            name.append(proc[temp4])
            update_list(temp4, burst[temp4] - 8, burst)
        if cntxswt > 0:
            time.append(time[-1] + cntxswt)
            name.append(0)
    for temp4 in endlist:
        burst.pop(temp4)
        proc.pop(temp4)
    endlist.clear()
    
    """    for End Q    """
    for temp4 in range(len(burst)):
        time.append(burst[temp4] + time[-1])
        name.append(proc[temp4])
        if cntxswt > 0:
            time.append(time[-1] + cntxswt)
            name.append(0) 

    
    """    avg wait time    """
    end_time = []
    sumy = 0
    avg_time = 0.0
    for i in range(process_count):
        end_time.append(process_end_time(name, time, i + 1))
        sumy = sumy + end_time[i] - burst0[i]
    avg_time = sumy / process_count
    create_label(window=prc_export_Win, text="Avrage Wait Time :", font='Helvetica 15 bold', font_color="Black",
                change_color=False, color="Green",x=350, y=400)
    create_label(window=prc_export_Win, text=avg_time, font='Helvetica 15 bold', font_color="Black",
                change_color=False, color="Green",x=550, y=400) 

    """    turn around time    """
    end_time2 = []
    sumt = 0
    turn_ar_time = 0.0
    for j in range(process_count):
        end_time2.append(process_end_time(name,time, j + 1))
        sumt = sumt + end_time2[j]
    turn_ar_time = sumt / process_count
    create_label(window=prc_export_Win, text="Turn Around Time :", font='Helvetica 15 bold', font_color="Black",
                change_color=False, color="Green",x=350, y=450)
    create_label(window=prc_export_Win, text=turn_ar_time, font='Helvetica 15 bold', font_color="Black",
                change_color=False, color="Green",x=550, y=450)

    """    show    """
    colorlist = ['Red', 'Orange', 'Yellow', 'green yellow', 'Green', 'Blue', 'Purple', 'Pink']
    alllen = 30*len(name)
    startx = ((600 - alllen)/2) + 300
    for temp6 in range(len(name)):
        if name[temp6] == 0:
            create_label(window=prc_export_Win, text=" L  ", font='Helvetica 12 bold', font_color="Black",
                        change_color=True, color="Gray",x=startx + (temp6 *30), y=250)
        else:
            newname = " " + "P" + str(name[temp6]) + " "
            create_label(window=prc_export_Win, text=newname, font='Helvetica 12 bold', font_color="Black",
                        change_color=True, color=colorlist[name[temp6] - 1],x=startx + (temp6 *30), y=250)

    for temp7 in range(len(time)):
        create_label(window=prc_export_Win, text=time[temp7], font='Helvetica 10 bold', font_color="Black",
                    change_color=False, color="Gray",x=startx + (temp7 *30) - 10, y=280)   

 
    """    end    """
    prc_export_Win.wm_attributes('-alpha', 1)
    prc_export_Win.mainloop() 




def create_proccess_magement_page(win):
    proccess_Win = Toplevel(win)
    proccess_Win.overrideredirect(True)
    proccess_Win.geometry("900x550+318+157")
    
    """    Create Canvas   """
    canvas = Canvas(proccess_Win, width=300, height=550)
    canvas.place(x=0, y=0)
    background_image = ImageTk.PhotoImage(Image.open("D:\Programming\Python\PythonCode\OS\images\Linear-Gradient2.png"))
    canvas.create_image(0, 0, anchor=NW, image=background_image)

    """    Create Label    """
    create_label(window=proccess_Win, text="Proccess Magement", font='Helvetica 20 bold', font_color="Black",
                 change_color=False, color="White",x=475, y=30)
    create_label(window=proccess_Win, text="Proccess", font='Helvetica 14 bold', font_color="Black",
                 change_color=False, color="White",x=350, y=70)
    create_label(window=proccess_Win, text="Burst Time", font='Helvetica 14 bold', font_color="Black",
                 change_color=False, color="White",x=475, y=70)
    create_label(window=proccess_Win, text="Arrival Time", font='Helvetica 14 bold', font_color="Black",
                 change_color=False, color="White",x=600, y=70)
    create_label(window=proccess_Win, text="Priority", font='Helvetica 14 bold', font_color="Black",
                 change_color=False, color="White",x=740, y=70)
    create_label(window=proccess_Win, text="Context Switch for RR and MLFQ : ", font='Helvetica 14 bold', font_color="Black",
                 change_color=False, color="White",x=350, y=360)

    """    Create Entry    """
    cntx = create_entry(window=proccess_Win, relief="flat", width=16, x=680, y=360, show="")
    ContextSwitch.append(cntx)

    """    Create Button    """
    button_FCFS = create_button(window=proccess_Win, text='First Come First Serve', font='Helvetica 9 bold',
                                command=lambda: FCFS(proccess_Win),
                                relief="flat", height=2, width=25, button_color='Gold',
                                font_color='Black', x=50, y=40, state=NORMAL)
    button_SJF = create_button(window=proccess_Win, text='Shortest Job First', font='Helvetica 9 bold',
                                command=lambda: SJF(proccess_Win),
                                relief="flat", height=2, width=25, button_color='Gold',
                                font_color='Black', x=50, y=90, state=NORMAL)
    button_Priority = create_button(window=proccess_Win, text='Priority', font='Helvetica 9 bold',
                                command=lambda: Priority_c(proccess_Win),
                                relief="flat", height=2, width=25, button_color='Gold',
                                font_color='Black', x=50, y=140, state=NORMAL)
    button_SRT = create_button(window=proccess_Win, text='Shortest Remaining Time', font='Helvetica 9 bold',
                                command=lambda: SRT(proccess_Win),
                                relief="flat", height=2, width=25, button_color='Gold',
                                font_color='Black', x=50, y=190, state=NORMAL)
    button_RR = create_button(window=proccess_Win, text='Round Robin', font='Helvetica 9 bold',
                                command=lambda: write(),
                                relief="flat", height=2, width=25, button_color='Gold',
                                font_color='Black', x=50, y=240, state=NORMAL)
    button_MLFQ = create_button(window=proccess_Win, text='MLFQ', font='Helvetica 9 bold',
                                command=lambda: MLFQ(),
                                relief="flat", height=2, width=25, button_color='Gold',
                                font_color='Black', x=50, y=290, state=NORMAL)
    button_add_process = create_button(window=proccess_Win, text='Add Process', font='Helvetica 9 bold',
                                command=lambda: add_process(proccess_Win),
                                relief="flat", height=2, width=25, button_color='Dark Orange',
                                font_color='Black', x=50, y=355, state=NORMAL)
    button_remove_process = create_button(window=proccess_Win, text='Remove Process', font='Helvetica 9 bold',
                                command=lambda: remove_process(),
                                relief="flat", height=2, width=25, button_color='Dark Orange',
                                font_color='Black', x=50, y=405, state=NORMAL)
    button_back_menu = create_button(window=proccess_Win, text='Back Menu', font='Helvetica 9 bold',
                                command=lambda: back_menu(proccess_Win),
                                relief="flat", height=2, width=25, button_color='Coral',
                                font_color='Black', x=50, y=470, state=NORMAL)

    proccess_Win.wm_attributes('-alpha', 1)
    proccess_Win.mainloop()

if __name__ == '__main__':
    """    Create Custom Window    """
    win = Tk()
    win.overrideredirect(True)
    win.geometry("900x550+318+157")

    """    Create Canvas   """
    canvas = Canvas(win, width=550, height=550)
    canvas.place(x=0, y=0)
    background_image = ImageTk.PhotoImage(Image.open("D:\Programming\Python\PythonCode\OS\images\Linear-Gradient.png"))
    canvas.create_image(0, 0, anchor=NW, image=background_image)

    """    Create Label    """
    create_label(window=win, text="CPU Scheduler", font='Helvetica 20 bold', font_color="Black",
                 change_color=False, color="White",x=625, y=50)

    """    Create Button    """
    button_proccess_magement = create_button(window=win, text='Proccess Magement', font='Helvetica 9 bold',
                                  command=lambda: create_proccess_magement_page(win),
                                  relief="flat", height=2, width=36, button_color='Orange',
                                  font_color='Black', x=595, y=400, state=NORMAL)
    button_exit = create_button(window=win, text='Exit', font='Helvetica 9 bold',
                                command=win.destroy,
                                relief="flat", height=2, width=36, button_color='Orange',
                                font_color='Black', x=595, y=445, state=NORMAL)

    win.wm_attributes('-alpha', 1)
    win.mainloop()