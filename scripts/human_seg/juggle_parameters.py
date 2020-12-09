from subprocess import run
import sys
def newTest(*param):
    with open('./scripts/human_seg/test.sh','r') as infile, open('./scripts/human_seg/newTest.sh','w') as outfile:
        for line in infile:
            #if line.startswith("--ncf"):
                #line = line[:6]+param[0]+line[-3:]
            if line.startswith("--pool_res"):
                line = line[:11]+param[1]+line[-3:]
            outfile.write(line)

if __name__=="__main__":
    for i in range(4):
        for j in range(4):
            param=[" ".join([str(2**(i+1+k)) for k in range(2,6)])]
            param.append("1800 "+str((4*i+j+1)*(1800-600)+600)+" 600")
            newTest(*param)
            run(['chmod','+x','./scripts/human_seg/newTest.sh'],check=True)
            #print("Testing with parametrs: --ncf "+param[0]+", --pool_res "+param[1]+":")
            print("Testing with parametrs: --pool_res "+param[1]+":")
            run(['bash','./scripts/human_seg/newTest.sh'],check=True)
        
    
