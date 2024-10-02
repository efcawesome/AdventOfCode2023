with open("Day5Input.txt") as f:
    almanac = [x.strip() for x in f.readlines()]

map_names = ["seed-soil", "soil-fert", "fert-wat", "wat-light", "light-temp", "temp-hum", "hum-loc"]
maps = {"seed-soil": [], "soil-fert": [], "fert-wat": [], "wat-light": [], "light-temp": [], "temp-hum": [], "hum-loc": []}


def puzzle1():
    min_location = float("inf")
    seeds = get_real_seeds()

    curr_map = -1

    for i in range(1, len(almanac)):
        if almanac[i] == "":
            curr_map += 1
        elif almanac[i][0].isnumeric():
            maps[map_names[curr_map]].append([int(a) for a in almanac[i].split(" ")])

    for seed in seeds:
        curr_num = seed
        for j in range(len(map_names)):
            m_nam = map_names[j]
            for row in maps[m_nam]:
                dest_start = row[0]
                source_start = row[1]
                source_end = source_start + row[2] - 1
                if source_start <= curr_num <= source_end:
                    curr_num = dest_start + curr_num - source_start
                    break

        if curr_num < min_location:
            min_location = curr_num

    print(min_location)


def get_seeds():
    return [int(s) for s in almanac[0].strip("seeds: ").split(" ")]

def get_real_seeds():
    seeds = []
    seed_list = [int(s) for s in almanac[0].strip("seeds: ").split(" ")]
    for n in range(len(seed_list)):
        if n % 2 == 0:
            [seeds.append(num) for num in range(seed_list[n], seed_list[n] + seed_list[n + 1] - 1)]
    return seeds


def puzzle2():
    min_location = 772954177
    _seeds = get_seeds()
    seed_ranges = []

    [seed_ranges.append(SeedRange(_seeds[n], _seeds[n+1])) for n in range(0, len(_seeds), 2)]

    curr_map = -1

    for i in range(1, len(almanac)):
        if almanac[i] == "":
            curr_map += 1
        elif almanac[i][0].isnumeric():
            maps[map_names[curr_map]].append([int(a) for a in almanac[i].split(" ")])

    for map_name in map_names:
        new_ranges = []
        i = 0
        did_something = True
        print(seed_ranges)
        while i < len(seed_ranges):
            did_something = False
            seed_range = seed_ranges[i]
            for row in maps[map_name]:
                if seed_range.start <= row[1] <= seed_range.last_num: #new range in between seed range
                    if row[1] + row[2] - 1 <= seed_range.last_num: #end num less than/equal last seed
                        new_ranges.append(SeedRange(row[0], row[2]))
                        if seed_range.last_num - (row[1] + row[2] - 1) > 0:
                            seed_ranges.insert(i, SeedRange(row[1] + row[2], seed_range.last_num - (row[1] + row[2] - 1))) #insert high range
                        if row[1] - seed_range.start > 0:
                            seed_ranges.insert(i, SeedRange(seed_range.start, row[1] - seed_range.start)) #insert low range
                        seed_ranges.remove(seed_range) #remove old
                    else: #end num above last seed
                        new_ranges.append(SeedRange(row[0], seed_range.last_num - row[1] + 1))
                        if row[1] - seed_range.start > 0:
                            seed_ranges.insert(i, SeedRange(seed_range.start, row[1] - seed_range.start)) #insert low range
                        seed_ranges.remove(seed_range)  # remove old

                    i -= 1
                    did_something = True
                    break
                elif row[1] <= seed_range.start <= row[1] + row[2] - 1: #new range beneath seed range
                    if seed_range.last_num <= row[1] + row[2] - 1: #to above seed range
                        new_ranges.append(SeedRange(seed_range.start - (row[1] - row[0]), seed_range.srange))
                        seed_ranges.remove(seed_range)
                    else: #into seed range
                        new_ranges.append(SeedRange(seed_range.start - (row[1] - row[0]), row[1] + row[2] - seed_range.start))
                        if seed_range.last_num + 1 - (row[1] + row[2]) > 0:
                            seed_ranges.insert(i, SeedRange(row[1] + row[2], seed_range.last_num + 1 - (row[1] + row[2])))
                        seed_ranges.remove(seed_range)

                    i -= 1
                    did_something = True
                    break

            if not did_something:
                new_ranges.append(seed_range)
                seed_ranges.remove(seed_range)
                i -= 1

            i += 1

        [seed_ranges.append(x) for x in new_ranges if x.srange > 0 and 0 <= x.start <= x.last_num]

    print([str(se) for se in sorted(seed_ranges, key=lambda seed: seed.start)])
    print(min([s.start for s in seed_ranges]))


def combine_adjacents(tlist):
    # combine arrays idk
    k = 0
    temp_list = sorted(tlist, key=lambda seed: seed.start)
    while k < len(temp_list) - 1:
        if temp_list[k].last_num + 1 == temp_list[k + 1].start:
            new_seed = SeedRange(temp_list[k].start, temp_list[k].srange + temp_list[k + 1].srange)
            for kjasjdkj in range(2):
                temp_list.remove(temp_list[k])

            temp_list.insert(k, new_seed)
            k = -1

        k += 1

    return temp_list

class SeedRange:
    def __init__(self, st, sr):
        self.start = st
        self.srange = sr
        self.last_num = st + sr - 1

    def __str__(self):
        return "start: " + str(self.start) + ", end: " + str(self.last_num) + ", range: " + str(self.srange)

    def __int__(self):
        return self.start


puzzle2()
