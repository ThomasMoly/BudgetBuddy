if __name__ == "__main__":
    import tkinter as tk
    root = tk.Tk()
    root.title("BudgetBuddy by TA\u2082IR Systems")
    root.geometry("880x495")
    root.config(bg="#171717")

    dummy_ent_list = ["e", 1610, 2, 28, "YEETUS", "MCSCEETUS", 3.14]
    def dummy_struct(entry):
        print(f"{entry}")
        print("To be replaced by struct_integrate")

input_frame = tk.Frame(root, width=880, height=495)
input_frame.pack(expand=True)


def exp_update():
    exp_yr = 1610
    exp_mth = 2
    exp_dy = 28
    exp_cat = "YEETUS"
    exp_nm = "MCSCEETUS"
    exp_pr = 3.14
    dummy_ent_list = ["e", exp_yr, exp_mth, exp_dy, exp_cat, exp_nm, exp_pr]
    dummy_struct(dummy_ent_list)

btn_entr = tk.Button(input_frame, text="   Enter   ", font=("Consolas", 12), command=exp_update, bg="#00FFD5")
btn_entr.place(x=520, y=437)

def update():
    print("Update: TO BE REPLACED")

btn_update = tk.Button(input_frame, text="   Update   ", font=("Consolas",14), command=update, bg="#8000FF")
btn_update.place(x=714, y=437)

def dat_wipe():
    print("Dat_wipe: TO BE REPLACED")

btn_del_accnt = tk.Button(input_frame, text="Wipe Data", font=("Consolas", 12), command=dat_wipe, bg="#FF5E00")
btn_del_accnt.place(x=729, y=380)

exp_day = ""
txtbx_exp_day = tk.Entry(input_frame, textvariable=exp_day, state="normal", font=("Consolas", 14), width=5)
txtbx_exp_day.place(x=50, y=437)
lbl_exp_day = tk.Label(text= "Day:", font=("Consolas", 10), bg="#171717", fg="#e1e1e1")
lbl_exp_day.place(x=50, y=417)

exp_nm = ""
txtbx_nm = tk.Entry(input_frame, textvariable=exp_nm, state="normal", font=("Consolas", 14), width=8)
txtbx_nm.place(x=262, y=437)
lbl_nm = tk.Label(text= "Name:", font=("Consolas", 10), bg="#171717", fg="#e1e1e1")
lbl_nm.place(x=262, y=417)

exp_price = ""
txtbx_exp_price = tk.Entry(input_frame, textvariable=exp_nm, state="normal", font=("Consolas", 14), width=9)
txtbx_exp_price.place(x=395, y=437)
lbl_exp_price = tk.Label(text= "Price:", font=("Consolas", 10), bg="#171717", fg="#e1e1e1")
lbl_exp_price.place(x=395, y=417)


root.mainloop()
