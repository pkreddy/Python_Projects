x = 23;
y = 12;
z = mean([x,y]) > 10 ;
z
z < 3
z > 3

%conditional data selection
A = randi(4,3,4);
A
I = A(A < 2.5);
I

%if else statements
if z > 3
    a = 1
else
    a = 0
end

%for loop
y(1) = 1;
for n = 1:6
    y(n+1) = y(n) - 0.1 * y(n);
end

y

%while loop
amount(1) = 1000;
r = 0.08;
p = 1;
while amount(p)<2000
    amount(p+1) = amount(p) * (r+1);
    p = p + 1;
end
amount