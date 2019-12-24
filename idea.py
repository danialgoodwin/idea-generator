#!/usr/bin/env python3


from random import randrange


locations = []
challenges = []
niches = []
types = []
goals = []


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
    print('locations:', locations)
    print('challenges:', challenges)
    print('niches:', niches)
    print('types:', types)
    print('goals:', goals)


def new_idea():
    parse_data_file()
    debug()
    location = locations[randrange(len(locations))]
    challenge = challenges[randrange(len(challenges))]
    niche = niches[randrange(len(niches))]
    game_type = types[randrange(len(types))]
    goal = goals[randrange(len(goals))]
    print(f'In {location}, with {challenge}, use {niche} and {game_type} to {goal}.')
 

def main():
    new_idea()


if __name__ == "__main__":
    main()
