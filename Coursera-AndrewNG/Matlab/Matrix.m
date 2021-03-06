A = [-4,1.9,-3.2,-12;-0.25,2,9,0.3;0.1,7,-1,5];
A;
A';

%identity matrix
I = eye(10);
I;

%zero matrix
Z = zeros(10,3);
Z

%random matrix between numbers 0 and 2
M = randi([0,2],3,2);
N= randi([0,2],3,2);

%random normal matrix
randn(1,7)

%diagonal matrix
diag([-1,2,3])

M([1,2],2)
M(:,2)

length(M)
size(M)

C = [M,N]
D = [M;N]

%mutiplying ararys
A = randi(3,3,2)
B = randi(2,2,3)
B * A
A * B
