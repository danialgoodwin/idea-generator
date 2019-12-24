#!/usr/bin/env python3


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
            if not line:
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
    parse_data()
    debug()
    location = locations[random.int(len(locations))]
    challenge = challenges[random.int(len(challenges))]
    niche = niches[random.int(len(niches))]
    type = types[random.int(len(types))]
    goal = goals[random.int(len(goals))]
    print(f'In {location}, with {challenge}, use {niche} and {type} to {goal}')
 

def main():
    new_idea()


if __name__ == "__main__":
    main()
