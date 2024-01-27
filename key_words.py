# Takes the data produced by the facial features AI and produces key words to be used in the
# comments.

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
    - male
    - mouth slightly open
    - mustach
    - narrow eyes
    - no beard
    - oval face
    - pale skin
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
    5. Choose one of these words to be used in the insult for each of the three attributes
    6. Send these keywords to Danny for the actual insult/complement generation
    7. Use this program multiple times for each person in the game session
"""