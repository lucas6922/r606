nbfiles = 5
lastctx = ""     # The last context submitted to the generator
lastact = ""     # The last action received from the user
genamt = 80     # Amount of text for each action to generate
generated_tkns = 0 # If using a backend that supports Lua generation modifiers, how many tokens have already been generated, otherwise 0
spfilename = ""     # Filename of soft prompt to load, or an empty string if not using a soft prompt
editln = 0      # Which line was last selected in Edit Mode
sp  = None   # Current soft prompt tensor (as a NumPy array)
sp_length = 0      # Length of current soft prompt in tokens, or 0 if not using a soft prompt

class colors:
    PURPLE    = '\033[95m'
    BLUE      = '\033[94m'
    CYAN      = '\033[96m'
    GREEN     = '\033[92m'
    YELLOW    = '\033[93m'
    RED       = '\033[91m'
    END       = '\033[0m'
    UNDERLINE = '\033[4m'


