import copy

# open data file
def openFiledData():
	fname = 'data-1.txt'
	with open(fname) as f:
	    content = f.readlines()

	content = [x.strip() for x in content]
	return content

def openFilePara():
	fname = 'para1-1.txt'
	with open(fname) as f:
		content = f.readlines()

	content = [x.strip() for x in content]
	for line in content:
		#print(str.find("(",0))
		if "(" and ")" in line:
			item=line[line.index("(")+1:line.index(")")]
			value=line[line.index("=")+1:]
			dictRaw[int(item)]=float(value)

# preprocess data format
def preProcessing_data(line):
	tmp = []
	while len(line)!=1:
		test = [ (int(i)) for i in (line[line.find("{")+1:line.find("}")].split(', ')) ]
		line = line[line.find("}")+1:]
		tmp.append(test)
		dataSet.append(test)
	ori_dataSet.append(tmp)


def x_in_y(query, base):
	l = len(query)*[0]
	i = 0
	if len(query) < 1:
		return False
	
	for j in range(len(base)):
		if i >= len(query):
			break
		if i > len(query):
			break
		if query[i] == base[j]:
			l[i] = 1
			i+=1

	return not (0 in l)

def getFirstEle(data):
	return ([ firstEle.append([i])  for i in data if [i] not in firstEle])


def getFirstFeq(firstEle, ori_dataSet, ori_dataSet_len):
	dictionary = dict()
	for key, ele in enumerate(firstEle):
		for data in ori_dataSet:
			# print ele, data
			for sub in data:
				if x_in_y(ele, sub):
					if key not in dictionary:
						dictionary[key] = 1
					else:
						dictionary[key] += 1
					break
	
	F1 = []
	for key , val in dictionary.iteritems():
		if val/float(ori_dataSet_len) >= dictRaw[firstEle[key][0]]:
			F1.append(firstEle[key])

	return F1, dictionary

# only 2 element
def candidateGen(F1, dictionary, dictRaw, ele, ori_dataSet_len):
    c2=[]
    finalc2=[]
   
    for item in range(len(F1)):
    	for tmpitem in range(item+1, len(F1)):
    		if abs(dictionary[item]/float(ori_dataSet_len) - dictionary[tmpitem]/float(ori_dataSet_len)) <= 0.05:
    			c2.append([[F1[item][0], F1[tmpitem][0]]])
    
    for element in c2:
        finalc2.append(element)
        finalc2.append([[element[0][0]],[element[0][1]]])
    # print finalc2
    return finalc2

def findcandiCount(C2, ori_dataSet, dictRaw):
	finaloutput=[]

	for sublst in C2:
		count = 0
		minVal = 1
		for a in sublst:
			for b in a:
				if dictRaw[b] < minVal:
					minVal = dictRaw[b]


		for sequence in ori_dataSet:
			flag = False
			
			# if len(sublst) == 1:
			# 	for subseq in sequence:
			# 		for i in sublst:
			# 			if x_in_y(i, subseq):
			# 				flag = True
			# 				count+=1
			# 				break

			# 		if flag:
			# 			break
			# else:
			i = 0
			l = len(sublst)*[0]
			for subseq in sequence:
				if i >= len(sublst):
					break
				if x_in_y(sublst[i], subseq):
					l[i] = 1
					i+=1
			if not (0 in l):
				count += 1

		# print count/float(len(ori_dataSet)), minVal
		if count/float(len(ori_dataSet)) > minVal:
			finaloutput.append(sublst)
		# print sublst, count, minVal
	return finaloutput

def pophead(item):
	tmp = copy.deepcopy(item)
	if len(tmp[0]) == 1:
		tmp.pop(0)
	else:
		tmp[0].pop(0)
	return tmp

def poptail(item):
	tmp = copy.deepcopy(item)
	# print len(tmp[len(tmp)-1])
	if len(tmp[len(tmp)-1]) == 1:
		tmp.pop()
	else:
		tmp[len(tmp)-1].pop()
	return tmp


def joinCandidate(F):
	candidate = list()
	for i in range(len(F)):
		for j in range(len(F)):

			a = copy.deepcopy(F[i])
			b = copy.deepcopy(F[j])
			# print a, b
			
			# pophead(a)
			# poptail(b)
			if pophead(a) == poptail(b):
				# print "1"
				# print a
				# print "2"
				# print b
				if len(b[-1]) > 1:
					# print b[-1]
					
					if len(a) == 1:
						a[0].pop()
					else:
						a.pop()
				a.append(b[-1])
				
					# a.append(b[-1])

				if a not in candidate:
					# print "3"
					candidate.append(a)

	return candidate
# joinCandidate([[[1],[2],[3]],[[1],[2,5]],[[1],[5],[3]],[[2],[3],[4]],[[2,5],[3]],[[3],[4],[5]],[[5],[3,4]]])

if __name__ == "__main__":
	
	content = openFiledData()

	dictRaw = dict()
	mis = openFilePara()
	# print dictRaw


	dataSet = list()
	ori_dataSet = list()
	result = map(preProcessing_data, content)

	firstEle = list()
	result = map(getFirstEle, dataSet)
	firstEle.sort()

	F1, dictionary = getFirstFeq(firstEle, ori_dataSet, len(ori_dataSet) )
	# print F1


	C2 = candidateGen(F1, dictionary, dictRaw, firstEle, len(ori_dataSet))
	final = findcandiCount(C2, ori_dataSet, dictRaw)
	# print final
	joinCandidate(final)
