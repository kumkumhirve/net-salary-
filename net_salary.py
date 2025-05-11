'''Q13: Write a program to calculate gross salary and net salary.
Accept basic salary from user, TA(Travel Allowance) i.e 10% of basic
salary, PF(Provident Fund) i.e 7.8% of basic , DA(Dearness
(Dearness Allowance) is 500.
gs=basic+da+ta; ns=gs-pf;'''


basic = int(input("enter the basic salary:"))
da = 500
ta = (10/100*basic)
pf =(7.8/100*basic)

gs = basic + da+ ta
ns=gs-pf
print(gs)
print(ns)

