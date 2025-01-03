import time

import plotly.graph_objects as go


def p1(data):
    def fill_dictionaries(i):
        d = {}
        while i < len(data) and data[i] != "":
            parts = [int(x) for x in data[i].split()]
            destination, source, r = parts[0], parts[1], parts[2]
            d[(source, source + r)] = destination
            i += 1
        i += 2
        return d, i

    def getValue(seed, d):
        for key in d.keys():
            if key[0] <= seed <= key[1]:
                return d[key] + abs(seed - key[0])
        return seed

    seeds = [int(x) for x in data[0].split(":")[1].split()]
    i = 3
    seed_to_soil, i = fill_dictionaries(i)
    soil_to_fertilizer, i = fill_dictionaries(i)
    fertilizer_to_water, i = fill_dictionaries(i)
    water_to_light, i = fill_dictionaries(i)
    light_to_temperature, i = fill_dictionaries(i)
    temperature_to_humidity, i = fill_dictionaries(i)
    humidity_to_location, i = fill_dictionaries(i)

    ds = [
        seed_to_soil,
        soil_to_fertilizer,
        fertilizer_to_water,
        water_to_light,
        light_to_temperature,
        temperature_to_humidity,
        humidity_to_location,
    ]
    locations = []

    viz_data = []

    for seed in seeds:
        l = [seed]
        for j in range(len(ds)):
            seed = getValue(seed, ds[j])
            l.append(seed)
        locations.append(seed)
        viz_data.append(l)

    fig = go.Figure(
        data=go.Parcoords(
            dimensions=list(
                [
                    dict(label="Seed", values=[l[0] for l in viz_data]),
                    dict(label="Soil", values=[l[1] for l in viz_data]),
                    dict(label="Fertilizer", values=[l[2] for l in viz_data]),
                    dict(label="Water", values=[l[3] for l in viz_data]),
                    dict(label="Light", values=[l[4] for l in viz_data]),
                    dict(label="Temperature", values=[l[5] for l in viz_data]),
                    dict(label="Humidity", values=[l[6] for l in viz_data]),
                    dict(label="Location", values=[l[7] for l in viz_data]),
                ]
            )
        )
    )

    fig.show()

    return min(locations)


def p2(data):
    def fill_dictionaries(i):
        d = {}
        while i < len(data) and data[i] != "":
            parts = [int(x) for x in data[i].split()]
            destination, source, r = parts[0], parts[1], parts[2]
            d[(source, source + r)] = destination
            i += 1
        i += 2
        return d, i

    def getValue(seed, d):
        for key in d.keys():
            if key[0] <= seed <= key[1]:
                return d[key] + abs(seed - key[0])
        return seed

    seeds = []
    line = [int(x) for x in data[0].split(":")[1].split()]
    for i in range(0, len(line), 2):
        seeds.append((line[i], line[i] + line[i + 1]))

    i = 3
    seed_to_soil, i = fill_dictionaries(i)
    soil_to_fertilizer, i = fill_dictionaries(i)
    fertilizer_to_water, i = fill_dictionaries(i)
    water_to_light, i = fill_dictionaries(i)
    light_to_temperature, i = fill_dictionaries(i)
    temperature_to_humidity, i = fill_dictionaries(i)
    humidity_to_location, i = fill_dictionaries(i)

    ds = [
        seed_to_soil,
        soil_to_fertilizer,
        fertilizer_to_water,
        water_to_light,
        light_to_temperature,
        temperature_to_humidity,
        humidity_to_location,
    ]

    mini = float("inf")
    for seed in seeds:
        for k in range(seed[0], seed[1]):
            v = k
            for j in range(len(ds)):
                v = getValue(v, ds[j])
            mini = min(mini, v)

    return mini


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        data = [line.strip() for line in f.readlines()]
    start = time.time()
    print(f"Part 1 : {p1(data)}")
    print(f"Time for part 1 : {time.time() - start}s")  # 563.24 ms
    start = time.time()
    print(f"Part 2 : {p2(data)}")
    print(
        f"Time for part 2 : {time.time() - start}s"
    )  # This takes hours to execute and gives the correct result + 1, no idea why
