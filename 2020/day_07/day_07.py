def get_outermost_bags(data, bag_slug):
    def containable_by(bag, found=None):
        if found is None:
            found = []
        new = [slug for slug, specs in data.items() if (bag in [*specs] and
                                                        slug not in found)]
        found += new
        for bag in new:
            new += containable_by(bag, found)
        return new

    return containable_by(bag_slug)


def count_inner_bags(data, bag_slug):
    def count_inner(bag):
        total = 0
        for bag, count in data[bag].items():
            total += int(count)
            total += int(count_inner(bag)) * int(count)
        return total

    return count_inner(bag_slug)


def parse_input(lines):
    data = {}
    for line in lines:
        bag_slug = line.split(' bag')[0]
        specs = {}
        for spec in line.split('contain ')[1][:-2].split(', '):
            split = spec.split(' ')
            number = split[0]
            slug = ' '.join(split[1:3])
            if number != "no":
                specs[slug] = number
        data[bag_slug] = specs
    return data


if __name__ == '__main__':
    data = parse_input(open('input.txt', 'r'))
    number = len(get_outermost_bags(data, 'shiny gold'))
    print(f'There are {number} bag colors')

    number = count_inner_bags(data, 'shiny gold')
    print(f'{number} individual bags are required')
