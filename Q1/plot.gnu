set style data histogram
set style histogram clustered gap 1
set style fill solid 0.4 border
set xlabel "Theta reflected (degrees)"
set ylabel "Distribution"

plot 'hmwk5c_problem1a.dat' u 2:xticlabels(1) title "theta=0",'' u 3:xticlabels(1) title "theta=30",'' u 4:xticlabels(1) title "theta=60"

pause -1 "Hit any key to continue"

set style data histogram
set style histogram clustered gap 1
set style fill solid 0.4 border
set xlabel "Phi reflected (degrees)"
set ylabel "Distribution"

plot 'hmwk5c_problem1b.dat' u 2:xticlabels(1) title "45 theta and 180 phi"

pause -1 "Hit any key to continue"
