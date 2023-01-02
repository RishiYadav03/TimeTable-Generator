from tkinter import *
import sqlite3

root = Tk()
root.title("Main window")

conn = sqlite3.connect('Table1.db')

c = conn.cursor()
'''c.execute("""CREATE TABLE timetable(
          day text,
          p1 text,
          p2 text,
          p3 text,
          Break text,
          p4 text,
          p5 text,
          p6 text,
          p7 text
)""")'''

#Switch type for data retrivation
rc=1
Crc=str(rc)
rc1=2
Crc1=str(rc1)
rc2=3
Crc2=str(rc2)
rc3=4
Crc3=str(rc3)
rc4=5
Crc4=str(rc4)
rc5=6
Crc5=str(rc5)
rc6=7
Crc6=str(rc6)
rc7=8
Crc7=str(rc7)
rc8=9
Crc8=str(rc8)
rc9=10
Crc9=str(rc9)
rc10=11
Crc10=str(rc10)
rc11=12
Crc11=str(rc11)
rc12=13
Crc12=str(rc12)

def update():
    conn = sqlite3.connect('Table1.db')
    c = conn.cursor()
    record_id = edit_box.get()

    c.execute("""UPDATE timetable SET
        day = :day,
        p1 = :p1,
        p2 = :p2,
        p3 = :p3,
        Break = :Break,
        p4 = :p4,
        p5 = :p5,
        p6 = :p6,
        p7 = :p7

        WHERE oid = :oid""",
              {'day': day_editor.get(),
               'p1': p1_editor.get(),
               'p2': p2_editor.get(),
               'p3': p3_editor.get(),
               'Break': Break_editor.get(),
               'p4': p4_editor.get(),
               'p5': p5_editor.get(),
               'p6': p6_editor.get(),
               'p7': p7_editor.get(),
               'oid': record_id
               })
    
    conn.commit()
    conn.close()

    editor.destroy()
    
def show():
    global newwin
    newwin = Tk()

    conn = sqlite3.connect('Table1.db')
    c = conn.cursor()

    Head_label = Label(newwin, text="Saraswati College of Engineering DS Department")
    Head_label.grid(row=0, column=2, columnspan=5)
    Head_label.config(font=("Arial",22))

    #Label for view
    L10 = Label(newwin, text="Day")
    L10.grid(row=1, column=0, padx=10)

    L11 = Label(newwin, text="1st Period")
    L11.grid(row=1, column=1, padx=10)

    L12 = Label(newwin, text="2nd Period")
    L12.grid(row=1, column=2, padx=10)

    L13 = Label(newwin, text="3rd Period")
    L13.grid(row=1, column=3, padx=10)

    L14 = Label(newwin, text="Break")
    L14.grid(row=1, column=4, padx=10)

    L15 = Label(newwin, text="4th Period")
    L15.grid(row=1, column=5, padx=10)

    L16 = Label(newwin, text="5th Period")
    L16.grid(row=1, column=6, padx=10)

    L17 = Label(newwin, text="6th Period")
    L17.grid(row=1, column=7, padx=10)

    L18 = Label(newwin, text="7th Period")
    L18.grid(row=1, column=8, padx=10)

    c.execute("SELECT * FROM timetable WHERE oid = " +Crc)
    records = c.fetchall()

    S20 = Entry(newwin, width=20)
    S20.grid(row=2, column=0, padx=10, pady=10)
    S21 = Entry(newwin, width=20)
    S21.grid(row=2, column=1, padx=10, pady=10)
    S22 = Entry(newwin, width=20)
    S22.grid(row=2, column=2, padx=10, pady=10)
    S23 = Entry(newwin, width=20)
    S23.grid(row=2, column=3, padx=10, pady=10)
    S24 = Entry(newwin, width=20)
    S24.grid(row=2, column=4, padx=10, pady=10)
    S25 = Entry(newwin, width=20)
    S25.grid(row=2, column=5, padx=10, pady=10)
    S26 = Entry(newwin, width=20)
    S26.grid(row=2, column=6, padx=10, pady=10)
    S27 = Entry(newwin, width=20)
    S27.grid(row=2, column=7, padx=10, pady=10)
    S28 = Entry(newwin, width=20)
    S28.grid(row=2, column=8, padx=10, pady=10)

    for record in records:
        S20.insert(0, record[0])
        S21.insert(0, record[1])
        S22.insert(0, record[2])
        S23.insert(0, record[3])
        S24.insert(0, record[4])
        S25.insert(0, record[5])
        S26.insert(0, record[6])
        S27.insert(0, record[7])
        S28.insert(0, record[8])

    c.execute("SELECT * FROM timetable WHERE oid = " +Crc1)
    records = c.fetchall()

    S30 = Entry(newwin, width=20)
    S30.grid(row=3, column=0, padx=10, pady=10)
    S31 = Entry(newwin, width=20)
    S31.grid(row=3, column=1, padx=10, pady=10)
    S32 = Entry(newwin, width=20)
    S32.grid(row=3, column=2, padx=10, pady=10)
    S33 = Entry(newwin, width=20)
    S33.grid(row=3, column=3, padx=10, pady=10)
    S34 = Entry(newwin, width=20)
    S34.grid(row=3, column=4, padx=10, pady=10)
    S35 = Entry(newwin, width=20)
    S35.grid(row=3, column=5, padx=10, pady=10)
    S36 = Entry(newwin, width=20)
    S36.grid(row=3, column=6, padx=10, pady=10)
    S37 = Entry(newwin, width=20)
    S37.grid(row=3, column=7, padx=10, pady=10)
    S38 = Entry(newwin, width=20)
    S38.grid(row=3, column=8, padx=10, pady=10)

    for record in records:
        S30.insert(0, record[0])
        S31.insert(0, record[1])
        S32.insert(0, record[2])
        S33.insert(0, record[3])
        S34.insert(0, record[4])
        S35.insert(0, record[5])
        S36.insert(0, record[6])
        S37.insert(0, record[7])
        S38.insert(0, record[8])

    c.execute("SELECT * FROM timetable WHERE oid = " +Crc2)
    records = c.fetchall()

    S40 = Entry(newwin, width=20)
    S40.grid(row=4, column=0, padx=10, pady=10)
    S41 = Entry(newwin, width=20)
    S41.grid(row=4, column=1, padx=10, pady=10)
    S42 = Entry(newwin, width=20)
    S42.grid(row=4, column=2, padx=10, pady=10)
    S43 = Entry(newwin, width=20)
    S43.grid(row=4, column=3, padx=10, pady=10)
    S44 = Entry(newwin, width=20)
    S44.grid(row=4, column=4, padx=10, pady=10)
    S45 = Entry(newwin, width=20)
    S45.grid(row=4, column=5, padx=10, pady=10)
    S46 = Entry(newwin, width=20)
    S46.grid(row=4, column=6, padx=10, pady=10)
    S47 = Entry(newwin, width=20)
    S47.grid(row=4, column=7, padx=10, pady=10)
    S48 = Entry(newwin, width=20)
    S48.grid(row=4, column=8, padx=10, pady=10)

    for record in records:
        S40.insert(0, record[0])
        S41.insert(0, record[1])
        S42.insert(0, record[2])
        S43.insert(0, record[3])
        S44.insert(0, record[4])
        S45.insert(0, record[5])
        S46.insert(0, record[6])
        S47.insert(0, record[7])
        S48.insert(0, record[8])

    c.execute("SELECT * FROM timetable WHERE oid = " +Crc3)
    records = c.fetchall()


    S50 = Entry(newwin, width=20)
    S50.grid(row=5, column=0, padx=10, pady=10)
    S51 = Entry(newwin, width=20)
    S51.grid(row=5, column=1, padx=10, pady=10)
    S52 = Entry(newwin, width=20)
    S52.grid(row=5, column=2, padx=10, pady=10)
    S53 = Entry(newwin, width=20)
    S53.grid(row=5, column=3, padx=10, pady=10)
    S54 = Entry(newwin, width=20)
    S54.grid(row=5, column=4, padx=10, pady=10)
    S55 = Entry(newwin, width=20)
    S55.grid(row=5, column=5, padx=10, pady=10)
    S56 = Entry(newwin, width=20)
    S56.grid(row=5, column=6, padx=10, pady=10)
    S57 = Entry(newwin, width=20)
    S57.grid(row=5, column=7, padx=10, pady=10)
    S58 = Entry(newwin, width=20)
    S58.grid(row=5, column=8, padx=10, pady=10)

    for record in records:
        S50.insert(0, record[0])
        S51.insert(0, record[1])
        S52.insert(0, record[2])
        S53.insert(0, record[3])
        S54.insert(0, record[4])
        S55.insert(0, record[5])
        S56.insert(0, record[6])
        S57.insert(0, record[7])
        S58.insert(0, record[8])

    c.execute("SELECT * FROM timetable WHERE oid = " +Crc4)
    records = c.fetchall()


    S60 = Entry(newwin, width=20)
    S60.grid(row=6, column=0, padx=10, pady=10)
    S61 = Entry(newwin, width=20)
    S61.grid(row=6, column=1, padx=10, pady=10)
    S62 = Entry(newwin, width=20)
    S62.grid(row=6, column=2, padx=10, pady=10)
    S63 = Entry(newwin, width=20)
    S63.grid(row=6, column=3, padx=10, pady=10)
    S64 = Entry(newwin, width=20)
    S64.grid(row=6, column=4, padx=10, pady=10)
    S65 = Entry(newwin, width=20)
    S65.grid(row=6, column=5, padx=10, pady=10)
    S66 = Entry(newwin, width=20)
    S66.grid(row=6, column=6, padx=10, pady=10)
    S67 = Entry(newwin, width=20)
    S67.grid(row=6, column=7, padx=10, pady=10)
    S68 = Entry(newwin, width=20)
    S68.grid(row=6, column=8, padx=10, pady=10)

    for record in records:
        S60.insert(0, record[0])
        S61.insert(0, record[1])
        S62.insert(0, record[2])
        S63.insert(0, record[3])
        S64.insert(0, record[4])
        S65.insert(0, record[5])
        S66.insert(0, record[6])
        S67.insert(0, record[7])
        S68.insert(0, record[8])
        
    c.execute("SELECT * FROM timetable WHERE oid = " +Crc5)
    records = c.fetchall()

    S70 = Entry(newwin, width=20)
    S70.grid(row=7, column=0, padx=10, pady=10)

    S71 = Entry(newwin, width=20)
    S71.grid(row=7, column=1, padx=10, pady=10)

    S72 = Entry(newwin, width=20)
    S72.grid(row=7, column=2, padx=10, pady=10)

    S73 = Entry(newwin, width=20)
    S73.grid(row=7, column=3, padx=10, pady=10)

    S74 = Entry(newwin, width=20)
    S74.grid(row=7, column=4, padx=10, pady=10)

    S75 = Entry(newwin, width=20)
    S75.grid(row=7, column=5, padx=10, pady=10)

    S76 = Entry(newwin, width=20)
    S76.grid(row=7, column=6, padx=10, pady=10)

    S77 = Entry(newwin, width=20)
    S77.grid(row=7, column=7, padx=10, pady=10)

    S78 = Entry(newwin, width=20)
    S78.grid(row=7, column=8, padx=10, pady=10)

    for record in records:
        S70.insert(0, record[0])
        S71.insert(0, record[1])
        S72.insert(0, record[2])
        S73.insert(0, record[3])
        S74.insert(0, record[4])
        S75.insert(0, record[5])
        S76.insert(0, record[6])
        S77.insert(0, record[7])
        S78.insert(0, record[8])
        
    L00 = Label(newwin, text="Teacher Name")
    L00.config(font=("Arial",22))
    L00.grid(row=8, column=3, columnspan=2)
    #teacher
    c.execute("SELECT * FROM timetable WHERE oid = " +Crc6)
    records = c.fetchall()

    S83 = Entry(newwin, width=20)
    S83.grid(row=9, column=3, padx=10, pady=10)
    S84 = Entry(newwin, width=20)
    S84.grid(row=9, column=4, padx=10, pady=10)

    for record in records:
        S83.insert(0, record[1])
        S84.insert(0, record[2])

    c.execute("SELECT * FROM timetable WHERE oid = " +Crc7)
    records = c.fetchall()

    S93 = Entry(newwin, width=20)
    S93.grid(row=10, column=3, padx=10, pady=10)
    S94 = Entry(newwin, width=20)
    S94.grid(row=10, column=4, padx=10, pady=10)

    for record in records:
        S93.insert(0, record[1])
        S94.insert(0, record[2])

    c.execute("SELECT * FROM timetable WHERE oid = " +Crc8)
    records = c.fetchall()

    S103 = Entry(newwin, width=20)
    S103.grid(row=11, column=3, padx=10, pady=10)
    S104 = Entry(newwin, width=20)
    S104.grid(row=11, column=4, padx=10, pady=10)

    for record in records:
        S103.insert(0, record[1])
        S104.insert(0, record[2])

    c.execute("SELECT * FROM timetable WHERE oid = " +Crc9)
    records = c.fetchall()

    S113 = Entry(newwin, width=20)
    S113.grid(row=12, column=3, padx=10, pady=10)
    S114 = Entry(newwin, width=20)
    S114.grid(row=12, column=4, padx=10, pady=10)

    for record in records:
        S113.insert(0, record[1])
        S114.insert(0, record[2])

    c.execute("SELECT * FROM timetable WHERE oid = " +Crc10)
    records = c.fetchall()

    S123 = Entry(newwin, width=20)
    S123.grid(row=13, column=3, padx=10, pady=10)
    S124 = Entry(newwin, width=20)
    S124.grid(row=13, column=4, padx=10, pady=10)

    for record in records:
        S123.insert(0, record[1])
        S124.insert(0, record[2])

    c.execute("SELECT * FROM timetable WHERE oid = " +Crc11)
    records = c.fetchall()

    S133 = Entry(newwin, width=20)
    S133.grid(row=14, column=3, padx=10, pady=10)
    S134 = Entry(newwin, width=20)
    S134.grid(row=14, column=4, padx=10, pady=10)

    for record in records:
        S133.insert(0, record[1])
        S134.insert(0, record[2])

    c.execute("SELECT * FROM timetable WHERE oid = " +Crc12)
    records = c.fetchall()

    S143 = Entry(newwin, width=20)
    S143.grid(row=15, column=3, padx=10, pady=10)
    S144 = Entry(newwin, width=20)
    S144.grid(row=15, column=4, padx=10, pady=10)

    for record in records:
        S143.insert(0, record[1])
        S144.insert(0, record[2])
def editframe():
    edit1=Toplevel(root)
    edit1.title("Edit frame")
    global edit_box
    edit_box=Entry(edit1, width=50)
    edit_box.grid(row=0,column=1,padx=20,pady=10)
    edit_boxlb=Label(edit1, text="Enter Row No. to Edit")
    edit_boxlb.grid(row=0,column=0)
    edit1_btn = Button(edit1, text="Edit Records", command=edit)
    edit1_btn.grid(row=2, column=0, columnspan=2, pady=10, padx=10, ipadx=120)
    
def edit():
    global editor
    editor = Tk()
    editor.title('Update')

    conn = sqlite3.connect('Table1.db')
    c = conn.cursor()

    record_id = edit_box.get()

    c.execute("SELECT * FROM timetable WHERE oid = " +record_id)
    records = c.fetchall()

    global day_editor
    global p1_editor
    global p2_editor
    global p3_editor
    global Break_editor
    global p4_editor
    global p5_editor
    global p6_editor
    global p7_editor

    day_editor = Entry(editor, width=30)
    day_editor.grid(row=0, column=1, padx=20, pady=(10,0))

    p1_editor = Entry(editor, width=30)
    p1_editor.grid(row=1, column=1, padx=20)

    p2_editor = Entry(editor, width=30)
    p2_editor.grid(row=2, column=1, padx=20)

    p3_editor = Entry(editor, width=30)
    p3_editor.grid(row=3, column=1, padx=20)

    Break_editor = Entry(editor, width=30)
    Break_editor.grid(row=4, column=1, padx=20)

    p4_editor = Entry(editor, width=30)
    p4_editor.grid(row=5, column=1, padx=20)

    p5_editor = Entry(editor, width=30)
    p5_editor.grid(row=6, column=1, padx=20)

    p6_editor = Entry(editor, width=30)
    p6_editor.grid(row=7, column=1, padx=20)

    p7_editor = Entry(editor, width=30)
    p7_editor.grid(row=8, column=1, padx=20)

    day_editor_label = Label(editor, text="Day Edit")
    day_editor_label.grid(row=0, column=0, pady=(10,0))

    p1_editor_label = Label(editor, text="Edit Period")
    p1_editor_label.grid(row=1, column=0)

    p2_editor_label = Label(editor, text="Edit Period")
    p2_editor_label.grid(row=2, column=0)

    p3_editor_label = Label(editor, text="Edit Period")
    p3_editor_label.grid(row=3, column=0)

    Break_editor_label = Label(editor, text="Edit Lunch Time")
    Break_editor_label.grid(row=4, column=0)

    p4_editor_label = Label(editor, text="Edit Period")
    p4_editor_label.grid(row=5, column=0)

    p5_editor_label = Label(editor, text="Edit Period")
    p5_editor_label.grid(row=6, column=0)

    p6_editor_label = Label(editor, text="Edit Period")
    p6_editor_label.grid(row=7, column=0)

    p7_editor_label = Label(editor, text="Edit Period")
    p7_editor_label.grid(row=8, column=0)

    for record in records:
        day_editor.insert(0, record[0])
        p1_editor.insert(0, record[1])
        p2_editor.insert(0, record[2])
        p3_editor.insert(0, record[3])
        Break_editor.insert(0, record[4])
        p4_editor.insert(0, record[5])
        p5_editor.insert(0, record[6])
        p6_editor.insert(0, record[7])
        p7_editor.insert(0, record[8])

    edit_btn = Button(editor, text="Save Records", command=update)
    edit_btn.grid(row=11, column=0, columnspan=2, pady=10, padx=10, ipadx=124)

def delete():
    conn = sqlite3.connect('Table1.db')
    #a create a cursor
    c = conn.cursor()
    #delete a record
    c.execute("DELETE from timetable WHERE oid=" + delete_box.get())
    conn.commit()
    conn.close()
    
"""def query():
    conn = sqlite3.connect('Table1.db')
    c = conn.cursor()
    c.execute("SELECT *, oid FROM timetable")
    records = c.fetchall()
    print_records = ' '
    for record in records:
        print_records += str(record) + "\n"

    query_label = Label(root, text=print_records)
    query_label.grid(row=13, column=0, columnspan=2)

    conn.commit()
    conn.close()"""
    
def submit():
    conn = sqlite3.connect('Table1.db')
    c = conn.cursor()
    c.execute("INSERT INTO timetable VALUES (:day, :p1, :p2, :p3, :Break, :p4, :p5, :p6, :p7)",
    {
                'day': "Time",
                'p1': a.get(),
                'p2': b.get(),
                'p3': y.get(),
                'Break': d.get(),
                'p4': z.get(),
                'p5': f.get(),
                'p6': g.get(),
                'p7': h.get(),
    })

    conn.commit()
    c.execute("INSERT INTO timetable VALUES (:day, :p1, :p2, :p3, :Break, :p4, :p5, :p6, :p7)",
    {
                'day': d1.get(),
                'p1': a1.get(),
                'p2': a4.get(),
                'p3': a5.get(),
                'Break': "Break",
                'p4': a6.get(),
                'p5': a7.get(),
                'p6': a3.get(),
                'p7': a2.get(),
    })

    conn.commit()

    c.execute("INSERT INTO timetable VALUES (:day, :p1, :p2, :p3, :Break, :p4, :p5, :p6, :p7)",
    {
                'day': d2.get(),
                'p1': a2.get(),
                'p2': a1.get(),
                'p3': a6.get(),
                'Break': "Break",
                'p4': a5.get(),
                'p5': a4.get(),
                'p6': a3.get(),
                'p7': a7.get(),
    })

    conn.commit()

    c.execute("INSERT INTO timetable VALUES (:day, :p1, :p2, :p3, :Break, :p4, :p5, :p6, :p7)",
    {
                'day': d3.get(),
                'p1': a7.get(),
                'p2': a6.get(),
                'p3': a3.get(),
                'Break': "Break",
                'p4': a5.get(),
                'p5': a2.get(),
                'p6': a1.get(),
                'p7': a4.get(),
    })

    conn.commit()

    c.execute("INSERT INTO timetable VALUES (:day, :p1, :p2, :p3, :Break, :p4, :p5, :p6, :p7)",
    {
                'day': d4.get(),
                'p1': a3.get(),
                'p2': a5.get(),
                'p3': a4.get(),
                'Break': "Break",
                'p4': a6.get(),
                'p5': a2.get(),
                'p6': a7.get(),
                'p7': a1.get(),
    })

    conn.commit()

    c.execute("INSERT INTO timetable VALUES (:day, :p1, :p2, :p3, :Break, :p4, :p5, :p6, :p7)",
    {
                'day': d5.get(),
                'p1': a4.get(),
                'p2': a2.get(),
                'p3': a7.get(),
                'Break': "Break",
                'p4': a3.get(),
                'p5': a5.get(),
                'p6': a1.get(),
                'p7': a6.get(),
    })

    conn.commit()

    c.execute("INSERT INTO timetable VALUES (:day, :p1, :p2, :p3, :Break, :p4, :p5, :p6, :p7)",
    {             'day': "0",
                  'p1': c1.get(),
                  'p2': a1.get(),
                  'p3': "0",
                  'Break': "0",
                  'p4': "0",
                  'p5': "0",
                  'p6': "0",
                  'p7': "0",
    })

    conn.commit()

    c.execute("INSERT INTO timetable VALUES (:day, :p1, :p2, :p3, :Break, :p4, :p5, :p6, :p7)",
    {             'day': "0",
                  'p1': c2.get(),
                  'p2': a2.get(),
                  'p3': "0",
                  'Break': "0",
                  'p4': "0",
                  'p5': "0",
                  'p6': "0",
                  'p7': "0",
    })

    conn.commit()

    c.execute("INSERT INTO timetable VALUES (:day, :p1, :p2, :p3, :Break, :p4, :p5, :p6, :p7)",
    {             'day': "0",
                  'p1': c3.get(),
                  'p2': a3.get(),
                  'p3': "0",
                  'Break': "0",
                  'p4': "0",
                  'p5': "0",
                  'p6': "0",
                  'p7': "0",
    })

    conn.commit()

    c.execute("INSERT INTO timetable VALUES (:day, :p1, :p2, :p3, :Break, :p4, :p5, :p6, :p7)",
    {             'day': "0",
                  'p1': c4.get(),
                  'p2': a4.get(),
                  'p3': "0",
                  'Break': "0",
                  'p4': "0",
                  'p5': "0",
                  'p6': "0",
                  'p7': "0",
    })

    conn.commit()

    c.execute("INSERT INTO timetable VALUES (:day, :p1, :p2, :p3, :Break, :p4, :p5, :p6, :p7)",
    {             'day': "0",
                  'p1': c5.get(),
                  'p2': a5.get(),
                  'p3': "0",
                  'Break': "0",
                  'p4': "0",
                  'p5': "0",
                  'p6': "0",
                  'p7': "0",
    })

    conn.commit()

    c.execute("INSERT INTO timetable VALUES (:day, :p1, :p2, :p3, :Break, :p4, :p5, :p6, :p7)",
    {             'day': "0",
                  'p1': c6.get(),
                  'p2': a6.get(),
                  'p3': "0",
                  'Break': "0",
                  'p4': "0",
                  'p5': "0",
                  'p6': "0",
                  'p7': "0",
    })

    conn.commit()

    c.execute("INSERT INTO timetable VALUES (:day, :p1, :p2, :p3, :Break, :p4, :p5, :p6, :p7)",
    {             'day': "0",
                  'p1': c7.get(),
                  'p2': a7.get(),
                  'p3': "0",
                  'Break': "0",
                  'p4': "0",
                  'p5': "0",
                  'p6': "0",
                  'p7': "0",
    })

    conn.commit()
    conn.close()
def deleteframe():
    del1=Toplevel(root)
    del1.title("Deletion frame")
    global delete_box
    delete_box=Entry(del1, width=50)
    delete_box.grid(row=0,column=1,padx=20,pady=10)
    delete_boxlb=Label(del1, text="Enter Row No. to Delete")
    delete_boxlb.grid(row=0,column=0)
    delete_btn = Button(del1, text="Delete Records", command=delete)
    delete_btn.grid(row=2, column=0, columnspan=2, pady=10, padx=10, ipadx=120)
    
def Table():
    Tab1=Toplevel(root)
    Tab1.title("Enter Time Table")
    Tab1.resizable(False,False)
    
    frame=Frame(Tab1,bg="white")
    frame.pack(fill="both",expand=True)

    """label=Label(frame,text="Fill Below Textbox to Complete Detail",bg="white",fg="black",padx=5,pady=5)
    label.grid(row=0,column=0)
    label.config(font=("Arial",16))"""
    
    global a
    lbl=Label(frame, text=" Enter time for 1st lecture ",bg="white",fg="Black",padx=5,pady=5)
    lbl.config(font=("Arial",12))
    lbl.grid(row=0,column=4)
    a=Entry(frame,width=50, bg="white", fg="black", borderwidth=5)
    a.grid(row=0,column=5,padx=20,pady=10)
    a.insert(0, " Enter timing ")

    global b
    lbl=Label(frame, text=" Enter timing for 2nd lecture ",bg="white",fg="Black",padx=5,pady=5)
    lbl.config(font=("Arial",12))
    lbl.grid(row=1,column=4)
    b=Entry(frame,width=50, bg="white", fg="black", borderwidth=5)
    b.grid(row=1,column=5,padx=20,pady=10)
    b.insert(0, " Enter timing ")

    global y
    lbl=Label(frame, text=" Enter timing for 3rd lecture ",bg="white",fg="Black",padx=5,pady=5)
    lbl.config(font=("Arial",12))
    lbl.grid(row=2,column=4)
    y=Entry(frame,width=50, bg="white", fg="black", borderwidth=5)
    y.grid(row=2,column=5,padx=20,pady=10)
    y.insert(0, " Enter timing ")

    global d
    lbl=Label(frame, text=" Break time ",bg="white",fg="Black",padx=5,pady=5)
    lbl.config(font=("Arial",12))
    lbl.grid(row=3,column=4)
    d=Entry(frame,width=50, bg="white", fg="black", borderwidth=5)
    d.grid(row=3,column=5,padx=20,pady=10)
    d.insert(0, " Enter timing ")

    global z
    lbl=Label(frame, text=" Enter timing for 5th lecture ",bg="white",fg="Black",padx=5,pady=5)
    lbl.config(font=("Arial",12))
    lbl.grid(row=4,column=4)
    z=Entry(frame,width=50, bg="white", fg="black", borderwidth=5)
    z.grid(row=4,column=5,padx=20,pady=10)
    z.insert(0, " Enter timing ")

    global f
    lbl=Label(frame, text=" Enter timing for 6th lecture ",bg="white",fg="Black",padx=5,pady=5)
    lbl.config(font=("Arial",12))
    lbl.grid(row=5,column=4)
    f=Entry(frame,width=50, bg="white", fg="black", borderwidth=5)
    f.grid(row=5,column=5,padx=20,pady=10)
    f.insert(0, " Enter timing ")

    global g
    lbl=Label(frame, text=" Enter timing for 7th lecture ",bg="white",fg="Black",padx=5,pady=5)
    lbl.config(font=("Arial",12))
    lbl.grid(row=6,column=4)
    g=Entry(frame,width=50, bg="white", fg="black", borderwidth=5)
    g.grid(row=6,column=5,padx=20,pady=10)
    g.insert(0, " Enter timing ")

    global h
    lbl=Label(frame, text=" Enter timing for 8th lecture ",bg="white",fg="Black",padx=5,pady=5)
    lbl.config(font=("Arial",12))
    lbl.grid(row=7,column=4)
    h=Entry(frame,width=50, bg="white", fg="black", borderwidth=5)
    h.grid(row=7,column=5,padx=20,pady=10)
    h.insert(0, " Enter timing ")

#enter
    global a1
    lbl=Label(frame, text="Enter Subject 1: ",bg="white",fg="Black",padx=5,pady=5)
    lbl.config(font=("Arial",12))
    lbl.grid(row=0,column=0)
    a1 = Entry(frame,width=50, bg="white", fg="black", borderwidth=5)
    a1.grid(row=0,column=1,padx=20,pady=10)
    a1.insert(0, " Subject Name ")
    
    global a2
    lbl=Label(frame, text="Enter Subject 2: ",bg="white",fg="Black",padx=5,pady=5)
    lbl.config(font=("Arial",12))
    lbl.grid(row=1,column=0)
    a2=Entry(frame,width=50, bg="white", fg="black", borderwidth=5)
    a2.grid(row=1,column=1,padx=20,pady=10)
    a2.insert(0, " Subject Name ")
    
    global a3
    lbl=Label(frame, text="Enter Subject 3: ",bg="white",fg="Black",padx=5,pady=5)
    lbl.config(font=("Arial",12))
    lbl.grid(row=2,column=0)
    a3=Entry(frame,width=50, bg="white", fg="black", borderwidth=5)
    a3.grid(row=2,column=1,padx=20,pady=10)
    a3.insert(0, " Subject Name ")
    
    global a4
    lbl=Label(frame, text="Enter Subject 4: ",bg="white",fg="Black",padx=5,pady=5)
    lbl.config(font=("Arial",12))
    lbl.grid(row=3,column=0)
    a4=Entry(frame,width=50, bg="white", fg="black", borderwidth=5)
    a4.grid(row=3,column=1,padx=20,pady=10)
    a4.insert(0, " Subject Name ")
    
    global a5
    lbl=Label(frame, text="Enter Subject 5: ",bg="white",fg="Black",padx=5,pady=5)
    lbl.config(font=("Arial",12))
    lbl.grid(row=4,column=0)
    a5=Entry(frame,width=50, bg="white", fg="black", borderwidth=5)
    a5.grid(row=4,column=1,padx=20,pady=10)
    a5.insert(0, " Subject Name ")

    global a6
    lbl=Label(frame, text="Enter Subject 6: ",bg="white",fg="Black",padx=5,pady=5)
    lbl.config(font=("Arial",12))
    lbl.grid(row=5,column=0)
    a6=Entry(frame,width=50, bg="white", fg="black", borderwidth=5)
    a6.grid(row=5,column=1,padx=20,pady=10)
    a6.insert(0, " Subject Name ")

    global a7
    lbl=Label(frame, text="Enter Subject 7: ",bg="white",fg="Black",padx=5,pady=5)
    lbl.config(font=("Arial",12))
    lbl.grid(row=6,column=0)
    a7=Entry(frame,width=50, bg="white", fg="black", borderwidth=5)
    a7.grid(row=6,column=1,padx=20,pady=10)
    a7.insert(0, " Subject Name ")

#enter for teacher
    global c1
    lbl=Label(frame, text="Enter teacher name",bg="white",fg="Black",padx=5,pady=5)
    lbl.config(font=("Arial",12))
    lbl.grid(row=0,column=2)
    c1=Entry(frame,width=50, bg="white", fg="black", borderwidth=5)
    c1.grid(row=0,column=3,padx=20,pady=10)
    c1.insert(0, " Teacher Name ")

    global c2
    lbl=Label(frame, text="Enter teacher name",bg="white",fg="Black",padx=5,pady=5)
    lbl.config(font=("Arial",12))
    lbl.grid(row=1,column=2)
    c2=Entry(frame,width=50, bg="white", fg="black", borderwidth=5)
    c2.grid(row=1,column=3,padx=20,pady=10)
    c2.insert(0, " Teacher Name ")

    global c3
    lbl=Label(frame, text="Enter teacher name",bg="white",fg="Black",padx=5,pady=5)
    lbl.config(font=("Arial",12))
    lbl.grid(row=2,column=2)
    c3=Entry(frame,width=50, bg="white", fg="black", borderwidth=5)
    c3.grid(row=2,column=3,padx=20,pady=10)
    c3.insert(0, " Teacher Name ")

    global c4
    lbl=Label(frame, text="Enter teacher name",bg="white",fg="Black",padx=5,pady=5)
    lbl.config(font=("Arial",12))
    lbl.grid(row=3,column=2)
    c4=Entry(frame,width=50, bg="white", fg="black", borderwidth=5)
    c4.grid(row=3,column=3,padx=20,pady=10)
    c4.insert(0, " Teacher Name ")

    global c5
    lbl=Label(frame, text="Enter teacher name",bg="white",fg="Black",padx=5,pady=5)
    lbl.config(font=("Arial",12))
    lbl.grid(row=4,column=2)
    c5=Entry(frame,width=50, bg="white", fg="black", borderwidth=5)
    c5.grid(row=4,column=3,padx=20,pady=10)
    c5.insert(0, " Teacher Name ")

    global c6
    lbl=Label(frame, text="Enter teacher name",bg="white",fg="Black",padx=5,pady=5)
    lbl.config(font=("Arial",12))
    lbl.grid(row=5,column=2)
    c6=Entry(frame,width=50, bg="white", fg="black", borderwidth=5)
    c6.grid(row=5,column=3,padx=20,pady=10)
    c6.insert(0, " Teacher Name ")

    global c7
    lbl=Label(frame, text="Enter teacher name",bg="white",fg="Black",padx=5,pady=5)
    lbl.config(font=("Arial",12))
    lbl.grid(row=6,column=2)
    c7=Entry(frame,width=50, bg="white", fg="black", borderwidth=5)
    c7.grid(row=6,column=3,padx=20,pady=10)
    c7.insert(0, " Teacher Name ")

    global d1
    lbl=Label(frame, text="Day Name",bg="white",fg="Black",padx=5,pady=5)
    lbl.config(font=("Arial",12))
    lbl.grid(row=10,column=4)
    d1=Entry(frame,width=50, bg="white", fg="black", borderwidth=5)
    d1.grid(row=10,column=5,padx=20,pady=10)
    d1.insert(0, " Day name ")

    global d2
    lbl=Label(frame, text="Day Name",bg="white",fg="Black",padx=5,pady=5)
    lbl.config(font=("Arial",12))
    lbl.grid(row=11,column=4)
    d2=Entry(frame,width=50, bg="white", fg="black", borderwidth=5)
    d2.grid(row=11,column=5,padx=20,pady=10)
    d2.insert(0, " Day name ")

    global d3
    lbl=Label(frame, text="Day Name",bg="white",fg="Black",padx=5,pady=5)
    lbl.config(font=("Arial",12))
    lbl.grid(row=12,column=4)
    d3=Entry(frame,width=50, bg="white", fg="black", borderwidth=5)
    d3.grid(row=12,column=5,padx=20,pady=10)
    d3.insert(0, " Day name ")

    global d4
    lbl=Label(frame, text="Day Name",bg="white",fg="Black",padx=5,pady=5)
    lbl.config(font=("Arial",12))
    lbl.grid(row=13,column=4)
    d4=Entry(frame,width=50, bg="white", fg="black", borderwidth=5)
    d4.grid(row=13,column=5,padx=20,pady=10)
    d4.insert(0, " Day name ")

    global d5
    lbl=Label(frame, text="Day Name",bg="white",fg="Black",padx=5,pady=5)
    lbl.config(font=("Arial",12))
    lbl.grid(row=14,column=4)
    d5=Entry(frame,width=50, bg="white", fg="black", borderwidth=5)
    d5.grid(row=14,column=5,padx=20,pady=10)
    d5.insert(0, " Day name ")

    query_btn = Button(frame, text="Show Records", command=show)
    query_btn.grid(row=10, column=2, columnspan=2, pady=10, padx=10, ipadx=122)

    submit_btn = Button(frame, text="Add data to databasse", command=submit)
    submit_btn.grid(row=9, column=2, columnspan=2, pady=10,  padx=10, ipadx=100)

#submit button
submit_btn = Button(root, text="Add Time Table", command=Table)
submit_btn.grid(row=9, column=0, columnspan=2, pady=10,  padx=10, ipadx=118) 

#create query button
query_btn = Button(root, text="Show Records", command=show)
query_btn.grid(row=10, column=0, columnspan=2, pady=10, padx=10, ipadx=122)

#Create  delete button
delete_btn = Button(root, text="Delete Records", command=deleteframe)
delete_btn.grid(row=11, column=0, columnspan=2, pady=10, padx=10, ipadx=120)

#Update button
edit_btn = Button(root, text="Edit Records", command=editframe)
edit_btn.grid(row=12, column=0, columnspan=2, pady=10, padx=10, ipadx=126)

conn.commit()

conn.close()

root.mainloop()
