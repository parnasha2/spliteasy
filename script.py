#spliteasy.tm

n=int(input("Enter number of friends: "))
print("You have", n, "friends.")
names=[]
for i in range(1, n+1):
    name=input("Enter name of your friend:")
    names.append(name)
print(names)


amount=[]
for i in range(1,n+1):
    f1=float(input("Enter amount of total money you owe:"))
    amount.append(f1)
print(names+amount)


paid=[]
for i in range(1, n+1):
    f2=float(input("Enter amount of money you paid for others:"))
    paid.append(f2)
print(names+paid)

net_amount=[a-b for a,b in zip(paid,amount)]
print("net amount:",net_amount)


for i in range(1,n):  
    creditor=max(net_amount)
    debtor=abs(min(net_amount))
    print("Creditor:", creditor)
    print("Debtor:", debtor)

    amount_paid=abs(min(creditor,debtor))
    remaining_creditor=creditor-amount_paid
    remaining_debtor=-(debtor-amount_paid)
    net_amount[net_amount.index(creditor)]=remaining_creditor
    net_amount[net_amount.index(-debtor)]=remaining_debtor

    print("Amount needed to pay creditor:", amount_paid)
    print("Remaning amount=",remaining_debtor)
    print("net amount",net_amount)
print("Number of rounds:", i)

   
    
   


        
