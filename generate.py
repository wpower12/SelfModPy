import pickle
import string, random
import tree_components

NUM_FILES = 5
FILE_DIR  = 'dynamic_files/'
SOURCE_CHARS = "ABCDEFafd123zf"
FN_LENGTH = 8


def generate_file():
	rand_tree = tree_components.get_tree( 3 )
	rand_fn   = get_rand_fn( FN_LENGTH, SOURCE_CHARS )
	pickle.dump( rand_tree, open( FILE_DIR+rand_fn, "wb" ) )

def get_rand_fn( size, chars ):
	str = ''.join(random.choice(chars) for x in range(size))
	return str+".p"

# Main
for i in range(NUM_FILES):
	generate_file()