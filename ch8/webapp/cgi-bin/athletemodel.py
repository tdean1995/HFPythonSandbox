import pickle
from athletelist import AthleteList

files = ['james2.txt','julie2.txt','mikey2.txt','sarah2.txt']
pickle_file = 'athletes.pickle'

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
        print('File error(get_coach_data): ' + str(ioerr))
        return(None)

def put_to_store(files_list):
    all_athletes = {}
    for file in files_list:
        ath  = get_coach_data(file)
        all_athletes[ath.name] = ath
        with open(pickle_file,'wb') as athlete_data:
            pickle.dump(all_athletes,athlete_data)
    return all_athletes   

def get_names_from_store():
    all_athletes = get_from_store()
    response = [all_athletes[each_ath].name for each_ath in all_athletes]
    return response	 

def get_from_store():
    try:                        
        with open(pickle_file,'rb') as athlete_data:
            all_athletes = pickle.load(athlete_data)
        return all_athletes
    except IOError as ioerr:
        print('File error (get_from_store): ' + str(ioerr))
        return None



