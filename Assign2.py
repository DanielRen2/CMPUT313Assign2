import sys
import math
import random

def findDegree(nodesList):#finds average degree of network
    degree = 0;
    for i in range(len(nodesList)):
        print(len(nodesList[i]));
        degree = degree + len(nodesList[i]);
        
    degree = degree/(len(nodesList));
    return degree;

def linkStateTransmissionCount(nodesList, numNodes):#finds average number of transmissions
    nodesHit = [];
    transmissionCount = 0;
    for i in range(numNodes):
        if i == 0:
            transmissionCount = len(nodesList[i]);
        else:
            transmissionCount = transmissionCount + (len(nodesList[i]) - 1);
    return transmissionCount;

def directVectorTransmission(nodesList, numNodes, longestPath):
    transmissionCount = 0;
    
    for i in range(numNodes):
        transmissionCount = transmissionCount + (len(nodesList[i]) * int(longestPath));
    
    return transmissionCount/numNodes;

def linkStatePathFinder(nodesList, numNodes, sourceNode):
    
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

def directVectorPath(nodesList, numNodes, sourceNode):
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

def avglinkStateRoute(nodesList, numNodes):
    avgLength = 0;
    totalAvgLength = 0;
    for i in range(numNodes):
        cost = linkStatePathFinder(nodesList, numNodes, int(i))
        print(cost);
        for j in cost:
            avgLength = avgLength + int(j);
        avgLength = avgLength/(numNodes - 1);
        totalAvgLength = totalAvgLength + avgLength;
        avgLength = 0;
    totalAvgLength = totalAvgLength/numNodes;
    return totalAvgLength;

def avgDirectVectorRoute(nodeList, numNodes):
    avgLength = 0;
    totalAvgLength = 0;
    longestPath = 0;
    for i in range(numNodes):
        cost = directVectorPath(nodeList, numNodes, int(i))
        print(cost);
        for j in cost:
            if int(j) > longestPath:
                longestPath = int(j);
            avgLength = avgLength + int(j);
        avgLength = avgLength/(numNodes - 1);
        totalAvgLength = totalAvgLength + avgLength;
        avgLength = 0;
    totalAvgLength = totalAvgLength/numNodes;
    return totalAvgLength, longestPath;    

def HPRI(nodeList, numNodes, source, destination):
    pathArray = [];
    transmissionCount = 0;
    run = 1;
    pathArray.append(int(source));
    previousNode = int(source);
    noAdd = 0;
    currentNode = int(source);
    nextJump = random.randint(0, len(nodeList[int(source)]) - 1);#using index
    #pathArray.append(int(nodeList[currentNode][nextJump]));
    print("testin spot 3: " + str(nodeList[currentNode]));
    print("testing spot 4: " + str(nextJump));
    print("testing spot 2: " + str(nodeList));
    print("testing spot 1: " + str(pathArray));
    
    while run == 1:
        if currentNode == int(destination):
            run == 2;
            print("finish");
            if len(pathArray) == 1:
                pathArray.append(int(currentNode));
            print(pathArray);
            break;
        if noAdd == 1:
            noAdd = 0;
        else:
            pathArray.append(int(nodeList[currentNode][nextJump]));
        previousNode = currentNode;
        currentNode = int(nodeList[currentNode][nextJump]);
        nextJump = random.randint(0, len(nodeList[int(currentNode)]) - 1);#using index
        print("this is next jump: " + str(nextJump));
        while int(nodeList[currentNode][nextJump]) == previousNode:
            print("can't jump back");
            print("this is previous node: " + str(previousNode));
            if len(nodeList[currentNode]) == 1:
                break;
            nextJump = random.randint(0, len(nodeList[int(currentNode)]) - 1);#using index
            print("this is new next jump: " + str(nextJump));
        if int(nodeList[currentNode][nextJump]) in pathArray:
            print("check");
            j = 0;
            for i in pathArray:
                if i == int(nodeList[currentNode][nextJump]):
                    pathArray = pathArray[:j + 1];
                j = j + 1;
            noAdd = 1;
        print("testing: " + str(pathArray));
        transmissionCount = transmissionCount + 1;
        
    return transmissionCount;

def HPRII(nodeList, numNodes, source, destination):
    pathArray = [];
    transmissionCount = 0;
    run = 1;
    pathArray.append(int(source));
    previousNode = int(source);
    noAdd = 0;
    currentNode = int(source);
    nextJump = random.randint(0, len(nodeList[int(source)]) - 1);#using index
    #pathArray.append(int(nodeList[currentNode][nextJump]));
    print("testin spot 3: " + str(nodeList[currentNode]));
    print("testing spot 4: " + str(nextJump));
    print("testing spot 2: " + str(nodeList));
    print("testing spot 1: " + str(pathArray));
    
    while run == 1:
        if str(destination) in nodeList[currentNode]:
            print("before finish");
            transmissionCount = transmissionCount + 1;
            pathArray.append(int(destination));
            print(pathArray);
            return transmissionCount;
        if currentNode == int(destination):
            run == 2;
            print("finish");
            if len(pathArray) == 1:
                pathArray.append(int(currentNode));
            print(pathArray);
            break;
        if noAdd == 1:
            noAdd = 0;
        else:
            pathArray.append(int(nodeList[currentNode][nextJump]));
        previousNode = currentNode;
        currentNode = int(nodeList[currentNode][nextJump]);
        nextJump = random.randint(0, len(nodeList[int(currentNode)]) - 1);#using index
        #print("this is next jump: " + str(nextJump));
        while int(nodeList[currentNode][nextJump]) == previousNode:
            #print("can't jump back");
            #print("this is previous node: " + str(previousNode));
            if len(nodeList[currentNode]) == 1:
                break;
            nextJump = random.randint(0, len(nodeList[int(currentNode)]) - 1);#using index
            #print("this is new next jump: " + str(nextJump));
        if int(nodeList[currentNode][nextJump]) in pathArray:
            #print("check");
            j = 0;
            for i in pathArray:
                if i == int(nodeList[currentNode][nextJump]):
                    pathArray = pathArray[:j + 1];
                j = j + 1;
            noAdd = 1;
        #print("testing: " + str(pathArray));
        transmissionCount = transmissionCount + 1;
        
    return transmissionCount;    

def main():
    
    inputFile = str(sys.argv[1]);#reads input file name
    f = open(inputFile, "r");#opens input file
    nodes = [];#creates node array
    neighbours = [];
    
    initial = 0;#checks for first line
    for line in f:#reads nodes and creates a 2d array of nodes and neighbours
        if initial == 0:#accounts for first line
            numNodes = int(line);
            print(line.rstrip());
            initial = 1;
        else:#all other lines
            for word in line.split():
                neighbours.append(word);
            nodes.append(neighbours);
            neighbours = [];
            print(line.rstrip());
    print(nodes);
    f.close();
    
    hitNodes = [];
    
    print("this is degree: " + str(findDegree(nodes)));
    print("average transmission is : " + str(linkStateTransmissionCount(nodes, numNodes)));
    print(avglinkStateRoute(nodes, numNodes));
    avgPathLength, longestPath = avgDirectVectorRoute(nodes, numNodes);
    print(longestPath);
    print(directVectorTransmission(nodes, numNodes, longestPath));
    count = HPRI(nodes, numNodes, 0, 2)
    print("this is count" + str(count));
    count = HPRII(nodes, numNodes, 0, 2)
    print(count);
if __name__ == "__main__":
    main()
    