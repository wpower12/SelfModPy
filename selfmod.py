import pickle, os, random
import tree_components

FILE_DIR   = 'dynamic_files/'
LOOP_COUNT = 5

files = os.listdir( FILE_DIR ) 

for i in range(LOOP_COUNT):
	fn   = random.choice( files )
	prog = pickle.load( open(FILE_DIR+fn, "rb") )
	old_res = prog.eval()
	tree_components.modify( prog )
	new_res = prog.eval()
	print( '{} old: {} new: {}'.format( fn, str(old_res), str(new_res) ) )