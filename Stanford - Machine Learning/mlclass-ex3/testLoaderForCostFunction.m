function testLoaderForCostFunction(X, y, lambda)
%ONEVSALL trains multiple logistic regression classifiers and returns all
%the classifiers in a matrix all_theta, where the i-th row of all_theta 
%corresponds to the classifier for label i
%   [all_theta] = ONEVSALL(X, y, num_labels, lambda) trains num_labels
%   logisitc regression classifiers and returns each of these classifiers
%   in a matrix all_theta, where the i-th row of all_theta corresponds 
%   to the classifier for label i

% Some useful variables
m = size(X, 1);
n = size(X, 2);

% You need to return the following variables correctly 
all_theta = zeros(1, n + 1);

% Add ones to the X data matrix
X = [ones(m, 1) X];
initial_theta = zeros(n + 1, 1);
[J, grad] = lrCostFunction(initial_theta, X, y, lambda)

num_labels = 2; s = 5; X = magic(s); y = mod( min( magic(s) ) , num_labels)' + 1;

[J Grad] = lrCostFunction(zeros(s,1), X, y, 0.1)