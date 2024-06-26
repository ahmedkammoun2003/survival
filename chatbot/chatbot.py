import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import random

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

question_answer_pairs = {
    "What should I do if aliens attack?": "Find shelter and stay calm. Follow emergency protocols if available.",
    "How can I protect myself from aliens?": "Stay indoors and avoid confrontation. Listen to official instructions.",
    "Where should I go during an alien invasion?": "Seek shelter in a secure location. Stay away from open areas.",
    "What supplies should I gather for an alien invasion?": "Stock up on food, water, and basic medical supplies.",
    "Is there a way to communicate with aliens?": "Avoid communication unless directed by authorities. Safety first.",
    "What if I encounter an alien?": "Do not approach. Seek safety immediately and report to authorities.",
    "What are the signs of an impending alien invasion?": "Unusual sightings, disturbances in technology, or unusual atmospheric phenomena.",
    "What are the early signs of an impending alien invasion?":"Unusual celestial phenomena, government alerts, or unexplained power outages.",
    "How can I prepare my family for an alien invasion?":"Develop a communication plan, establish a meeting point, and stock emergency supplies.",
    "Is there a way to distinguish between a false alarm and a real alien invasion threat?":"Monitor reliable news sources, verify information, and follow official instructions.",
    "Should I create a bug-out bag specifically for an alien invasion?":"Yes, include essentials like water, non-perishable food, first aid supplies, and communication tools.",
    "What should I do if I'm caught outdoors during an alien invasion?":"Seek immediate shelter or hide in dense vegetation away from main roads or buildings.",
    "How important is it to have a designated safe room in my home during an alien invasion?":"Critical for immediate protection, store emergency supplies and communication devices within.",
    "How can I mentally prepare my children for the possibility of an alien invasion?":"Discuss calmly, focus on safety measures and reassurance, practice emergency drills.",
    "What role do local authorities play in coordinating responses to an alien invasion?":"They provide information, organize evacuations if necessary, and maintain public safety.",
    "How should I prioritize my preparations for an alien invasion?":"Start with emergency kits and communication plans, then focus on fortifying your shelter and gathering supplies.",
    "What are some misconceptions about surviving an alien invasion?":"Misinformation on social media, exaggerated rumors, and lack of reliable sources.",
    "Where are the safest places to hide during an alien invasion in an urban environment?":"Basement of sturdy buildings, underground parking garages, or reinforced concrete structures.",
    "How can I minimize my heat signature to avoid alien detection?":"Use thermal blankets, stay in shaded areas, and avoid open flames or heat-emitting devices.",
    "Are there specific times of day when it's safer to move around during an alien invasion?":"Nighttime offers more cover but be cautious of alien patrols or enhanced senses.",
    "Should I rely on urban camouflage techniques during an alien invasion?":"Yes, blend into surroundings with dark clothing, avoid reflective surfaces, and use natural cover.",
    "How can I mask my scent to avoid detection by aliens?":"Use scent-blocking sprays or stay downwind of alien travel paths.",
    "What should I do if I encounter alien drones while hiding?":"Stay motionless, limit noise, and avoid direct eye contact or sudden movements.",
    "How can I evade aerial surveillance during an alien invasion?":"Move under dense tree canopies or into underground tunnels, avoid open areas or rooftops.",
    "What are the risks of using vehicles for evacuation during an alien invasion?":"Vehicles attract attention, risk mechanical failure, and are vulnerable to alien technology.",
    "How can I use decoys to divert alien attention from my hiding location?":"Place dummy objects or use automated sounds and lights to mislead alien sensors.",
    "How can I gather intelligence on alien movements without being detected?":"Use binoculars from concealed positions, monitor alien behavior patterns, and avoid direct confrontation.",
    "What are the essential features of an underground bunker for surviving an alien invasion?":"Reinforced walls, secure ventilation systems, and emergency exits.",
    "How can I strengthen existing structures against potential alien attacks?":"Install steel reinforcements, blast-resistant windows, and barricade entry points.",
    "Should I prioritize building an above-ground or underground shelter?":"Underground shelters offer better protection from alien detection and attacks.",
    "What materials should I avoid when constructing a shelter to protect against alien technology?":"Avoid materials that conduct electricity or emit strong electromagnetic signals.",
    "How can I camouflage my shelter to avoid alien detection?":"Use natural materials, blend with surrounding terrain, and minimize visible entry points.",
    "How can I protect my shelter from alien probes or reconnaissance drones?":"Install electromagnetic shielding or use reflective surfaces to deflect detection.",
    "How should I stock my shelter to sustain long-term survival during an alien invasion?":"Store non-perishable food, water filtration systems, medical supplies, and communication devices.",
    "What are the benefits of building a remote wilderness shelter during an alien invasion?":"Reduce human detection risk, access natural resources, and maintain isolation from alien activities.",
    "Can I use natural caves as shelters during an alien invasion?":"Yes, reinforce entrances, secure water sources, and improve ventilation for long-term occupancy.",
    "How can I disguise my shelter entrance to protect against alien probes?":"Use hidden hatches, camouflaged doors, or false rock formations to blend with surroundings.",
    "What are the best locations to find food and water during an alien invasion?":"Rivers, lakes, and natural springs provide safe water sources. Avoid contaminated areas.",
    "How can I filter and purify water sources to make them safe to drink during an alien invasion?":"Boil water, use portable water filters, or purify with iodine tablets or UV light.",
    "What wild edible plants are safe to consume during an alien invasion?":"Identify and harvest plants like dandelions, cattails, and wild berries. Avoid unfamiliar plants.",
    "How can I safely hunt small game for food during an alien invasion?":"Use silent weapons like bows or crossbows, practice stealth, and avoid attracting attention.",
    "Should I consider fishing as a primary food source during an alien invasion?":"Yes, fish in remote locations with quiet techniques and simple traps.",
    "How can I preserve and store perishable food during an alien invasion?":"Dry or smoke meats, store in sealed containers, and prioritize non-perishable foods.",
    "How can I maintain a sustainable food supply in an underground shelter during an alien invasion?":"Establish indoor gardens with grow lights, grow sprouts, and raise insects for protein.",
    "How can I scavenge abandoned urban areas for food and supplies during an alien invasion?":"Search non-contaminated stores, warehouses, and residential areas for canned goods and survival gear.",
    "How can I prepare and preserve food without electricity during an alien invasion?":"Use dehydration, fermentation, or salt curing methods for long-term storage.",
    "What should I do if I encounter aggressive wildlife while foraging for food during an alien invasion?":" Avoid confrontation, retreat slowly, and use non-lethal deterrents like loud noises or bear spray.",
    "What types of improvised weapons can be effective against alien invaders?":"Use blunt objects, knives, or repurpose household tools for close combat.",
    "How can I create defensive traps to protect my shelter from alien intruders?":"Set tripwires with noise makers, use pit traps, or create obstacles to slow down invaders.",
    "Should I consider using firearms for self-defense during an alien invasion?":"Use firearms responsibly, prioritize evasion, and avoid attracting unnecessary attention.",
    "How can I coordinate defense efforts with other survivors during an alien invasion?":"Establish communication channels, share intelligence, and coordinate patrols or lookout shifts.",
    "What are the risks of engaging in direct combat with alien invaders during an invasion?":"Aliens possess advanced technology and unknown capabilities. Avoid confrontation if possible.",
    "How can I use diversion tactics to distract alien forces away from my shelter?":"Create false trails, use decoys or simulated distress signals to mislead alien patrols.",
    "How can I protect myself from alien mind control or psychic abilities?":"Maintain mental resilience, avoid prolonged exposure to alien technology, and stay focused on survival tasks.",
    "What should I do if I encounter hostile human groups during an alien invasion?":"Avoid confrontation, negotiate if possible, and prioritize finding alternative safe havens.",
    "Can I use non-lethal tactics to incapacitate alien intruders during an invasion?":"Use stun devices, tranquilizers, or temporary immobilization techniques as a last resort.",
    "How can I maintain morale and motivation during prolonged alien invasion scenarios?":"Stay connected with supportive individuals, focus on short-term goals, and celebrate small victories.",
    "How can I establish reliable communication channels with other survivors during an alien invasion?":"Use encrypted radios, signal mirrors, or pre-arranged coded messages for secure communication.",
    "What emergency signals should I use to communicate distress during an alien invasion?":"Use recognized distress signals like SOS or specific pre-arranged patterns for identification.",
    "How can I create a makeshift communication hub for coordinating survival efforts?":"Establish central meeting points, distribute contact lists, and rotate message runners for updates.",
    "Can I use satellite communication systems during an alien invasion?":"Use sparingly, prioritize secure channels, and avoid drawing attention from alien surveillance.",
    "How should I communicate with potential rescuers or aid organizations during an alien invasion?":"Transmit location signals, maintain radio silence, and follow established rescue protocols.",
    "How can I differentiate between friendly and hostile groups during an alien invasion?":"Verify identities through pre-arranged codes, observe behavior patterns, and approach cautiously.",
    "How can I maintain communication discipline to avoid detection during an alien invasion?":"Use minimal transmission time, avoid unnecessary chatter, and switch frequencies regularly.",
    "How can I use survivor networks to exchange critical resources during an alien invasion?":" Establish barter systems, share skills or supplies, and support community-based survival initiatives.",
    "Should I establish communication protocols with neighboring survival groups during an alien invasion?":"Yes, coordinate resources, share intelligence, and plan joint defense or evacuation strategies.",
    "How can I encourage teamwork and cooperation within a survival network during an alien invasion?":"Assign roles based on skills, resolve conflicts diplomatically, and prioritize collective safety.",
    "What types of first aid supplies are essential during an alien invasion?":"Stock bandages, antiseptics, pain relievers, gauze, adhesive tape, scissors, tweezers, and a first aid manual. Include prescription medications and specialized items based on medical needs.",
    "How can I maintain hygiene and sanitation in a long-term shelter?":"Use portable toilets or buckets with lids, practice regular handwashing with soap or hand sanitizer, and properly dispose of waste. Stock hygiene products like toothpaste, soap, and sanitary items.",
    "What steps should I take if someone in my group is injured during an alien invasion?":"Provide immediate first aid, clean wounds, apply pressure to stop bleeding, and stabilize fractures. Seek professional medical help if possible and monitor for signs of infection.",
    "How can I identify and treat common illnesses without access to a doctor?":"Learn to recognize symptoms of common illnesses, use over-the-counter medications, maintain hydration, and rest. Research basic treatments for conditions like infections, fevers, and gastrointestinal issues.",
    "What are the best ways to fortify a vehicle against alien attacks?":"Reinforce windows with metal grates, install armor plating, and create hidden compartments for supplies. Keep the fuel tank full and maintain the vehicle regularly to ensure it’s in good working condition.",
    "How can I prepare my pets for an alien invasion?":"Stock extra pet food, water, and supplies. Keep pets indoors or in secure areas to avoid attracting attention. Prepare a pet emergency kit with necessary medications and comfort items.",
    "What role does exercise play in maintaining health during an alien invasion?":"Regular exercise maintains physical fitness, reduces stress, and boosts morale. Incorporate bodyweight exercises, stretching, and cardio activities that can be performed in confined spaces.",
    "How can I find and purify water in an urban environment during an alien invasion?":"Locate sources like rooftop rain catchments, water heaters, or public fountains. Purify water by boiling, using water purification tablets, or portable filters.",
    "What types of non-perishable foods are best to stockpile for an alien invasion?":"Canned goods, dried fruits, nuts, rice, pasta, and freeze-dried meals. Ensure a balanced diet by including protein sources, carbohydrates, and vitamins.",
    "How can I create and maintain a secure perimeter around my shelter?":"Use barriers like fences, thorny bushes, or makeshift barricades. Set up tripwires or noise-making devices to alert you of intruders. Regularly patrol and inspect the perimeter.",
    "What strategies can I use to avoid detection by alien surveillance technology?":"Limit electronic device usage, stay out of sight, use natural cover, and minimize heat signatures. Avoid areas known to be under surveillance.",
    "How can I create makeshift weapons from household items?":"Repurpose items like kitchen knives, heavy tools, or sports equipment. Create spears from broom handles and knives, or use duct tape to reinforce and sharpen objects.",
    "What are the psychological effects of prolonged isolation during an alien invasion?":"Feelings of anxiety, depression, and loneliness may occur. Maintain social connections, establish routines, and engage in mental health activities to mitigate these effects.",
    "How can I establish a secure communication network with other survivors?":"Use encrypted radios, develop coded messages, and set regular check-in times. Use low-tech methods like signal mirrors or message drops if electronic communication is compromised.",
    "What are the signs that it's safe to emerge from a shelter after an alien invasion?":"Monitor reliable news sources for official all-clear signals. Observe decreased alien activity and wait for confirmation from authorities or trusted networks.",
    "How can I teach my children to stay safe during an alien invasion?":"Explain the situation in age-appropriate terms, practice emergency drills, and emphasize the importance of staying calm and following instructions.",
    "How can I manage limited resources during an extended alien invasion?":"Ration supplies carefully, prioritize essential needs, and find ways to recycle and repurpose materials. Establish a system for fair distribution within your group.",
    "What should I include in a communication plan for my family during an alien invasion?":"Designate primary and secondary meeting locations, agree on emergency contact methods, and ensure everyone knows the plan. Keep written copies for reference.",
    "How can I maintain morale and motivation during prolonged alien invasion scenarios?":"Stay connected with supportive individuals, focus on short-term goals, and celebrate small victories. Engage in recreational activities and maintain a positive outlook.",
    "How can I identify safe evacuation routes during an alien invasion?":"Monitor official channels for evacuation information, avoid main roads if they're congested or monitored, and plan multiple routes to increase chances of safe passage.",
    "What are the best practices for maintaining a healthy diet in a shelter during an alien invasion?":"Balance protein, carbs, and fats; include vitamins and minerals through supplements if fresh produce isn't available. Rotate stock to keep food fresh and avoid nutrient deficiencies.",
    "How can I develop effective contingency plans for different scenarios during an alien invasion?":"Identify potential threats, prioritize risks, create step-by-step responses, and practice drills. Update plans regularly based on new information and experiences.",
    "What are the psychological effects of prolonged isolation during an alien invasion?":"Feelings of anxiety, depression, and loneliness may occur. Maintain social connections, establish routines, and engage in mental health activities to mitigate these effects.",
    "How can I secure my digital devices against potential alien hacking or surveillance?":"Use strong passwords, enable encryption, disconnect from networks when not in use, and avoid transmitting sensitive information. Consider using older, non-digital methods for communication and record-keeping.",
    "How can I establish a secure communication network with other survivors?":"Use encrypted radios, develop coded messages, and set regular check-in times. Use low-tech methods like signal mirrors or message drops if electronic communication is compromised.",
    "What are the signs that it's safe to emerge from a shelter after an alien invasion?":"Monitor reliable news sources for official all-clear signals. Observe decreased alien activity and wait for confirmation from authorities or trusted networks.",
    "How can I teach my children to stay safe during an alien invasion?":"Explain the situation in age-appropriate terms, practice emergency drills, and emphasize the importance of staying calm and following instructions.",
    "How can I manage limited resources during an extended alien invasion?":"Ration supplies carefully, prioritize essential needs, and find ways to recycle and repurpose materials. Establish a system for fair distribution within your group.",
    "What should I include in a communication plan for my family during an alien invasion?":"Designate primary and secondary meeting locations, agree on emergency contact methods, and ensure everyone knows the plan. Keep written copies for reference.",
    "What are the most effective ways to secure doors and windows against alien entry?":"Install reinforced locks, use metal bars or grates, and reinforce with plywood or metal sheeting. Consider using additional barriers like heavy furniture.",
    "How can I make my home more defensible against alien attacks?":"Strengthen doors and windows, create safe rooms, establish early warning systems, and fortify entry points with barriers or traps.",
    "What are the best ways to maintain mental health during an alien invasion?":"Stay connected with others, engage in regular physical activity, practice mindfulness or meditation, and establish a daily routine to maintain a sense of normalcy.",
    "How can I safely dispose of waste in a long-term shelter?":"Use sealed containers for trash, establish a compost system for organic waste, and regularly remove waste to a safe distance from the shelter if possible.",
    "How can I build a sustainable water supply system in an underground shelter?":"Collect rainwater, install a filtration system, and store water in large containers. Rotate water storage to prevent stagnation and contamination.",
    "How can I create a hidden shelter entrance to avoid alien detection?":"Use camouflaged doors, blend entry points with natural surroundings, and install hidden hatches or false walls to conceal access points.",
    "What are the best methods to communicate with potential rescuers during an alien invasion?":"Use signal flares, reflective mirrors, or pre-arranged visual signals. Maintain radio silence except for scheduled check-ins to avoid detection.",
    "How can I prepare for the possibility of food scarcity during an alien invasion?":"Stockpile non-perishable foods, learn foraging and hunting skills, and establish a small-scale garden or hydroponics system if possible.",
    "What should I do if I encounter an alien with peaceful intentions?":"Approach cautiously, follow non-verbal communication cues, and contact authorities or experts for guidance. Prioritize safety while assessing the situation.",
    "How can I make improvised medical devices or tools in a survival situation?":"Use everyday items: create splints from sticks or boards, tourniquets from belts or cloth, and slings from shirts or scarves. Sterilize tools with heat if necessary.",
    "How can I prevent and manage fires in a shelter during an alien invasion?":"Keep fire extinguishers and blankets handy, create firebreaks, and establish safe cooking areas. Regularly check and maintain electrical and heating systems.",
    "How can I effectively communicate with other survivors using non-verbal signals?":"Develop a set of hand signals, use flashlights for Morse code, and create pre-arranged visual cues like colored flags or markers.",
    "How can I maintain a positive mindset during an alien invasion?":"Focus on small, achievable goals, maintain social connections, engage in hobbies or activities, and practice gratitude to keep spirits high.",
    "What should I do if an alien invasion disrupts local infrastructure?":"Prepare for power outages, loss of water supply, and communication breakdowns. Stockpile essential supplies and develop self-sufficient systems.",
    "How can I use natural barriers to enhance the security of my shelter?":"Utilize dense vegetation, natural rock formations, and water bodies to create obstacles. Reinforce with man-made barriers for added protection.",
    "How can I teach my family basic survival skills in preparation for an alien invasion?":"Conduct regular training sessions on first aid, fire-starting, navigation, and foraging. Practice emergency drills and scenario planning together.",
    "How can I maintain security without drawing attention during an alien invasion?":"Use discreet surveillance, avoid visible fortifications, and employ passive defenses like noise traps or natural barriers. Keep a low profile to avoid detection.",
    "What are the best practices for storing and preserving important documents during an alien invasion?":"Store documents in waterproof, fireproof containers. Keep digital copies on encrypted drives and distribute duplicates in multiple secure locations.",
    "How can I establish a reliable power source for my shelter during an alien invasion?":"Use solar panels, wind turbines, or generators with proper fuel storage. Consider manual power devices like hand-crank radios and chargers.",
    "How can I avoid spreading illness within a shelter during an alien invasion?":"Isolate sick individuals, practice good hygiene, disinfect common areas regularly, and ensure proper ventilation. Stock medical supplies and PPE.",
    "How can I ensure my dog's safety during an alien invasion?":"Keep your dog indoors or in a secure area. Provide a safe, quiet space where your dog can feel secure. Ensure your dog wears a collar with identification tags at all times.",
    "What essential supplies should I have for my dog during an alien invasion?":"Stock up on dog food, water, medications, a leash, collar, identification tags, a crate or carrier, bedding, toys, and a first aid kit specifically for pets.",
    "How can I keep my dog calm during an alien invasion?":"Maintain a routine as much as possible, provide comfort items like favorite toys or blankets, use calming aids such as pheromone sprays or anxiety vests, and ensure your dog gets regular exercise.",
    "How should I plan for my dog's dietary needs during an alien invasion?":"Stockpile enough dog food to last several weeks or months. If you run out of dog food, research safe human foods that can substitute, such as cooked meat, rice, and vegetables (avoid toxic foods like chocolate, grapes, and onions).",
    "How can I train my dog to assist with survival tasks during an alien invasion?":"Teach basic commands like sit, stay, and come. Train your dog to alert you to dangers, carry small items, or even help with simple tasks like retrieving objects.",
    "What should I do if my dog gets injured during an alien invasion?":"Provide immediate first aid, clean wounds with antiseptic, bandage injuries, and keep your dog calm and immobilized. Seek veterinary help as soon as it is safe and possible.",
    "How can I manage my dog's waste in a confined shelter during an alien invasion?":"Designate a specific area for your dog to relieve itself, use puppy pads or newspaper, and clean up waste promptly to maintain hygiene. Dispose of waste in sealed bags away from living areas.",
    "What precautions should I take when venturing outside with my dog during an alien invasion?":"Keep your dog on a leash, stay aware of surroundings, avoid areas with high alien activity, and be prepared to return to shelter quickly. Train your dog to stay quiet to avoid detection.",
    "How can I keep my dog entertained and mentally stimulated in a shelter?":"Provide toys, puzzle feeders, and regular playtime. Teach new tricks or commands to keep your dog's mind engaged and reduce stress.",
    "What are the signs of stress in my dog, and how can I address them during an alien invasion?":"Signs of stress include excessive barking, whining, pacing, drooling, and destructive behavior. Address stress by maintaining a routine, providing a calm environment, and using calming aids.",
    "How can I ensure my dog gets enough exercise during an alien invasion?":"Create indoor exercise routines, such as playing fetch in a hallway, using stairs for climbing exercises, or teaching new tricks that involve movement.",
    "What should I do if my dog encounters an alien or alien technology?":"Immediately recall your dog to safety. Keep your dog on a leash during outings to prevent it from approaching unknown entities or objects. Avoid letting your dog sniff or interact with alien technology.",
    "How can I prevent my dog from drawing attention to our hiding spot?":"Train your dog to be quiet on command, provide mental stimulation to reduce boredom-related noise, and use calming aids if necessary. Keep your dog close and under control.",
    "What emergency signals should I teach my dog to recognize during an alien invasion?":"Train your dog to respond to specific signals, such as a whistle or hand signals, to stay quiet, come to you, or hide. Practice these signals regularly.",
    "How can I make sure my dog does not run away if we need to evacuate quickly?":"Keep your dog on a leash or in a carrier during evacuation. Train your dog to stay close to you and respond reliably to recall commands.",
    "How can I protect my dog from extreme weather conditions during an alien invasion?":"Ensure your shelter is temperature-controlled. Provide adequate bedding for warmth, shade for cooling, and water to prevent dehydration.",
    "What should I include in a first aid kit for my dog during an alien invasion?":"Include bandages, antiseptic wipes, tweezers, scissors, styptic powder, a thermometer, adhesive tape, and any necessary medications. Know basic pet first aid procedures.",
    "How can I identify if my dog is suffering from dehydration or malnutrition during an alien invasion?":"Symptoms of dehydration include dry gums, lethargy, sunken eyes, and loss of skin elasticity. Signs of malnutrition include weight loss, dull coat, and weakness. Ensure regular feeding and access to clean water.",
    "How can I create a safe, designated area for my dog in an underground shelter?":"Use a crate or build a small enclosure with comfortable bedding and familiar items. Ensure the area is well-ventilated and secure from hazards.",
    "How can I handle the emotional needs of my dog during an alien invasion?":"Provide affection, maintain routines, engage in play, and ensure your dog feels secure and loved. Pay attention to changes in behavior and address any signs of distress promptly."
}

def preprocess_text(text):
    tokens = word_tokenize(text.lower())
    tokens = [token for token in tokens if token.isalnum()]
    tokens = [token for token in tokens if token not in stopwords.words('english')]
    lemmatizer = WordNetLemmatizer()
    tokens = [lemmatizer.lemmatize(token) for token in tokens]
    return tokens

def respond_to_question(question):
    question_tokens = preprocess_text(question)
    best_match = None
    max_score = 0

    for key in question_answer_pairs:
        score = sum(token in preprocess_text(key) for token in question_tokens)
        if score > max_score:
            max_score = score
            best_match = key

    if best_match:
        return question_answer_pairs[best_match]
    else:
        return "I'm sorry, I don't understand your question about surviving an alien invasion."