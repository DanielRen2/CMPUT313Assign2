import sys
import math
import random

def findDegree(nodesList):#finds average degree of network
    degree = 0;
    for i in range(len(nodesList)):
        degree = degree + len(nodesList[i]);
        
    degree = degree/(len(nodesList));
    return degree;

def findCI(array, mean):
    tscore = 2.776;
    T = 5;
    s = 0;
    for i in array:
        s = s + ((int(i) - int(mean))**2)
    s = s/4;
    s = math.sqrt(s);
    print("testing testing testing: " + str(s));
    c1 = mean - (tscore * (s/math.sqrt(T)));
    c2 = mean + (tscore * (s/math.sqrt(T)));
    return c1, c2;
        

def linkStateTransmissionCount(nodesList, numNodes):#finds average number of transmissions
    nodesHit = [];
    transmissionCount = 0;
    for i in range(numNodes):
        if i == 0:
            transmissionCount = len(nodesList[i]);
        else:
            transmissionCount = transmissionCount + (len(nodesList[i]) - 1);
    return transmissionCount;

def directVectorTransmission(nodesList, numNodes, longestPath):#counts transmissions for Distance Vector
    transmissionCount = 0;
    
    for i in range(numNodes):
        transmissionCount = transmissionCount + (len(nodesList[i]) * int(longestPath));
    
    return transmissionCount/numNodes;

def linkStatePathFinder(nodesList, numNodes, sourceNode):#finds all paths for linked state
    
    cost = [100] * (numNodes);
    finished = [];
    queue = [];
    queue2 = [];
    
    cost[sourceNode] = 0;
    
    for i in nodesList[sourceNode]:
        cost[int(i)] = 1;
        queue.append(i);
    
    run = 1;
    distance = 2;
    
    while run == 1:
        if len(queue) == 0:
            run = 0;
        for i in queue:
            for j in nodesList[int(i)]:
                if j == sourceNode:
                    continue;
                if cost[int(j)] <= distance:
                    continue;
                if cost[int(j)] > distance:
                    cost[int(j)] = distance;
                    if j in queue2:
                        continue;
                    else:
                        queue2.append(j);
        queue = queue2;
        queue2 = [];
        distance = distance + 1;
    
    return cost;

def directVectorPath(nodesList, numNodes, sourceNode):#finds all path for distance vector
    cost = [100] * (numNodes);
    finished = [];
    queue = [];
    queue2 = [];
    
    cost[sourceNode] = 0;
    
    for i in nodesList[sourceNode]:
        cost[int(i)] = 1;
        queue.append(i);
    
    run = 1;
    distance = 2;
    
    while run == 1:
        if len(queue) == 0:
            run = 0;
        for i in queue:
            for j in nodesList[int(i)]:
                if j == sourceNode:
                    continue;
                if cost[int(j)] <= distance:
                    continue;
                if cost[int(j)] > distance:
                    cost[int(j)] = distance;
                    if j in queue2:
                        continue;
                    else:
                        queue2.append(j);
        queue = queue2;
        queue2 = [];
        distance = distance + 1;
        
    return cost;

def avglinkStateRoute(nodesList, numNodes):#finds averages for linked state
    avgLength = 0;
    totalAvgLength = 0;
    for i in range(numNodes):
        cost = linkStatePathFinder(nodesList, numNodes, int(i))
        for j in cost:
            avgLength = avgLength + int(j);
        avgLength = avgLength/(numNodes - 1);
        totalAvgLength = totalAvgLength + avgLength;
        avgLength = 0;
    totalAvgLength = totalAvgLength/numNodes;
    return totalAvgLength;

def avgDirectVectorRoute(nodeList, numNodes):#finds averages for direct vector
    avgLength = 0;
    totalAvgLength = 0;
    longestPath = 0;
    for i in range(numNodes):
        cost = directVectorPath(nodeList, numNodes, int(i))
        for j in cost:
            if int(j) > longestPath:
                longestPath = int(j);
            avgLength = avgLength + int(j);
        avgLength = avgLength/(numNodes - 1);
        totalAvgLength = totalAvgLength + avgLength;
        avgLength = 0;
    totalAvgLength = totalAvgLength/numNodes;
    return totalAvgLength, longestPath;    

def HPRI(nodeList, numNodes, source, destination):#hot potato routing 1
    pathArray = [];
    transmissionCount = 0;
    run = 1;
    pathArray.append(int(source));
    previousNode = int(source);
    noAdd = 0;
    currentNode = int(source);
    nextJump = random.randint(0, len(nodeList[int(source)]) - 1);#using index 
    while run == 1:
        if currentNode == int(destination):
            run == 2;
            if len(pathArray) == 1:
                pathArray.append(int(currentNode));
            break;
        if noAdd == 1:
            noAdd = 0;
        else:
            pathArray.append(int(nodeList[currentNode][nextJump]));
        previousNode = currentNode;
        currentNode = int(nodeList[currentNode][nextJump]);
        nextJump = random.randint(0, len(nodeList[int(currentNode)]) - 1);#using index
        while int(nodeList[currentNode][nextJump]) == previousNode:
            if len(nodeList[currentNode]) == 1:
                break;
            nextJump = random.randint(0, len(nodeList[int(currentNode)]) - 1);#using index
        if int(nodeList[currentNode][nextJump]) in pathArray:
            j = 0;
            for i in pathArray:
                if i == int(nodeList[currentNode][nextJump]):
                    pathArray = pathArray[:j + 1];
                j = j + 1;
            noAdd = 1;
        transmissionCount = transmissionCount + 1;
        
    return transmissionCount, pathArray;

def avgCalcHPRI(nodeList, numNodes):#finds averages for hot potato
    runTArray = [];
    runLArray = [];
    transmission = 0;
    totalrunAvg = 0;
    avgTransmission = 0;
    totalTransmission = 0;
    avgPathlen = 0;
    totalAvgPathlen = 0;
    totalrunPathlen = 0;
    
    run = 0;
    while run < 5:
        for i in range(numNodes):
            for j in range(numNodes):
                if i == j:
                    continue;
                transmission, pathArray = HPRI(nodeList, numNodes, i, j)
                avgPathlen = avgPathlen + (len(pathArray));
                avgTransmission = avgTransmission + transmission;
            avgTransmission = avgTransmission/(numNodes - 1);
            avgPathlen = avgPathlen/(numNodes - 1);
            totalTransmission = totalTransmission + avgTransmission;
            totalAvgPathlen = totalAvgPathlen + avgPathlen;
            avgTransmission = 0;
            avgPathlen = 0;
        totalTransmission = totalTransmission/numNodes;
        totalAvgPathlen = totalAvgPathlen/numNodes;
        runTArray.append(totalTransmission);
        runLArray.append(totalAvgPathlen);
        totalrunAvg = totalrunAvg + totalTransmission;
        totalrunPathlen = totalrunPathlen + totalAvgPathlen;
        totalTransmission = 0;
        totalAvgPathlen = 0;
        run = run + 1;
    totalrunAvg = totalrunAvg/5;
    totalrunPathlen = totalrunPathlen/5;
    Tc1, Tc2 = findCI(runTArray, totalrunAvg);
    Lc1, Lc2 = findCI(runLArray, totalrunPathlen);
    return totalrunAvg, totalrunPathlen, Tc1, Tc2, Lc1, Lc2;

def HPRII(nodeList, numNodes, source, destination):#hot potato routing 2
    pathArray = [];
    transmissionCount = 0;
    run = 1;
    pathArray.append(int(source));
    previousNode = int(source);
    noAdd = 0;
    currentNode = int(source);
    nextJump = random.randint(0, len(nodeList[int(source)]) - 1);#using index
    
    while run == 1:
        if str(destination) in nodeList[currentNode]:
            transmissionCount = transmissionCount + 1;
            pathArray.append(int(destination));
            return transmissionCount, pathArray;
        if currentNode == int(destination):
            run == 2;
            if len(pathArray) == 1:
                pathArray.append(int(currentNode));
            break;
        if noAdd == 1:
            noAdd = 0;
        else:
            pathArray.append(int(nodeList[currentNode][nextJump]));
        previousNode = currentNode;
        currentNode = int(nodeList[currentNode][nextJump]);
        nextJump = random.randint(0, len(nodeList[int(currentNode)]) - 1);#using index
        while int(nodeList[currentNode][nextJump]) == previousNode:
            if len(nodeList[currentNode]) == 1:
                break;
            nextJump = random.randint(0, len(nodeList[int(currentNode)]) - 1);#using index
        if int(nodeList[currentNode][nextJump]) in pathArray:
            j = 0;
            for i in pathArray:
                if i == int(nodeList[currentNode][nextJump]):
                    pathArray = pathArray[:j + 1];
                j = j + 1;
            noAdd = 1;
        transmissionCount = transmissionCount + 1;
        
    return transmissionCount, pathArray;  

def avgCalcHPRII(nodeList, numNodes):#finds averages for hot potato 2
    runTArray = [];
    runLArray = [];    
    transmission = 0;
    totalrunAvg = 0;
    avgTransmission = 0;
    totalTransmission = 0;
    avgPathlen = 0;
    totalAvgPathlen = 0;
    totalrunPathlen = 0;
    
    run = 0;
    while run < 5:
        for i in range(numNodes):
            for j in range(numNodes):
                if i == j:
                    continue;
                transmission, pathArray = HPRII(nodeList, numNodes, i, j)
                avgPathlen = avgPathlen + (len(pathArray));
                avgTransmission = avgTransmission + transmission;
            avgTransmission = avgTransmission/(numNodes - 1);
            avgPathlen = avgPathlen/(numNodes - 1);
            totalTransmission = totalTransmission + avgTransmission;
            totalAvgPathlen = totalAvgPathlen + avgPathlen;
            avgTransmission = 0;
            avgPathlen = 0;
        totalTransmission = totalTransmission/numNodes;
        totalAvgPathlen = totalAvgPathlen/numNodes;
        runTArray.append(totalTransmission);
        runLArray.append(totalAvgPathlen);        
        totalrunAvg = totalrunAvg + totalTransmission;
        totalrunPathlen = totalrunPathlen + totalAvgPathlen;
        totalTransmission = 0;
        totalAvgPathlen = 0;
        run = run + 1;
    totalrunAvg = totalrunAvg/5;
    totalrunPathlen = totalrunPathlen/5;
    Tc1, Tc2 = findCI(runTArray, totalrunAvg);
    Lc1, Lc2 = findCI(runLArray, totalrunPathlen);    
    return totalrunAvg, totalrunPathlen, Tc1, Tc2, Lc1, Lc2;

def main():
    
    inputFile = str(sys.argv[1]);#reads input file name
    f = open(inputFile, "r");#opens input file
    nodes = [];#creates node array
    neighbours = [];
    
    initial = 0;#checks for first line
    for line in f:#reads nodes and creates a 2d array of nodes and neighbours
        if initial == 0:#accounts for first line
            numNodes = int(line);
            #print(line.rstrip());
            initial = 1;
        else:#all other lines
            for word in line.split():
                neighbours.append(word);
            nodes.append(neighbours);
            neighbours = [];
            #print(line.rstrip());
    #print(nodes);
    f.close();
    
    hitNodes = [];
    
    print(str(findDegree(nodes)));#degree of network
    print("Link State Routing: " + str(linkStateTransmissionCount(nodes, numNodes)) + " " + str(avglinkStateRoute(nodes, numNodes)));
    
    avgPathLength, longestPath = avgDirectVectorRoute(nodes, numNodes);
    print("Distance Vector Routing: " + str(directVectorTransmission(nodes, numNodes, longestPath)) + " " + str(avgPathLength));

    avgTransmission, avgPathlen, Tc1, Tc2, Lc1, Lc2 = avgCalcHPRI(nodes, numNodes);
    print("Hot Potato I: " + str(avgTransmission) + " (" + str(Tc1) + ", " + str(Tc2)+ "), " + str(avgPathlen) + " (" + str(Lc1) + ", " + str(Lc2) + ")");
    
    avgTransmission, avgPathlen, Tc1, Tc2, Lc1, Lc2 = avgCalcHPRII(nodes, numNodes);
    print("Hot Potato II: " + str(avgTransmission) + " (" + str(Tc1) + ", " + str(Tc2)+ "), " + str(avgPathlen) + " (" + str(Lc1) + ", " + str(Lc2) + ")");
  

if __name__ == "__main__":
    main()
    