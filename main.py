import ptsim_lib2 as pt
import diffTree as df
from multiprocessing import Process, Queue
import numpy as np
import psutil
import ray

N1 = 'sequence ( ActivityA and ( ActivityC ActivityHL ) and ( xor ( ActivityGG ActivityE ActivityET ActivityBV ) xor ( ActivityIB ActivityHN ActivityJB ActivityII ) ) and ( ActivityKW ActivityKV ActivityKU ActivityKT ActivityKS ActivityKR ActivityKQ ActivityKP ActivityKL ActivityKK ActivityJW ActivityJV ActivityJU ActivityJT ActivityHM ActivityD xor ( tau xorLoop ( ActivityID tau tau ) ) sequence ( xorLoop ( xor ( ActivityDX ActivityCU ActivityEI ActivityJL ActivityJP ActivityJD ActivityBX ActivityGI ActivityGK ActivityGJ ActivityIK ActivityIW ActivityIR ActivityIP ActivityFL ActivityHR ActivityAC ActivityHZ ActivityAX ActivityEV ActivityAN ActivityFE ActivityG ActivityHP ActivityEX ActivityFC ActivityN ActivityBO ) tau tau ) and ( xor ( tau ActivityFV ) xorLoop ( xor ( sequence ( xor ( ActivityAJ ActivityIH ActivityIF ActivityIG ActivityAP ActivityGH ActivityFM ActivityBH ActivityAZ ActivityP ActivityHQ ActivityEZ ActivityFA ActivityFB ActivityFD ActivityFH ActivityI ActivityK ActivityJ ActivityFJ ActivityIA ActivityBP ActivityJN ActivityJH ActivityJS ActivityJO ActivityJJ ActivityIQ ActivityIU ActivityIZ ActivityIY ActivityJA ActivityIM ActivityIN ActivityIO ActivityHW ActivityJI ActivityJR ActivityAL ActivityJF ActivityED ActivityEM ActivityEK ActivityEL ActivityCD ActivityDJ ActivityDA ActivityBZ ActivityJG ActivityCP ActivityHX ActivityIT ActivityEF ActivityDH ActivityEW ActivityFI ActivityEG ActivityHU ActivityHT ActivityHY ActivityDZ ActivityCW ActivityCL ActivityDR ActivityCN ActivityFG ActivityAE ActivityIV ActivityDP ActivityFK ActivityHV ) xorLoop ( xor ( sequence ( xor ( tau ActivityGT ActivityGF ActivityGD ) and ( xor ( tau ActivityJZ ) xor ( tau ActivityKB ) xor ( tau ActivityKA ) xor ( tau ActivityJQ ) xor ( tau ActivityJY ) sequence ( and ( xor ( tau ActivityJM ) xor ( tau ActivityJE ) sequence ( xor ( tau ActivityV ) and ( xor ( tau ActivityJC ) xor ( tau ActivityIL ) xor ( tau ActivityIS ) xor ( tau ActivityIX ) sequence ( xor ( tau ActivityT ) and ( xor ( tau ActivityKI ) sequence ( xor ( tau ActivityU ) and ( xor ( tau ActivityJX ) sequence ( xor ( ActivityHE ActivityHK ActivityHG and ( xor ( tau ActivityGX ) xor ( tau ActivityGY ) ) ) and ( xor ( tau ActivityIJ ) sequence ( and ( xor ( tau ActivityHS ) sequence ( xor ( tau ActivityR ActivityAM ) and ( xor ( tau ActivityHJ ) sequence ( xor ( tau ActivityHI ) and ( xor ( tau ActivityHO ) sequence ( xor ( ActivityGL sequence ( xor ( tau ActivityFF ActivityEY ) xor ( tau ActivityEU ) xor ( tau ActivityFN ) xor ( tau ActivityFR ActivityFX ) ) ActivityAQ ActivityAK and ( xor ( tau ActivityBM ) sequence ( xor ( tau ActivityBE ) and ( xor ( tau ActivityBG ) sequence ( xor ( tau ActivityBN ) and ( xor ( tau ActivityBK ) sequence ( xor ( tau ActivityBD ActivityBC ) and ( xor ( tau ActivityBJ ) xor ( and ( xor ( tau ActivityBF ) xor ( tau ActivityBL ) ) ActivityBB ) ) ) ) ) ) ) ) ActivityH ActivityBQ and ( ActivityAG ActivityAI ActivityAH ) ActivityS ActivityW ) and ( xor ( tau ActivityIE ) sequence ( xor ( tau ActivityGB ) and ( xor ( tau ActivityIC ) sequence ( and ( xor ( tau ActivityDY ) sequence ( xorLoop ( xor ( ActivityEC ActivityCB ActivityDW and ( xor ( tau ActivityEJ ) xor ( sequence ( xor ( tau ActivityDC ) xor ( tau ActivityEB ActivityEE ActivityCO ) ) sequence ( xor ( tau ActivityCF ) xor ( tau ActivityEH ) ) ) ) ActivityCT ActivityCJ ActivityCZ ActivityCY ActivityCR ActivityDU ActivityCH ActivityDF ActivityDE ActivityCC ActivityCM ActivityCK ActivityDD ActivityCG ActivityDG ActivityDL ActivityDI ActivityCS ActivityDN ActivityDT ActivityDM ActivityDV ActivityDQ ActivityDO ActivityCI ) tau tau ) xor ( tau xorLoop ( xor ( ActivityCA ActivityDS ActivityEN ActivityCQ ActivityEA ActivityER ActivityCE ActivityCX ActivityDK ActivityDB ActivityEP ActivityBY ActivityCV ) tau tau ) ) ) ) xor ( tau ActivityEO ) xor ( tau ActivityKC ) and ( xor ( tau ActivityGW ) sequence ( xor ( tau ActivityKJ ) and ( xor ( tau ActivityX ) xor ( tau ActivityHA ) xor ( sequence ( xor ( tau ActivityKD ) and ( xor ( tau ActivityQ ) sequence ( xor ( tau and ( ActivityZ ActivityAB ActivityAA ) ) xor ( tau ActivityKG ) xor ( tau ActivityKH ) ) ) xor ( tau ActivityKO ) ) ActivityKM ActivityKE ) ) xor ( sequence ( xor ( tau ActivityKF ) xor ( tau ActivityAR ) and ( xor ( tau ActivityAV ) xor ( tau ActivityAT ) xor ( tau ActivityAW ) xor ( tau ActivityAU ) ) xor ( tau ActivityKN ) ) ActivityGV ) xor ( tau ActivityGZ ) ) ) ) ) ) ) xor ( tau and ( ActivityBS ActivityBT ActivityBU ) ) ) ) xor ( tau ActivityHH ) ) ) ) ) xor ( ActivityGO ActivityGQ ActivityAO sequence ( xor ( tau ActivityAF ) xor ( tau ActivityAD ) ) ActivityGS and ( ActivityBA ActivityBI ) ActivityGP ActivityGN ActivityL ActivityGR ) ) ) ) ) ) ) ) ) ) ) xor ( ActivityBW sequence ( xor ( tau ActivityHD ) xor ( tau ActivityHC ) xor ( tau ActivityGU ) ) sequence ( xor ( tau ActivityFW ActivityFS ) xor ( tau ActivityFO ) ) ) ) ) xor ( tau ActivityES ActivityGM ActivityFZ ActivityGA ActivityGE ActivityF ActivityHB ActivityAY ActivityFT ActivityEQ ActivityHF ActivityFU ActivityFP ActivityM ActivityFY ActivityAS ActivityBR ActivityO ActivityGC ActivityY ) ) ActivityFQ ) tau tau ) ) ActivityJK ) tau tau ) ) ) ) ActivityB )'
N2 = 'sequence ( ActivityA and ( ActivityC ActivityHL ) and ( xor ( ActivityGG ActivityE ActivityET ActivityBV ) xor ( ActivityIB ActivityHN ActivityJB ActivityII ) ) and ( ActivityKW ActivityKV ActivityKU ActivityKT ActivityKS ActivityKR ActivityKQ ActivityKP ActivityKL ActivityKK ActivityJW ActivityJV ActivityJU ActivityJT ActivityHM ActivityD xor ( tau xorLoop ( ActivityID tau tau ) ) sequence ( xorLoop ( xor ( ActivityDX ActivityCU ActivityEI ActivityJL ActivityJP ActivityJD ActivityBX ActivityGI ActivityGK ActivityGJ ActivityIK ActivityIW ActivityIR ActivityIP ActivityFL ActivityHR ActivityAC ActivityHZ ActivityAX ActivityEV ActivityAN ActivityFE ActivityG ActivityHP ActivityEX ActivityFC ActivityN ActivityBO ) tau tau ) and ( xor ( tau ActivityFV ) xorLoop ( xor ( sequence ( xor ( ActivityAJ ActivityIH ActivityIF ActivityIG ActivityAP ActivityGH ActivityFM ActivityBH ActivityAZ ActivityP ActivityHQ ActivityEZ ActivityFA ActivityFB ActivityFD ActivityFH ActivityI ActivityK ActivityJ ActivityFJ ActivityIA ActivityBP ActivityJN ActivityJH ActivityJS ActivityJO ActivityJJ ActivityIQ ActivityIU ActivityIZ ActivityIY ActivityJA ActivityIM ActivityIN ActivityIO ActivityHW ActivityJI ActivityJR ActivityAL ActivityJF ActivityED ActivityEM ActivityEK ActivityEL ActivityCD ActivityDJ ActivityDA ActivityBZ ActivityJG ActivityCP ActivityHX ActivityIT ActivityEF ActivityDH ActivityEW ActivityFI ActivityEG ActivityHU ActivityHT ActivityHY ActivityDZ ActivityCW ActivityCL ActivityDR ActivityCN ActivityFG ActivityAE ActivityIV ActivityDP ActivityFK ActivityHV ) xorLoop ( xor ( sequence ( xor ( tau ActivityGT ActivityGF ActivityGD ) and ( xor ( tau ActivityJZ ) xor ( tau ActivityKB ) xor ( tau ActivityKA ) xor ( tau ActivityJQ ) xor ( tau ActivityJY ) sequence ( and ( xor ( tau ActivityJM ) xor ( tau ActivityJE ) sequence ( xor ( tau ActivityV ) and ( xor ( tau ActivityJC ) xor ( tau ActivityIL ) xor ( tau ActivityIS ) xor ( tau ActivityIX ) sequence ( xor ( tau ActivityT ) and ( xor ( tau ActivityKI ) sequence ( xor ( tau ActivityU ) and ( xor ( tau ActivityJX ) sequence ( xor ( ActivityHE ActivityHK ActivityHG and ( xor ( tau ActivityGX ) xor ( tau ActivityGY ) ) ) and ( xor ( tau ActivityIJ ) sequence ( and ( xor ( tau ActivityHS ) sequence ( xor ( tau ActivityR ActivityAM ) and ( xor ( tau ActivityHJ ) sequence ( xor ( tau ActivityHI ) and ( xor ( tau ActivityHO ) sequence ( xor ( ActivityGL sequence ( xor ( tau ActivityFF ActivityEY ) xor ( tau ActivityEU ) xor ( tau ActivityFN ) xor ( tau ActivityFR ActivityFX ) ) ActivityAQ ActivityAK and ( xor ( tau ActivityBM ) sequence ( xor ( tau ActivityBE ) and ( xor ( tau ActivityBG ) sequence ( xor ( tau ActivityBN ) and ( xor ( tau ActivityBK ) sequence ( xor ( tau ActivityBD ActivityBC ) and ( xor ( tau ActivityBJ ) xor ( and ( xor ( tau ActivityBF ) xor ( tau ActivityBL ) ) ActivityBB ) ) ) ) ) ) ) ) ActivityH ActivityBQ and ( ActivityAG ActivityAI ActivityAH ) ActivityS ActivityW ) and ( xor ( tau ActivityIE ) sequence ( xor ( tau ActivityGB ) and ( xor ( tau ActivityIC ) sequence ( and ( xor ( tau ActivityDY ) sequence ( xorLoop ( xor ( ActivityEC ActivityCB ActivityDW and ( xor ( tau ActivityEJ ) xor ( sequence ( xor ( tau ActivityDC ) xor ( tau ActivityEB ActivityEE ActivityCO ) ) sequence ( xor ( tau ActivityCF ) xor ( tau ActivityEH ) ) ) ) ActivityCT ActivityCJ ActivityCZ ActivityCY ActivityCR ActivityDU ActivityCH ActivityDF ActivityDE ActivityCC ActivityCM ActivityCK ActivityDD ActivityCG ActivityDG ActivityDL ActivityDI ActivityCS ActivityDN ActivityDT ActivityDM ActivityDV ActivityDQ ActivityDO ActivityCI ) tau tau ) xor ( tau xorLoop ( xor ( ActivityCA ActivityDS ActivityEN ActivityCQ ActivityEA ActivityER ActivityCE ActivityCX ActivityDK ActivityDB ActivityEP ActivityBY ActivityCV ) tau tau ) ) ) ) xor ( tau ActivityEO ) xor ( tau ActivityKC ) and ( xor ( tau ActivityGW ) sequence ( xor ( tau ActivityKJ ) and ( xor ( tau ActivityX ) xor ( tau ActivityHA ) xor ( sequence ( xor ( tau ActivityKD ) and ( xor ( tau ActivityQ ) sequence ( xor ( tau and ( ActivityZ ActivityAB ActivityAA ) ) xor ( tau ActivityKG ) xor ( tau ActivityKH ) ) ) xor ( tau ActivityKO ) ) ActivityKM ActivityKE ) ) xor ( sequence ( xor ( tau ActivityKF ) xor ( tau ActivityAR ) and ( xor ( tau ActivityAV ) xor ( tau ActivityAT ) xor ( tau ActivityAW ) xor ( tau ActivityAU ) ) xor ( tau ActivityKN ) ) ActivityGV ) xor ( tau ActivityGZ ) ) ) ) ) ) ) xor ( tau and ( ActivityBS ActivityBT ActivityBU ) ) ) ) xor ( tau ActivityHH ) ) ) ) ) xor ( ActivityGO ActivityGQ ActivityAO sequence ( xor ( tau ActivityAF ) xor ( tau ActivityAD ) ) ActivityGS and ( ActivityBA ActivityBI ) ActivityGP ActivityGN ActivityL ActivityGR ) ) ) ) ) ) ) ) ) ) ) xor ( ActivityBW sequence ( xor ( tau ActivityHD ) xor ( tau ActivityHC ) xor ( tau ActivityGU ) ) sequence ( xor ( tau ActivityFW ActivityFS ) xor ( tau ActivityFO ) ) ) ) ) xor ( tau ActivityES ActivityGM ActivityFZ ActivityGA ActivityGE ActivityF ActivityHB ActivityAY ActivityFT ActivityEQ ActivityHF ActivityFU ActivityFP ActivityM ActivityFY ActivityAS ActivityBR ActivityO ActivityGC ActivityY ) ) ActivityFQ ) tau tau ) ) ActivityJK ) tau tau ) ) ) ) ActivityB )'
PT1='sequence ( xor ( A AI ) xor ( sequence ( C xorLoop ( sequence ( E and ( H G ) F ) sequence ( xor ( I sequence ( AJ AK AL ) ) J ) tau ) D ) sequence ( xor ( sequence ( AE AF ) Y ) xor ( AA AB ) xor ( sequence ( AG AH ) Z ) AC AD ) sequence ( K and ( S M ) and ( W V X U xor ( P Q O R ) ) and ( T N ) L ) ) B and ( T F ) )'
PT2='sequence ( A xor ( sequence ( K and ( S M ) and ( X W V U xor ( R O P Q ) ) and ( T N ) L ) sequence ( Y xor ( AB AA ) Z AC AD ) sequence ( C xorLoop ( sequence ( E and ( H G ) F ) sequence ( I J ) tau ) D ) ) B and ( T N ) )'

def readModel(name, batchSize, interval):
    model = [[str(x) for x in range(interval)] for y in range(batchSize)] 
    
    for x in range(0,batchSize):
        batch = x+1
        for y in range(0,interval):
            size = (y+1)*10
            PTformula =  './data/'+name+'/'+ str(batch) + '/'+ str(size) +'.ptf'
            f=open(PTformula, "r")
            model[x][y]= f.read().replace('_','').replace('Activity','')
            #print(model[x][y] + "\n\n")
            
    return model

def doWork(a,b,i,q):
    print("Calculating sim[" + str(i) + "]")
    #create a random list of N integers
    result = pt.simular(a,b)
   
    #put the result in the Queue to return the the calling process
    q.put(result)

if __name__ == '__main__':
    A = readModel('A',5,100)
    B = readModel('B',5,100)
    c = readModel('C',5,100)
    #print('sim(A, B) =' + str(pt.simular(PT1, PT2)))
    #print('sim(A, B) =' + str(pt.simular(A[0][1], A[1][1])))

    print("-----------")
    dirA = './data/Model_A.csv'
    dirB = './data/Model_B.csv'
    dirC = './data/Model_C.csv'
    
#    f1= open(dirA,"w+")
#    f1.write("time,sim(A1.A2),sim(A1.A3),sim(A1.A4),sim(A1.A5),sim(A2.A3),sim(A2.A4),sim(A2.A5),sim(A3.A4),sim(A3.A5),sim(A4.A5)\r\n")
#    for t in range(0,100):
#        print("A:"+str(t+1))
#        f1.write(str(t+1)+","+str(pt.simular(A[0][t],A[1][t]))+","+str(pt.simular(A[0][t],A[2][t]))+","+str(pt.simular(A[0][t],A[3][t]))+","+str(pt.simular(A[0][t],A[4][t]))+","+str(pt.simular(A[1][t],A[2][t]))+","+str(pt.simular(A[0][t],A[3][t]))+","+str(pt.simular(A[1][t],A[4][t]))+","+str(pt.simular(A[2][t],A[3][t]))+","+str(pt.simular(A[2][t],A[4][t]))+","+str(pt.simular(A[3][t],A[4][t]))+"\r\n")
#    f1.close()
#    
#    f2= open(dirB,"w+")
#    f2.write("time,sim(B1.B2),sim(B1.B3),sim(B1.B4),sim(B1.B5),sim(B2.B3),sim(B2.B4),sim(B2.B5),sim(B3.B4),sim(B3.B5),sim(B4.B5)\r\n")
#    for t in range(0,100):
#        print("B:"+str(t+1))
#        f2.write(str(t+1)+","+str(pt.simular(B[0][t],B[1][t]))+","+str(pt.simular(B[0][t],B[2][t]))+","+str(pt.simular(B[0][t],B[3][t]))+","+str(pt.simular(B[0][t],B[4][t]))+","+str(pt.simular(B[1][t],B[2][t]))+","+str(pt.simular(B[0][t],B[3][t]))+","+str(pt.simular(B[1][t],B[4][t]))+","+str(pt.simular(B[2][t],B[3][t]))+","+str(pt.simular(B[2][t],B[4][t]))+","+str(pt.simular(B[3][t],B[4][t]))+"\r\n")
#    f2.close()


    
    f3= open(dirC,"w+")
    f3.write("time,sim(C1.C2),sim(C1.C3),sim(C1.C4),sim(C1.C5),sim(C2.C3),sim(C2.C4),sim(C2.C5),sim(C3.C4),sim(C3.C5),sim(C4.C5)\r\n")
    for t in range(0,100):
        #if (t!=6):
        print("C:"+str(t+1))
        #create a Queue to share results
        q = Queue()
        #create 4 sub-processes to do the work
        p1 = Process(target=doWork, args=(c[0][t],c[1][t],0,q))
        p1.start()
        p2 = Process(target=doWork, args=(c[0][t],c[2][t],1,q))
        p2.start()
        p3 = Process(target=doWork, args=(c[0][t],c[3][t],2,q))
        p3.start()
        p4 = Process(target=doWork, args=(c[0][t],c[4][t],3,q))
        p4.start()
        p5 = Process(target=doWork, args=(c[1][t],c[2][t],4,q))
        p5.start()
        p6 = Process(target=doWork, args=(c[1][t],c[3][t],5,q))
        p6.start()
        p7 = Process(target=doWork, args=(c[1][t],c[4][t],6,q))
        p7.start()
        p8 = Process(target=doWork, args=(c[2][t],c[3][t],7,q))
        p8.start()
        p9 = Process(target=doWork, args=(c[2][t],c[4][t],8,q))
        p9.start()
        p10 = Process(target=doWork, args=(c[3][t],c[4][t],9,q))
        p10.start()
            
        sim = []
        #grab 10 values from the queue, one for each process
        for i in range(10):
            #set block=True to block until we get a result
            sim.append(q.get(True))
            
        p1.join()
        p2.join()
        p3.join()
        p4.join()
        p5.join()
        p6.join()
        p7.join()
        p8.join()
        p9.join()
        p10.join()
        f3.write(str(t+1)+","+str(sim[0])+","+str(sim[1])+","+str(sim[2])+","+str(sim[3])+","+str(sim[4])+","+str(sim[5])+","+str(sim[6])+","+str(sim[7])+","+str(sim[8])+","+str(sim[9])+"\r\n")
    f3.close()
