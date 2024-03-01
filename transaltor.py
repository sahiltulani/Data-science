import tkinter as tk
import pyttsx3
from googletrans import Translator

def lang_translator(lang):
    user_input=textarea.get(0.0,tk.END)
    translator=Translator()
    result=translator.translate(user_input,dest=lang)
    output.config(text=result.text)
def speak():
    user_input2=textarea.get(0.0,tk.END)
    translator2=Translator()
    result2=translator2.translate(user_input2,dest='en')
    if result2.dest=='en':
        pyttsx3.speak(result2.text)
    else:
        output.config(text='Cant speak language right now')  


root = tk.Tk()
root.title('transltor')
root.geometry('950x600')
root.config(bg='white')
translate_btn=tk.Button(text='translate',font=('',25),width=10,bg='green',fg='white',command=('en'))
punjabi_btn=tk.Button(text='punjabi',font=('',25),width=10,bg='blue',fg='white',command=lambda:lang_translator('punjabi'))
hindi_btn=tk.Button(text='Hindi',font=('',25),width=10,bg='orange',fg='white',command=lambda:lang_translator('hi'))
speak_btn=tk.Button(text='speak',font=('',25),width=10,bg='red',fg='white',command=speak)
translate_btn.grid(row=1,column=1,pady=5,padx=5)
punjabi_btn.grid(row=2,column=1,pady=5,padx=5)
hindi_btn.grid(row=3,column=1,pady=5,padx=5)
speak_btn.grid(row=4,column=1,pady=5,padx=5)
textarea=tk.Text()
textarea.grid(row=1,column=2,rowspan=4,padx=50,pady=5)
sub_heading=tk.Label(text='Translation',font=('Arial',20),fg='#3f51b5',bg='white')
sub_heading.grid(row=5,column=1,columnspan=2)
output=tk.Label(text='',font=('Arial',20),fg='#3f51b5',bg='white')
output.grid(row=6,column=1,columnspan=2,pady=10)






root.mainloop()