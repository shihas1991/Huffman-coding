import sys
def freq(str):
    freqs={}
    for ch in str:
       #print  freqs.get(ch,1)
       freqs[ch]=freqs.get(ch,0) + 1
    return freqs
#print freq(sys.argv[1])
def sortfreq(freqs):
    letters= freqs.keys()
    tuples=[]
    for let in  letters:
           tuples.append((freqs[let],let))
    tuples.sort()
    return tuples
#tuples=sortfreq(freq(sys.argv[1]))
def buildTree(tuples) :
     while len(tuples) > 1 :
         leastTwo = tuple(tuples[0:2])                  # get the 2 to combine 
         theRest  = tuples[2:]                          # all the others
         combFreq = leastTwo[0][0] + leastTwo[1][0]     # the branch points freq
        # print combFreq
         tuples   = theRest + [(combFreq,leastTwo)]
         print tuples      
         tuples.sort()                                  # sort it into place
     return tuples[0] 
#tree=buildTree(tuples)
#print tree
def trimTree(tree):
    p=tree[1]
    if type(p) == type(""):return p
    else:
     return (trimTree(p[0]),trimTree(p[1]))
#node=trimTree(tree)
#print node
codes={} 
def assigncodes(node,ptr=""):
     global codes
     if type(node) == type(""):
         codes[node]=ptr
     else:
      assigncodes(node[0],ptr+"0")
      assigncodes(node[1],ptr+"1")
#assigncodes(node)
#print codes   
def encode(str):
    output=""
    for ch in str:
        output +=codes[ch]
    return output
#print encode(sys.argv[1])
def decode (tree, str) :
     output = ""
     p = tree
     for bit in str :
         if bit == '0' : 
                         p = p[0]     # Head up the left branch
                        # print "left is ",p
         else          : 
                         p = p[1]     # or up the right branch
                        # print "right is ",p
         if type(p) == type("") :     
             output += p              # found a character. Add to output
             p = tree                 # and restart for next character
     return output
def showCodes(str):
   return  encode(str)
def showString(tree,str):
    return decode(tree,str)
#print decode(node,encode(sys.argv[1]))
def main () :
    debug = True
    str = sys.stdin.read()
    freqs = freq(str)
    tuples = sortfreq(freqs)

    tree = buildTree(tuples)
    if debug : print "Built tree", tree

    tree = trimTree(tree)
    if debug : print "Trimmed tree", tree

    assigncodes(tree)
    if debug :print "codes is", showCodes(str)
    
    small=showCodes(str)
    if debug :print "decode is" ,showString(tree,small)
 
    small = encode(str)
    original = decode (tree, small)
    print "Original text length", len(str)
    print "Requires %d bits. (%d bytes)" % (len(small), (len(small)+7)/8)
    print "Restored matches original", str == original
    print "Code for space is ", codes[' ']
    print "Code for letter e ", codes['e']
    print "Code for letter y ", codes['y']
    print "Code for letter z ", codes['z']

if __name__ == "__main__" : main()

