def primeFactors(number):
    time = 0
    factors = []
    for x in range(2, number):
        if (number % x == 0):
            factors.append(x)
        time += 1
    print factors
    print "The time in second is: " + str(time) + " seconds"
primeFactors(376835043318661)
