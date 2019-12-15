import math


def get_requirements(amount_dict, amount, chemical):
    if chemical == "ORE":
        amount_dict["ORE"] += amount
        return amount_dict
    if amount <= amount_dict[chemical]:
        amount_dict[chemical] -= amount
        return amount_dict
    amount -= amount_dict[chemical]
    amount_dict[chemical] = 0
    output_amount, recipe = reactions[chemical]
    num_executions = math.ceil(amount / output_amount)
    for i_amount, i_chemical in recipe:
        amount_dict = get_requirements(amount_dict, num_executions * i_amount,
                                       i_chemical)
    amount_dict[chemical] += num_executions * output_amount - amount
    return amount_dict


with open("input.txt", "r") as f:
    raw_reactions = list(map(str.strip, f.readlines()))

reactions = {"ORE": (0, [])}
for reaction in raw_reactions:
    r_input, r_output = reaction.split(" => ")
    r_inputs = [(int(s.split(" ")[0]), s.split(" ")[1])
                for s in r_input.split(", ")]
    r_output_amount, r_output_chemical = r_output.split(" ")
    reactions[r_output_chemical] = (int(r_output_amount), r_inputs)

amount_ore = 1_000_000_000_000
low, high = 0, amount_ore
last_amount_fuel = 0
while (amount_fuel := (low + high) // 2) != last_amount_fuel:
    amount_dict = {chemical: 0 for chemical in reactions.keys()}
    ore_needed = get_requirements(amount_dict, amount_fuel, "FUEL")["ORE"]
    if ore_needed > amount_ore:
        high = amount_fuel
    else:
        low = amount_fuel
    last_amount_fuel = amount_fuel
print(last_amount_fuel)
