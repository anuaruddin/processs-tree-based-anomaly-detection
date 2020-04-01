import re as re

seq_ope = ['sequence', 'xorLoop', '[x]', '[-], [*]']
neq_ope = ['xor', 'and', '[+]', '[-], [*]']

def levenshtein(s1, s2):
    n = len(s1)
    m = len(s2)

    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(n + 1):
        dp[i][0] = i

    for j in range(m + 1):
        dp[0][j] = j

    for i in range(1, n + 1):
        for j in range(1, m + 1):
          if s1[i - 1] == 'tau' or s2[j - 1] == 'tau':
            cost = 0
          else:
            cost = 1 - simular(s1[i - 1], s2[j - 1])

            #cost = 0 if s1[i - 1] == s2[j - 1] else 1
            dp[i][j] = min(dp[i - 1][j] + 1,         # insertion
                           dp[i][j - 1] + 1,         # deletion
                           dp[i - 1][j - 1] + cost)  # replacement
    return dp[n][m]

def levenshtein_ori(s1, s2):
    n = len(s1)
    m = len(s2)

    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(n + 1):
        dp[i][0] = i

    for j in range(m + 1):
        dp[0][j] = j

    for i in range(1, n + 1):
        for j in range(1, m + 1):
          if s1[i - 1] == 'tau' or s2[j - 1] == 'tau':
            cost = 0
          else:
            cost = 0 if s1[i - 1] == s2[j - 1] else 1
            dp[i][j] = min(dp[i - 1][j] + 1,         # insertion
                           dp[i][j - 1] + 1,         # deletion
                           dp[i - 1][j - 1] + cost)  # replacement
    return dp[n][m]

def sub_tree(process_tree):
    subtree_list = []
    roots = process_tree.split(' ')[0]
    lines = process_tree.split(' ')[2:-1]
    #print(lines)
    while lines:
        word = lines.pop(0)
        if word in seq_ope or word in neq_ope:
            start_count = 0
            while lines:
                bit = lines.pop(0)
                word = word + ' ' + bit
                
                if bit == '(':
                    start_count += 1
                elif bit == ')':
                    start_count -= 1
                    
                    if start_count == 0:
                        break
                    
        subtree_list.append(word)
    
    return roots, subtree_list

def cross_check(set1, set2):
    ##print("Running subset cross-check")
    n = len(set1)
    m = len(set2)
    #print('set1: ' + str(set1))
    #print('set2: ' + str(set2))

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
    


    if (len(s1)>len(s2)):
        for i in range(abs(len(s1)-len(s2))):
            s2.append(str('_'))
    elif (len(s1)<len(s2)):
        for i in range(abs(len(s1)-len(s2))):
            s1.append(str('_'))

    # print("n:" + str(len(s1)) + " " + str(s1))
    # print("m:" + str(len(s2)) + " " + str(s2))
    
    results = []
    for i in s1:
        s1_sim = []
        for j in s2:
            s1_sim.append(simular(i, j))
        
        results.append(s1_sim)
    
    #print(results)
    sumsA = 0
    for i in results:
        ###print(i)
        ###print("max : " + str(max(i)))
        sumsA += max(i)
    ###print("sumsA: " + str(sumsA))
    ###print(s1)
    ###print(s2)
    #s2_ave = sums / n
   
    sumsB = 0
    for i in range(0,max(n,m)-1):
        s1_list = list()
        for j in results:
            #print(''+str(j[i]))
            s1_list.append(j[i])
        sumsB += max(s1_list)
    #s1_ave = sumsB / m
    setsim = min(sumsA,sumsB) / max(n,m)
    #print('setsim='+str(setsim))
    return setsim

def simular(tree1, tree2):
    tree1 = re.sub(' +', ' ', tree1)
    tree2 = re.sub(' +', ' ', tree2)
    #" ".join(tree1.split())
    #" ".join(tree2.split())

    roots1, subtree1 = sub_tree(tree1)
    roots2, subtree2 = sub_tree(tree2)

    #print("-----------------------------------------------------")
    #print("<Comparing>")
    #print("Subtree1: " + tree1)
    #print("Subtree2: " + tree2)
    
    if not subtree1 or not subtree2:
        # if roots1 == roots2: #if both are action nodes
        #     sim = 1
        if not subtree1 and not subtree2:
            ##print("Both are action nodes")
            if roots1 == 'tau' or roots2 == 'tau':
              sim = 1
            else:
              sim = 1 - levenshtein_ori(tree1, tree2) / max(len(tree1),len(tree2))
        elif not subtree1:
            ##print("A is action node")
            if tree1 == 'tau':
              sim = 1
            else:
              #newtree2 = [roots2, '('] + subtree2 + [')']
              ###print(tree1)
              ###print(newtree2)
              if roots2 in seq_ope:
                ###print("Root of B is a sequence operator")
                sim = 0
              else:
                #sim = 1 - levenshtein_ori(tree1, newtree2) / max(len(tree1),len(newtree2))
                sim = cross_check(tree1, subtree2)
        elif not subtree2:
            ##print("B is action node")
            if tree2 == 'tau':
              sim = 1
            else:
              #newtree1 = [roots1, '('] + subtree1 + [')']
              ###print(newtree1)
              ###print(tree2)
              if roots1 in seq_ope:
                ###print("Root of B is a sequence operator")
                sim = 0
              else:
                #sim = 1 - levenshtein_ori(newtree1, tree2) / max(len(newtree1),len(tree2))
                sim = cross_check(subtree1, tree2)
    elif roots1 in seq_ope and roots2 in seq_ope:
        ##print("Both are ordered operator")
        # tre1 = [roots1, '('] + subtree1 + [')']
        # tre2 = [roots2, '('] + subtree2 + [')']
        sim = 1 - levenshtein(subtree1, subtree2) / max(len(subtree1),len(subtree2))
    elif ( (roots1 == 'xor' and roots2 == 'xor') or (roots1 == '[+]' and roots2 == '[+]')):
        ##print("Both are unordered operator (xor)")
        sim = cross_check(subtree1, subtree2)
    elif (roots1 == 'and' and roots2 == 'and') or (roots1 == '[+]' and roots2 == '[+]'):
        ##print("Both are ordered operator (and)")
        sim = cross_check(subtree1, subtree2)
    else:
        #newtree1 = [roots1, '('] + subtree1 + [')']
        #newtree2 = [roots2, '('] + subtree2 + [')']
        #sim = 1 - levenshtein_ori(tree1, tree2) / max(len(tree1),len(tree2))
        sim = 0
    
    ##print("Partial Similarity : " + str(sim))
    ##print("-----------------------------------------------------")

    return sim
