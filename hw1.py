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
    try:
        l = len(query)
    except TypeError:
        l = 1
        query = type(base)((query,))

    for i in range(len(base)):
        if base[i:i+l] == query:
            return True
    return False

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
	return F1



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

	result = getFirstFeq(firstEle, ori_dataSet, len(ori_dataSet) )
	print result



