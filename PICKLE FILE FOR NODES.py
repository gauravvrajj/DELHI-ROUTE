import pickle
pickle_in=open("station_map","rb")
example_dict = pickle.load(pickle_in)

print(example_dict)