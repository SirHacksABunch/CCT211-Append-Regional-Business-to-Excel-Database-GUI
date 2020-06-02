'''By: Alexander Sigarev
For: CCT211 (User Interface Programming)
University: University of Toronto
Date Assignment Completed: January 25th, 2020
Date Code & GUI Updated for Final GitHub Code Release: June 2nd, 2020'''
#Assignment 1

from tkinter import *
from tkinter import Tk, Label, Button
from tkinter import messagebox
import tkinter as tk
import csv

class RegionalBusinessDatabaseAppendEntry:
    def __init__(self, master):
        self.master = master
        self.master.title("Regional Business Database: Add Entry to Excel Spreadsheet")
        self.master.geometry('900x850')

        menu = Menu(self.master)
        self.master.config(menu=menu)

        helpTab = Menu(menu, tearoff=0)
        menu.add_cascade(label='Help: ', menu=helpTab)
        helpTab.add_cascade(label='About', command=lambda: messagebox.askokcancel("About:", "This application allows you to enter in a business'"\
                                                                                  " information into the file-accessible Regional Business Database."))
        helpTab.add_cascade(label='Instructions', command=lambda: messagebox.askokcancel("Instructions:", "Add a business' information in the corresponding"\
                                                                                         " fields and click the [Append to Excel Spreadsheet] button when done. Upon"\
                                                                                         " first use, the Excel spreadsheet will automatically be created for you. Please"\
                                                                                         " note that due to programming limitations, you have to press tab after the last"\
                                                                                         " entry box you edit (known as focusout) to ensure proper updating of"\
                                                                                         " information."))
        helpTab.add_cascade(label='Application Details', command=lambda: messagebox.askokcancel("Application Details:" ,"Programmed by Alexander Sigarev for the course"\
                                                                                           " CCT211: User Interface Programming, offered at the University of Toronto."))
        
        
        self.strCENT_XInput = ''
        self.strCENT_XCheck = ''
        self.strCENT_YInput = ''
        self.strCENT_YCheck = ''
        self.strBusinessIDInput = ''
        self.strBusinessIDCheck = ''
        self.strNameInput = ''
        self.strNameCheck = ''
        self.strStreetNumberInput = ''
        self.strStreetNumberCheck = ''
        self.strStreetNameInput = ''
        self.strStreetNameCheck = ''
        self.strUnitNumberInput = ''
        self.strUnitNumberCheck = ''
        self.strPostalCodeInput = ''
        self.strPostalCodeCheck = ''
        self.strLocationInput = ''
        self.strLocationCheck = ''
        self.strWardInput = ''
        self.strWardCheck = ''
        self.strNAICSSectorInput = ''
        self.strNAICSSectorCheck = ''
        self.strEmployeeRangeInput = ''
        self.strEmployeeRangeCheck = ''
        self.strPhoneInput = ''
        self.strPhoneCheck = ''
        self.strFaxInput = ''
        self.strFaxCheck = ''
        self.strEmailInput = ''
        self.strEmailCheck = ''
        self.strWebAddressInput = ''
        self.strWebAddressCheck = ''
        self.lstFinalizedInputs = []
        self.lstFinalizedChecks = []
        

        #CENT_X
        self.labelCENT_X = Label(master, text="GPS Longitude (CENT_X)", background = "blue", foreground = "white").grid(row=0, sticky="N"+"E"+"S"+"W") #Decimal / 4 SIG FIGS
        validateCENT_X = (master.register(self.CENT_XIsFloat), "%S")
        self.entryCENT_X = tk.Entry(master, width=50, validate="focusout", validatecommand=validateCENT_X)
        self.entryCENT_X.grid(row=0, column=1,sticky="N"+"E"+"S"+"W")
        self.labelCheckCENT_X = Label(master, background = "cyan")
        self.labelCheckCENT_X.grid(row=1, columnspan=2, sticky="N"+"E"+"S"+"W")

        #CENT_Y        
        self.labelCENT_Y = Label(master, text="GPS Latitude (CENT_Y)", background = "white", foreground = "blue").grid(row=2, sticky="N"+"E"+"S"+"W") #Decimal / 4 SIG FIGS
        validateCENT_Y = (master.register(self.CENT_YIsFloat), "%S")
        self.entryCENT_Y = tk.Entry(master, width=50, validate="focusout", validatecommand=validateCENT_Y)
        self.entryCENT_Y.grid(row=2, column=1,sticky="N"+"E"+"S"+"W")
        self.labelCheckCENT_Y = Label(master, background = "cyan")
        self.labelCheckCENT_Y.grid(row=3, columnspan=2, sticky="N"+"E"+"S"+"W")

        #BusinessID        
        self.labelBusinessID = Label(master, text="Internal ID based on certification (Business ID)", background = "blue", foreground = "white").grid(row=4, sticky="N"+"E"+"S"+"W") #Integer / 4-5 DIGITS
        validateBusinessIDEntry = (master.register(self.BusinessIDIsInt), "%S")
        self.entryBusinessID = tk.Entry(master, width=50, validate="focusout", validatecommand=validateBusinessIDEntry)
        self.entryBusinessID.grid(row=4, column=1,sticky="N"+"E"+"S"+"W")
        self.labelCheckBusinessID = Label(master, background = "cyan")
        self.labelCheckBusinessID.grid(row=5, columnspan=2, sticky="N"+"E"+"S"+"W")

        #Name        
        self.labelName = Label(master, text="Registered name (Name)", background = "white", foreground = "blue").grid(row=6, sticky="N"+"E"+"S"+"W") #String
        validateName = (master.register(self.NameIsStr), "%S")
        self.entryName = tk.Entry(master, width=50, validate="focusout", validatecommand=validateName)
        self.entryName.grid(row=6, column=1,sticky="N"+"E"+"S"+"W")
        self.labelCheckName = Label(master, background = "cyan")
        self.labelCheckName.grid(row=7, columnspan=2, sticky="N"+"E"+"S"+"W")

        #Street Number
        self.labelStreetNumber = Label(master, text="Street Number", background = "blue", foreground = "white").grid(row=8, sticky="N"+"E"+"S"+"W") #Integer
        validateStreetNumber = (master.register(self.StreetNumberIsInt), "%S")
        self.entryStreetNumber = tk.Entry(master, width=50, validate="focusout", validatecommand=validateStreetNumber)
        self.entryStreetNumber.grid(row=8, column=1,sticky="N"+"E"+"S"+"W")
        self.labelCheckStreetNumber = Label(master, background = "cyan")
        self.labelCheckStreetNumber.grid(row=9, columnspan=2, sticky="N"+"E"+"S"+"W")

        #Street Name        
        self.labelStreetName = Label(master, text="Street Name", background = "white", foreground = "blue").grid(row=10, sticky="N"+"E"+"S"+"W") #String
        validateStreetName = (master.register(self.StreetNameIsStr), "%S")
        self.entryStreetName = tk.Entry(master, width=50, validate="focusout", validatecommand=validateStreetName)
        self.entryStreetName.grid(row=10, column=1,sticky="N"+"E"+"S"+"W")
        self.labelCheckStreetName = Label(master, background = "cyan")
        self.labelCheckStreetName.grid(row=11, columnspan=2, sticky="N"+"E"+"S"+"W")

        #Unit Number        
        self.labelUnitNumber = Label(master, text="Unit Number", background = "blue", foreground = "white").grid(row=12, sticky="N"+"E"+"S"+"W") #String
        validateUnitNumber = (master.register(self.UnitNumberIsStr), "%S")
        self.entryUnitNumber = tk.Entry(master, width=50, validate="focusout", validatecommand=validateUnitNumber)
        self.entryUnitNumber.grid(row=12, column=1,sticky="N"+"E"+"S"+"W")
        self.labelCheckUnitNumber = Label(master, background = "cyan")
        self.labelCheckUnitNumber.grid(row=13, columnspan=2, sticky="N"+"E"+"S"+"W")

        #Postal Code        
        self.labelPostalCode = Label(master, text="Postal Code", background = "white", foreground = "blue").grid(row=14, sticky="N"+"E"+"S"+"W") #String
        validatePostalCode = (master.register(self.PostalCodeIsStr), "%S")
        self.entryPostalCode = tk.Entry(master, width=50, validate="focusout", validatecommand=validatePostalCode)
        self.entryPostalCode.grid(row=14, column=1,sticky="N"+"E"+"S"+"W")
        self.labelCheckPostalCode = Label(master, background = "cyan")
        self.labelCheckPostalCode.grid(row=15, columnspan=2, sticky="N"+"E"+"S"+"W")

        #Location        
        self.labelLocation = Label(master, text="Location", background = "blue", foreground = "white").grid(row=16, sticky="N"+"E"+"S"+"W") #String
        validateLocation = (master.register(self.LocationIsStr), "%S")
        self.entryLocation = tk.Entry(master, width=50, validate="focusout", validatecommand=validateLocation)
        self.entryLocation.grid(row=16, column=1,sticky="N"+"E"+"S"+"W")
        self.labelCheckLocation = Label(master, background = "cyan")
        self.labelCheckLocation.grid(row=17, columnspan=2, sticky="N"+"E"+"S"+"W")

        #Ward        
        self.labelWard = Label(master, text="Regional Ward (Only Wards #1-11)", background = "white", foreground = "blue").grid(row=18, sticky="N"+"E"+"S"+"W") #Integer / 1-11 only
        validateWard = (master.register(self.WardIsInt), "%S")
        self.entryWard = tk.Entry(master, width=50, validate="focusout", validatecommand=validateWard)
        self.entryWard.grid(row=18, column=1,sticky="N"+"E"+"S"+"W")
        self.labelCheckWard = Label(master, background = "cyan")
        self.labelCheckWard.grid(row=19, columnspan=2, sticky="N"+"E"+"S"+"W")

        #NAICSSector        
        self.labelNAICSSector = Label(master, text="NAICSSector (Category of business selected from NAICS)", background = "blue", foreground = "white").grid(row=20, sticky="N"+"E"+"S"+"W") #String
        validateNAICSSector = (master.register(self.NAICSSectorIsStr), "%S")
        self.entryNAICSSector = tk.Entry(master, width=50, validate="focusout", validatecommand=validateNAICSSector)
        self.entryNAICSSector.grid(row=20, column=1,sticky="N"+"E"+"S"+"W")
        self.labelCheckNAICSSector = Label(master, background = "cyan")
        self.labelCheckNAICSSector.grid(row=21, columnspan=2, sticky="N"+"E"+"S"+"W")

        #Employee Range        
        self.labelEmployeeRange = Label(master, text="Employee Range, Categorical (e.g. 1-10)", background = "white", foreground = "blue").grid(row=22, sticky="N"+"E"+"S"+"W") #String
        validateEmployeeRange = (master.register(self.EmployeeRangeIsStr), "%S")
        self.entryEmployeeRange = tk.Entry(master, width=50, validate="focusout", validatecommand=validateEmployeeRange)
        self.entryEmployeeRange.grid(row=22, column=1,sticky="N"+"E"+"S"+"W")
        self.labelCheckEmployeeRange = Label(master, background = "cyan")
        self.labelCheckEmployeeRange.grid(row=23, columnspan=2, sticky="N"+"E"+"S"+"W")

        #Phone        
        self.labelPhone = Label(master, text="Phone Number", background = "blue", foreground = "white").grid(row=24, sticky="N"+"E"+"S"+"W") #Integer
        validatePhone = (master.register(self.PhoneIsInt), "%S")
        self.entryPhone = tk.Entry(master, width=50, validate="focusout", validatecommand=validatePhone)
        self.entryPhone.grid(row=24, column=1,sticky="N"+"E"+"S"+"W")
        self.labelCheckPhone = Label(master, background = "cyan")
        self.labelCheckPhone.grid(row=25, columnspan=2, sticky="N"+"E"+"S"+"W")

        #FAX        
        self.labelFax = Label(master, text="Fax Number", background = "white", foreground = "blue").grid(row=26, sticky="N"+"E"+"S"+"W") #Integer
        validateFax = (master.register(self.FaxIsInt), "%S")
        self.entryFax = tk.Entry(master, width=50, validate="focusout", validatecommand=validateFax)
        self.entryFax.grid(row=26, column=1,sticky="N"+"E"+"S"+"W")
        self.labelCheckFax = Label(master, background = "cyan")
        self.labelCheckFax.grid(row=27, columnspan=2, sticky="N"+"E"+"S"+"W")

        #E-Mail        
        self.labelEmail = Label(master, text="Email Address", background = "blue", foreground = "white").grid(row=28, sticky="N"+"E"+"S"+"W") #String
        validateEmail = (master.register(self.EmailIsStr), "%S")
        self.entryEmail = tk.Entry(master, width=50, validate="focusout", validatecommand=validateEmail)
        self.entryEmail.grid(row=28, column=1,sticky="N"+"E"+"S"+"W")
        self.labelCheckEmail = Label(master, background = "cyan")
        self.labelCheckEmail.grid(row=29, columnspan=2, sticky="N"+"E"+"S"+"W")

        #WebAddress        
        self.labelWebAddress = Label(master, text="URL", background = "white", foreground = "blue").grid(row=30, sticky="N"+"E"+"S"+"W") #String
        validateWebAddress = (master.register(self.WebAddressIsStr), "%S")
        self.entryWebAddress = tk.Entry(master, width=50, validate="focusout", validatecommand=validateWebAddress)
        self.entryWebAddress.grid(row=30, column=1,sticky="N"+"E"+"S"+"W")
        self.labelCheckWebAddress = Label(master, background = "cyan")
        self.labelCheckWebAddress.grid(row=31, columnspan=2, sticky="N"+"E"+"S"+"W")

        #CSV Button Finalization [Code Checks for Green Lst & Create Function to Open & Write CSV File]
        self.appendToExcelSpreadsheetButton = Button(master, text="Append to Excel Spreadsheet", command=self.buttonFinalization, background = "blue", foreground = "white", relief="raised")
        self.appendToExcelSpreadsheetButton.grid(row=32, columnspan=2)

        #Scale Rows & Columns
        self.master.columnconfigure(0, weight=1)
        self.master.columnconfigure(1, weight=1)
        self.master.rowconfigure(0, weight=1)
        self.master.rowconfigure(1, weight=1)
        self.master.rowconfigure(2, weight=1)
        self.master.rowconfigure(3, weight=1)
        self.master.rowconfigure(4, weight=1)
        self.master.rowconfigure(5, weight=1)
        self.master.rowconfigure(6, weight=1)
        self.master.rowconfigure(7, weight=1)
        self.master.rowconfigure(8, weight=1)
        self.master.rowconfigure(9, weight=1)
        self.master.rowconfigure(10, weight=1)
        self.master.rowconfigure(11, weight=1)
        self.master.rowconfigure(12, weight=1)
        self.master.rowconfigure(13, weight=1)
        self.master.rowconfigure(14, weight=1)
        self.master.rowconfigure(15, weight=1)
        self.master.rowconfigure(16, weight=1)
        self.master.rowconfigure(17, weight=1)
        self.master.rowconfigure(18, weight=1)
        self.master.rowconfigure(19, weight=1)
        self.master.rowconfigure(20, weight=1)
        self.master.rowconfigure(21, weight=1)
        self.master.rowconfigure(22, weight=1)
        self.master.rowconfigure(23, weight=1)
        self.master.rowconfigure(24, weight=1)
        self.master.rowconfigure(25, weight=1)
        self.master.rowconfigure(26, weight=1)
        self.master.rowconfigure(27, weight=1)
        self.master.rowconfigure(28, weight=1)
        self.master.rowconfigure(29, weight=1)
        self.master.rowconfigure(30, weight=1)
        self.master.rowconfigure(31, weight=1)
        self.master.rowconfigure(32, weight=1)
        

    def CENT_XIsFloat(self, *args):
        try:
            float(self.entryCENT_X.get())
            if len(self.entryCENT_X.get()) == 5 and self.entryCENT_X.get().count(".") == 1:
                self.labelCheckCENT_X.config(text="Valid CENT_X Coordinates", bg="light green")
                self.strCENT_XInput = self.entryCENT_X.get()
                self.strCENT_XCheck = 'green'
                return True
            else:
                self.labelCheckCENT_X.config(text="Invalid CENT_X Coordinates. Valid when 4 digits with one decimal anywhere in entry", bg="red")
                self.strCENT_XCheck = 'red'
                return False
        except ValueError:
            self.labelCheckCENT_X.config(text="Invalid CENT_X Coordinates. Valid when 4 digits with one decimal anywhere in entry", bg="red")
            self.strCENT_XCheck = 'red'
            return False

    def CENT_YIsFloat(self, *args):
        try:
            float(self.entryCENT_Y.get())
            if len(self.entryCENT_Y.get()) == 5 and self.entryCENT_Y.get().count(".") == 1:
                self.labelCheckCENT_Y.config(text="Valid CENT_Y Coordinates", bg="light green")
                self.strCENT_YInput = self.entryCENT_Y.get()
                self.strCENT_YCheck = 'green'
                return True
            else:
                self.labelCheckCENT_Y.config(text="Invalid CENT_Y Coordinates. Valid when 4 digits with one decimal anywhere in entry", bg="red")
                self.strCENT_YCheck = 'red'
                return False
        except ValueError:
            self.labelCheckCENT_Y.config(text="Invalid CENT_Y Coordinates. Valid when 4 digits with one decimal anywhere in entry", bg="red")
            self.strCENT_YCheck = 'red'
            return False

    def BusinessIDIsInt(self, *args):
        try:
            int(self.entryBusinessID.get())
            if len(self.entryBusinessID.get()) == 4 or len(self.entryBusinessID.get()) == 5:
                self.labelCheckBusinessID.config(text="Valid Business ID", bg="light green")
                self.strBusinessIDInput = self.entryBusinessID.get()
                self.strBusinessIDCheck = 'green'
                return True
            else:
                self.labelCheckBusinessID.config(text="Invalid Business ID. Valid when 4-5 digits entered", bg="red")
                self.strBusinessIDCheck = 'red'
                return False
        except ValueError:
            self.labelCheckBusinessID.config(text="Invalid Business ID. Valid when 4-5 digits entered", bg="red")
            self.strBusinessIDCheck = 'red'
            return False

    def NameIsStr(self, *args):
        if self.entryName.get() == '':
            self.labelCheckName.config(text="Business cannot have a blank Name", bg="red")
            self.strNameCheck = 'red'
            return False
        else:
            self.labelCheckName.config(text="Valid Name", bg="light green")
            self.strNameInput = self.entryName.get()
            self.strNameCheck = 'green'
            return True

    def StreetNumberIsInt(self, *args):
        if self.entryStreetNumber.get() == '':
            self.labelCheckStreetNumber.config(text="Business cannot have a blank Street Number", bg="red")
            self.strStreetNumberCheck = 'red'
            return False
        else:
            try:
                int(self.entryStreetNumber.get())
                self.labelCheckStreetNumber.config(text="Valid Street Number", bg="light green")
                self.strStreetNumberInput = self.entryStreetNumber.get()
                self.strStreetNumberCheck = 'green'
                return True
            except ValueError:
                self.labelCheckStreetNumber.config(text="Invalid Street Number", bg="red")
                self.strStreetNumberCheck = 'red'
                return False

    def StreetNameIsStr(self, *args):
        if self.entryStreetName.get() == '':
            self.labelCheckStreetName.config(text="Business cannot have a blank Street Name", bg="red")
            self.strStreetNameCheck = 'red'
            return False
        else:
            self.labelCheckStreetName.config(text="Valid Street Name", bg="light green")
            self.strStreetNameInput = self.entryStreetName.get()
            self.strStreetNameCheck = 'green'
            return True

    def UnitNumberIsStr(self, *args):
        if self.entryUnitNumber.get() == '':
            self.labelCheckUnitNumber.config(text="Business cannot have a blank Unit Number", bg="red")
            self.strUnitNumberCheck = 'red'
            return False
        else:
            self.labelCheckUnitNumber.config(text="Valid Unit Number", bg="light green")
            self.strUnitNumberInput = self.entryUnitNumber.get()
            self.strUnitNumberCheck = 'green'
            return True

    def PostalCodeIsStr(self, *args):
        if len(self.entryPostalCode.get()) != 7 or self.entryPostalCode.get()[3] != ' ':
            self.labelCheckPostalCode.config(text= "Invalid Postal Code. Please do "+ "L1L 1L1" + " format", bg="red")
            self.strPostalCodeCheck = 'red'
            return False
        elif self.entryPostalCode.get() == '':
            self.labelCheckPostalCode.config(text="Business cannot have a blank Postal Code", bg="red")
            self.strPostalCodeCheck = 'red'
            return False
        elif len(self.entryPostalCode.get()) == 7 and self.entryPostalCode.get()[3] == ' ':
            if self.entryPostalCode.get()[0].isalpha() and self.entryPostalCode.get()[2].isalpha() and self.entryPostalCode.get()[5].isalpha():
                if self.entryPostalCode.get()[1].isdigit() and self.entryPostalCode.get()[4].isdigit() and self.entryPostalCode.get()[6].isdigit():
                    self.labelCheckPostalCode.config(text="Valid Postal Code", bg="light green")
                    self.strPostalCodeInput = self.entryPostalCode.get()
                    self.strPostalCodeCheck = 'green'
                    return True
                else:
                     self.labelCheckPostalCode.config(text= "Invalid Postal Code. Please do "+ "L1L 1L1" + " format", bg="red")
                self.strPostalCodeCheck = 'red'
                return False
            else:
                self.labelCheckPostalCode.config(text= "Invalid Postal Code. Please do "+ "L1L 1L1" + " format", bg="red")
                self.strPostalCodeCheck = 'red'
                return False
        else:
            self.labelCheckPostalCode.config(text= "Invalid Postal Code. Please do "+ "L1L 1L1" + " format", bg="red")
            self.strPostalCodeCheck = 'red'
            return False

    def LocationIsStr(self, *args):
        if self.entryLocation.get() == '':
            self.labelCheckLocation.config(text="Business cannot have a blank Location", bg="red")
            self.strLocationCheck = 'red'
            return False
        else:
            self.labelCheckLocation.config(text="Valid Location", bg="light green")
            self.strLocationInput = self.entryLocation.get()
            self.strLocationCheck = 'green'
            return True

    def WardIsInt(self, *args):
        try:
            int(self.entryWard.get())
            if int(self.entryWard.get()) in range(1,12):
                self.labelCheckWard.config(text="Valid Ward", bg="light green")
                self.strWardInput = self.entryWard.get()
                self.strWardCheck = 'green'
                return True
            else:
                self.labelCheckWard.config(text="Invalid Ward", bg="red")
                self.strWardCheck = 'red'
                return False
        except ValueError:
            self.labelCheckWard.config(text="Invalid Ward", bg="red")
            self.strWardCheck = 'red'
            return False

    def NAICSSectorIsStr(self, *args):
        if self.entryNAICSSector.get() == '':
            self.labelCheckNAICSSector.config(text="Business cannot have a blank NAICSSector", bg="red")
            self.strNAICSSectorCheck = 'red'
            return False
        else:
            self.labelCheckNAICSSector.config(text="Valid NAICSSector", bg="light green")
            self.strNAICSSectorInput = self.entryNAICSSector.get()
            self.strNAICSSectorCheck = 'green'
            return True

    def EmployeeRangeIsStr(self, *args):
        if self.entryEmployeeRange.get() == '':
            self.labelCheckEmployeeRange.config(text="Business cannot have a blank Employee Range", bg="red")
            self.strEmployeeRangeCheck = 'red'
            return False
        elif self.entryEmployeeRange.get().count("-") == 1:
            EmployeeRangeDigits = self.entryEmployeeRange.get().replace('-', '')
            if EmployeeRangeDigits.isdigit():
                self.labelCheckEmployeeRange.config(text="Valid Employee Range", bg="light green")
                self.strEmployeeRangeInput = self.entryEmployeeRange.get()
                self.strEmployeeRangeCheck = 'green'
                return True
            else:
                self.labelCheckEmployeeRange.config(text="Invalid Employee Range. Range must include hypehn (-)", bg="red")
                self.strEmployeeRangeCheck = 'red'
                return False
        else:
            self.labelCheckEmployeeRange.config(text="Invalid Employee Range. Range must include hyphen (-)", bg="red")
            self.strEmployeeRangeCheck = 'green'
            return False

    def PhoneIsInt(self, *args):
        try:
            if len(self.entryPhone.get()) == 12 and self.entryPhone.get()[0:3].isdigit() and self.entryPhone.get()[3] == '-' and \
               self.entryPhone.get()[4:7].isdigit() and self.entryPhone.get()[7] == '-' and self.entryPhone.get()[8:12].isdigit():
                self.labelCheckPhone.config(text="Valid Phone Number", bg="light green")
                self.strPhoneInput = self.entryPhone.get()
                self.strPhoneCheck = 'green'
                return True
            else:
                self.labelCheckPhone.config(text="Invalid Phone Number. Please do ???-???-???? format", bg="red")
                self.strPhoneCheck = 'red'
                return False
        except ValueError:
            self.labelCheckPhone.config(text="Invalid Phone Number. Please do ???-???-???? format", bg="red")
            self.strPhoneCheck = 'red'
            return False

    def FaxIsInt(self, *args):
        try:
            if len(self.entryFax.get()) == 12 and self.entryFax.get()[0:3].isdigit() and self.entryFax.get()[3] == '-' and \
               self.entryFax.get()[4:7].isdigit() and self.entryFax.get()[7] == '-' and self.entryFax.get()[8:12].isdigit():
                self.labelCheckFax.config(text="Valid FAX Number", bg="light green")
                self.strFaxInput = self.entryFax.get()
                self.strFaxCheck = 'green'
                return True
            else:
                self.labelCheckFax.config(text="Invalid FAX Number. Please do ???-???-???? format", bg="red")
                self.strFaxCheck = 'red'
                return False
        except ValueError:
            self.labelCheckFax.config(text="Invalid FAX Number. Please do ???-???-???? format", bg="red")
            self.strFaxCheck = 'red'
            return False

    def EmailIsStr(self, *args):
        if self.entryEmail.get() == '':
            self.labelCheckEmail.config(text="Business cannot have a blank E-Mail", bg="red")
            self.strEmailCheck = 'red'
            return False
        elif self.entryEmail.get().count('@') == 1 and (self.entryEmail.get()[-4] == '.' or self.entryEmail.get()[-3] == '.'):
            self.labelCheckEmail.config(text="Valid E-Mail", bg="light green")
            self.strEmailInput = self.entryEmail.get()
            self.strEmailCheck = 'green'
            return True
        else:
            self.labelCheckEmail.config(text="Invalid E-Mail. Valid when _@_.[domain]", bg="red")
            self.strEmailCheck = 'red'
            return False

    def WebAddressIsStr(self, *args):
        if self.entryWebAddress.get() == '':
            self.labelCheckWebAddress.config(text="Business cannot have a blank Web Address", bg="red")
            self.strWebAddressCheck = 'red'
            return False
        elif self.entryWebAddress.get()[0:4] == 'www.' and (self.entryWebAddress.get()[-4] == '.' or self.entryWebAddress.get()[-3] == '.') and \
             self.entryWebAddress.get().count(' ') == 0:
            self.labelCheckWebAddress.config(text="Valid Web Address", bg="light green")
            self.strWebAddressInput = self.entryWebAddress.get()
            self.strWebAddressCheck = 'green'
            return True
        else:
            self.labelCheckWebAddress.config(text="Invalid Web Address. Valid when www.[website name].[domain]", bg="red")
            self.strWebAddressCheck = 'red'
            return False
    
    
    def buttonFinalization(self, **args): #Does not update properly when clicking button, also does not remove the old stuff
        self.lstFinalizedInputs.append(self.strCENT_XInput)
        self.lstFinalizedInputs.append(self.strCENT_YInput)
        self.lstFinalizedInputs.append(self.strBusinessIDInput)
        self.lstFinalizedInputs.append(self.strNameInput)
        self.lstFinalizedInputs.append(self.strStreetNumberInput)
        self.lstFinalizedInputs.append(self.strStreetNameInput)
        self.lstFinalizedInputs.append(self.strUnitNumberInput)
        self.lstFinalizedInputs.append(self.strPostalCodeInput)
        self.lstFinalizedInputs.append(self.strLocationInput)
        self.lstFinalizedInputs.append(self.strWardInput)
        self.lstFinalizedInputs.append(self.strNAICSSectorInput)
        self.lstFinalizedInputs.append(self.strEmployeeRangeInput)
        self.lstFinalizedInputs.append(self.strPhoneInput)
        self.lstFinalizedInputs.append(self.strFaxInput)
        self.lstFinalizedInputs.append(self.strEmailInput)
        self.lstFinalizedInputs.append(self.strWebAddressInput)
        
        self.lstFinalizedChecks.append(self.strCENT_XCheck)
        self.lstFinalizedChecks.append(self.strCENT_YCheck)
        self.lstFinalizedChecks.append(self.strBusinessIDCheck)
        self.lstFinalizedChecks.append(self.strNameCheck)
        self.lstFinalizedChecks.append(self.strStreetNumberCheck)
        self.lstFinalizedChecks.append(self.strStreetNameCheck)
        self.lstFinalizedChecks.append(self.strUnitNumberCheck)
        self.lstFinalizedChecks.append(self.strPostalCodeCheck)
        self.lstFinalizedChecks.append(self.strLocationCheck)
        self.lstFinalizedChecks.append(self.strWardCheck)
        self.lstFinalizedChecks.append(self.strNAICSSectorCheck)
        self.lstFinalizedChecks.append(self.strEmployeeRangeCheck)
        self.lstFinalizedChecks.append(self.strPhoneCheck)
        self.lstFinalizedChecks.append(self.strFaxCheck)
        self.lstFinalizedChecks.append(self.strEmailCheck)
        self.lstFinalizedChecks.append(self.strWebAddressCheck)
        if '' in self.lstFinalizedChecks[-16:] or 'red' in self.lstFinalizedChecks[-16:]: #Indexing negatively from first lst value to last to ensure CSV writing is proper
            self.lstFinalizedInputs.clear()
            self.lstFinalizedChecks.clear()
            confirmError = messagebox.askokcancel("Error!", "Error: You did not focusout correctly or one of your inputs is invalid. Please be sure to press tab once"\
                                                  " after editing the last entry box (known as focusout) and to check for invalid inputs as well.")
        elif len(self.lstFinalizedChecks[-16:]) == 16 and (('' not in self.lstFinalizedChecks[-16:]) or ('red' not in self.lstFinalizedChecks[-16:])):
            confirmAddingEntry = messagebox.askyesno("Confirm adding entry?", "Your business inputs are all valid. Press Yes to add the business into the database or " \
                                                     "No to edit or double check your inputs.")
            if confirmAddingEntry:
                try:
                    csvfile = open('regional_business_data_record.csv')
                    csvfile.close()
                    with open('regional_business_data_record.csv', mode='a', newline='') as csvfile:
                        RegionalBusinessDatabase = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_MINIMAL)

                        RegionalBusinessDatabase.writerow([self.lstFinalizedInputs[-16], self.lstFinalizedInputs[-15], self.lstFinalizedInputs[-14], \
                                                               self.lstFinalizedInputs[-13], self.lstFinalizedInputs[-12], self.lstFinalizedInputs[-11],  \
                                                               self.lstFinalizedInputs[-10], self.lstFinalizedInputs[-9], self.lstFinalizedInputs[-8], \
                                                               self.lstFinalizedInputs[-7], self.lstFinalizedInputs[-6], self.lstFinalizedInputs[-5], \
                                                               self.lstFinalizedInputs[-4], self.lstFinalizedInputs[-3], self.lstFinalizedInputs[-2], \
                                                            self.lstFinalizedInputs[-1]])
                except FileNotFoundError:
                    with open('regional_business_data_record.csv', mode='a+', newline='') as csvfile:
                        RegionalBusinessDatabase = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_MINIMAL)
                        RegionalBusinessDatabase.writerow(['CENT_X', 'CENT_Y', 'BusinessID', 'BusinessName', 'Street Number', 'Street Name', 'Unit Number', 'Postal Code', \
                                                                   'Location', 'Ward', 'NAICSSector', 'Employee Range', 'Phone', 'Fax', 'Email Address', 'URL'])
                        RegionalBusinessDatabase.writerow([self.lstFinalizedInputs[-16], self.lstFinalizedInputs[-15], self.lstFinalizedInputs[-14], \
                                                               self.lstFinalizedInputs[-13], self.lstFinalizedInputs[-12], self.lstFinalizedInputs[-11],  \
                                                               self.lstFinalizedInputs[-10], self.lstFinalizedInputs[-9], self.lstFinalizedInputs[-8], \
                                                               self.lstFinalizedInputs[-7], self.lstFinalizedInputs[-6], self.lstFinalizedInputs[-5], \
                                                               self.lstFinalizedInputs[-4], self.lstFinalizedInputs[-3], self.lstFinalizedInputs[-2], \
                                                            self.lstFinalizedInputs[-1]])
                self.lstFinalizedInputs.clear()
                self.lstFinalizedChecks.clear()
                confirmSuccess = messagebox.askokcancel("Success!", "Success: The business has been successfully appended to the Regional Business Database csv file."\
                                                        " If you are appending a new business, please focusout properly for inputs to be updated when appending to the"\
                                                        " database file.")
        else:
            self.lstFinalizedInputs.clear()
            self.lstFinalizedChecks.clear()
            confirmError = messagebox.askokcancel("Error!", "Error: You did not focusout correctly or one of your inputs is invalid. Please be sure to press tab once"\
                                                  " after editing the last entry box (known as focusout) and to check for invalid inputs as well.")

root = Tk()
gui = RegionalBusinessDatabaseAppendEntry(root)
root.mainloop()
