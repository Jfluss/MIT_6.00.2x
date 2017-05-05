import random
import pylab

# Global Variables
MAXRABBITPOP = 1000
CURRENTRABBITPOP = 50
CURRENTFOXPOP = 300

def rabbitGrowth():
    """ 
    rabbitGrowth is called once at the beginning of each time step.

    It makes use of the global variables: CURRENTRABBITPOP and MAXRABBITPOP.

    The global variable CURRENTRABBITPOP is modified by this procedure.

    For each rabbit, based on the probabilities in the problem set write-up, 
      a new rabbit may be born.
    Nothing is returned.
    """
    # you need this line for modifying global variables
    global CURRENTRABBITPOP

    for i in range(CURRENTRABBITPOP):
        if random.random()<(1-CURRENTRABBITPOP/MAXRABBITPOP):
            CURRENTRABBITPOP += 1
    
            
def foxGrowth():
    """ 
    foxGrowth is called once at the end of each time step.

    It makes use of the global variables: CURRENTFOXPOP and CURRENTRABBITPOP,
        and both may be modified by this procedure.

    Each fox, based on the probabilities in the problem statement, may eat 
      one rabbit (but only if there are more than 10 rabbits).

    If it eats a rabbit, then with a 1/3 prob it gives birth to a new fox.

    If it does not eat a rabbit, then with a 1/10 prob it dies.

    Nothing is returned.
    """
    # you need these lines for modifying global variables
    global CURRENTRABBITPOP
    global CURRENTFOXPOP
    success = 0
    fail = 0
    for i in range(CURRENTFOXPOP):
        if CURRENTRABBITPOP == 10:
            break
        if CURRENTFOXPOP == 10:
            break
        if random.random()<(CURRENTRABBITPOP/MAXRABBITPOP):
            CURRENTRABBITPOP -= 1
            success += 1
        else:
            fail += 1
    for i in range(success):
        if random.random()<float(1/3):
            CURRENTFOXPOP += 1
    for i in range(fail):
        if random.random()<float(1/10):
            CURRENTFOXPOP -= 1
            
    
            
def runSimulation(numSteps):
    """
    Runs the simulation for `numSteps` time steps.

    Returns a tuple of two lists: (rabbit_populations, fox_populations)
      where rabbit_populations is a record of the rabbit population at the 
      END of each time step, and fox_populations is a record of the fox population
      at the END of each time step.

    Both lists should be `numSteps` items long.
    """
    rabbits = []
    foxes = []
    for i in range(numSteps):
        rabbitGrowth()
        foxGrowth()
        rabbits.append(CURRENTRABBITPOP)
        foxes.append(CURRENTFOXPOP)
    pylab.plot(rabbits, label = 'rabbits')
    pylab.plot(foxes, label = 'foxes')
    pylab.legend(loc = 'upper center')
    coeff1 = pylab.polyfit(range(len(rabbits)), rabbits, 2)
    pylab.plot(pylab.polyval(coeff1, range(len(rabbits))))
    coeff2 = pylab.polyfit(range(len(foxes)), foxes, 2)
    pylab.plot(pylab.polyval(coeff2, range(len(foxes))))
    pylab.show
    return rabbits, foxes
        
