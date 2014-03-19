cargo = ["Spices", "Cannons", "Tea", "Contraband", "Fruit", "Textiles"]

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

new_port = {
    #Name: [Generation Dictionary, Demand Dictionary, Coordinates]
    "Barbados": [
        {"Cannons":100, "Contraband":2, "Fruit":500,
            "Textiles":300, "Tea":400, "Spices":80},
        {"Cannons":100, "Contraband":100, "Fruit":100,
            "Textiles":100, "Tea":100, "Spices":100},
        [13.1667, 59.5500]
    ],
    "Bermuda": [
        {"Cannons":100, "Contraband":100, "Fruit":100,
            "Textiles":100, "Tea":100, "Spices":100},
        {"Cannons":100, "Contraband":100, "Fruit":100,
            "Textiles":100, "Tea":100, "Spices":100},
        [32.3333, 64.7500]
    ],
    "Bahamas": [
        {"Cannons":10, "Contraband":80, "Fruit":50,
            "Textiles":200, "Tea":50, "Spices":150},
        {"Cannons":100, "Contraband":100, "Fruit":100,
            "Textiles":100, "Tea":100, "Spices":100},
        [23.9167, 77.6667]
    ],
    "Tortuga": [
        {"Cannons":300, "Contraband":400, "Fruit":30,
            "Textiles":20, "Tea":10, "Spices":40},
        {"Cannons":100, "Contraband":100, "Fruit":100,
            "Textiles":100, "Tea":100, "Spices":100},
        [10.9317, 65.3081]
    ],

}

port_prices = {
    # Initial, sigma, sell price coefficient, min, max
    "Spices": [30, 3, .8, 10, 60],
    "Cannons": [100, 10, .8, 30, 200],
    "Tea": [40, 5, .8, 10, 80],
    "Contraband": [400, 40, .8, 200, 800],
    "Fruit": [60, 8, .8, 20, 120],
    "Textiles": [40, 5, .8, 4, 65]
}

list_ports = ["Barbados", "Bermuda", "Bahamas", "Tortuga"]

crew_price = [1, 5]