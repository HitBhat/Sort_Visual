from tkinter import *
from tkinter import *
from tkinter import ttk
import random
from bubbleSortAlgo import bubbleSort


root = Tk()
root.title('Sorting Algorithm Visualisation')
root.maxsize(900, 600)
root.config(bg="black")
# Upto this point it creates a black window of max size 900*600 with a title

# variables
selected_alg = StringVar()
data = []

def drawData(data, colorArray):
    canvas.delete("all")
    c_height = 380
    c_width = 600
    x_width = c_width/(len(data) + 1)
    # so that we don't start from the borders
    offset = 30
    spacing = 10
    normalisedData = [i / max(data) for i in data]
    for i, height in enumerate(normalisedData):
        # top left
        x0 = i * x_width + offset + spacing
        y0 = c_height - height * 340
        #bottom right
        x1 = (i+1)*x_width + offset
        y1 = c_height

        canvas.create_rectangle(x0, y0, x1, y1, fill=colorArray[i]) #red not been moved
        canvas.create_text(x0+2, y0, anchor=SW, text=str(data[i]))
    root.update_idletasks()
# Command for UI button
def generate():
    global data
    # print('Alg Selected', selected_alg.get())  # to get the value selected from combobox
    # data = [6, 4, 2, 1]
    # smart thing will be to normalise the data, before showing it onto the screen

    # its not that the user always enters a value that can be converted to min value we need to do this as try except
    # try:
    #     minValue = int(minEntry.get())
    # except:
    #     minValue = 1
    #
    #
    # try:
    #     maxValue = int(maxEntry.get())
    # except:
    #     maxValue = 20
    #
    #
    # try:
    #     sizeValue = int(sizeEntry.get())
    # except:
    #     sizeValue = 10

    # if minValue   < 0 : minValue=0
    #
    # if maxValue > 100 : maxValue =100
    #
    # if sizeValue > 30 or sizeValue < 3 : size = 25

    # if minValue>maxValue: minValue, maxValue = maxValue, minValue
    minValue = int(minEntry.get())
    maxValue = int(maxEntry.get())
    sizeValue = int(sizeEntry.get())

    data = []
    for _ in range(sizeValue):
        data.append(random.randrange(minValue, maxValue+1))

    drawData(data, ['red' for x in range(len(data))])

def startAlgorithm():
    global data
    bubbleSort(data, drawData, speedScale.get())

# frame/base layout
UI_frame = Frame(root, width=600, height=200, bg='grey')
UI_frame.grid(row=0, column=0, padx=10, pady=5)

#canvas
canvas = Canvas(root, width=600, height=380, bg='white')
canvas.grid(row=1, column=0, padx=10, pady=5)

#User Interface
#Row[0]
Label(UI_frame, text='Algorithm', bg='grey').grid(row=0, column=0, padx=5, pady=10, sticky=W)
algMenu = ttk.Combobox(UI_frame, textvariable=selected_alg, values=['Bubble Sort', 'Merge Sort'])
algMenu.grid(row=0, column=1, padx=5, pady=12)
algMenu.current(0)

speedScale = Scale(UI_frame, from_=0.1, to=2.0, length=200, digits = 2, resolution=0.2, orient=HORIZONTAL, label='Select Speed')
speedScale.grid(row=0, column=2, padx=5, pady=5)
Button(UI_frame, text='Start', command=startAlgorithm , bg='red').grid(row=0, column=3, padx=5, pady=10, sticky=W)

#Row[1]
# Label(UI_frame, text='Size', bg='grey').grid(row=1, column=0, padx=5, pady=10, sticky=W)
sizeEntry = Scale(UI_frame, from_=3, to=25, resolution=1, orient=HORIZONTAL, label='Data Size')
sizeEntry.grid(row=1, column=0, padx=5, pady=10, sticky=W)

# Label(UI_frame, text='Min Value', bg='grey').grid(row=1, column=2, padx=5, pady=10, sticky=W)
minEntry = Scale(UI_frame, from_=0, to=10, resolution=1, orient=HORIZONTAL, label='Min Value')
minEntry.grid(row=1, column=1, padx=5, pady=10, sticky=W)

# Label(UI_frame, text='Max Value', bg='grey').grid(row=1, column=4, padx=5, pady=10, sticky=W)
maxEntry = Scale(UI_frame, from_=10, to=100, resolution=1, orient=HORIZONTAL, label='Max Value')
maxEntry.grid(row=1, column=2, padx=5, pady=10, sticky=W)

Button(UI_frame, text='Generate', command=generate, bg='white').grid(row=1, column=3, padx=5, pady=10, sticky=W)
root.mainloop()