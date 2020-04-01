import ptsim_lib2 as pt
import diffTree as df
#import ray as ray
#
#ray.init()

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
        f.close()
    return model

def trainNormalModel(model, directory):
    f= open(directory,"w+")
    f.write("time,sim(X1.X2),sim(X1.X3),sim(X1.X4),sim(X1.X5),sim(X2.X3),sim(X2.X4),sim(X2.X5),sim(X3.X4),sim(X3.X5),sim(X4.X5)\r\n")
    for t in range(0,100):
        print(name+":"+str(t+1))
        f.write(str(t+1)+","+str(pt.simular(model[0][t],model[1][t]))+","+str(pt.simular(model[0][t],model[2][t]))+","+str(pt.simular(model[0][t],model[3][t]))+","+str(pt.simular(model[0][t],model[4][t]))+","+str(pt.simular(model[1][t],model[2][t]))+","+str(pt.simular(model[0][t],model[3][t]))+","+str(pt.simular(model[1][t],model[4][t]))+","+str(pt.simular(model[2][t],model[3][t]))+","+str(pt.simular(model[2][t],model[4][t]))+","+str(pt.simular(model[3][t],model[4][t]))+"\r\n")
    f.close()
    
def anomalyDetection(normal,obs,x, interval, directory):
    f1= open(directory,"w+")
    f1.write("time,sim(X1.Obs),sim(X2.Obs),sim(X3.Obs),sim(X4.Obs),sim(X5.Obs)\r\n")
    for t in range(0,interval):
        print("Detection:"+str(t+1))
        f1.write(str(t+1)+","+str(pt.simular(normal[0][t],obs[x][t]))+","+str(pt.simular(normal[1][t],obs[x][t]))+","+str(pt.simular(normal[2][t],obs[x][t]))+","+str(pt.simular(normal[3][t],obs[x][t]))+","+str(pt.simular(normal[4][t],obs[x][t]))+"\r\n")
    f1.close()
    

if __name__ == '__main__':
    interval = 20
    A = readModel('A',5,interval)
    #B = readModel('B',5,interval)
    #c = readModel('C',5,interval)
    
    obs = readModel('Observed10',3,interval)

    print("-----------")
    dirA = './data/Model_A.csv'
    dirB = './data/Model_B.csv'
    dirC = './data/Model_C.csv'
    
    dirA_5a = './data/Model_A_5a.csv'
    dirA_5b = './data/Model_A_5b.csv'
    dirA_5ab = './data/Model_A_5ab.csv'
    dirA_3a = './data/Model_A_3a.csv'
    dirA_3b = './data/Model_A_3b.csv'
    dirA_3ab = './data/Model_A_3ab.csv'
    dirA_10a = './data/Model_A_10a.csv'
    dirA_10b = './data/Model_A_10b.csv'
    dirA_10ab = './data/Model_A_10ab.csv'
#    trainNormalModel(A,dirA)
#    trainNormalModel(B,dirB)
    
    #5%
#    anomalyDetection(A,obs,0,interval, dirA_5a) #5a
#    anomalyDetection(A,obs,1,interval, dirA_5b) #5b
#    anomalyDetection(A,obs,2,interval, dirA_5ab) #5ab
    
    #3%
    #5%
#    anomalyDetection(A,obs,3,interval, dirA_3a) #5a
#    anomalyDetection(A,obs,4,interval, dirA_3b) #5b
#    anomalyDetection(A,obs,5,interval, dirA_3ab) #5ab
    
    #10%
    anomalyDetection(A,obs,0,interval, dirA_10a) #5a
    anomalyDetection(A,obs,1,interval, dirA_10b) #5b
    anomalyDetection(A,obs,2,interval, dirA_10ab) #5ab
