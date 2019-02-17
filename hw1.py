import copy

# open data file
SDC=0.05
def openFiledData():
	fname = 'data-2.txt'
	with open(fname) as f:
	    content = f.readlines()

	content = [x.strip() for x in content]
	return content

def openFilePara():
	fname = 'para1-2.txt'
	with open(fname) as f:
		content = f.readlines()

	content = [x.strip() for x in content]
	for line in content:
		#print(str.find("(",0))
		if "(" and ")" in line:
			item=line[line.index("(")+1:line.index(")")]
			value=line[line.index("=")+1:]
			dictRaw[int(item)]=float(value)
		else: 
			global SDC
			SDC=float(line[line.index("=")+1:])
			# print SDC
# preprocess data format
def preProcessing_data(line):
	tmp = []
	while len(line)!=1:
		test = [ (int(i)) for i in (line[line.find("{")+1:line.find("}")].split(', ')) ]
		line = line[line.find("}")+1:]
		test.sort()
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
def candidateGen(F1, dictionary, dictRaw, ele, ori_dataSet_len, SDC):
    c2=[]
    finalc2=[]
    # print SDC
    for item in range(len(F1)):
    	if dictionary[item]/float(ori_dataSet_len) >= dictRaw[ F1[item][0]]:
    		for tmpitem in range(len(F1)):
    			
    		# 	print abs(dictionary[item]/float(ori_dataSet_len) - dictionary[tmpitem]/float(ori_dataSet_len))
    		# if item!=tmpitem:
    		
	    		# if (dictionary[tmpitem]/float(ori_dataSet_len) >= dictRaw[ F1[item][0]]) and abs(dictionary[item]/float(ori_dataSet_len) - dictionary[tmpitem]/float(ori_dataSet_len)) <= SDC:
	    		# 	c2.append([[F1[item][0], F1[tmpitem][0]]])
	    		if (dictionary[tmpitem]/float(ori_dataSet_len) >= dictRaw[ F1[tmpitem][0]]):
	    			# if F1[tmpitem] == [90]:
    				# 	print F1[item], F1[tmpitem]
	    			c2.append([[F1[item][0], F1[tmpitem][0]]])
	    
    # print c2
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
		temp_count=0
		# print count/float(len(ori_dataSet)), minVal
		# print sublst, count
		# print sublst

		if count/float(len(ori_dataSet)) > minVal:
			out = "<"
			finaloutput.append(sublst)
			for lst in sublst:
				# print lst
				# for a in lst:
				# 	print a
				out_data = ', '.join(str(x) for x in lst)
				# print out_data
				out += "{" + out_data + "}"
			out += ">"
				# print lst
			print "%s     count: %d" % (out, count)
			# temp_count+=1
			# print sublst, count
	# print temp_count
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
			# print F[i], F[j]

			a = copy.deepcopy(F[i])
			b = copy.deepcopy(F[j])
			
			# print a, b
			tmp = []
			# if len(F[j][-1]) > 1:

			# 	test1 = pophead(a)
			# 	for index in range(len(F[j][-1])):
			# 		test2 = copy.deepcopy(b)
			# 		popitem = test2[-1].pop(index)
					
			# 		# 
			# 		if test1 == test2:
			

			# 			if len(a[0]) > 1:
			# 				test1[0].insert(0, a[0][0])
			# 			else:
			# 				test1.insert(0, [a[0][0]])

						
			# 			test1[-1].insert(index,popitem)
						
			# 			print test1
			# 			if test1 not in candidate:
			# 				# print "3"
			# 				candidate.append(test1)
			# 				# print test1

			# if len(F[i][0]) > 1:
			# 	print a, b

			# 	test2 = poptail(b)
			# 	for index in range(len(F[i][0])):
			# 		test1 = copy.deepcopy(a)
			# 		popitem = test1[0].pop(index)
					
			# 		# 
			# 		if test1 == test2:

			# 			test1[0].insert(index, popitem)
						
			# 			if len(b[-1]) > 1:
			# 				test1[-1].append(b[-1][-1])
			# 			else:
			# 				test1.append([b[-1][-1]])

			# 			print test1
			# 			print ""
			# 			if test1 not in candidate:
			# 				# print "3"
			# 				candidate.append(test1)

			# else:
			test1 = pophead(a)
			test2 = poptail(b)
			
			# print test1
			
			if test1 == test2:
				# print a, b
				# print test1, test2

				if len(a[0]) > 1:
					test1[0].insert(0, a[0][0])
				else:
					test1.insert(0, [a[0][0]])

				if len(b[-1]) > 1:
					test1[-1].append(b[-1][-1])
				else:
					test1.append([b[-1][-1]])

				if test1 not in candidate:
					candidate.append(test1)
					# print test1



	return candidate


def pruningCandidate(L, F):
	# print F
	can = list()
	for line in L:
		# print line
		
		flag = True

		for i in range(len(line)):
			tmp = copy.deepcopy(line)
			if len(tmp[i]) > 1:
				for j in range(len(tmp[i])):
					test = copy.deepcopy(tmp)
					test[i].pop(j)
					# print j
					# print test
					if test not in F:
						flag = False
			else:
				tmp.pop(i)
				test = tmp
				# print test
				if test not in F:
					flag = False
		# print flag

		if flag == True:
			can.append(line)
	return can


# F3 = [[[1],[2],[3]],[[1],[2,5]],[[1],[5],[3]],[[2],[3],[4]],[[2,5],[3]],[[3],[4],[5]],[[5],[3,4]]]
# test = [[[1,2],[4]], [[1,2],[5]], [[1],[4,5]], [[1,4],[6]], [[2],[4,5]], [[2],[4],[6]]]
# F3 = [[[1],[2]],[[1, 2]]]
# L = joinCandidate(F3)
# print L
# print aaa

# pruningCandidate(L, F3)

# L = joinCandidate(test)
# pruningCandidate(L, test)

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
	for i in dictionary:
		print "<{%d}>     count: %d" % (F1[i][0], dictionary[i])



	C2 = candidateGen(F1, dictionary, dictRaw, firstEle, len(ori_dataSet), SDC)

	
	final = findcandiCount(C2, ori_dataSet, dictRaw)
	print len(final)
	
	while(len(final)!=0):
	# print final
		print "=============="
		Fk = joinCandidate(final)
		print len(Fk)


		Ck = pruningCandidate(Fk, final)
		print len(Ck)

		if [[6],[1],[13]] in Ck:
			print "HIII"
			break

		final = findcandiCount(Ck, ori_dataSet, dictRaw)
		print len(final)
	

