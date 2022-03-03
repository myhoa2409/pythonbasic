#!/usr/bin/env python
# coding: utf-8

# In[52]:


# vẽ hình tròn draw circle
import turtle
pen = turtle.Turtle()
# chỉnh size, màu
pen.pensize(5)
pen.color("#B63E3E")
pen.fillcolor("#5CB63E")
pen.begin_fill()
face_size = 200
eye_size =17.5
#vẽ mặt
pen.penup()
pen.goto(0,-200)
pen.pendown()
pen.circle(face_size)
pen.end_fill()
#vẽ mắt
pen.fillcolor("#B66D3E")
pen.penup()
pen.goto(-100,50)
pen.pendown()

pen.begin_fill()
pen.circle(eye_size)
pen.end_fill()


pen.fillcolor("#B66D3E")
pen.penup()
pen.goto(100,50)
pen.pendown()

pen.begin_fill()
pen.circle(eye_size)
pen.end_fill()

#vẽ mũi nose
pen.fillcolor("#B66D3E")
pen.penup()
pen.goto(0,50)
pen.pendown()
pen.begin_fill()
pen.circle(-70,steps=3)
pen.end_fill()
#smile
pen.penup()
pen.goto(-100,-70)
pen.pendown()
pen.right(90)
pen.circle(100,180)
pen.mainloop()

turtle.done()


# In[ ]:


#tính diện tích hình tam giác
a=10
b=20
c=15

p=(a+b+c)/2

s=(p*(p-a)*(p-b)*(p-c))**0.5

print(s)

