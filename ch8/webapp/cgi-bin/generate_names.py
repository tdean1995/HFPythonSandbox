
import athletemodel
import json
import yate
def generate_names():
     athletes = athletemodel.get_names_from_store()
     json_athletes = json.dumps(athletes)
     print(yate.start_response('application/json'))
     print(json_athletes)

#if __name__ == '__main__':
print('hello')
	
