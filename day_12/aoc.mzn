% Declare the length of the arrangement
int: length;

% Declare the variables for each position in the arrangement
array[1..length] of var {0, 1}: arrangement;

% Declare the constraints based on the given numbers (2,1,2,3)
constraint count(arrangement, 1) == 2 + 1 + 2 + 3;

% Define a constraint that checks that the arrangements have
constraint isValid(arrangement, [2, 1, 2, 3]);

% Solve the problem
solve satisfy;

% Output the solution
output ["Arrangement: ", show(arrangement)];
