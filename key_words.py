# Takes the data produced by the facial features AI and produces key words to be used in the
# comments.

import random

"""
Attributes to generate keywords from
    - 5 o clock shadow, faint stubble growth after a shave
    - arched eyebrows
    - attractive
    - bags under eyes
    - bald
    - bangs
    - big lips
    - big nose
    - black hair
    - blonde hair
    - blurry brown hair
    - bushy eyebrows
    - chubby
    - double chin
    - eyeglasses
    - goatee
    - gray hair
    - heavy makeup
    - high cheekbones
    - mouth slightly open
    - mustach
    - narrow eyes
    - no beard
    - oval face
    - pointy nose
    - receding hairline
    - rosy cheeks
    - sideburns
    - smiling
    - straight_hair
    - wavy_hair
    - wearing earrings
    - wearing hat
    - wearing lipstick
    - wearing necklace
    - wearing necktie
    - young
"""

"""
Plan for the algorithm:
    1. Get the data from Alejandro's facial features section
        - Organize it if necessary for easier analysis
    2. Retrieve the top 10 highest valued attributes and 10 lowest valued attributes
    3. Out of those, select 3 attributes
    4. Each attribute is linked to one keyword through a dictionary, use these keywords
       in combination with chatgpt to generate 5 similar words, either insult or complement
    5. Choose two of these words and then one of those two plus the keyword to be used in the insult
       or complement for each attribute
    6. Send these keywords to Danny for the actual insult/complement generation
    7. Use this program multiple times for each person in the game session
"""

#Two dictionaries, one for low, one for high, note 19, 25 missing

low_scores = {
    0: "no stubble",
    1: "round eyebrows",
    2: "ugly",
    3: "fresh eyes",
    3: "fresh eyes",
    4: "not bald",
    5: "big forhead",
    6: "small lips",
    7: "button nose",
    8: "not black hair",
    9: "not blonde hair",
    10: "not brown hair",
    11: "skinny brows",
    12: "hollow cheeks",
    13: "chin",
    14: "no glasses",
    15: "no goatee",
    16: "not gray hair",
    17: "little makeup",
    18: "low cheekbones",
    20: "tight lipped",
    21: "no mustache",
    22: "big eyes",
    23: "beard",
    24: "round head",
    26: "stubby nose",
    27: "healthy hairline",
    28: "non-rosy cheeks",
    29: "no sideburns",
    30: "unhappy",
    31: "curly hair",
    32: "straight hair",
    33: "no earrings",
    34: "no hat",
    35: "no lipstick",
    36: "no necklace",
    37: "no necktie",
    38: "old"
}

high_scores = {
    0: "stubble",
    1: "sharp eyebrows",
    2: "beautiful",
    3: "baggy eyes",
    4: "bald",
    5: "bangs",
    6: "plump lips",
    7: "big nose",
    8: "black hair",
    9: "blonde hair",
    10: "brown hair",
    11: "thick brows",
    12: "chubby",
    13: "double chin",
    14: "glasses",
    15: "goatee",
    16: "gray hair",
    17: "lots of makeup",
    18: "high cheekbones",
    20: "gaping mouth",
    21: "mustache",
    22: "small eyes",
    23: "baby face",
    24: "long head",
    26: "pointy nose",
    27: "balding",
    28: "blushing",
    29: "sideburns",
    30: "happy",
    31: "straight hair",
    32: "curly hair",
    33: "earrings",
    34: "hat",
    35: "lipstick",
    36: "necklace",
    37: "necktie",
    38: "young"
}

def gen_key(data):
    
    return 0

def get_attributes(data):
    raw_data = data
    sorted_data = raw_data.copy()
    sorted_data[19] = -1
    sorted_data[25] = -1
    sorted_data.sort(reverse=True)

    highs = []
    lows = []
    temp_raw = raw_data.copy()
    temp_raw[19] = -1
    temp_raw[25] = -1
    for i in range(36):
        if (i <= 9):
            idx = temp_raw.index(sorted_data[i])
            highs.append(idx)
            temp_raw[idx] = -1
        elif (i >= 26):
            idx = temp_raw.index(sorted_data[i])
            lows.append(idx)
            temp_raw[idx] = -1
    
    #print(highs)
    #print(lows)

    highs_or_lows = random.randint(0, 1)
    attributes = []
    if (0 == highs_or_lows):
        a1 = highs[random.randint(0, 9)]
        a2 = highs[random.randint(0, 9)]
        a3 = lows[random.randint(0, 9)]
        #print(str(a1) + " " + str(a2) + " " + str(a3))
        attributes = [high_scores.get(a1), 
                      high_scores.get(a2), 
                      low_scores.get(a3)]
    else:
        a1 = lows[random.randint(0, 9)]
        a2 = lows[random.randint(0, 9)]
        a3 = highs[random.randint(0, 9)]
        #print(str(a1) + " " + str(a2) + " " + str(a3))
        attributes = [low_scores.get(a1), 
                      low_scores.get(a2), 
                      high_scores.get(a3)]

    return attributes


"""print(get_attributes([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]))
print(get_attributes([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38]))
print(get_attributes([0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1]))"""