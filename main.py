import networkx as nx
import matplotlib.pyplot as plt
from tkinter import *


def color_neighbours(g, mapp, colored, value):
    try:
        for i in range(1, value):
            count = 0
            for node in list(colored):
                if sortedList[i] in list(g.neighbors(node)) and color_map[count] == colored.get(node):
                    count = count + 1
            mapp.append(color_map[count])
            colored[sortedList[i]] = color_map[count]
            for z in range(len(sortedList) - (i + 1)):
                mapp.append(defColor)
            plt.close()
            nx.draw_networkx(g, node_color=mapp, nodelist=sortedList)
            if i + 1 == value:
                plt.show()
            else:
                plt.show(block=False)
                plt.pause(1)
                plt.close()

            for y in range(len(sortedList) - (i + 1)):
                mapp.remove(defColor)

        for i in range(len(sortedList) - value):
            mapp.append(defColor)
    except IndexError:
        Label(newWindow, text="Number of colors are not enough to solve this graph.Please add more colors.").pack()


def first_color(g, mapp, colored):
    mapp.append(color_map[0])
    colored[sortedList[0]] = color_map[0]
    for y in range(len(sortedList) - len(colored)):
        mapp.append(defColor)
    nx.draw_networkx(g, node_color=mapp, nodelist=sortedList)
    plt.show(block=False)
    plt.pause(1)
    plt.close()
    for y in range(len(sortedList) - len(colored)):
        mapp.remove(defColor)


def openNewWindow():
    plt.close()
    button12["state"] = "disabled"
    Label(newWindow,
          text="Choose color").pack()

    button4.pack()

    button5.pack()

    button6.pack()

    button7.pack()

    button8.pack()

    button9.pack()

    button10.pack()

    button11.pack()


def colorChoose(m):
    if m == "red" and m not in color_map:
        color_map.append(m)
        button4["state"] = "disabled"

    if m == "green" and m not in color_map:
        color_map.append(m)
        button5["state"] = "disabled"

    if m == "gray" and m not in color_map:
        color_map.append(m)
        button6["state"] = "disabled"

    if m == "orange" and m not in color_map:
        color_map.append(m)
        button7["state"] = "disabled"

    if m == "pink" and m not in color_map:
        color_map.append(m)
        button8["state"] = "disabled"

    if m == "yellow" and m not in color_map:
        color_map.append(m)
        button9["state"] = "disabled"

    if m == "purple" and m not in color_map:
        color_map.append(m)
        button10["state"] = "disabled"

    if m == "cyan" and m not in color_map:
        color_map.append(m)
        button11["state"] = "disabled"
    button3.pack()
    entry3.pack()


def colorGraph(g):
    coloredNodes = {}
    new_map = []
    val = intVar.get()
    if val > len(sortedList):
        val = len(sortedList)
    if val == 0:
        pass
    else:
        first_color(g, new_map, coloredNodes)
        color_neighbours(g, new_map, coloredNodes, val)


def addNode():
    Node1 = Nodevar1.get()
    Node2 = Nodevar2.get()
    if Node1 == "default" or Node2 == "default":
        Label(root, text="Please enter a value.").pack()

    elif Node1 == Node2 and Node1 not in G.nodes():
        txt = "Values you have entered are the same and we can not connect a node to itself." \
              "Adding " + Node1 + " to graph. "
        Label(root, text=txt).pack()
        G.add_node(Node1)

    elif Node1 == Node2 and Node1 in G.nodes():
        txtt = "Values you have entered are the same and we can not connect a node to itself." + Node1 + " already " \
                                                                                                         "exists. "
        Label(root, text=txtt).pack()

    elif Node1 in G.nodes():
        txt1 = "You have " + Node1 + " in your graph.Connecting " + Node1 + " with " + Node2 + " ."
        Label(root, text=txt1).pack()
        G.add_node(Node2)

        G.add_edge(Node1, Node2)
    elif Node2 in G.nodes():
        txt2 = "You have " + Node2 + " in your graph.Connecting " + Node2 + " with " + Node1 + " ."
        Label(root, text=txt2).pack()
        G.add_node(Node1)

        G.add_edge(Node1, Node2)

    else:
        txt3 = "You have connected " + Node1 + " with " + Node2 + "."
        Label(root, text=txt3).pack()
        G.add_node(Node1)
        G.add_node(Node2)
        G.add_edge(Node1, Node2)

    for node in G.nodes():
        if node in NodeList:
            continue
        NodeList.append(node)


def showGraph():
    if nx.is_empty(G):
        Label(root, text="Graph is empty therefore you can not show it.Please add nodes.").pack()

    elif not nx.is_connected(G):
        Label(root,
              text=""
                   "Your graph is not connected,thus you can not solve this problem.Please connect necessary nodes."
              ).pack()
        Label(root, text="(Try connecting last 2 nodes with the ones you created before.)").pack()

    else:
        indeks = []
        degree = []
        for (node, val) in G.degree():
            degree.append(val)

        for i in range(len(degree)):
            _max = 0
            for j in range(len(degree)):
                if j not in indeks:
                    if degree[j] > _max:
                        _max = degree[j]
                        idx = j
            indeks.append(idx)
            sortedList.append(NodeList[idx])
        button12.pack()
        button1["state"] = "disabled"
        button2["state"] = "disabled"
        nx.draw_networkx(G)
        plt.show(block=False)
        plt.pause(6)
        plt.close()


root = Tk()
newWindow = Toplevel(root)
newWindow.geometry("400x700")
G = nx.Graph()
root.geometry("800x800")
plt.figure()
frame = Frame(root)
frame.pack()
bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)
Nodevar1 = StringVar(root, value="default")
Nodevar2 = StringVar(root, value="default")
intVar = IntVar(root)
NodeList = []
sortedList = []
color_map = []
defColor = "#1f78b4"

label1 = Label(frame, text="Enter the node")
label1.pack(side=LEFT)
entry1 = Entry(frame, textvariable=Nodevar1)
entry1.pack(side=LEFT)

label2 = Label(frame, text="Enter its neighbour")
label2.pack(side=LEFT)
entry2 = Entry(frame, textvariable=Nodevar2)
entry2.pack(side=LEFT)
entry3 = Entry(newWindow, textvariable=intVar)

button1 = Button(frame, text="Add", command=addNode)
button1.pack(side=LEFT)
button2 = Button(frame, text="Show Graph", command=showGraph)
button2.pack(side=LEFT)
button3 = Button(newWindow, text="Color Graph n times", command=lambda g=G: colorGraph(g))
button4 = Checkbutton(newWindow, bg='RED', width=2, command=lambda m="red": colorChoose(m))
button5 = Checkbutton(newWindow, bg='GREEN', width=2, command=lambda m="green": colorChoose(m))
button6 = Checkbutton(newWindow, bg='GRAY', width=2, command=lambda m="gray": colorChoose(m))
button7 = Checkbutton(newWindow, bg='ORANGE', width=2, command=lambda m="orange": colorChoose(m))
button8 = Checkbutton(newWindow, bg='PINK', width=2, command=lambda m="pink": colorChoose(m))
button9 = Checkbutton(newWindow, bg='YELLOW', width=2, command=lambda m="yellow": colorChoose(m))
button10 = Checkbutton(newWindow, bg='PURPLE', width=2, command=lambda m="purple": colorChoose(m))
button11 = Checkbutton(newWindow, bg='CYAN', width=2, command=lambda m="cyan": colorChoose(m))
button12 = Button(newWindow, text="Press to see and choose colors.", command=openNewWindow)

root.mainloop()