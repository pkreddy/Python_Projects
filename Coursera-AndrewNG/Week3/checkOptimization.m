options = optimset('GradObj','on','MaxIter',100);
initialTheta = zeros(2,1);
%[optTheta, functionVal, exitFlag] = fminunc(@costFunction, initialTheta, options);
[optTheta, functionVal, exitFlag] = fminunc(@costFunction, initialTheta);
optTheta
functionVal