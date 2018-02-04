from tkinter import*
from tkinter import Tk, StringVar, ttk
import random
import datetime
import time;

root=Tk()
root.geometry("1350x750+0+0")
root.title("Shop Management System")

TopFrame = Frame(root, width = 1350, height = 100, bd=14, relief='raise')
TopFrame.pack(side=TOP)

BottomFrame = Frame(root, width = 1350, height = 200, bd=34, relief='raise')
BottomFrame.pack(side=BOTTOM)

LeftmidFrame = Frame(BottomFrame, width = 750, height = 1000, bd=14, relief='raise')
LeftmidFrame.pack(side=LEFT)


RightmidFrame = Frame(BottomFrame, width = 600, height = 1000, bd=14, relief='raise')
RightmidFrame.pack(side=RIGHT)



lblTitle = Label(TopFrame, font=('arial', 30, 'bold'), text="SHOP MANAGEMENT SYSTEM", bd=10, width=41, justify='center')
lblTitle.grid(row=0,column=0)


#=============VARIABLES==================================================================================================
var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
var4 = IntVar()
var5 = IntVar()
var6 = IntVar()
var7 = IntVar()
var8 = IntVar()
var9 = IntVar()
var10 = IntVar()
var11 = IntVar()
var12 = IntVar()
var13 = IntVar()
var14 = IntVar()
var15 = IntVar()
var16 = IntVar()
var17 = IntVar()
var18 = IntVar()
var19 = IntVar()
var20 = IntVar()
VAT = StringVar()
Tax = StringVar()
Date1 = StringVar()


var1.set("0")
var2.set("")
var3.set("")
var4.set("")
var5.set("")
var6.set("")
var7.set("")
var8.set("")
var9.set("")
var10.set("")
var11.set("")
var12.set("")
var13.set("")
var14.set("")
var15.set("")
var16.set("")
var17.set("")
var18.set("")
var19.set("")
var20.set("")
VAT.set("")
Tax.set("")
Date1.set(time.strftime("%d/%m/%y"))

def product():
        if( var1.get() == "PID001"):
            var2.set("Rice")
            var3.set("White Seed")
            var4.set("200")
            var5.set("50")
            var6.set("2")
            var7.set("")
            var8.set("")
            var9.set("")
        elif (var1.get() == "PID002"):
            var2.set("Banana")
            var3.set("Black/White Seed")
            var4.set("120")
            var5.set("10")
            var6.set("2")
            var7.set("")
            var8.set("")
            var9.set("")







        
#=============(LEFT)PRODUCT DETAILS============================================================================================

lblProductID = Label(LeftmidFrame, font=('arial', 10, 'bold'), text="Product ID", bd=10, width=20, anchor='w')
lblProductID.grid(row=0,column=0)



cmbProductID = ttk.Combobox(LeftmidFrame, textvariable = var1, state='readonly' , font =('arial', 9, 'bold'), width=20 )
cmbProductID['value']=['','PID001','PID002','PID003','PID004','PID005']
cmbProductID.current(0)
cmbProductID.grid(row=0,column=1)

#=====PRODUCT NAME===============
lblProductName1 = Label(LeftmidFrame, font=('arial', 10, 'bold'), text="Product Name", bd=10, width=20, anchor='w')
lblProductName1.grid(row=1,column=0)


lblProductName2 = Label(LeftmidFrame, font=('arial', 10, 'bold'), textvariable = var2, bd=10, width=18, relief='sunken')
lblProductName2.grid(row=1,column=1)


#===DESCRIPTIONS=============
lblDescription1 = Label(LeftmidFrame, font=('arial', 10, 'bold'), text="Description", bd=10, width=20, anchor='w')
lblDescription1.grid(row=2,column=0)


lblDescription2 = Label(LeftmidFrame, font=('arial', 10, 'bold'), textvariable = var3, bd=10, width=18, relief='sunken')
lblDescription2.grid(row=2,column=1)



#====STOCK LEVEL===============
lblStockLevel1 = Label(LeftmidFrame, font=('arial', 10, 'bold'), text="Stock Level", bd=10, width=20, anchor='w')
lblStockLevel1.grid(row=3,column=0)


lblStockLevel2 = Label(LeftmidFrame, font=('arial', 10, 'bold'), textvariable = var4, bd=10, width=18, relief='sunken')
lblStockLevel2.grid(row=3,column=1)




#===============
lblReorderlevel1 = Label(LeftmidFrame, font=('arial', 10, 'bold'), text="Reorder Level", bd=10, width=20, anchor='w')
lblReorderlevel1.grid(row=4,column=0)
lblReorderlevel2 = Label(LeftmidFrame, font=('arial', 10, 'bold'), textvariable = var5, bd=10, width=18, relief='sunken')
lblReorderlevel2.grid(row=4,column=1)



lblOutofstock1 = Label(LeftmidFrame, font=('arial', 10, 'bold'), text="Out of Stock", bd=10, width=20, anchor='w')
lblOutofstock1.grid(row=5,column=0)
lblOutofstock2 = Label(LeftmidFrame, font=('arial', 10, 'bold'), textvariable = var6, bd=10, width=18, relief='sunken')
lblOutofstock2.grid(row=5,column=1)




lblNooforder1 = Label(LeftmidFrame, font=('arial', 10, 'bold'), text="NO. of Order", bd=10, width=20, anchor='w')
lblNooforder1.grid(row=6,column=0)
lblNooforder2 = Label(LeftmidFrame, font=('arial', 10, 'bold'), textvariable = var7, bd=10, width=18, relief='sunken')
lblNooforder2.grid(row=6,column=1)


lblAction1 = Label(LeftmidFrame, font=('arial', 10, 'bold'), text="Action", bd=10, width=20, anchor='w')
lblAction1.grid(row=7,column=0)
lblAction2 = Label(LeftmidFrame, font=('arial', 10, 'bold'), textvariable = var8, bd=10, width=18, relief='sunken')
lblAction2.grid(row=7,column=1)




lblReorderdate1 = Label(LeftmidFrame, font=('arial', 10, 'bold'), text="Reorder Date", bd=10, width=20, anchor='w')
lblReorderdate1.grid(row=8,column=0)
lblReorderdate2 = Label(LeftmidFrame, font=('arial', 10, 'bold'), textvariable = Date1, bd=10, width=18, relief='sunken')
lblReorderdate2.grid(row=8,column=1)

lblDiscount1 = Label(LeftmidFrame, font=('arial', 10, 'bold'), text="Discount", bd=10, width=20, anchor='w')
lblDiscount1.grid(row=9,column=0)
lblDiscount2 = Label(LeftmidFrame, font=('arial', 10, 'bold'), textvariable = var9, bd=10, width=18, relief='sunken')
lblDiscount2.grid(row=9,column=1)


lblCostperunit1 = Label(LeftmidFrame, font=('arial', 10, 'bold'), text="Cost per unit", bd=10, width=20, anchor='w')
lblCostperunit1.grid(row=10,column=0)
lblCostperunit2 = Label(LeftmidFrame, font=('arial', 10, 'bold'), textvariable = var10, bd=10, width=18, relief='sunken')
lblCostperunit2.grid(row=10,column=1)


#=========(RIGHT MID FRAME)============


lblValidfrom1 = Label(RightmidFrame, font=('arial', 10, 'bold'), text="Valid from", bd=15, width=10, anchor='w')
lblValidfrom1.grid(row=0,column=0)
lblValidfrom2 = Label(RightmidFrame, font=('arial', 10, 'bold'), textvariable = Date1, bd=14, width=15, relief='sunken')
lblValidfrom2.grid(row=0,column=1)


lblDateexpires1 = Label(RightmidFrame, font=('arial', 10, 'bold'), text="Date Expires", bd=15, width=10, anchor='w')
lblDateexpires1.grid(row=0,column=2)
lblDateexpires2 = Label(RightmidFrame, font=('arial', 10, 'bold'), textvariable = Date1, bd=14, width=15, relief='sunken')
lblDateexpires2.grid(row=0,column=3)



lblRemainder1 = Label(RightmidFrame, font=('arial', 10, 'bold'), text="Remainder", bd=15, width=10, anchor='w')
lblRemainder1.grid(row=1,column=0)
lblRemainder2 = Label(RightmidFrame, font=('arial', 10, 'bold'), textvariable = var11, bd=14, width=15, relief='sunken')
lblRemainder2.grid(row=1,column=1)


lblOnsales1 = Label(RightmidFrame, font=('arial', 10, 'bold'), text="On sales", bd=15, width=10, anchor='w')
lblOnsales1.grid(row=1,column=2)
lblOnsales2 = Label(RightmidFrame, font=('arial', 10, 'bold'), textvariable = var12, bd=14, width=15, relief='sunken')
lblOnsales2.grid(row=1,column=3)

lblOrderid1 = Label(RightmidFrame, font=('arial', 10, 'bold'), text="Order Id", bd=15, width=10, anchor='w')
lblOrderid1.grid(row=2,column=0)


cmbOrderid = ttk.Combobox(RightmidFrame, textvariable = var13, state='readonly' , font =('arial', 9, 'bold'), width=20 )
cmbOrderid['value']=['','ORD001','ORD002','ORD003','ORD004','ORD005']
cmbOrderid.current(0)
cmbOrderid.grid(row=2,column=1)


lblDateordered1 = Label(RightmidFrame, font=('arial', 10, 'bold'), text="Date Ordered", bd=15, width=10, anchor='w')
lblDateordered1.grid(row=2,column=2)
lblDateordered2 = Label(RightmidFrame, font=('arial', 10, 'bold'), textvariable = Date1, bd=14, width=15, relief='sunken')
lblDateordered2.grid(row=2,column=3)



lblCustomerid1 = Label(RightmidFrame, font=('arial', 10, 'bold'), text="Customer Id", bd=15, width=10, anchor='w')
lblCustomerid1.grid(row=3,column=0)


cmbCustomerid = ttk.Combobox(RightmidFrame, textvariable = var14, state='readonly' , font =('arial', 9, 'bold'), width=20 )
cmbCustomerid['value']=['','CID001','CID002','CID003','CID004','CID005']
cmbCustomerid.current(0)
cmbCustomerid.grid(row=3,column=1)


lblNoofitemord1 = Label(RightmidFrame, font=('arial', 10, 'bold'), text="No. of Item Ord.", bd=15, width=10, anchor='w')
lblNoofitemord1.grid(row=3,column=2)
lblNoofitemord2 = Label(RightmidFrame, font=('arial', 10, 'bold'), textvariable = var15, bd=14, width=15, relief='sunken')
lblNoofitemord2.grid(row=3,column=3)

lblFirstname1 = Label(RightmidFrame, font=('arial', 10, 'bold'), text="First Name", bd=15, width=10, anchor='w')
lblFirstname1.grid(row=4,column=0)
txtFirstname2 = Entry(RightmidFrame, font=('arial', 10, 'bold'),  bd=14, width=15)
txtFirstname2.grid(row=4,column=1)


lblItemordered1 = Label(RightmidFrame, font=('arial', 10, 'bold'), text="Item Ordered", bd=15, width=10, anchor='w')
lblItemordered1.grid(row=4,column=2)
lblItemordered2 = Label(RightmidFrame, font=('arial', 10, 'bold'), textvariable = var16, bd=14, width=15, relief='sunken')
lblItemordered2.grid(row=4,column=3)

lblSurname1 = Label(RightmidFrame, font=('arial', 10, 'bold'), text="Surname", bd=15, width=10, anchor='w')
lblSurname1.grid(row=5,column=0)
txtSurname2 = Entry(RightmidFrame, font=('arial', 10, 'bold'),  bd=14, width=15)
txtSurname2.grid(row=5,column=1)


lblPaymentmethod1 = Label(RightmidFrame, font=('arial', 10, 'bold'), text="Payment Method", bd=15, width=10, anchor='w')
lblPaymentmethod1.grid(row=5,column=2)

cmbPaymentmethod = ttk.Combobox(RightmidFrame, textvariable = var17, state='readonly' , font =('arial', 9, 'bold'), width=20 )
cmbPaymentmethod['value']=['','Cash','Master card','Visa Debit card','Debit card','Others']
cmbPaymentmethod.current(0)
cmbPaymentmethod.grid(row=5,column=3)




lblAddress1 = Label(RightmidFrame, font=('arial', 10, 'bold'), text="Address", bd=15, width=10, anchor='w')
lblAddress1.grid(row=6,column=0)
txtAddress2 = Entry(RightmidFrame, font=('arial', 10, 'bold'),  bd=14, width=14)
txtAddress2.grid(row=6,column=1)


lblAccounttype1 = Label(RightmidFrame, font=('arial', 10, 'bold'), text="Account Type", bd=15, width=10, anchor='w')
lblAccounttype1.grid(row=6,column=2)


cmbAccounttype = ttk.Combobox(RightmidFrame, textvariable = var18, state='readonly' , font =('arial', 9, 'bold'), width=20 )
cmbAccounttype['value']=['','Credit Account','Debit Account' , 'Customer Account' , ' Commercial Account']
cmbAccounttype.current(0)
cmbAccounttype.grid(row=6,column=3)




lblVAT1 = Label(RightmidFrame, font=('arial', 10, 'bold'), text="VAT", bd=15, width=10, anchor='w')
lblVAT1.grid(row=7,column=0)

cmbVAT = ttk.Combobox(RightmidFrame, textvariable = VAT, state='readonly' , font =('arial', 9, 'bold'), width=20 )
cmbVAT['value']=['','Yes','No']
cmbVAT.current(0)
cmbVAT.grid(row=7,column=1)


lblTax1 = Label(RightmidFrame, font=('arial', 10, 'bold'), text="Tax", bd=15, width=10, anchor='w')
lblTax1.grid(row=7,column=2)
lblTax2 = Label(RightmidFrame, font=('arial', 10, 'bold'), textvariable = Tax, bd=14, width=15, relief='sunken')
lblTax2.grid(row=7,column=3)

lblSubtotal1 = Label(RightmidFrame, font=('arial', 10, 'bold'), text="Sub Total", bd=15, width=10, anchor='w')
lblSubtotal1.grid(row=8,column=0)
lblSubtotal2 = Label(RightmidFrame, font=('arial', 10, 'bold'), textvariable = var19, bd=14, width=15, relief='sunken')
lblSubtotal2.grid(row=8,column=1)


lblTotal1 = Label(RightmidFrame, font=('arial', 10, 'bold'), text="Total", bd=15, width=10, anchor='w')
lblTotal1.grid(row=8,column=2)
lblTotal2 = Label(RightmidFrame, font=('arial', 10, 'bold'), textvariable = var20, bd=14, width=15, relief='sunken')
lblTotal2.grid(row=8,column=3)



btnTotal = Button(RightmidFrame, font=('arial', 10, 'bold'), text="Total", bd=6 , width = 10, command = product)
btnTotal.grid(row=9,column=0)
lblReset = Button(RightmidFrame, font=('arial', 10, 'bold'), text="Reset", bd=2)
lblReset.grid(row=9,column=1)
lblExit = Button(RightmidFrame, font=('arial', 10, 'bold'), text="Exit", bd=2)
lblExit.grid(row=9,column=2)


#==lblCostperunit1 = Label(RightmidFrame, font=('arial', 10, 'bold'), text="                        ", bd=15, width=10, anchor='w')
#==lblCostperunit1.grid(row=9,column=2)
#==lblCostperunit2 = Label(RightmidFrame, font=('arial', 10, 'bold'), textvariable = var4, bd=14, width=15, relief='sunken')
#==lblCostperunit2.grid(row=9,column=3)


root.mainloop()




