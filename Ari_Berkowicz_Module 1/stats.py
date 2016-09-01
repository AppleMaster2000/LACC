def mean(list):
	sum = 0
	for x in list:
		sum = sum + x
	sum = sum / len(list)
	return sum
    
def median(list):
    list = sorted(list)
    if(len(list) % 2 == 0):
        s = (list[len(list)/2]+list[len(list)/2 + 1]/2)
    if(len(list) % 2 == 1):
        s = (list[len(list)/2])
    return s
def mode(a):
    l = len(a)
    dict = {};
    for x in range(0,l):
        keys = dict.keys()
        if a[x] in keys:
            dict[a[x]] += 1
        else:
            dict[a[x]] = 1
        largest = max(dict, key=dict.get)
    return largest
