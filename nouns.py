# Here we have a classifcation of nouns for use in doing things
inanimate = [
    "chair",
    "flower",
    "movie",
    "postal stamps",
    "kimono; Japanese traditional dress",
    "guitar",
    "ticket",
    "bamboo hat",
    "toy",
    "souvenir",
    "camera",
    "DVD",
    "CD",
    "baggage",
    "desk",
    "coupons",
    "chopsticks",
    "personal computer",
]

subjects = [
    "literature",
    "politics",
]

practice_able = [
    "piano",
]

study_able = subjects + [
    "grammar",
    "word; vocabulary",
    "kanji; Chinese character",
]

animals = [
    "dog",
    "cow",
    "cat",
]

people = [
    "college student",
    "child",
    "grandfather; old man",
    "grandmother; old woman",
    "man",
    "woman",
    "boy",
    "girl",
]

personal_people = [
    "brothers and sisters",
    "younger sister",
    "younger brother",
    "older brother",
    "older sister",
    "(my) older sister",
    "(my) father",
    "(my) mother",
    "boyfriend",
    "girlfriend",
    "roommate",
    # "daughter",
    # "family",
]

animate = (
    animals
    + personal_people
    + [
        "good child",
        # "doctor",
        # "you",
        # "God",
        # "adult",
        "man",
        "woman",
        "guardian deity of children",
    ]
)


wear_able = [
    "kimono; Japanese traditional dress",
    "bamboo hat",
    "clothes",
    "glasses",
    "gloves",
    "pants",
    "shirt",
]

become_able = [
    "rich person",
    "celebrity",
    "actress",
    "orthopedic surgeon",
    "cartoonist",
    "firefighter",
    "otorhinolaryngologist; ENT doctor",
    "chef",
    "dentist",
    "dermatologist",
    "police officer",
    "actor; actress",
    "surgeon",
    "singer",
    "college student",
    "physician",
    "doctor",
    "baseball player",
    "ophthalmologist",
    "nurse",
    "writer",
    "office worker",
    "astronaut",
    "obstetrician and gynecologist",
    "journalist",
    "president of a company",
    "president of a country",
]

do_able = [
    "good deed",
    "business to take care of",
    "homestay; living with a local family",
    "fishing",
    "homework",
    "camp",
    "game",
    "outdoor activities",
    "part-time job",
    "exercise",
    "cooking; dish",
    "travel",
    "barbecue",
    "surfing",
    "ski",
    "present",
    "date (romantic, not calendar)",
    "drive",
    "baseball",
    "shopping",
    "questionnaire",
    "karaoke",
    "tennis",
    "soccer",
]

make_able = [
    "questionnaire",
    "bamboo hat",
]

write_able = [
    "song",
    "e-mail",
    "essay; composition",
    "letter",
    "postcard",
]

see_able = [
    "TV",
    "movie",
    "Kabuki; traditional Japanese theatrical art",
    "picture; photograph",
]

read_able = [
    "magazine",
    "kanji; Chinese character",
    "textbook",
]

means_of_transport = [
    "train",
    "airplane",
    "ship; boat",
    "bus",
    "car",
    "Shinkansen; “Bullet Train”",
]

hear_able = [
    "music",
    "voice",
    "CD",
]

drink_able = [
    "green tea",
    "wine",
    "drink",
    "water",
    "milk",
    "sake; alcohol",
    "beer",
    "coffee",
    "juice",
    "medicine",
]

eat_able = [
    "snack; sweets",
    "bread",
    "food",
    "hamburger",
    "sushi",
    "cake",
    "pizza",
    "sweet bun",
    "tempura",
    "apple",
    "tomato",
    "ice cream",
    "breakfast",
    "lunch",
    "dinner",
    "rice cake",
    "boxed lunch",
    "rice; meal",
]

buy_able = drink_able + eat_able + inanimate

body_parts = [
    "head",
    "hair",
    "ear",
    "throat",
    "neck",
    "eye",
    "nose",
    "back (body)",
    "mouth",
    "tooth",
    "finger",
    # "breast", # hmmmmmmmmm
    "shoulder",
    "hand; arm",
    "leg; foot",
    "face",
    "stomach",
    "buttocks",
]

colors = [
    "purple",
    "green",
    "pink",
    "gray",
    "light blue",
    "silver",
    "gold",
]

weather = [
    "rain",
    "sunny weather",
    "snow",
    "cloudy weather",
]

places_relative = [
    "back",
    "left",
    "left side",
    "right",
    "right side",
    "inside",
    "between",
    "front",
    "on",
    "under",
    "near; nearby",
]

places_abstract = [
    "class",
    "party",
    "concert",
]

directions = [
    "north",
    "south",
    "west",
    "east",
]

# Sub-places within a place
sub_places = [
    "restroom",
    "exit",
    "entrance",
    "gate",
    "corner",
    # "platform",
    "door",
    "cafeteria; dining commons",
    "stairs",
]

frequency = [
    "every week",
    "every day",
    "every night",
]

personal_places = [
    "home; house; my place",
    "home; house",
    "country; place of origin",
    "room",
    "apartment",
    "neighborhood",
    "dormitory",
]

places_absolute = [
    "town; city",
    # "farm",
    "school",
    "bookstore",
    "department store",
    "supermarket",
    "hospital",
    "municipal hospital",
    "temple",
    "shrine",
    "castle",
    "art museum",
    "hotel",
    "shop; store",
    "shop; stand",
    "mountain",
    "park",
    "lake",
    "river",
    "sea",
    "barber’s",
    "beauty parlor",
    "convenience store",
    "ticket vending area",
    "restaurant",
    "festival",
    "station",
    "bus stop",
    "spa; hot spring",
    "foreign country",
    "Australia",
    "Mexico",
    "Italy",
    # "the Milky Way",
]

durations = [
    "one hour",
    "for two to three days",
    # ". . . hours",
]

# These don't have to _strictly_ refer to past times, but they can.
times_past = [
    "yesterday",
    "the day before yesterday",
    "the year before last",
    "two months ago",
    "two weeks ago",
    "last month",
    "last week",
    "last year",
]

times_future = [
    "breakfast",
    "dinner",
    "lunch",
    "morning",
    "noon",
    "night",
    "weekend",
    "this morning",
    "tonight",
    "today",
    "this week",
    "this semester",
    "this month",
    "this year",
    "tomorrow",
    "the day after tomorrow",
    "next semester",
    "next month",
    "next week",
    "next year",
    "the month after next",
    "the week after next",
    "the year after next",
    "near future",
    "future",
]

times_relative = times_past + times_future

times_absolute = [
    "New Year’s",
    "birthday",
    "holiday; day off; absence",
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday",
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
    "the first day of a month",
    "the second day of a month",
    "the third day of a month",
    "the fourth day of a month",
    "the fifth day of a month",
    "the sixth day of a month",
    "the seventh day of a month",
    "the eighth day of a month",
    "the ninth day of a month",
    "the tenth day of a month",
    "the eleventh day of a month",
    "the fourteenth day of a month",
    "the twentieth day of a month",
    "the twenty-fourth day of a month",
    "spring",
    "summer",
    "fall",
    "winter",
]

categories = [
    "color",
    "sports",
    "hobby; pastime",
    "food",
    "drink",
    "weather",
    "foreign country",
    "job; work; occupation",
    "season",
    "place",
    # "temperature (weather)",
]

no_idea = [
    "Car No. 1",
    "last car; tail end",
    "first car; front end",
    "nonsmoking car",
    "blonde hair",
    "super express",
    "transfer",
    "colloquial expression",
    "round trip",
    "money",
    "bath",
    "student discount",
    "meaning",
    "when",
    "reply",
    "company",
    "registered mail",
    "cold",
    "bookish expression",
    "one way",
    "money",
    "injury",
    "express",
    "air",
    "credit card",
    "airmail",
    "antibiotic",
    "blackboard",
    "in the morning",
    "answer",
    "excellent food",
    "this person (polite)",
    "parcel",
    "things; matters",
    "club activity",
    "overtime work",
    "match; game",
    "reserved seat",
    "departing second",
    "oneself",
    "deadline",
    "shower",
    "general admission seat",
    "last train",
    "cram school",
    "(boarding) ticket",
    "black and white",
    "traffic light",
    "stress",
    "grade (on a test, etc.)",
    "cough",
    "exam",
    "question",
    "operation",
    "departing first",
    "special delivery",
    "thermometer",
    "strip of fancy paper",
    "injection",
    "next",
    "polite expression",
    "weather forecast",
    "when . . . ; at the time of . . .",
    "the heavens; the sky",
    "commuter’s pass",
    "test",
    "electricity",
    "year",
    "next",
    "something",
    "diary",
    "wish",
    "× (wrong)",
    "pronunciation",
    "band",
    "person",
    "first",
    "people",
    "illness; sickness",
    "standard Japanese",
    "flight",
    "second",
    "local (train)",
    "hangover",
    "surface mail",
    "bath",
    "culture",
    "page",
    "reply",
    "dialect",
    "homesickness",
    "I (used by men)",
    "insurance",
    "host family",
    "minus",
    "window",
    "counter",
    "○ (correct)",
    "everyone; all of you",
    "all",
    "once upon a time",
    "the other side; over there",
    "thing (concrete object)",
    "example",
    "X-ray",
    "we",
    "mountain road",
    "dream",
]

noun_lists = [
    inanimate,
    subjects,
    practice_able,
    study_able,
    animals,
    people,
    personal_people,
    animate,
    wear_able,
    become_able,
    do_able,
    make_able,
    write_able,
    see_able,
    read_able,
    means_of_transport,
    hear_able,
    drink_able,
    eat_able,
    buy_able,
    body_parts,
    colors,
    weather,
    places_relative,
    places_abstract,
    directions,
    sub_places,
    frequency,
    personal_places,
    places_absolute,
    durations,
    times_past,
    times_future,
    times_relative,
    times_absolute,
    categories,
]
