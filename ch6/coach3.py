class AthleteList(list):
	def __init__(self,a_name,a_dob = None, a_times = []):
		list.__init__([])
		self.name = a_name
		self.dob = a_dob
		self.extend(a_times)
	def top3(self):
		return sorted(set([sanitize(t) for t in self]))[0:3]
	def add_time(self,time):
		self.append(time)
	def add_times(self,list_of_times):
		self.extend(list_of_times)

def get_coach_data(filename):
	try:
		with open(filename) as f:
			data = f.readline()
			data = data.strip().split(',')
			name = data.pop(0)
			dob = data.pop(0)
			times = data
			athlete = AthleteList(name,dob,times)
		return athlete
		
	except IOError as ioerr:
		print('File error: ' + str(ioerr))
		return(None)

def sanitize(time_string):
	if '-' in time_string:
		splitter = '-'
	elif ':' in time_string:
		splitter = ':'
	else:
		return(time_string)
	(mins,secs) = time_string.split(splitter)
	return (mins + '.' + secs)

files = ['james2.txt','julie2.txt','mikey2.txt','sarah2.txt']

athletes = []
for file in files:
	athletes.append(get_coach_data(file))

for athlete in athletes:
	print (athlete.name + "'s fastest times are: " + str(athlete.top3()))

vera = AthleteList('Vera Vi')
vera.add_time('1.31')
print(vera.top3())
vera.add_times(['2.22','1-21','2:22'])
print(vera.top3())