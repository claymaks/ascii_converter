x = [1000000, 250000, 62500 ];
white_orig = [0.007685024738311768,0.0021851801872253417,0.000738983154296875];
black_orig = [0.007741038799285889,0.0021913981437683104,0.0007198810577392578];

black_white_first = [3.0307645201683044,0.7600762248039246,0.1905120611190796];
white_white_first = [2.7640769481658936,0.6942452788352966,0.17801642417907715];

black_black_first = [0.6681182702382406,0.16788678169250487,0.04204425811767578];
white_black_first = [2.902859687805176,0.7228957414627075,0.179287850856781];

n_black_black_first = [0.5738448202610016,0.14760440587997437,0.037952929735183716];
n_white_black_first = [0.5597416083017985,0.14494964281717937,0.03650126457214355];

n_black_white_first = [0.5982930342356364,0.14575999577840168,0.03649206161499023];
n_white_white_first = [0.6455373605092366,0.1595635732014974,0.04317255020141601];

plot(x,n_black_black_first, '-ko', 'linewidth', 1, 'MarkerSize', 5);
hold on;
plot(x,n_white_black_first, '-ko', 'linewidth', 1, 'MarkerSize', 5);
plot(x,n_black_white_first, '-k*', 'linewidth', 1, 'MarkerSize', 5);
plot(x,n_white_white_first, '-k*', 'linewidth', 1, 'MarkerSize', 5);

hold off;

white = n_white_black_first;
black = n_black_black_first;
slope1 = ((white(end) + black(end)) / 2) - ((white(1) + black(1)) / 2);
slope1 = slope1 / (x(end) - x(1));
b1 = ((white(1) + black(1)) / 2) - (slope1 * white(1));
s1 = "y = " + slope1 + "x + " + b1 + "";

white = n_white_white_first;
black = n_black_white_first;
slope2 = ((white(end) + black(end)) / 2) - ((white(1) + black(1)) / 2);
slope2 = slope2 / (x(end) - x(1));
b2 = ((white(1) + black(1)) / 2) - (slope2 * white(1));
s2 = "y = " + slope2 + "x + " + b2 + "";
legend(s1, s1, s2, s2)

disp(s1);
disp(s2);
s1 = s1 + ".png";
saveas(gcf, "final_outcome.png")
