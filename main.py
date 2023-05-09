import tkinter

#WINDOW
window = tkinter.Tk()
window.minsize(400,300)
window.title("BMI Calculator")

#CALCULATE FUNC
def calculate_bmi():
    global bmi

    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get())
        bmi = (weight / ((height/100) ** 2))

        if bmi < 18.5:
            info_label.config(text=f"Your bmi is {bmi:.2f}. You are under weight!")
        elif 18.5 <= bmi <= 24.9:
            info_label.config(text=f"Your bmi is {bmi:.2f}. You are normal weight.")
        elif 25 <= bmi <= 29.9:
            info_label.config(text=f"Your bmi is {bmi:.2f}. You are over weight.")
        elif 30 <= bmi <= 34.9:
            info_label.config(text=f"Your bmi is {bmi:.2f}. You are obesity (Class I) weight.")
        elif 35 <= bmi <= 39.9:
            info_label.config(text=f"Your bmi is {bmi:.2f}. You are obesity (Class II) weight.")
        elif bmi >= 40 :
            info_label.config(text=f"Your bmi is {bmi:.2f}. You are extreme obesity.")


        weight_entry.delete(0,10)
        height_entry.delete(0,10)

        weight_entry.focus()
    except ValueError:
        info_label.config(text="Please check weight and height")

#WIDGETS

weight_label = tkinter.Label(text="Enter your weight(kg):")
weight_label.place(x=150, y=0)

weight_entry = tkinter.Entry()
weight_entry.config(width=16)
weight_entry.place(x=152, y=25)

info_label = tkinter.Label(text="")
info_label.place(x=90 ,y=150)


height_label = tkinter.Label(text="Enter your height(cm): ")
height_label.place(x=150, y=50)

height_entry = tkinter.Entry()
height_entry.config(width=16)
height_entry.place(x=152, y=75)

calculate_button = tkinter.Button(text="Calculate your BMI",command=calculate_bmi)
calculate_button.config(width=14)
calculate_button.place(x=150, y=110)





window.mainloop()