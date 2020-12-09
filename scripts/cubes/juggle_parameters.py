from subprocess import run
import sys
def newTest(*param):
    with open('./scripts/'+sys.argv[1]+'/test.sh','r') as infile, open('./scripts/'+sys.argv[1]+'/newTest.sh','w') as outfile:
        for line in infile:
            if line.startswith("--ncf"):
                line = line[:6]+param[0]+line[-3:]
            if line.startswith("--pool_res"):
                line = line[:11]+param[1]+line[-3:]
            outfile.write(line)

if __name__=="__main__":
    for i in range(4):
        for j in range(4):
            param=[" ".join([str(2**(i+1+k)) for k in range(2,6)])]
            param.append("600 "+("450 ","")[j%2]+("300 ","")[(j//2)%2]+"210")
            run(['chmod','+x','./scripts/'+sys.argv[1]+'/newTest.sh'],check=True)
            newTest(*param)
            print("Testing with parametrs: --ncf "+param[0]+", --pool_res "+param[1]+":")
            run(['bash','./scripts/'+sys.argv[1]+'/newTest.sh'],check=True)
        
    
