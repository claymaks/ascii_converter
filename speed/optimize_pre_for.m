x = [1000000, 250000, 62500 ];
white = [0.007685024738311768,0.0021851801872253417,0.000738983154296875];
black = [0.007741038799285889,0.0021913981437683104,0.0007198810577392578];
plot(x,black, '-ko', 'linewidth', 1, 'MarkerSize', 5);
hold on;
plot(x,white, '-ko', 'linewidth', 1, 'MarkerSize', 5);


slope = ((white(end) + black(end)) / 2) - ((white(1) + black(1)) / 2);
slope = slope / (x(end) - x(1));

b = ((white(1) + black(1)) / 2) - (slope * white(1));
s = "y = " + slope + "x + " + b;
disp(s);
s = s + ".png";
saveas(gcf, s)
