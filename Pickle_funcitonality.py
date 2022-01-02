import pickle
Example_list_to_pickle = ["Vamshi","Krishna","Hackerssploit"]
save_file = open("file_to_pickle","wb") # writing into the file in binary
pickle.dump(Example_list_to_pickle,save_file)
save_file.close()
open_file = open("file_to_pickle","rb")
pickled_File =pickle.load(open_file)
print(pickled_File)
