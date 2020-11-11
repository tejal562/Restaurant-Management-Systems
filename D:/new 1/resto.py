
from tkinter import*
import random
import time;

root = Tk()
root.geometry("1600x800+0+0")
root.title("Restaurant Management Systems")


text_Input = StringVar()
operator ="" 

Tops = Frame(root, width = 1600,height = 50,bg="powder blue", relief=SUNKEN)
Tops.pack(side=TOP)

f1 = Frame(root, width = 800,height = 700, relief=SUNKEN)
f1.pack(side=LEFT)

f2 = Frame(root, width = 1600,height = 700, relief=SUNKEN)
f2.pack(side=RIGHT)
#=============================time=============================
localtime=time.asctime(time.localtime(time.time()))
#=========================info========================================
lblInfo = Label(Tops, font=('arial',30, 'bold'),text="Tejal Sharad Jadhav",fg="Black", bd=10, anchor='w')
lblInfo.grid(row=0,column=0)

lblInfo = Label(Tops, font=('arial',50, 'bold'),text="Restaurant Management Systems",fg="Black", bd=10, anchor='w')
lblInfo.grid(row=1,column=0)


lblInfo = Label(Tops, font=('arial',20, 'bold'),text=localtime,fg="Black", bd=10, anchor='w')
lblInfo.grid(row=2,column=0)
#=================================calculator=======================

def btnClick(numbers):
    global operator
    operator = operator + str(numbers)
    text_Input.set(operator)

def btnClearDisplay():
    global operator
    operator=""
    text_Input.set("")

def btnEqualsInput():
    global operator
    sumup=str(eval(operator))
    text_Input.set(sumup)
    operator=""
                    
def Ref():
    x = random.randint(10908, 500876)
    randomRef = str(x)
    rand.set(randomRef)

    CoF =float(Fries.get())
    CoD =float(Drinks.get())
    CoFilet =float(Filet.get())
    CoBurger =float(Burger.get())
    CoChicken_Burger =float(Chicken_Burger.get())
    CoCheese_Burger =float(Cheese_Burger.get())
    
    CostofFries = CoF * 0.99
    CostofDrinks = CoD * 1.00
    CostofFilet = CoFilet * 2.99
    CostofBurger = CoBurger * 2.87
    CostofChicken_Burger = CoChicken_Burger * 2.89
    CostofCheese_Burger = CoCheese_Burger * 2.69

    CostofMeal = "INR", str('%.2f' % (CostofFries + CostofDrinks + CostofFilet + CostofBurger
                                      + CostofChicken_Burger + CostofCheese_Burger))
    
    PayTax = ((CostofFries + CostofDrinks + CostofFilet + CostofBurger
                                      + CostofChicken_Burger + CostofCheese_Burger) * 0.2)

    TotalCost = (CostofFries + CostofDrinks + CostofFilet + CostofBurger
                                      + CostofChicken_Burger + CostofCheese_Burger)

    Service_Charge = ((CostofFries + CostofDrinks + CostofFilet + CostofBurger
                                      + CostofChicken_Burger + CostofCheese_Burger)/99)
 
    
 
 
    

    CostofMeal = "INR", str('%.2f' % Service_Charge)
    OverAllCost ="INR", str('%.2f' % (PayTax + TotalCost + Service_Charge ))
    PaidTax = "INR", str('%.2f' % PayTax)
    ServiceCharge.set(ServiceCharge)
    Cost.set(CostofMeal)
    Tax.set(PaidTax)
    SubTotal.set(CostofMeal)
    Total.set(OverAllCost)
   
 
   
   

def qExit():
    root.destroy()

def Reset():
    rand.set("")
    Fries.set("")
    Burger.set("")
    Filet.set("")
    SubTotal.set("")
    Total.set("")
    ServiceCharge.set("") 
    Drinks.set("")
    Tax.set("")
    Cost.set("")
    Chicken_Burger.set("")
    Cheese_Burger.set("")

txtDisplay = Entry(f2,font=('arial', 20,'bold'), textvariable=text_Input ,bd=30, insertwidth=4,
                    bg="blue", justify='right').grid(columnspan=4)

btn7=Button(f2,padx=16,bd=8, fg="black",font=('arial', 20,'bold'),
            text="7", bg="blue",command=lambda:btnClick(7)).grid(row=1,column=0)

btn8=Button(f2,padx=16,bd=8, fg="black",font=('arial', 20,'bold'),
            text="8", bg="blue",command=lambda:btnClick(8)).grid(row=1,column=1)

btn9=Button(f2,padx=16,bd=8, fg="black",font=('arial', 20,'bold'),
            text="9", bg="blue",command=lambda:btnClick(9)).grid(row=1,column=2)

Addition=Button(f2,padx=16,bd=8, fg="black",font=('arial', 20,'bold'),
            text="+", bg="blue",command=lambda:btnClick("+")).grid(row=1,column=3)
#============================================================================================

btn4=Button(f2,padx=16,bd=8, fg="black",font=('arial', 20,'bold'),
            text="4", bg="blue",command=lambda:btnClick(4)).grid(row=2,column=0)

btn5=Button(f2,padx=16,bd=8, fg="black",font=('arial', 20,'bold'),
            text="5", bg="blue",command=lambda:btnClick(5)).grid(row=2,column=1)

btn6=Button(f2,padx=16,bd=8, fg="black",font=('arial', 20,'bold'),
            text="6", bg="blue",command=lambda:btnClick(6)).grid(row=2,column=2)

Subtraction=Button(f2,padx=16,pady=16,bd=8, fg="black",font=('arial', 20,'bold'),
            text="-", bg="blue",command=lambda:btnClick("-")).grid(row=2,column=3)
#===============================================================================
btn1=Button(f2,padx=16,pady=16,bd=8, fg="black",font=('arial', 20,'bold'),
            text="1", bg="blue",command=lambda:btnClick(1)).grid(row=3,column=0)

btn2=Button(f2,padx=16,pady=16,bd=8, fg="black",font=('arial', 20,'bold'),
            text="2", bg="blue",command=lambda:btnClick(2)).grid(row=3,column=1)

btn3=Button(f2,padx=16,pady=16,bd=8, fg="black",font=('arial', 20,'bold'),
            text="3", bg="blue",command=lambda:btnClick(3)).grid(row=3,column=2)

Multiplication=Button(f2,padx=16,pady=16,bd=8, fg="black",font=('arial', 20,'bold'),
            text="*", bg="blue",command=lambda:btnClick("*")).grid(row=3,column=3)

#====================================================================================
btn0=Button(f2,padx=16,pady=16,bd=8, fg="black",font=('arial', 20,'bold'),
            text="0", bg="blue",command=lambda:btnClick(0)).grid(row=4,column=0)

btnClear=Button(f2,padx=16,pady=16,bd=8, fg="black",font=('arial', 20,'bold'),
            text="C", bg="blue",command=btnClearDisplay).grid(row=4,column=1)

btnEquals=Button(f2,padx=16,pady=16,bd=8, fg="black",font=('arial', 20,'bold'),
            text="=", bg="blue",command=btnEqualsInput).grid(row=4,column=2)

Division=Button(f2,padx=16,pady=16,bd=8, fg="black",font=('arial', 20,'bold'),
            text="/", bg="blue",command=lambda:btnClick("/")).grid(row=4,column=3)

#======================================================res info==============================================
rand = StringVar()
Fries = StringVar()
Burger = StringVar()
Filet = StringVar()
SubTotal = StringVar()
Total = StringVar()
ServiceCharge = StringVar() 
Drinks = StringVar()
Tax = StringVar()
Cost = StringVar()
Chicken_Burger = StringVar()
Cheese_Burger = StringVar()


lblReference = Label(f1,font=('arial', 16,'bold'), text="Reference", bd=16, anchor='w')
lblReference.grid(row=0,column=0)
txtReference=Entry(f1,font=('arial', 16,'bold'), textvariable=rand, bd=10, insertwidth=4,
                   bg="powder blue", justify = 'right')
txtReference.grid(row=0,column=1)

lblFries = Label(f1,font=('arial', 16,'bold'), text="Veg_Maratha", bd=16, anchor='w')
lblFries.grid(row=1,column=0)
txtFries=Entry(f1,font=('arial', 16,'bold'), textvariable=Fries, bd=10, insertwidth=4,
                   bg="powder blue", justify = 'right')
txtFries.grid(row=1,column=1)

lblBurger = Label(f1,font=('arial', 16,'bold'), text="Kaju_Carry", bd=16, anchor='w')
lblBurger.grid(row=2,column=0)
txtBurger=Entry(f1,font=('arial', 16,'bold'), textvariable=Burger, bd=10, insertwidth=4,
                   bg="powder blue", justify = 'right')
txtBurger.grid(row=2,column=1)

lblFilet = Label(f1,font=('arial', 16,'bold'), text="Mix_veg", bd=16, anchor='w')
lblFilet.grid(row=3,column=0)
txtFilet=Entry(f1,font=('arial', 16,'bold'), textvariable=Filet, bd=10, insertwidth=4,
                   bg="powder blue", justify = 'right')
txtFilet.grid(row=3,column=1)

lblChicken = Label(f1,font=('arial', 16,'bold'), text="Panner", bd=16, anchor='w')
lblChicken.grid(row=4,column=0)
txtChicken=Entry(f1,font=('arial', 16,'bold'), textvariable=Chicken_Burger, bd=10, insertwidth=4,
                   bg="powder blue", justify = 'right')
txtChicken.grid(row=4,column=1)

lblCheese = Label(f1,font=('arial', 16,'bold'), text="Vda rassa", bd=16, anchor='w')
lblCheese.grid(row=5,column=0)
txtCheese=Entry(f1,font=('arial', 16,'bold'), textvariable=Cheese_Burger, bd=10, insertwidth=4,
                   bg="powder blue", justify = 'right')
txtCheese.grid(row=5,column=1)



#=====================================res2=============================

lblDrinks = Label(f1,font=('arial', 16,'bold'), text="Drinks", bd=16, anchor='w')
lblDrinks.grid(row=0,column=2)
txtDrinks = Entry(f1,font=('arial', 16,'bold'), textvariable=Drinks, bd=10, insertwidth=4,
                   bg="powder blue", justify='right')
txtDrinks.grid(row=0,column=3)

lblCost = Label(f1,font=('arial', 16,'bold'), text="Cost of Meal", bd=16, anchor='w')
lblCost.grid(row=1,column=2)
txtCost=Entry(f1,font=('arial', 16,'bold'), textvariable=Cost, bd=10, insertwidth=4,
                   bg="powder blue", justify='right')
txtCost.grid(row=1,column=3)

lblServiceCharge = Label(f1,font=('arial', 16,'bold'), text="Service Charge", bd=16, anchor='w')
lblServiceCharge.grid(row=2,column=2)
txtServiceCharge =Entry(f1,font=('arial', 16,'bold'), textvariable=ServiceCharge , bd=10, insertwidth=4,
                   bg="powder blue", justify='right')
txtServiceCharge.grid(row=2,column=3)

lblStateTax = Label(f1,font=('arial', 16,'bold'), text="State Tax", bd=16, anchor='w')
lblStateTax.grid(row=3,column=2)
txtStateTax=Entry(f1,font=('arial', 16,'bold'), textvariable=Tax, bd=10, insertwidth=4,
                   bg="powder blue", justify='right')
txtStateTax.grid(row=3,column=3)

lblSubTotal = Label(f1,font=('arial', 16,'bold'), text="Sub Total", bd=16, anchor='w')
lblSubTotal.grid(row=4,column=2)
txtSubTotal=Entry(f1,font=('arial', 16,'bold'), textvariable=SubTotal, bd=10, insertwidth=4,
                   bg="powder blue", justify='right')
txtSubTotal.grid(row=4,column=3)

lblTotalCost = Label(f1,font=('arial', 16,'bold'), text="Total Cost", bd=16, anchor='w')
lblTotalCost.grid(row=5,column=2)
txtTotalCost=Entry(f1,font=('arial', 16,'bold'), textvariable=Total, bd=10, insertwidth=4,
                   bg="powder blue", justify='right')
txtTotalCost.grid(row=5,column=3)
 
#===========================button==================================================

btnTotal=Button(f1,padx=16,pady=8, bd=16, fg="black",font=('arial', 16,'bold'), width=10,
                text="Total", bg="powder blue", command = Ref).grid(row=7, column=1)


btnReset=Button(f1,padx=16,pady=8, bd=16, fg="black",font=('arial', 16,'bold'), width=10,
                text="Reset", bg="powder blue", command = Reset).grid(row=7, column=2)


btnExit=Button(f1,padx=16,pady=8, bd=16, fg="black",font=('arial', 16,'bold'), width=10,
                text="Exit", bg="powder blue", command = qExit).grid(row=7, column=3)


root.mainloop()
