Cargo = ["Spices", "Cannons", "Tea", "Contraband", "Fruit", "Textiles"]

upgrade_items = {
    1: [["Iron Hull", "Damage Reduction +.05, Speed -1", 1000],
        ["damage_red", .05], ["speed", -1]],
    2: [["Bamboo Rudder", "Speed +10, Cargo +5", 1400],
        ["speed", 10], ["max_cargo", 5]],
    3: [["Testisman", "Life -10", 1], ["max_health", -10]],
    4: [["Ultimate", "Life +10, Speed +50, Cargo +10", 14000],
        ["max_health", 10], ["speed", 50], ["max_cargo", 10]]
}

ship_type = {
    #Name, Price, Cannons, Cargo, Crew, Speed, Health, Damage Reduction
    None: [0, 0, 0, 0, 0, 0, 0],
    "Schooner": [1400, 10, 50, 20, 30, 18, 0],
    "Galleon": [800, 10, 30, 20, 14, 14, 0],
    "War Galleon": [5000, 50, 100, 100, 30, 50, .1],
    "Flying Dutchman": [140000, 100, 1400, 250, 140, 140, .42]
}


port_prices = {
    # initial, mu, sell_price
    "Spices": [30, 3, .8],
    "Cannons": [100, 10, .8],
    "Tea": [40, 5, .8],
    "Contraband": [400, 40, .8],
    "Fruit": [60, 8, .8],
    "Textiles": [40, 5, .8]
}

list_ports = ["Barbados", "Bermuda", "Bahamas", "Tortuga"]

crew_price = [1, 5]