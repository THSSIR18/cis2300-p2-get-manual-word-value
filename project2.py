Purpose: Use my word "ferrari" to remove the letters F, E, R, A, I from the text below 

#Likening his Maker to the grazed ox,
#Jehovah, who, in one night, when he passed
#From Egypt marching, equalled with one stroke
#Both her first-born and all her bleating gods.

#New and improved text below (done manually by me) 

#Lknng hs Mk to th gzd ox, 
#Jhovh, who, n on nght, whn h pssd 
#om gypt mchng, qulld wth on stok 
#Both h st-bon nd ll h btng gods.
                       #^human error when done by me was deleting the l by accident, that's why my most recent change was today using Sublime below

#New and improved text below (done by Sublime Text) 
#lknng hs mk to th gzd ox,
#jhovh, who, n on nght, whn h pssd
#om gypt mchng, qulld wth on stok
#both h st-bon nd ll h bltng gods.

#Text should be identical^ 

# define variables for letter values that I need:
a = 1
b = 2
c = 3
d = 4
e = 5
f = 6
g = 7
h = 8
i = 9
j = 10
k = 11
l = 12
m = 13
n = 14
o = 15
p = 16
q = 17
r = 18
s = 19
t = 20
u = 21
v = 22
w = 23
x = 24
y = 25
z = 26

# calculate (compute) the value for: 'Lknng hs Mk to th gzd ox, Jhovh, who, n on nght, whn h pssd om gypt mchng, qulld wth on stok Both h st-bon nd ll h btng gods.'
#questions 
#(1) there must be an easier way instead of having to add all the single letters by themselves, what is one idea?
#(2) what is an easier way to do this

value = l+k+n+n+g+h+s+m+k+t+o+t+h+g+z+d+o+x+ \
    j+h+o+v+h+w+h+o+n+o+n+n+g+h+t+w+h+n+h+p+s+s+d+ \
    o+m+g+y+p+t+m+c+h+n+g+q+u+l+l+d+w+t+h+o+n+s+t+o+k+ \
    b+o+t+h+h+s+t+b+o+n+n+d+l+l+h+b+l+t+n+g+g+o+d+s

# print out the value
print(value)
