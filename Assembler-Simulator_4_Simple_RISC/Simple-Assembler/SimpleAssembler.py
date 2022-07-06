import sys
#infile=sys.stdin
infile=sys.stdin.read().splitlines()
count=0
output=[]
labels={}
variables={}

register = {
    "R0": "000",
    "R1": "001",
    "R2": "010",
    "R3": "011",
    "R4": "100",
    "R5": "101",
    "R6": "110",
    "FLAGS": "111",
    }

def jlt(arr, labels,count):
    out = "01100000"
    if len(arr) == 2:
        if labels.get(arr[1]) is not None:
            mem = labels.get(arr[1])
            out+=(mem).zfill(8)
            return out
        else:
            raise SyntaxError(f"ERROR: LABEL WAS NOT FOUND , at line {count}")
            
    else:
        raise SyntaxError(f"ERROR: INVALID ARGUMENTS , at line {count}")
       
def jmp(arr, labels,count):

    out = "11111000"
    if len(arr) == 2:
        if labels.get(arr[1]) is not None:
            mem = labels.get(arr[1])
            out+= (mem).zfill(8)
            return out
        else:
            raise SyntaxError(f"ERROR: LABEL WAS NOT FOUND , at line {count}")

    else:
        raise SyntaxError(f"ERROR: INVALID ARGUMENTS , at line {count}")
            
def mul(arr,register,count):
    if "FLAGS" in arr:
        raise SyntaxError(f"ERROR: FLAGS CANNOT BE AN OPERAND HERE , at line {count}")
    if len(arr)!= 4:
        raise SyntaxError(f"ERROR:INVALID ARGUMENTS , at line {count}")
    else:
        c = 0
        bin_string = "1011000"
        for j in range(1, 4):
            for i in register:
                if i == arr[j]:
                    bin_string = bin_string + register[i]
                    c = 0
                    break
                else:
                    c = 1
            if c == 1:
                raise SyntaxError(f"ERROR: INVALID REGISTER CODE , at line {count}")
        return bin_string

def add(arr,register,count):
    if "FLAGS" in arr:
        raise SyntaxError(f"ERROR: FLAGS CANNOT BE AN OPERAND HERE , at line {count}")
    
    if len(arr)!= 4:
        raise SyntaxError(f"ERROR:INVALID ARGUMENTS , at line {count}")
    
    else:
        c = 0
        bin_string = "1000000"
        for j in range(1, 4):
            for i in register:
                if i == arr[j]:
                    bin_string = bin_string + register[i]
                    c = 0   
                    break
        
                else:
                    c = 1 
            if c == 1:
                raise SyntaxError(f"ERROR: INVALID REGISTER CODE , at line {count}")
            
        return bin_string

def je(arr, labels,count):
    out = "01111000"
    if len(arr) == 2:
        if labels.get(arr[1]) is not None:
            mem = labels.get(arr[1])
            out+= (mem).zfill(8)
            return out
        else:
            raise SyntaxError(f"ERROR: LABEL WAS NOT FOUND , at line {count}")
    else:
        raise SyntaxError(f"ERROR: INVALID ARGUMENTS , at line {count}")
        
def ld(arr, variables,count):
    out= "00100"
    if len(arr) == 3:
        if arr[1] in registers:
            out+= registers.get(arr[1])
            if variables.get(arr[2]):
                mem = variables.get(arr[2])
                out+=(mem).zfill(8)
                return output
            else:
                raise SyntaxError(f"ERROR: VARIABLE WAS NOT FOUND  , at line {count}")
                
        elif arr[1] == "FLAGS":
            raise SyntaxError(f"ERROR: CANNOT WRITE TO FLAG REGISTER  , at line {count}")
            
        else:
            raise SyntaxError(f"ERROR: NO SUCH REGISTER , at line {count}")
            
    else:
        raise SyntaxError(f"ERROR: INVALID ARGUMENTS , at line {count}")
      
def AND(arr,register,count):
    if "FLAGS" in arr:
        raise SyntaxError(f"ERROR: FLAGS CANNOT BE AN OPERAND HERE  , at line {count}")
    if len(arr)!= 4:
         raise SyntaxError(f"ERROR:INCORRECT NUMBER OF OPERANDS  , at line {count}")
    else:
        c = 0
        bin_string = "1110000"
        for j in range(1, 4):
            for i in register:
                if i == arr[j]:
                    bin_string+= register[i]
                    c = 0
                    break
                else:
                    c = 1
            if c == 1:
                raise SyntaxError(f"ERROR: INVALID REGISTER CODE  , at line {count}")
        return bin_string

def div(arr,register,count):
    if "FLAGS" in arr:
        raise SyntaxError(f"ERROR: FLAGS CANNOT BE AN OPERAND HERE  , at line {count}")
    if len(arr)!= 3:
       raise SyntaxError(f"ERROR:INVALID ARGUMENTS  , at line {count}")
    else:
        c = 0
        bin_string = "1011100000"
        for j in range(1, 3): 
            for i in register:
                if i == arr[j]:
                    bin_string = bin_string + register[i]
                    c = 0
                    break
                else:
                    c = 1
            if c == 1:
                raise SyntaxError(f"ERROR: INVALID REGISTER CODE , at line {count}")
        return bin_string

def Compare(arr,register,count):
    if "FLAGS" in arr:
        raise SyntaxError(f"ERROR: FLAGS CANNOT BE AN OPERAND HERE , at line {count}")
    if len(arr)!= 3:
       raise SyntaxError(f"ERROR:INVALID ARGUMENTS , at line {count}")
    else:
        c = 0
        bin_string = "1111000000"
        for j in range(1, 3): 
            for i in register:
                if i == arr[j]:
                    bin_string = bin_string + register[i]
                    c = 0
                    break
                else:
                    c = 1
            if c == 1:
                raise SyntaxError(f"ERROR: INVALID REGISTER CODE , at line {count}")
        return bin_string

def Invert(arr,register,count):
    if "FLAGS" in arr:
        raise SyntaxError(f"ERROR: FLAGS CANNOT BE AN OPERAND HERE , at line {count}")
    if len(arr)!= 3:
       raise SyntaxError(f"ERROR:INVALID ARGUMENTS , at line {count}")
    else:
        c = 0
        bin_string = "1110100000"
        for j in range(1, 3): 
            for i in register:
                if i == arr[j]:
                    bin_string = bin_string + register[i]
                    c = 0
                    break
                else:
                    c = 1
            if c == 1:
                raise SyntaxError(f"ERROR: INVALID REGISTER CODE , at line {count}")
        return bin_string   

def mov(arr,register,count):
    if len(arr)!= 3:
        raise SyntaxError(f"ERROR: INVALID ARGUMENTS , at line {count}")
    if arr[2] in register:
        c = 0
        bin_string = "10011000000"
        for j in range(1, 3):
            for i in register:
                if i == arr[j] and (not ((j == 1) and (i == "FLAGS"))):
                    bin_string = bin_string + register[i]
                    c = 0
                    break
                else:
                    if (arr[j] == "FLAGS") and (j == 1):
                       raise SyntaxError(f"ERROR: CANNOT WRITE TO FLAGS  , at line {count}")
                    c = 1
            if c == 1:
                raise SyntaxError(f"ERROR: INVALID REGISTER CODE  , at line {count}")
        return bin_string

    else:
        c = 0
        bin_string = "10010"

        if arr[2][0] != "$":
            raise SyntaxError(f"ERROR: INVALID OPERAND  , at line {count}")
        arr[2] = arr[2][1:]

        try:
           
            num = int(arr[2])
            if num > 255 or num < 0:
                raise SyntaxError( f"ERROR: {num} CANNOT BE USED AS AN IMMEDITATE VALUE  , at line {count}")
            for i in register:
                if i == arr[1] and i != "FLAGS":
                    bin_string = bin_string + register[i]
                    c=0
                    break
                else:
                    if (arr[1] == "FLAGS") :
                        raise SyntaxError(f"ERROR: CANNOT WRITE TO FLAGS  , at line {count}")
                    c = 1
            if c == 1:
                raise SyntaxError(f"ERROR: INVALID REGISTER CODE  , at line {count}")

            else:
                bin_string = bin_string + format(num, "08b")  
                return bin_string
        except:
            raise SyntaxError(f"ERROR: THIS INSTRUCTION ONLY TAKES INT/REG  , at line {count}")

def XOR(arr,register,count):
    if "FLAGS" in arr:
        raise SyntaxError(f"ERROR: FLAGS CANNOT BE AN OPERAND HERE  , at line {count}")
    if len(arr)!= 4:
        raise SyntaxError(f"ERROR:INVALID ARGUMENTS  , at line {count}")
    else:
        c = 0
        bin_string = "1101000"
        for j in range(1, 4):
            for i in register:
                if i == arr[j]:
                    bin_string = bin_string + register[i]
                    c = 0
                    break
                else:
                    c = 1
            if c == 1:
                raise SyntaxError(f"ERROR: INVALID REGISTER CODE  , at line {count}")
        return bin_string

def OR(arr,register,count):
    if "FLAGS" in arr:
        raise SyntaxError(f"ERROR: FLAGS CANNOT BE AN OPERAND HERE  , at line {count}")
    if len(arr)!= 4:
        raise SyntaxError(f"ERROR:INVALID ARGUMENTS  , at line {count}")
    else:
        c = 0
        bin_string = "1101100"
        for j in range(1, 4):
            for i in register:
                if i == arr[j]:
                    bin_string = bin_string + register[i]
                    c = 0
                    break
                else:
                    c = 1
            if c == 1:
                raise SyntaxError(f"ERROR: INVALID REGISTER CODE  , at line {count}")
        return bin_string

def sub(arr,register,count):
    if "FLAGS" in arr:
        raise SyntaxError(f"ERROR: FLAGS CANNOT BE AN OPERAND HERE  , at line {count}")
    if len(arr)!= 4:
        raise SyntaxError(f"ERROR:INVALID ARGUMENTS  , at line {count}")
    else:
        c = 0
        bin_string = "1000100"
        for j in range(1, 4):
            for i in register:
                if i == arr[j]:
                    bin_string = bin_string + register[i]
                    c = 0
                    break
                else:
                    c = 1
            if c == 1:
                raise SyntaxError(f"ERROR: INVALID REGISTER CODE  , at line {count}")
        return bin_string

def jgt(arr, labels,count):
    out="01101"
    if len(arr) == 2:
        out+="000"
        if lables.get(arr[1]) is not None:
            mem = labels.get(arr[1])
            out+=(mem).zfill(8)
            return out
        else:
            raise SyntaxError(f"ERROR: LABEL WAS NOT FOUND , at line {count} ")
    else:
        raise SyntaxError(f"ERROR: INVALID ARGUMENTS  , at line {count}")

def st(arr, variables,register,count):
    out="10101"
    if len(arr) == 3:
        if arr[1] in registers:
            out+=registers.get(arr[1])
            if variables.get(arr[2]):
                mem = variables.get(arr[2])
                out+= mem.zfill(8)
                return out
            else:
                raise SyntaxError(f"ERROR: VARIABLE WAS NOT FOUND , at line {count}")
                
        elif arr[1] == "FLAGS":
            raise SyntaxError(f"ERROR: CANNOT SAVE FLAG REGISTER TO MEMORY , at line {count}")
            
        else:
            raise SyntaxError(f"ERROR: INVALID REGISTER CODE , at line {count}")
            
    else:
        raise SyntaxError(f"ERROR: INVALID ARGUMENTS , at line {count}")
        
def Rshift(arr,register,count):
    out= "01000"

    if "FLAGS" in arr:
        raise SyntaxError(f"ERROR: FLAGS CANNOT BE AN OPERAND HERE  , at line {count}")

    if len(arr) == 3:
        if arr[1] == "FLAGS":
            raise SyntaxError(f"ERROR: INVALID USE OF FLAGS  , at line {count}")
            
        if arr[1] in register:
            out+=register.get(arr[1])
        else:
            raise SyntaxError(f"ERROR: INVALID REGISTER CODE  , at line {count}")
           
        imm = arr[2]

        if imm[0] == "$":

            imm = int(imm[1 : len(imm)])

            if imm in range(256):
                imm_bin = str(bin(imm))
                imm_bin = imm_bin[2 : len(imm_bin)]
                if len(imm_bin) < 8:
                    imm_bin = (8 - len(imm_bin)) * "0" + imm_bin
                out+=imm_bin
            else:
                raise SyntaxError(f"ERROR: IMMIDIATE OUT OF BOUND  , at line {count}")
        else:
            raise SyntaxError(f"ERROR: INVALID IMMIDIATE INPUT  , at line {count}")
            
        return out

    else:
        raise SyntaxError(f"ERROR: INVALID ARGUMENTS  , at line {count}")
       
def Lshift(arr,register,count):
    out= "01001"

    if "FLAGS" in arr:
        raise SyntaxError(f"ERROR: FLAGS CANNOT BE AN OPERAND HERE  , at line {count}")

    if len(arr) == 3:
        if arr[1] == "FLAGS":
            raise SyntaxError(f"ERROR: INVALID USE OF FLAGS  , at line {count}")
            
        if arr[1] in register:
            out+=register.get(arr[1])
        else:
            raise SyntaxError(f"ERROR: INVALID REGISTER CODE  , at line {count}")
        
        imm = arr[2]

        if imm[0] == "$":

            imm = int(imm[1 : len(imm)])

            if imm in range(256):
                imm_bin = str(bin(imm))
                imm_bin = imm_bin[2 : len(imm_bin)]
                if len(imm_bin) < 8:
                    imm_bin = (8 - len(imm_bin)) * "0" + imm_bin
                out+= imm_bin
            else:
                raise SyntaxError(f"ERROR: IMMIDIATE OUT OF BOUND  , at line {count}")
                

        else:
            raise SyntaxError(f"ERROR: INVALID IMMIDIATE INPUT  , at line {count}")
            
        return out

    else:
        raise SyntaxError(f"ERROR: INVALID ARGUMENTS  , at line {count}")

def bin(dec):
    s=""
    while dec!=0:
        s+=str(dec%2)
        dec=dec//2
    return s[::-1]


hltCount=0
varCount=0
for line in infile:
    list_1=line.strip().split()
    if list_1[0]=="":
        continue
    else:
        count+=1
        list_1=line.strip().split()
        if line.split(":")[-1].strip()=="hlt":
            hltCount+=1
        if list_1[0]=="var":
            varCount+=1
            if len(list_1)!=2:
                raise SyntaxError(f'Invalid definition of variable {list_1[0]} , at line {count}')
            if count>varCount:
                raise SyntaxError(f"invalid definition of variable {list_1[1]} , at line {count}")
        elif ":" in line:
            if line.split(":")[1].strip()=="":
                raise SyntaxError(f'No argument passed after label , at line {count}')
            if line.split(":")[0].strip() in labels:
                raise SyntaxError(f"invalid definition of label {line.split(':')[0].strip()} , at line {count}")
            if not line.split(":")[0].strip().isalnum():
                raise SyntaxError(f"invalid label name {line.split(':')[0].strip()} , at line {count}")
            labels[line.split(":")[0].strip()] = bin(count-varCount-1)

if hltCount==0:
    raise SyntaxError(f'No halt defined')
if hltCount>1 or infile[-1].split(":")[-1].strip()!="hlt":
    raise SyntaxError(f"invalid definition of halt , at line {count}")

count=0
for line in infile:
    list_1=line.strip().split()
    if line=="":
        continue
    else:
        count+=1
        if list_1[0]=="var":
            if list_1[1] in variables:
                raise SyntaxError(f"Invalid definition of variable {list_1[0]}, at line {count}")
            variables[list_1[1]] = bin(len(infile)-varCount+count-1)

        else:
            if ":" in line and len(line.split(":"))>2:
                raise SyntaxError(f'2 Labels not allowed , at line {count}')

            if ":" in line:
                list_1 = line.split(":")[1].strip().split()

            if list_1[0]=="mov":
                output.append(mov(list_1,register,count)) 
            elif list_1[0] == "hlt":
                output.append("0101000000000000")
            elif list_1[0]== "add":
                output.append(add(list_1,register,count))
            elif list_1[0] == "sub":
                output.append(sub(list_1,register,count))
            elif list_1[0]== "mul":
                output.append(mul(list_1,register,count))
            elif list_1[0] == "div":
                    output.append(div(list_1,register,count))
            elif list_1[0]== "mov":
                output.append(mov(list_1,register,count))
            elif list_1[0]== "and":
                output.append(AND(list_1,register,count))
            elif list_1[0]== "cmp":
                output.append(Compare(list_1,register,count))
            elif list_1[0]== "not":
                output.append( Invert(list_1,register,count))
            elif list_1[0]== "ls":
                output.append(Lshift(list_1,register,count))
            elif list_1[0]== "rs":
                output.append( Rshift(list_1,register,count))
            elif list_1[0]== "or":
                output.append( OR(list_1,register,count))
            elif list_1[0]== "xor":
                output.append(XOR(list_1,register,count))
            elif list_1[0]== "jgt":
                output.append(jgt(list_1, labels,count))
            elif list_1[0]== "ld":
                output.append(ld(list_1, variables,count))
            elif list_1[0]== "st":
                output.append(st(list_1, variables,register,count))
            elif list_1[0]== "jmp":
                output.append(jmp(list_1, labels,count))
            elif list_1[0]== "jlt":
                output.append( jlt(list_1, labels,count))
            elif list_1[0]== "je":
                output.append(je(list_1, labels,count))
            else:
                raise SyntaxError(f"General Syntax Error , at line {count}")

for i in output:
    print(i)
        



#outfile = sys.stdout
 
#sample_input = #output
 
#for ip in sample_input:
    # Prints to stdout
    #outfile.write(ip + '\n')














