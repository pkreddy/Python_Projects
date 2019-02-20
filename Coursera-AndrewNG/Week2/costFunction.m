function[jVal, gradient] = costFunction(theta)
jVal = (theta(1)-5)^2 + (theta(2)-5)^2;
gradient = zeros(2,1);
graient(1) = 2 * (theta(1) - 5);
graient(2) = 2 * (theta(2) - 5);
end


