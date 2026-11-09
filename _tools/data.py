SERVICES = [
    # slug, short name, malayalam name, book anchor, one-line english summary
    ("electrician", "Electrician", "ഇലക്ട്രീഷ്യൻ", "electrical", "Fans, switches, lights and wiring faults"),
    ("plumber", "Plumber", "പ്ലംബർ", "plumbing", "Leaking taps, blocked drains, pipe and motor work"),
    ("carpenter", "Carpenter", "ആശാരി (കാർപെന്റർ)", "carpentry", "Doors, locks, hinges, shelves and furniture repair"),
    ("tile-work", "Tile Work", "ടൈൽ വർക്ക്", "tile", "Broken tile replacement, regrouting and new tiling"),
    ("painter", "Painter", "പെയിന്റർ", "painting", "Room painting, touch ups and damp patch work"),
    ("welding-work", "Welding Work", "വെൽഡിംഗ് വർക്ക്", "welding", "Gate, grill and railing repair"),
    ("gypsum-false-ceiling", "Gypsum False Ceiling", "ജിപ്സം ഫോൾസ് സീലിംഗ്", "gypsum", "False ceiling work and repairs"),
    ("masonry-work", "Masonry Work", "മേസൺ വർക്ക് (കല്ലുപണി)", "masonry", "Small wall, plaster and patch work"),
    ("water-tank-cleaning", "Water Tank and Well Cleaning", "വാട്ടർ ടാങ്ക്, കിണർ ക്ലീനിംഗ്", "interlock", "Overhead tank, sump and well cleaning"),
    ("appliance-repair", "AC, Fridge, TV and Washing Machine Repair", "എസി, ഫ്രിഡ്ജ്, ടിവി, വാഷിംഗ് മെഷീൻ റിപ്പയർ", "appliance", "AC service, fridge, TV and washing machine repair"),
    ("handyman", "Handyman", "ഹാൻഡിമാൻ", "handyman", "Small fixes and fittings around the house"),
    ("cctv-installation", "CCTV Camera Installation", "സിസിടിവി ക്യാമറ ഇൻസ്റ്റലേഷൻ", "cctv", "Camera fitting, setup and repair"),
    ("furniture-assembly", "Furniture Assembly", "ഫർണിച്ചർ അസംബ്ലി", "furniture", "Beds, wardrobes, tables and flat pack furniture"),
    ("mosquito-net", "Mosquito Net Installation", "കൊതുകുവല ഫിറ്റിംഗ്", "mosquito", "Window and door mosquito nets"),
    ("sofa-cleaning", "Sofa and Carpet Cleaning", "സോഫ, കാർപെറ്റ് ക്ലീനിംഗ്", "sofa", "Sofa, carpet and mattress cleaning"),
    ("home-deep-cleaning", "Home Deep Cleaning", "ഹോം ഡീപ് ക്ലീനിംഗ്", "cleaning", "Full house, kitchen and bathroom deep cleaning"),
    ("pest-control", "Pest Control", "പെസ്റ്റ് കൺട്രോൾ", "pest", "Cockroach, ant, termite and mosquito treatment"),
]

# slug, english, malayalam
AREAS = [
    ("varapuzha", "Varapuzha", "വരാപ്പുഴ"),
    ("kottuvally", "Kottuvally", "കോട്ടുവള്ളി"),
    ("chittattukara", "Chittattukara", "ചിറ്റാറ്റുകര"),
    ("vadakkekara", "Vadakkekara", "വടക്കേക്കര"),
    ("kedamangalam", "Kedamangalam", "കെടാമംഗലം"),
    ("chendamangalam", "Chendamangalam", "ചേന്ദമംഗലം"),
    ("moothakunnam", "Moothakunnam", "മൂത്തകുന്നം"),
    ("manjali", "Manjali", "മാഞ്ഞാലി"),
    ("ezhikkara", "Ezhikkara", "ഏഴിക്കര"),
    ("alangad", "Alangad", "ആലങ്ങാട്"),
    ("aluva", "Aluva", "ആലുവ"),
]

ML_AREAS = "നോർത്ത് പറവൂർ, വരാപ്പുഴ, കോട്ടുവള്ളി, ചിറ്റാറ്റുകര, വടക്കേക്കര, കെടാമംഗലം, ചേന്ദമംഗലം, മൂത്തകുന്നം, മാഞ്ഞാലി, ഏഴിക്കര, ആലങ്ങാട്, ആലുവ"

# Popular services shown first on area pages (rotated per area for variety)
TOP = ["electrician", "plumber", "appliance-repair", "handyman", "water-tank-cleaning", "cctv-installation"]

# Short, true, non-specific intro variants. {a}=area
INTROS = [
    "Looking for a reliable electrician, plumber or AC technician in {a}? FixMate Kerala sends trained workers to homes in {a} and agrees the price with you before any work starts.",
    "From a leaking tap to a fan that will not start, FixMate Kerala handles everyday home repairs for families in {a}, with clear prices shown before you book.",
    "Homes in {a} can book electricians, plumbers, carpenters, cleaners and more through FixMate Kerala. One booking, one visit, and the price is agreed up front.",
]
INTROS2 = [
    "Book online in two minutes, or call or WhatsApp us and we will confirm a visit time that suits you.",
    "Send a photo of the problem on WhatsApp and we will tell you which job to book and what it is likely to cost.",
    "We are a North Paravur based team, so {a} is part of our regular service area.",
]
