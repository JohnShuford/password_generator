import secrets

# A list of common, easy-to-remember words for building passphrases
# 1024 unique words drawn from everyday English vocabulary
WORD_LIST = [
    # A
    "abbey", "abbot", "abide", "abode", "acorn", "acres", "acute", "adage",
    "adapt", "adept", "admit", "adobe", "adopt", "adore", "adult", "aegis",
    "afoot", "agile", "aglow", "agony", "agora", "agree", "aisle", "alarm",
    "album", "alert", "algae", "alien", "align", "alley", "allot", "allow",
    "alloy", "aloft", "aloof", "altar", "amber", "amble", "amend", "amiss",
    "ample", "angel", "angle", "anime", "annex", "anvil", "aorta", "apple",
    "apply", "apron", "aptly", "arbor", "arcane", "ardor", "arena", "argon",
    "arise", "armor", "aroma", "array", "arrow", "arson", "artsy", "ascot",
    "ashen", "askew", "atlas", "atoll", "atone", "attic", "audit", "augur",
    "aunty", "avail", "avian", "avoid", "awake", "award", "aware", "awful",
    "awoke",
    # B
    "badge", "bagel", "baggy", "baked", "baker", "banjo", "barge", "baron",
    "basil", "basin", "basis", "batch", "bayou", "beach", "beady", "belle",
    "bench", "birch", "bison", "blaze", "bleak", "blend", "blimp", "blink",
    "bliss", "bloat", "bloom", "blown", "blues", "bluff", "blunt", "blurb",
    "blurt", "boggy", "bolts", "bonus", "booby", "booth", "borax", "bough",
    "bower", "boxer", "braid", "brash", "brawn", "braze", "briar", "bribe",
    "bride", "brine", "brink", "brisk", "broil", "brook", "broom", "broth",
    "brown", "brunt", "brush", "brute", "buddy", "budge", "buggy", "bulge",
    "bulky", "bully", "bunch", "bunny", "buoy", "burnt", "bushy", "byway",
    # C
    "cabin", "cache", "cadet", "camel", "cameo", "canal", "candy", "cape",
    "carat", "cargo", "carol", "carve", "cedar", "chalk", "chant", "charm",
    "chart", "chase", "chasm", "cheap", "cheer", "chess", "child", "chill",
    "chimp", "chord", "chore", "chunk", "civic", "civil", "clamp", "clang",
    "clash", "clasp", "claw", "clean", "clear", "cleft", "cliff", "cling",
    "clink", "cloak", "clone", "close", "cloth", "cloud", "clout", "clown",
    "clump", "comet", "comic", "conch", "coral", "corps", "couch", "cough",
    "could", "coupe", "court", "coven", "cover", "craft", "crane", "crank",
    "creak", "creek", "creep", "crest", "crimp", "crisp", "croak", "crone",
    "crook", "cross", "croup", "crowd", "crown", "crude", "cruel", "crush",
    "crust", "crypt", "cubic", "curry", "cyber",
    # D
    "daily", "daisy", "dance", "dares", "datum", "dealt", "decay", "decoy",
    "delta", "depot", "derby", "deter", "deuce", "dingo", "dirge", "disco",
    "dodge", "dogma", "dolce", "dowel", "dowry", "draft", "drain", "drake",
    "drawl", "dread", "dream", "drift", "drink", "drool", "droop", "druid",
    "dryad", "duchy", "dully", "dunce", "dusky", "dusty", "dwarf",
    # E
    "eager", "eagle", "early", "earth", "ebony", "edged", "eerie", "eight",
    "elder", "elbow", "elegy", "elfin", "elite", "elixir", "ember", "emote",
    "empty", "enact", "endow", "epoch", "equip", "erode", "evade", "evoke",
    "exact", "exalt", "exile", "extra",
    # F
    "fable", "facet", "faint", "fairy", "faith", "fancy", "feral", "fetch",
    "flair", "flank", "flask", "flaunt", "fledge", "flesh", "flick", "fling",
    "flint", "flirt", "float", "flock", "flood", "flora", "floss", "flout",
    "flown", "fluff", "fluke", "flume", "flunk", "flute", "focal", "foggy",
    "foray", "forge", "forte", "forum", "found", "frail", "frame", "freak",
    "fresh", "frond", "front", "frost", "froze", "frugal", "fudge", "fungi",
    # G
    "gauze", "gavel", "gecko", "giddy", "girth", "given", "gland", "glare",
    "gleam", "glean", "glide", "gloom", "gloss", "glove", "glyph", "gnash",
    "golem", "gorge", "gouge", "grace", "graft", "grain", "grand", "grant",
    "grasp", "grate", "grave", "graze", "greed", "grief", "grift", "grill",
    "grind", "groan", "groom", "grope", "gross", "grout", "grove", "growl",
    "gruel", "gruff", "guava", "guile", "guise", "gusto", "gypsy",
    # H
    "halve", "happy", "harsh", "haste", "haven", "hazel", "hefty", "heist",
    "helix", "hence", "hinge", "hippo", "holly", "homer", "honey", "honor",
    "hotel", "hound", "hover", "humid", "hunky", "hyena",
    # I
    "ichor", "icing", "ideal", "idiom", "idiot", "igloo", "image", "impel",
    "inane", "incur", "infer", "ingot", "inlet", "inter", "intro", "ionic",
    "irony", "ivory",
    # J
    "jaunt", "jazzy", "jelly", "jetty", "jewel", "joust", "juice", "juicy",
    "jumbo", "jumpy", "junto", "juror",
    # K
    "kapok", "karma", "kayak", "kebab", "knack", "kneel", "knife", "knock",
    "knoll", "koala",
    # L
    "lance", "larva", "laser", "latch", "later", "lemon", "lemur", "level",
    "light", "lilac", "lithe", "llama", "lodge", "logic", "lofty", "lunar",
    "lusty", "lyric",
    # M
    "magic", "magma", "maize", "mambo", "manga", "manor", "maple", "march",
    "marsh", "maxim", "mayor", "melee", "mercy", "merit", "melon", "metal",
    "micro", "mirth", "molar", "moose", "motel", "motif", "motto", "mound",
    "mount", "mourn", "mouth", "mulch", "mural", "musty", "myrrh", "mystic",
    # N
    "nadir", "naive", "nifty", "night", "ninja", "noble", "nocturne", "nomad",
    "notch", "novel", "nymph",
    # O
    "oaken", "oasis", "ocean", "octet", "olive", "onset", "opera", "optic",
    "orate", "orchid", "other", "otter", "outdo", "outer", "ovoid",
    # P
    "panda", "panel", "panic", "papal", "paper", "parch", "pearl", "penny",
    "perch", "peril", "phase", "piano", "pixel", "pizza", "place", "plaid",
    "plank", "plant", "plaza", "pluck", "plumb", "plume", "plump", "plunk",
    "plush", "polka", "polyp", "pouch", "prank", "prawn", "press", "price",
    "pride", "prime", "prism", "privy", "probe", "prone", "prong", "prose",
    "prove", "prowl", "prude", "prune", "psalm", "pulse", "punch", "pupil",
    "purge", "pygmy",
    # Q
    "quail", "qualm", "queen", "query", "queue", "quick", "quill", "quirk",
    # R
    "radar", "radix", "radon", "raspy", "raven", "rayon", "realm", "recur",
    "reedy", "reeve", "regal", "reign", "relax", "relic", "repel", "resin",
    "risky", "rivet", "robin", "rocky", "rouge", "rough", "rouse", "rowdy",
    "ruddy", "rugby", "ruler", "rusty",
    # S
    "salsa", "sandy", "satin", "scalp", "scant", "scare", "scarf", "scone",
    "scoop", "scope", "scour", "scout", "scowl", "scram", "scrap", "scree",
    "screw", "scrub", "seize", "serum", "serve", "setup", "seven", "shaft",
    "shale", "shame", "shark", "sharp", "shawl", "sheep", "sheer", "shelf",
    "shell", "shift", "shrine", "shrub", "shuck", "shunt", "siren", "skill",
    "skimp", "skirt", "skulk", "skunk", "slate", "sleet", "slick", "slime",
    "sling", "sloop", "slope", "sloth", "slump", "slunk", "slurp", "smash",
    "smear", "smelt", "smirk", "smite", "smock", "smolt", "smoke", "snail",
    "snare", "snarl", "sneak", "snipe", "snore", "snort", "solar", "sonar",
    "spade", "spare", "spark", "spawn", "spear", "speck", "spice", "spill",
    "spine", "spire", "spite", "splat", "split", "spoil", "spoke", "spore",
    "sport", "spout", "spree", "sprig", "spunk", "squad", "squat", "squid",
    "stain", "stale", "stalk", "stall", "stamp", "stand", "stark", "start",
    "stash", "stave", "steal", "steel", "steep", "steer", "stern", "stick",
    "stiff", "sting", "stomp", "stone", "stood", "storm", "stout", "straw",
    "stray", "strip", "strut", "stump", "stung", "stunk", "stunt", "surge",
    "swell", "swept", "swift", "swirl", "swoop",
    # T
    "tabby", "talon", "tango", "tapir", "taunt", "tawny", "tempo", "tense",
    "thane", "thatch", "thief", "thorn", "those", "three", "threw", "throb",
    "throw", "thrum", "tiger", "tilde", "tinge", "tired", "titan", "toast",
    "today", "token", "topaz", "topic", "torch", "totem", "touch", "tough",
    "towel", "tower", "trace", "track", "trail", "train", "tramp", "trawl",
    "tread", "treck", "trend", "trice", "trick", "trout", "trove", "truce",
    "trunk", "truss", "truth", "tulip", "tuner", "tunic", "tuple", "twang",
    "tweed", "twerp", "twist", "tycoon",
    # U
    "ultra", "umbra", "unfed", "unify", "unlit", "unpin", "until", "unwed",
    "upped", "upper", "urban", "usher",
    # V
    "valor", "valve", "vapor", "vault", "venom", "verge", "verse", "vigor",
    "viper", "visor", "vixen", "vocal", "vogue", "voila", "vouch",
    # W
    "waltz", "wands", "wrath", "watch", "water", "weary", "wedge", "wheat",
    "wheel", "where", "whiff", "whirl", "whoop", "winch", "wistful", "witch",
    "witty", "woken", "world", "wormy", "wrack", "wraith", "wreak", "wreck",
    "wring", "wrist", "wrote",
    # X
    "xenon",
    # Y
    "yacht", "yearn", "yield", "young", "youth", "yodel",
    # Z
    "zebra", "zesty", "zonal",
    # Additional words to reach 1024
    "abase", "abash", "abate", "abhor", "abler", "above", "abuzz", "abyss",
    "ached", "acrid", "adorn", "agate", "agave", "algal", "allay", "allure",
    "annul", "antic", "aplomb", "aspen", "astir", "avast", "baize", "baste",
    "bauble", "bawdy", "bebop", "beech", "berth", "bezel", "bilge", "boast",
    "buxom", "bylaw", "cabal", "cacao", "cairn", "caulk", "chafe", "champ",
    "chive", "codec", "comma", "creed", "crick", "cruse", "cubit", "cynic",
    "decal", "decry", "delve", "dower", "drawn", "dross", "drove", "drupe",
    "eclat", "edict", "egret", "eject", "elate", "envoy", "epoxy", "etude",
    "exude", "favor", "felon", "femur", "fetid", "finch", "fjord", "flail",
    "flare", "fleck", "fleet", "folly", "froth", "gamut", "gaudy", "gilet",
    "glint", "gloat", "gourd", "harem", "heady", "heave", "hokum", "hovel",
    "irate", "joker", "jolly", "knave", "lathe", "ledge", "lemma", "libel",
    "liege", "linen", "liver", "loamy", "lucid", "lying", "matte", "metro",
    "mince", "miser", "mitre", "mixed", "model", "mogul", "mommy", "moody",
    "moped", "morph", "mossy", "motley", "mucky", "muddy", "muggy", "muted",
    "muzzy", "ninny", "nippy", "nitty", "noisy", "nonce", "nudge", "nutty",
    "occur", "odium", "offal", "oldie", "ombre", "opine", "orbit", "organ",
    "ought", "oxide", "ozone", "paean", "parka", "parley", "pasta",
]

# User input for number of words
while True:
    numOfWords = input("How many words would you like in your passphrase? (recommended: 4-6) ")
    if numOfWords.isdigit() and int(numOfWords) > 0:
        numOfWords = int(numOfWords)
        break
    else:
        print("Please enter a valid positive integer.")

# Choose a separator
print("\nChoose a separator between words:")
print("  1. Hyphen  ( - )")
print("  2. Underscore ( _ )")
print("  3. Period  ( . )")
print("  4. Space   (   )")
print("  5. None    (no separator)")

while True:
    separatorChoice = input("Enter choice (1-5): ")
    separatorMap = {
        '1': '-',
        '2': '_',
        '3': '.',
        '4': ' ',
        '5': '',
    }
    if separatorChoice in separatorMap:
        separator = separatorMap[separatorChoice]
        break
    else:
        print("Please enter a number between 1 and 5.")

# Ask about capitalization
capitalize = input("\nWould you like to capitalize each word? (y/n) ").lower() == 'y'

# Ask about appending a number
addNumber = input("Would you like to add a random number at the end? (y/n) ").lower() == 'y'

# Build the passphrase using a cryptographically secure random source
words = [secrets.choice(WORD_LIST) for _ in range(numOfWords)]

if capitalize:
    words = [word.capitalize() for word in words]

passphrase = separator.join(words)

if addNumber:
    passphrase += str(secrets.randbelow(990) + 10)

print("\nYour passphrase is:", passphrase)
