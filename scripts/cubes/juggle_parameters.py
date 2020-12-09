

from subprocess import run
import sys
def newTest(*param):
    with open('./scripts/cubes/test.sh','r') as infile, open('./scripts/cubes/newTest.sh','w') as outfile:
        for line in infile:
            #if line.startswith("--ncf"):
                #line = line[:6]+param[0]+line[-3:]
            if line.startswith("--pool_res"):
                line = line[:11]+param[1]+line[-3:]
            outfile.write(line)

if __name__=="__main__":
    options=["525 450 ",
             "525 300 ",
             "450 300 "]
    for i in range(4):
        for j in range(4):
            param=[" ".join([str(2**(i+1+k)) for k in range(2,6)])]
            param.append("600 "+str((i+1)*(600-405)//5+405)+" "+str((j+1)*(405-210)//5+210)+" "+"210")
            newTest(*param)
            run(['chmod','+x','./scripts/cubes/newTest.sh'],check=True)
            #print("Testing with parametrs: --ncf "+param[0]+", --pool_res "+param[1]+":")
            print("Testing with parametrs: --pool_res "+param[1]+":")
            run(['bash','./scripts/cubes/newTest.sh'],check=True)
        
    
