#list comprehension synatx:(operation loop condition)

x=[1,2,3,4,5,6,7,8,9,10]

xsqr=[i**2 for i in x]
xcube=[i**3 for i in x]
xeven=[i for i in x if i%2 == 0]
xodd=[i for i in x if i%2 !=0]
xevencube=[i**3 for i in x if i%2 == 0]
print(xsqr,"\n", xcube,"\n",xeven,"\n",xodd,"\n",xevencube)
