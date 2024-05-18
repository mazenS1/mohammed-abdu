import tkinter as tk 
import time


text_set = ["اه اه اه اههه اه اه اهههه اه اهههه ... القلببب من يمكم نزاعععع","لو حاولو صعب تحويله ... القلببب من يمكم نزاع ... لوحاولو تحويلهه... ايوههه قلبي قلبي عليك التاععع"]

sleep_time_between_lines = 1
sleep_time_between_chars = 0.17

def محمد_عبدة():
    current_text = ""
    for i, line in enumerate(text_set):
        if i != 0:  
            time.sleep(sleep_time_between_lines)
        line += "\n"  
        for char in line:
            time.sleep(sleep_time_between_chars)  
            current_text += char  
            label.config(text=current_text)
            root.update()


root = tk.Tk()
root.title("محمد عبده")
root.geometry("500x500")  
root.configure(bg='black')  
label = tk.Label(root, fg="white", bg="black", font=("Helvetica", 16,"bold") )  
label.pack()


start_button = tk.Button(root, text="محمد عبده", command=محمد_عبدة, bg="lightgray" )
start_button.place(x=225, y=100)  

root.mainloop()
