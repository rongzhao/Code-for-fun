"""This program is used to calculate the median value in a list"""
import sys

def main():
    print "type in a list:"
    ls = []
    for line in sys.stdin:
        ls.append(float(line))
    #type <CTRL-d> to send EOF
    print ls
    print
    ls.sort()
    if len(ls)%2 == 1:
        median = ls[(len(ls) - 1)/2]
    else:
        median = (ls[len(ls)/2 - 1] + ls[len(ls)/2])/2
    print 'median is', median
    print

if __name__ == '__main__':
    main()
