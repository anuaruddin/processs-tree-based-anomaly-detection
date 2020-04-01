import ptsim_lib as pt

def seqDiff(op, set1, set2):
    subDiff = ""
    ##print("Running subset cross-check")
    n = len(set1)
    m = len(set2)
    ###print('set1: ' + str(set1))
    ###print('set2: ' + str(set2))

    s1 = list()
    s2 = list()

    if type(set1) is str:
      ###print(str(set1) + ' is str')
      s1.append(set1)
    else:
      ###print(str(set1) + ' is not str')
      s1 = set1

    if type(set2) is str:
       ###print(str(set2) + ' is str')
       s2.append(set2)
    else:
      ###print(str(set2) + ' is not str')
      s2 = set2
    
    ###print("n:" + str(len(s1)) + " " + str(s1))
    ###print("m:" + str(len(s2)) + " " + str(s2))

    if (len(s1)>len(s2)):
        for i in range(abs(len(s1)-len(s2))):
            s2.append(str('_'))
    elif (len(s1)<len(s2)):
        for i in range(abs(len(s1)-len(s2))):
            s1.append(str('_'))

    ##print('s1: ' + str(s1))
    ##print('s2: ' + str(s2))
    for i in range(0,len(s1)):
        for j in range(0,len(s2)):
            if i==j and s1[i] != '_':
                #print('s1[i]:' + s1[i])
                #print('s2[j]:' + s2[j])
                subDiff += ' ' + diffTree(s1[i], s2[j]) + ' '
                #print('running diffTree(s1[i], s2[j])')
    
    ftree = op + ' ( ' + subDiff + ' ) '
    
    return ftree

def neqDiff(op, set1, set2):
    ##print("Running subset cross-check")
    n = len(set1)
    m = len(set2)
    ###print('set1: ' + str(set1))
    ###print('set2: ' + str(set2))

    s1 = list()
    s2 = list()
    subDiff = ""

    if type(set1) is str:
      ###print(str(set1) + ' is str')
      s1.append(set1)
    else:
      ###print(str(set1) + ' is not str')
      s1 = set1

    if type(set2) is str:
       ###print(str(set2) + ' is str')
       s2.append(set2)
    else:
      ###print(str(set2) + ' is not str')
      s2 = set2
    
    ###print("n:" + str(len(s1)) + " " + str(s1))
    ###print("m:" + str(len(s2)) + " " + str(s2))
    finalSet = list()
    if (len(s1)>len(s2)):
        for i in range(abs(len(s1)-len(s2))):
            s2.append(str('_'))

    elif (len(s1)<len(s2)):
        for i in range(abs(len(s1)-len(s2))):
            s1.append(str('_'))

    #print('finalset : ' + str(finalSet))
    #print('addset : ' + str(addSet))
    
    for i in s1:
        #print('s1+:' + str(s1))
        for j in s2:
            #print('s2+:' + str(s2))
            if i == j and j not in finalSet and i != '_':
                finalSet.append(i)
                
    if len(finalSet) < max(len(s1),len(s2)):
        for i in range(abs(max(len(s1),len(s2))-len(finalSet))):
            finalSet.append('tau')
        
    ftree = op + ' ( ' + listToString(finalSet) + ' ) '
    ##print('subDiff neq :' + ftree)
      
    return ftree

def diffTree(tree1, tree2):
    tree1 = pt.re.sub(' +', ' ', tree1)
    tree2 = pt.re.sub(' +', ' ', tree2)
    roots1, subtree1 = pt.sub_tree(tree1)
    #print("Subtree1=" + str(subtree1))
    roots2, subtree2 = pt.sub_tree(tree2)
    #print("Subtree2=" + str(subtree2))
    diffTree = ""
    subdiff = ""

    #print("-----------------------------------------------------")
    #print("<Comparing>")
    #print("Subtree1: " + tree1)
    #print("Subtree2: " + tree2)
    
    if (roots1 in pt.seq_ope or roots1 in pt.neq_ope) and (roots2 in pt.seq_ope or roots2 in pt.neq_ope): #if operator
        r1 = roots1.replace('*','')
        r2 = roots2.replace('*','')
        if r1 == r2 :
            if r1 in pt.seq_ope:
                #print('(1)')
                subdiff = seqDiff(roots1, subtree1, subtree2)
                diffTree += subdiff
            elif r1 in pt.neq_ope:
                #print('(2)')
                subdiff = neqDiff(roots1, subtree1, subtree2)
                diffTree += subdiff
        else:
            if r1 in pt.seq_ope and r2 in pt.seq_ope:
                #print('(3)')
                subdiff = seqDiff('[x]', subtree1, subtree2) #add ordered operator wildcard
                diffTree+=subdiff
            elif r1 in pt.neq_ope and r2 in pt.neq_ope:
                #print('(4)')
                subdiff = neqDiff('[+]', subtree1, subtree2) #add non-ordered wildcard
                diffTree+=subdiff
            else:
                #print('(5)')
                #subdiff = neqDiff('[-]', subtree1, subtree2) #add universal operator wildcard
                #diffTree+=subdiff
                diffTree += 'tau'
    elif not subtree1 or not subtree2: #if not operator
        r1 = roots1.replace('*','')
        r2 = roots2.replace('*','')
        print(r1)
        print(r2)
        if not subtree1 and not subtree2:
            ##print("Both are action nodes")
            #print('(6)')
            #print(roots1)
            #print(roots2)

            if r1 == r2:
                diffTree += roots1
            else:
                diffTree += 'tau'

        elif not subtree1:
            ##print("Subtree1 is action node")
            if r2 in pt.seq_ope:
                #print('(7)')
                #subdiff += '[*]' + ' ( ' + roots1 + '* ' + tree2 + ' ' + 'tau' + ' ) '
                subdiff += 'tau'
                diffTree += subdiff
            elif r2 in pt.neq_ope:
                #print('(8)')
                #subdiff += '[*]' + ' ( ' + roots1 + '* ' + listToString(subtree2) + ' ' + 'tau ' + ' ) '
                subdiff += 'tau'
                diffTree += subdiff

        elif not subtree2:
            ##print("Subtree2 is action node")
            if r1 in pt.seq_ope:
                #print('(9)')
                #subdiff += '[*]' + ' ( ' + roots2 + '*' + tree1 + ' ) '
                subdiff += 'tau'
                diffTree+=subdiff
            elif r1 in pt.neq_ope:
                #print('(10)')
                #subdiff += neqDiff('[*]', roots2, subtree1)

                #subdiff += '[*]' + ' ( ' + roots2 + '* ' + listToString(subtree1) + ' ) '
                #subdiff += 'XOR' + ' ( ' + roots2 + ' ' + listToString(subtree1) + ' ' + 'tau ' + ' ) '
                subdiff = 'tau'
                diffTree+=subdiff

    diffTree = pt.re.sub(r'\s+', ' ', diffTree).strip()
    return diffTree

def listToString(s):  
    
    # initialize an empty string 
    str1 = ""  
    # traverse in the string   
    for ele in s:
        if ele is list:
            str1 += listToString(ele)
        else:
            str1 += ' ' + ele + ' '   
    
    # return string   
    return str1