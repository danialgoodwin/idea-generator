#!/usr/bin/env python3


from random import randrange


locations = []
challenges = []
niches = []
types = []
goals = []

businesses = []
topics = []


def parse_data_section(section_name, data):
    if section_name == 'location':
        locations.append(data)
    elif section_name == 'challenge':
        challenges.append(data)
    elif section_name == 'niche':
        niches.append(data)
    elif section_name == 'type':
        types.append(data)
    elif section_name == 'goal':
        goals.append(data)
    elif section_name == 'business':
        businesses.append(data)
    elif section_name == 'topic':
        topics.append(data)


def parse_data_file():
    with open('data.txt') as f:
        for line in f:
            line = line.rstrip('\n')
            if (not line) or (line.startswith('//')):
                continue
            elif line.startswith('#'):
                space_index = line.find(' ') + 1
                colon_index = line.find(':')
                section_name = line[space_index:colon_index]
            else:
                parse_data_section(section_name, line)


def debug():
    print('==========')
    print('locations:', locations)
    print('challenges:', challenges)
    print('niches:', niches)
    print('types:', types)
    print('goals:', goals)
    print('businesses:', businesses)
    print('topics:', topics)
    print('==========')


def new_game_idea():
    print('new_game_idea()')
    location = locations[randrange(len(locations))]
    challenge = challenges[randrange(len(challenges))]
    niche = niches[randrange(len(niches))]
    game_type = types[randrange(len(types))]
    goal = goals[randrange(len(goals))]
    print(f'In {location}, with {challenge}, use {niche} and {game_type} to {goal}.')


def new_business_idea():
    print('new_business_idea()')
    business = businesses[randrange(len(businesses))]
    topic = topics[randrange(len(topics))]
    print(f'The {business} of {topic}.')


def main():
    parse_data_file()
    debug()
    new_game_idea()
    new_game_idea()
    new_business_idea()
    new_business_idea()


if __name__ == "__main__":
    main()
