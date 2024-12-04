predicate consecutive(array[int] of var int: x, int: i, int: n) = (
    if i + n > length(x) then
        false
    else
        forall(j in i..i+n-1) (
            x[j] == 1
        ) /\ (i+n == length(x) \/ x[i+n] == 0)
    endif
);

% predicate consecutive_groups(array[int] of var int: x, array[int] of int: groups) = (
%     let {
%         % Calculate the cumulative sum of groups
%         array[int] of int: cumsum = array1d(1..length(groups), [sum(j in 1..i)(groups[j]+1) | i in 1..length(groups)]);
%         % Calculate the starting index for each group
%         array[int] of int: starts = [1] ++ [cumsum[i-1] + 1 | i in 2..length(groups)];
%     } in
%     forall(i in 1..length(groups)) (
%         consecutive(x, starts[i], groups[i])
%     )
% );

predicate consecutive_groups(array[int] of var int: x, array[int] of int: groups) =
    let {
        % The number of groups
        int: num_groups = length(groups),
        % The length of the array
        int: n = length(x),
        % An array to store the lengths of the groups of consecutive 1s in x
        array[1..n] of var 0..n: group_lengths,
        % An array to store the starting indices of the groups of consecutive 1s in x
        array[1..n] of var 0..n: group_starts
    } in
    % The number of groups of consecutive 1s in x is equal to num_groups
    sum([bool2int(group_lengths[i] > 0) | i in 1..n]) == num_groups;

    array[1..n] of var 0..n: ones = [i | i in 1..n, x[i] = 1];
    
    % Check that number 




    % /\
    % The lengths of the groups of consecutive 1s in x are equal to the lengths specified in groups
    % forall(i in 1..num_groups) (
        % group_lengths[i] = groups[i]
    % ) /\
    % The groups of consecutive 1s in x are separated by at least one 0
    % forall(i in 1..num_groups-1) (
        % group_starts[i] + group_lengths[i] < group_starts[i+1]
    % ) /\
    % Calculate the lengths and starting indices of the groups of consecutive 1s in x
    % forall(i in 1..n) (
        % if i = 1 then
            % group_starts[i] = 1 /\ group_lengths[i] = if x[i] = 1 then 1 else 0 endif
        % else
            % group_starts[i] = if x[i] = 1 /\ x[i-1] = 0 then i else group_starts[i-1] endif /\
            % group_lengths[i] = if x[i] = 1 then group_lengths[i-1] + 1 else 0 endif
        % endif
    % );

% Declare the length of the arrangement
int: length = 16;

% Declare the variables for each position in the arrangement
array[1..length] of var {0, 1}: arrangement;
array[1..4] of int: groups = [2, 1, 2, 3];

% Declare the constraints based on the given numbers (2,1,2,3)
% constraint count(arrangement, 1) == 2 + 1 + 2 + 3;

constraint consecutive_groups(arrangement, groups);
% Define a constraint that checks that the arrangements have
% constraint isValid(arrangement, [2, 1, 2, 3]);

% Solve the problem
solve satisfy;

% Output the solution
output ["Arrangement: ", show(arrangement)];
