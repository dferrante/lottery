"""Usage: requires 6 arguments (the winning numbers), with the last one being the megaball or whatevertheheck
eg: python didwewin.py 1 9 14 35 44 23

to easily make python lists of your lottery numbers to paste in, run like so:
python didwewin.py numbers
"""

import sys, random

work = False #set to True if not using work pool numbers
work_pool_size = 10

#put lottery numbers here, use numbers cmd line arg to fill with 6-tuple integer lists
our_played_numbers = []
work_played_numbers = []


played_numbers = our_played_numbers if not work else work_played_numbers
pool_size = 1 if not work else work_pool_size

megamillions_winnings = {
    (0, True): 2,
    (1, True): 3,
    (2, True): 10,
    (3, False): 7,
    (3, True): 150,
    (4, False): 150,
    (4, True): 10000,
    (5, False): 250000,
    (5, True): 305000000, #JJJJJJACKPOT!
}

powerball_winnings = {
    (0, True): 4,
    (1, True): 4,
    (2, True): 7,
    (3, False): 7,
    (3, True): 100,
    (4, False): 100,
    (4, True): 10000,
    (5, False): 1000000,
    (5, True): 550000000, #JJJJJJACKPOT!
}

winnings = powerball_winnings

def enterline():
    line = []
    for x in range(1,7):
        n = raw_input('#%s:' % x)
        try:
            line.append(int(n))
        except:
            raise
    print line
    return line

if __name__ == '__main__':
    if sys.argv[1] == 'numbers':
        print "enter numbers for each line. when finished, enter any non-number"
        l = []
        while True:
            try:
                l.append(enterline())
            except:
                break
        print l
        sys.exit()

    winning_numbers = sys.argv[1:]
    if len(winning_numbers) != 6:
        print "you didn't numbers right"
        print __doc__
        sys.exit()

    try:
        winning_numbers = map(int, winning_numbers)
    except:
        print "you didn't numbers right"
        print __doc__
        sys.exit()

    white_balls = set(winning_numbers[:5])
    megaball = winning_numbers[5]

    grandtotal = 0
    for play in played_numbers:
        playset = set(play[:5])
        megaballmatch = True if megaball == play[5] else False
        matched = len(playset.intersection(white_balls))

        if (matched, megaballmatch) in winnings.keys():
            grandtotal += winnings[(matched, megaballmatch)]
            print 'Won $%s with: %s' % (winnings[(matched, megaballmatch)], str(play))

        if (matched, megaballmatch) == (5, True):
            print 'what. the. fuck.'

    print '-------------'
    print 'Grand Total (pretax): $%s' % grandtotal
    if pool_size > 1:
        print 'Per Person Total (pretax): $%s' % (grandtotal/float(pool_size))

