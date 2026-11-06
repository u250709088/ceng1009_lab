# def gradeMark(mark):
#     if mark >= 90:
#         return "A"
#     elif mark >= 80:
#         return "B"
#     elif mark >= 70:
#         return "C"
#     elif mark >= 60:
#         return "D"
#     else:
#         return "F"
#
# marks = [95, 80, 70, 60,65,9,40,81]
# for mark in marks:
#     print("Grade is" ,gradeMark(mark))
#
# mark = float(input("Enter your mark: "))
# print("Grade is" ,gradeMark(mark))
# import turtle
#
# def chooseColor(height):
#     if height >=200:
#         return "purple"
#     elif height >=100:
#         return "pink"
#     else:
#         return "blue"
#
# def drawBar(t, height,gap):
#     t.penup()
#     t.left(90)
#     t.forward(height + gap)
#     t.write(" " + str(height))
#     t.backward(height + gap)
#     t.right(90)
#     t.pendown()
#
#
#     t.begin_fill()
#     t.left(90)
#     t.forward(height)
#     t.right(90)
#     t.forward(40)
#     t.right(90)
#     t.forward(height)
#     t.left(90)
#     t.end_fill()
#
#     t.fillcolor(chooseColor(height))
#     t.begin_fill()
#     t.left(90)
#     t.forward(height)
#     t.right(90)
#     t.forward(40)
#     t.right(90)
#     t.forward(height)
#     t.left(90)
#     t.end_fill()
#
#
#
# def barChart(data):
#     maxheight = max(data)
#     num_bars = len(data)
#     border = 10
#
#     gap = (maxheight + border) / 25
#
#     wn = turtle.Screen()
#     wn.bgcolor("pink")
#     right = 40 * num_bars + border
#     top = maxheight + 4 + border
#     wn.setworldcoordinates(-border, -border, right, top)
#
#     right = 40 * num_bars + border
#     top = maxheight + 4 * border
#
#     wn.setworldcoordinates(-border, -border, right, right)
#     t = turtle.Turtle()
#     t.color("red")
#     t.pensize(2)
#
#     for height in data:
#         drawBar(t, height, gap)
#     wn.exitonclick()
# data = [48, 117, 200, 240, 160, 260, 220]
# barChart(data)


# import turtle
#
# def chooseColor(height):
#     if height >=200:
#         return "purple"
#     elif height >=100:
#         return "pink"
#     else:
#         return "blue"
#
# def drawBar(t, height,gap):
#     if (height >= 0):
#         labelY = height + gap
#     else:
#         labelY = gap
#
#
#     t.penup()
#     t.left(90)
#     t.forward(labelY)
#     t.write(" " + str(height))
#     t.backward(labelY)
#     t.right(90)
#     t.pendown()
#
#
#     t.begin_fill()
#     t.left(90)
#     t.forward(height)
#     t.right(90)
#     t.forward(40)
#     t.right(90)
#     t.forward(height)
#     t.left(90)
#     t.end_fill()
#
#     t.fillcolor(chooseColor(height))
#     t.begin_fill()
#     t.left(90)
#     t.forward(height)
#     t.right(90)
#     t.forward(40)
#     t.right(90)
#     t.forward(height)
#     t.left(90)
#     t.end_fill()
#
#
# def barChart(data):
#     max_height = max(data)
#     min_height = min(data)
#     num_bars = len(data)
#     border = 10
#
#     gap = (max_height + border) / 25
#
#
#     wn = turtle.Screen()
#     wn.bgcolor("yellow")
#     right = 40 * num_bars + border
#     top = max_height + 4 + border
#     bottom = min(min_height,0) - border
#     wn.setworldcoordinates(-border, -border, right, top)
#
#     right = 40 * num_bars + border
#     top = max_height + 4 * border
#
#     wn.setworldcoordinates(-border, -border, right, top)
#     t = turtle.Turtle()
#     t.color("red")
#     t.pensize(2)
#
#     for height in data:
#         drawBar(t, height, gap)
#     wn.exitonclick()
#
# data = [48, 117, 200, -60, 160, 260, -120]
# barChart(data)



# import math
#
# def findHypot(a,b):
#     hypot = math.sqrt(a**2 + b**2)
#     return hypot
#
# def CalcWithMath(a,b):
#     hypot = math.sqrt(a**2 + b**2)
#     return hypot
#
# print(findHypot(a:3,b:4))
# print(calcWithMath(a:3,b:4)