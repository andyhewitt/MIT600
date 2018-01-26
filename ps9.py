# 6.00 Problem Set 9
#
# Intelligent Course Advisor
#
# Name:
# Collaborators:
# Time:
#

SUBJECT_FILENAME = "subjects.txt"
SHORT_SUBJECT_FILENAME = "shortened_subjects.txt"
VALUE, WORK = 0, 1

#
# Problem 1: Building A Subject Dictionary
#
def loadSubjects(filename):
    """
    Returns a dictionary mapping subject name to (value, work), where the name
    is a string and the value and work are integers. The subject information is
    read from the file named by the string filename. Each line of the file
    contains a string of the form "name,value,work".

    returns: dictionary mapping subject name to (value, work)
    """

    # The following sample code reads lines from the specified file and prints
    # each one.
    inputFile = open(filename, 'r')
    workDict = {}   
    for line in inputFile:
        n, v, w = line.split(',')
        workDict[n] = (int(v), int(w))
    return workDict

    # TODO: Instead of printing each line, modify the above to parse the name,
    # value, and work of each subject and create a dictionary mapping the name
    # to the (value, work).

def printSubjects(subjects):
    """
    Prints a string containing name, value, and work of each subject in
    the dictionary of subjects and total value and work of all subjects
    """
    totalVal, totalWork = 0,0
    if len(subjects) == 0:
        return 'Empty SubjectList'
    res = 'Course\tValue\tWork\n======\t====\t=====\n'
    subNames = sorted(subjects)
    for s in subNames:
        val = subjects[s][VALUE]
        work = subjects[s][WORK]
        res = res + s + '\t' + str(val) + '\t' + str(work) + '\n'
        totalVal += val
        totalWork += work
    res = res + '\nTotal Value:\t' + str(totalVal) +'\n'
    res = res + 'Total Work:\t' + str(totalWork) + '\n'
    print(res)

#
# Problem 2: Subject Selection By Greedy Optimization
#

def cmpValue(subInfo1, subInfo2):
    """
    Returns True if value in (value, work) tuple subInfo1 is GREATER than
    value in (value, work) tuple in subInfo2
    """
    return subInfo1[VALUE] > subInfo2[VALUE]

def cmpWork(subInfo1, subInfo2):
    """
    Returns True if work in (value, work) tuple subInfo1 is LESS than than work
    in (value, work) tuple in subInfo2
    """
    return subInfo1[WORK] < subInfo2[WORK]

def cmpRatio(subInfo1, subInfo2):
    """
    Returns True if value/work in (value, work) tuple subInfo1 is 
    GREATER than value/work in (value, work) tuple in subInfo2
    """
    val1 = float(subInfo1[VALUE])
    wor1 = float(subInfo1[WORK])
    val2 = float(subInfo2[VALUE])
    wor2 = float(subInfo2[WORK])
    
    return (val1 / wor1) > (val2 / wor2)

def cmpSum(subInfo1, subInfo2):
    return sum(subInfo1) > sum(subInfo2)


def greedyAdvisor(subjects, maxWork, comparator):
    """
    Returns a dictionary mapping subject name to (value, work) which includes
    subjects selected by the algorithm, such that the total work of subjects in
    the dictionary is not greater than maxWork.  The subjects are chosen using
    a greedy algorithm.  The subjects dictionary should not be mutated.

    subjects: dictionary mapping subject name to (value, work)
    maxWork: int >= 0
    comparator: function taking two tuples and returning a bool
    returns: dictionary mapping subject name to (value, work)
    """
    workHour = 0
    greedyDict = {}
    compList = subjects.copy()

    while workHour <= maxWork and len(greedyDict) <= len(subjects):
        if comparator == cmpWork:
            candidate = (0, 100)
        else:
            candidate = (0, 1)
            
        course = ''   
        for item in compList:
            if comparator(compList[item], candidate) and compList[item][WORK] + workHour <= maxWork and compList[item] not in greedyDict:
                candidate = subjects[item]
                course = item
        if course != '':
            greedyDict[course] = candidate
            workHour += greedyDict[course][WORK]
            del compList[course]
        else:
            return greedyDict



            

#
# Problem 3: Subject Selection By Brute Force
#
def bruteForceAdvisor(subjects, maxWork):
    """
    Returns a dictionary mapping subject name to (value, work), which
    represents the globally optimal selection of subjects using a brute force
    algorithm.

    subjects: dictionary mapping subject name to (value, work)
    maxWork: int >= 0
    returns: dictionary mapping subject name to (value, work)
    """
    bruteList = generateSubset(subjects)
    return findOptimul(bruteList, maxWork)

#smallCatalog = {'6.00': (16, 8), '1.00': (7, 7), '15.01': (9, 6), '6.01': (5, 3)}

def generatePrintBinary(num, digit):
    bStr = ''
    bStr = "{0:b}".format(num)
    

    while digit - len(bStr) > 0:
        bStr = '0' + bStr

    return bStr
    
def generateSubset(items):
    digit = 2 ** len(items)
    template = []
    for i in range(digit):
        template.append(generatePrintBinary(i, len(items)))
    course = []
    value = []
    for j in items:
        course.append(j)
        value.append(items[j])
    brute = []

    for bi in template:
        elem = {}
        for obj in range(len(bi)):
            if bi[obj] == '1':
                elem[course[obj]] = value[obj]
        brute.append(elem)
    return brute
        
def findOptimul(subset, maxWork):
    best = 0
    candidate = {}
    count = 0
    for item in subset:
        work = 0
        for b in item:
            work += item[b][WORK]
            if maxWork >= work > best:
                best = work
                candidate = item
            if work == maxWork:
                return item
            
        count += 1
    return candidate
        
