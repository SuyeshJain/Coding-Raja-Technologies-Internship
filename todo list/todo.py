from tkinter import *
# from tkinter import ttk


class todo:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do-List")
        self.root.geometry("950x710+300+150")

        self.label = Label(
            self.root,
            text="To-DO-List-App",
            font="ariel,25,bold",
            width=10,
            bd=5,
            bg="green",
            fg="black",
        )
        self.label.pack(side="top", fill=BOTH)

        self.label2 = Label(
            self.root,
            text="Add-Task",
            font="ariel,18,bold",
            width=10,
            bd=5,
            bg="green",
            fg="black",
        )
        self.label2.place(x=150, y=50)

        self.label3 = Label(
            self.root,
            text="Tasks",
            font="ariel,18,bold",
            width=10,
            bd=5,
            bg="green",
            fg="black",
        )
        self.label3.place(x=590, y=50)

        self.main_text = Listbox(
            self.root, height=15, width=40, bd=5, font="ariel,20,bold"
        )
        self.main_text.place(x=430, y=120)

        self.text = Text(self.root, bd=5, height=2, width=30, font="ariel,10,bold")
        self.text.place(x=40, y=120)

        # ***************************add task***************************

        def add():
            content = self.text.get(1.0, END)
            self.main_text.insert(END, content)
            with open("data.txt", "w") as file:
                file.write(content)
            self.text.delete(1.0, END)

        def delete():
            delete_ = self.main_text.curselection()
            look = self.main_text.get(delete_[0])
            with open("data.txt", "r+") as f:
                new_f = f.readlines()
                f.seek(0)
                for line in new_f:
                    item = str(look)
                    if item not in line:
                        f.write(line)
                f.truncate()
            self.main_text.delete(delete_[0])

        with open('data.txt' , 'r') as file:
            read = file.readlines()
            for i in read:
                ready = i.split()
                self.main_text.insert(END, ready)
            file.close()

        self.button = Button(
            self.root,
            text="Add",
            font="ariel,18,bold",
            width=10,
            bd=5,
            bg="green",
            fg="black",
            command=add,
        )
        self.button.place(x=150, y=250)

        self.button2 = Button(
            self.root,
            text="Delete",
            font="ariel,18,bold",
            width=10,
            bd=5,
            bg="green",
            fg="black",
            command=delete,
        )
        self.button2.place(x=150, y=350)


def main():
    root = Tk()
    ui = todo(root)
    root.mainloop()


if __name__ == "__main__":
    main()
