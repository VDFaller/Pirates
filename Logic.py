import random
import math
import Config
import sys
from PyQt5 import QtGui, QtCore, QtWidgets
from copy import deepcopy
import UI.NameCaptain
import time
from functools import partial


def test(Window):
    """Another Test"""
    Window.stackedWidget.setCurrentIndex(1)
    Window.Welcome.setText("Welcome to {}".format("Barbados"))


def sail_something(Window):
    """Some more testing shit"""
    Window.Welcome.setText("Now you're sailing to {}".format(
        Config.list_ports[random.randint(0, len(Config.list_ports) - 1)]))


def initiate_players(num_players, ports, window):
    """Creates a certain number of players and assigns them a port"""
    class name_player_dia(QtWidgets.QDialog, UI.NameCaptain.Ui_Dialog):
        """The Dialog for initiation"""
        def __init__(self):
            super(name_player_dia, self).__init__()
            self.setupUi(self)
    players = []
    for i in range(num_players):
        dia = name_player_dia()
        dia.label.setText("Player {}".format(i + 1))
        if dia.exec_() == QtWidgets.QDialog.Accepted:
            name = dia.lineEdit.text()
        each = Player(None, ports[random.choice(Config.list_ports)], name)
        players.append(each)
    return players


def instance_ports(port_list):
    """creates classes all ports in the port list
    and assigns players with the correct port for where they are"""
    ports = [Port(i) for i in port_list]
    port_dict = {ports[i].name: ports[i] for i in range(len(ports))}
    return port_dict


class Ship:
    """Ship with all the fun"""
    def __init__(self, name):
        self.name = name
        self.cost = Config.ship_type[name][0]
        self.max_cargo = Config.ship_type[name][2]
        self.max_crew = Config.ship_type[name][3]
        self.speed = Config.ship_type[name][4]
        self.max_health = Config.ship_type[name][5]
        self.health = self.max_health
        self.damage_red = Config.ship_type[name][6]
        self.max_cannons = Config.ship_type[name][1]
        self.cannons = 0
        self.cargo = {"Spices": 0,
            "Cannons": 0,
            "Tea": 0,
            "Contraband": 0,
            "Fruit": 0,
            "Textiles": 0
        }

    def random_ship(self):
        current_cargo = random.randint(0, self.max_cargo)
        while current_cargo > 0:
            sel_cargo = list(self.cargo.items())[random.choice(
                range(len(self.cargo)))][0]
            adder = random.randint(0, current_cargo)
            self.cargo[sel_cargo] += adder
            current_cargo -= adder
        self.cannons = random.randint(0, self.max_cannons)

    def upgrade_ship(self, i):
        """Upgrades ship based on the config available"""
        i = int(i)
        for x in range(1, len(Config.upgrade_items[i])):
            attribute = Config.upgrade_items[i][x][0]
            value = Config.upgrade_items[i][x][1]
            if hasattr(self, attribute):
                setattr(self, attribute, getattr(self, attribute) + value)
                self.cost += value
            else:
                #print(""""###Can't upgrade non-existent attribute '{}'
                    #.""".format(attribute))
                raise AttributeError(
                    """Can't upgrade non-existent attribute
                     '{}'.""".format(attribute)
                )

    def equip_cannons(self, window):  # no UI
        """Takes cannons out of cargo and puts them in bays"""
        if self.cargo["Cannons"] == 0:
            window.textBrowser.append("You have no cannons to equip")
        elif self.cannons == self.max_cannons:
            window.textBrowser.append("Cannon bays full")
        else:
            bays = self.max_cannons - self.cannons
            equipped = min(self.cargo["Cannons"], bays)
            self.cannons += equipped
            self.cargo["Cannons"] -= equipped
            window.textBrowser.append("{} cannons equipped".format(equipped))

    def unequip_cannons(self, window):  # no UI
        """cannons from bays to cargo"""
        if self.cannons == 0:
            window.textBrowser.append("No Cannons")
        elif sum(self.cargo.values()) == self.max_cargo:
            window.textBrowser.append("No Room")
        else:
            equip = min(self.max_cargo - sum(self.cargo.values()), self.cannons)
            self.cannons -= equip
            self.cargo["Cannons"] += equip
            window.textBrowser.append("{} cannons unequipped". format(equip))


class Player:
    def __init__(self, ship, port, name):
        """Starts the player off with 0 everything and 5000 deblunes"""
        self.name = name
        if self.name in ["Hollinger", "Dan", "Daniel", "Quadratix", "Quad"]:
            print("Hollinger, you sir are a douche")
            self.name = "My love"
        elif self.name.lower() in ["michelle", "mccune"]:
            self.name = "Dave"
        self.ship = Ship(ship)
        self.money = 5000
        self.port = port
        self.turn_loss = 0
        self.crew = Crew()
        self.port_location = "Pier"
        self.stat_sailing = .20
        self.stat_manuever = .20
        self.stat_board = .20
        self.stat_murder = .20

    def change_money(self, direction, amount, window):
        if direction == "up":
            self.money += amount
        elif direction == "down":
            self.money -= amount
        else:
            window.textBrowser.append("not 'up' or 'down'")

    def buy_cargo(self, window):
        #opens the buy cargo dialog
        dia = Game.Cargo_UI(self, window, "buy")
        dia.show()

    def sell_cargo(self, window):
        #opens the sell cargo dialog
        dia = Game.Cargo_UI(self, window, "sell")
        dia.show()

    def update_cargo(self, window):
        for i in self.ship.cargo:
            getattr(window, i).setNum(self.ship.cargo[i])
        window.Player_Name.setText(self.name)
        window.Crew.setNum(self.crew.number)
        window.V_Money.setNum(self.money)
        window.Eq_Cannons.setNum(self.ship.cannons)

    def buy_upgrade(self):  # old
        """Selects an upgrade, checks money then runs upgrade_ship"""
        print("Here are our available upgrades")
        print("You currently have {} deblunes".format(self.money))
        pprint(Config.upgrade_items, "Select", "Name", "Description",
            "Cost", sub=True)
        print("Please choose an upgrade to purchase.")
        try:
            i = int(input())
            if i not in Config.upgrade_items:
                print("Sorry, That's not an option")
            elif self.money < Config.upgrade_items[i][0][2]:
                print("Are you trying to cheat me")
            else:
                self.ship.upgrade_ship(i)
        except ValueError:
            print("A number please")

    def hire_crew(self, window):  # basic
        self.crew.number = self.ship.max_crew
        self.crew.price = self.port.crew_price
        window.textBrowser.append("{} hired at ${}/day".format(
            self.crew.number, self.crew.price))

    def fire_crew(self, window):  # basic
        self.crew.number = 0
        self.crew.price = 0
        window.textBrowser.append("Fired all Crew")

    def pay_crew(self, window):  # Needs update
        """Pays your crew everyday"""
        if self.crew.number > 0:
            cost = self.crew.price * self.crew.number
            if self.money > cost:
                self.change_money("down", cost, window)
                window.textBrowser.append("Paid Crew ${}".format(cost))
                self.crew.attitude = min(self.crew.attitude + .5, 100)
            else:
                self.crew.attitude = max(self.crew.attitude - 5, 0)
                window.textBrowser.append("You can't afford your crew, UhOh")

    def buy_ship(self, window):
        """Stops execution until ok/cancel is pressed"""
        window.change_ship("NA", "Galleon")
        window.stackedWidget.setCurrentIndex(4)
        #window.fake = QtGui.QLabel(window.gridLayoutWidget)
        #window.fake.setText("FAKE!")
        #window.fake.setAlignment(QtCore.Qt.AlignCenter)
        #window.gridLayout.addWidget(window.fake, 5, 0, 1, 0)

    def purchase_ship(self, window):
        """buys the ship and updates money"""  # needs sell old ship
        if self.money < int(window.V_Price.text()):
            window.textBrowser.append("You can't afford that brokearse")
        elif sum(self.ship.cargo.values()) > int(window.V_Cargo.text()):
            window.textBrowser.append("You should sell some cargo first")
        else:
            temp = self.ship
            self.ship = Ship(window.H_Ship_Name.text())
            self.ship.cargo = temp.cargo
            self.change_money("down", self.ship.cost, window)
            window.textBrowser.append(self.ship.name)
            window.to_shipyard()

    def cancel_purchase_ship(self, window):
        """If you don't want to make a purchase"""
        if self.ship.name is None:
            window.textBrowser.append("You need a ship")
        else:
            window.to_shipyard()

    def repair(self, window):  # no UI
        """Use time to repair your ship"""
        time = math.floor((self.ship.max_health - self.ship.health) / 10)
        self.ship.health = self.ship.max_health
        self.turn_loss = time
        window.textBrowser.append("Losing {} turns".format(time))
        window.game.myturn = False

    def buy_repair(self, window):  # no UI
        """Use Money to Repair your ship"""
        cost = (self.ship.max_health - self.ship.health) * 10
        if self.money >= cost:
            self.money -= cost
            self.ship.health = self.ship.max_health
            window.textBrowser.append("Fixed, it cost {}".format(cost))
        else:
            window.textBrowser.append("Too Broke")


class Port:
    """Where all the port prices are kept"""
    def __init__(self, name):
        self.name = name
        self.price, self.sell_price, self.crew_price = self.make_prices()
        self.owner = None

    def make_prices(self):
        """creates the prices when the port is initiated"""
        price = {}
        for i in Config.port_prices:
            cost = math.floor(random.gauss(
                Config.port_prices[i][0],
                Config.port_prices[i][1]))
            price[i] = cost
        sell_price = deepcopy(price)
        for i in sell_price:
            sell_price[i] = math.floor(price[i] * Config.port_prices[i][2])
        crew_price = random.randint(Config.crew_price[0], Config.crew_price[1])
        return price, sell_price, crew_price

    def change_prices(self):
        """Changes the prices in the port based on current prices of the port"""
        for i in self.price:
            new_price = math.floor(random.gauss(self.price[i],
                Config.port_prices[i][1]))
            if new_price > Config.port_prices[i][4]:
                new_price = Config.port_prices[i][4]
            elif new_price < Config.port_prices[i][3]:
                new_price = Config.port_prices[i][3]
            self.price[i] = new_price
        self.sell_price = deepcopy(self.price)
        for i in self.sell_price:
            self.sell_price[i] = math.floor(self.price[i] *
                    Config.port_prices[i][2])
        self.crew_price = random.randint(Config.crew_price[0],
            Config.crew_price[1])


class Crew:
    #If I want crew to be more than just a number
    def __init__(self):
        self.number = 0
        self.attitude = 70
        self.accuracy = 20
        self.inebriation = 10
        self.price = 0

import Game
