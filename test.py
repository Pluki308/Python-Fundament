from appJar import gui

def option_changed(name):
    print("Selected:", app.getOptionBox("options"))

app = gui("OptionBox Example", "300x200")

app.addLabel("title", "Choose an option:")
app.addOptionBox("options", ["Apple", "Banana", "Cherry"])



app.go()
