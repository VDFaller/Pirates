from PyQt5 import QtGui, QtCore, QtWidgets
import sys
import UI.MainUI
import Logic
import Config
import random
import shelve
import time
import UI.Buy_Cargo
from functools import partial


class MainWindow(QtWidgets.QMainWindow, UI.MainUI.Ui_MainWindow):
    """The Main Window where everything happens"""
    def __init__(self, parent=None):
        """Initializes shit (Don't use partial as most of the variables
        aren't created yet)"""
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.btn_hire_crew.clicked.connect(
            lambda: self.game.current_player.hire_crew(self))
        self.btn_fire_crew.clicked.connect(
            lambda: self.game.current_player.fire_crew(self))
        self.btn_to_pier.clicked.connect(self.to_pier)
        self.btn_to_pier_2.clicked.connect(self.to_pier)
        self.btn_to_pe.clicked.connect(self.to_pe)
        self.btn_to_shipyard.clicked.connect(self.to_shipyard)
        self.btn_buy_ship.clicked.connect(
            lambda: self.game.current_player.buy_ship(self))
        self.actionExit.triggered.connect(self.save_game)
        self.actionNew.triggered.connect(self.new_game)
        self.actionLoad.triggered.connect(self.load_game)
        self.btn_debug.clicked.connect(self.debug)
        self.lE_debug.returnPressed.connect(self.debug)
        self.btn_buy_cargo.clicked.connect(
            lambda: self.game.current_player.buy_cargo(self))
        self.btn_sail.clicked.connect(
                lambda: self.game.sail(self))
        self.btn_sell_cargo.clicked.connect(
            lambda: self.game.current_player.sell_cargo(self))
        self.btn_buy_repair.clicked.connect(
            lambda: self.game.current_player.buy_repair(self))
        self.btn_diy_repair.clicked.connect(
            lambda: self.game.current_player.repair(self))
        self.btn_equip_cannons.clicked.connect(
            lambda: self.game.current_player.ship.equip_cannons(self))
        self.btn_unequip_cannons.clicked.connect(
            lambda: self.game.current_player.ship.unequip_cannons(self))
        self.btn_next_ship.clicked.connect(lambda: self.change_ship("next"))
        self.btn_prev_ship.clicked.connect(lambda: self.change_ship("prev"))
        self.btn_buy.clicked.connect(
            lambda: self.game.current_player.purchase_ship(self))
        self.btn_back_to_SY.clicked.connect(
            lambda: self.game.current_player.cancel_purchase_ship(self))

    def debug(self):
        """So I can figure shit out"""
        setup = self.lE_debug.text()
        if setup.lower() == "cheat":
            self.game.current_player.money += 10000
            self.game.current_player.ship.cannons += 20
            self.game.current_player.crew.number += 40
            self.textBrowser.append("Fucking cheater!")
        elif setup.lower()[:4] == "run ":
            eval(setup[4:])
        else:
            add = "self.textBrowser.append(str(" + self.lE_debug.text() + "))"
            eval(add)

    def change_ship(self, direction, setting=True):
        """Changes which ship you are choosing to buy"""
        if setting is True:
            current = self.H_Ship_Name.text()
            list1 = list(Config.ship_type.keys())
            list1.remove(None)
            boop = list1.index(current)
            if direction == "next":
                new = list1[(boop + 1) % len(list1)]
            elif direction == "prev":
                new = list1[boop - 1]
        else:
            new = setting
        self.H_Ship_Name.setText(new)
        self.V_Price.setText(str(Config.ship_type[new][0]))
        self.V_Cannon.setText(str(Config.ship_type[new][1]))
        self.V_Cargo.setText(str(Config.ship_type[new][2]))
        self.V_Crew.setText(str(Config.ship_type[new][3]))
        self.V_Speed.setText(str(Config.ship_type[new][4]))
        self.V_Health.setText(str(Config.ship_type[new][5]))
        self.ship_pic.setPixmap(QtGui.QPixmap(":/icons/" + new + ".jpg"))

    def to_pier(self):
        """Travel to pier"""
        self.stackedWidget.setCurrentIndex(1)

    def to_pe(self):
        """Travel to Pirate Emporium"""
        self.stackedWidget.setCurrentIndex(3)

    def to_shipyard(self):
        """Travel to Shipyard"""
        self.stackedWidget.setCurrentIndex(2)

    def exitApp(self):
        """Shitty way to quit"""
        sys.exit(0)

    def new_game(self):
        """Runs tha actual Game"""
        self.game = Game(self)
        self.game.play(self)

    def save_game(self):
        """DOESN'T SAVE"""
        saved = shelve.open("saves/the_only")
        saved["Game_var"] = self.game
        saved.close()

    def load_game(self):
        """DOESN'T LOAD"""
        saved = shelve.open("saves/the_only")
        self.game = saved["Game_var"]
        saved.close()
        self.stackedWidget.setCurrentIndex(1)


class Game(object):
    """The Game Class"""
    def __init__(self, window):
        """The Obvious"""
        self.window = window
        self.makeshitgo = True
        super(Game, self).__init__()
        self.turn = 1
        self.num_players = 1
        """Makes ports and players"""
        self.ports = Logic.instance_ports(Config.list_ports)
        self.players = Logic.initiate_players(self.num_players,
            self.ports, window)
        self.npc = [Logic.Player("Galleon",
            Logic.Port("Bermuda"), "Blackbeard")]
        window.InfoBar.show()

    def play(self, window):
        """starts the game"""
        while self.makeshitgo:
            for i in self.ports:
                self.ports[i].change_prices()
            window.textBrowser.append("Turn {}".format(self.turn))
            for i in self.players:
                window.to_pier()
                self.myturn = True
                i.pay_crew(window)
                self.current_player = i
                window.stackedWidget.setCurrentIndex(1)
                window.Welcome.setText("Welcome to {}".format(i.port.name))
                if i.turn_loss > 0:
                    self.textBrowser.append("You still have {} turns to wait"
                        .format(i.turn_loss))
                    i.turn_loss -= 1
                    self.myturn = False
                elif i.ship.name is None:
                    i.buy_ship(window)
                while self.myturn:
                    QtWidgets.qApp.processEvents()
                    self.current_player.update_cargo(window)
                    time.sleep(.05)
            self.turn += 1

    def sail(self, window):
        """Ends turn and Goes somewhere else,
        percent chance for random encounter"""
        self.current_player.port = self.ports[random.choice(Config.list_ports)]
        p2 = self.npc[0]
        if random.random() > .8:  # 20% Chance to fight
            self.battle = Battle(self.current_player, p2, window)
        else:
            self.myturn = False

    def mutiny(player):
        """Has the crew mutiny against you and throw you off your ship"""
        print("Oh shit, the crew is mutinying")
        print("I guess you're fucked.")
        player.ship = Logic.Ship(None)

    def trade_ships(p1, p2):
        """I want to take the ship and as much cargo as I can hold then give
        the other player my current ship"""
        """Fix this"""
        temp_ship = p1.ship
        temp_inv = [p1.ship.cannons, p1.ship.cargo]
        temp2_inv = [p2.ship.cannons, p2.ship.cargo]
        p1.ship = p2.ship
        p1.ship.cannons, p1.ship.cargo = temp_inv
        p2.ship = temp_ship
        p2.ship.cannons, p2.ship.cargo = temp2_inv
        return True


class Cargo_UI(QtWidgets.QDialog, UI.Buy_Cargo.Ui_Dialog):
    """The Dialog for initiation"""
    def __init__(self, player, window, trade):
        """Just initiate"""
        super().__init__()
        self.window = window
        self.player = player
        self.setupUi(self)
        self.trade = trade
        # initiates all the buttons and sets up buy/sell prices
        for i in Config.port_prices:
            up = getattr(self, "btn_" + i + "_up")
            up.clicked.connect(partial(self.up, i))
            down = getattr(self, "btn_" + i + "_down")
            down.clicked.connect(partial(self.down, i))
            add_price = getattr(self, "H_" + i)
            if trade == "buy":
                add_price.setText(i +
                    " (" + str(self.player.port.price[i]) + ")")
            elif trade == "sell":
                add_price.setText(i +
                    " (" + str(self.player.port.sell_price[i]) + ")")
        self.buttonBox.accepted.connect(
            partial(self.accept_, self.player, self.window))

    def count_cargo(self, player):
        """counts total cargo selected as well as on ship"""
        want = int(self.V_Cannons.text()) + \
            int(self.V_Contraband.text()) + \
            int(self.V_Spices.text()) + \
            int(self.V_Fruit.text()) + \
            int(self.V_Textiles.text()) + \
            int(self.V_Tea.text())
        have = sum(player.ship.cargo.values())
        cargo = want + have
        return cargo

    def up(self, item):
        """makes selects direction of button with some error checking"""
        total_cargo = self.count_cargo(self.player)
        total_cost = int(self.V_Total.text())
        label = getattr(self, "V_" + str(item))
        current = int(label.text())
        if self.trade == "buy":
            price = self.player.port.price[item]
            okaygo = total_cargo < self.player.ship.max_cargo
            no_str = "That's max cargo"
        elif self.trade == "sell":
            price = self.player.port.sell_price[item]
            #just to make sure you have enough 'item' to sell
            okaygo = self.player.ship.cargo[item] > current
            no_str = "You have no more to sell"
        if  okaygo:
            label.setNum(current + 1)
            self.V_Total.setNum(total_cost + price)
        else:
            self.window.textBrowser.append(no_str)

    def down(self, item):
        """easier for down"""
        total_cost = int(self.V_Total.text())
        label = getattr(self, "V_" + item)
        if self.trade == "buy":
            price = self.player.port.price[item]
        elif self.trade == "sell":
            price = self.player.port.sell_price[item]
        current = int(label.text())
        if current > 0:
            label.setNum(current - 1)
            self.V_Total.setNum(total_cost - price)

    def accept_(self, player, window):
        """checks for enough money and buys/sells"""
        if self.trade == "buy":
            if int(self.V_Total.text()) <= player.money:
                for i in player.ship.cargo:
                    num = int(getattr(self, "V_" + i).text())
                    player.ship.cargo[i] += num
                window.to_pe()
                player.change_money("down",
                    int(self.V_Total.text()), window)
                self.close()
            else:
                window.textBrowser.append("Go get more moolah")
        if self.trade == "sell":
            for i in player.ship.cargo:
                num = int(getattr(self, "V_" + i).text())
                player.ship.cargo[i] -= num
            player.change_money("up", int(self.V_Total.text()), window)
            window.to_pe()
            self.close()


class Battle(object):
    """When You need to battle."""
    def __init__(self, p1, p2, window):
        """Starts a battle loop"""
        super(Battle, self).__init__()
        self.p1 = p1
        self.p2 = p2
        self.window = window
        if p2.name == "Blackbeard":
            p2.ship = Logic.Ship("Galleon")
            p2.ship.random_ship()
            p2.crew.number = p2.ship.cannons * 2
        window.stackedWidget.setCurrentIndex(5)
        try:
            window.btn_attack.clicked.disconnect()
            window.btn_flee.clicked.disconnect()
            window.btn_board.clicked.disconnect()
        except:
            pass
        window.btn_attack.clicked[()].connect(lambda x=p1, y=p2:
            self.attack(x, y, window))
        window.btn_flee.clicked[()].connect(lambda x=p1, y=p2: [
            self.flee(x, y, window), self.attack(y, x, window, False)])
        window.btn_board.clicked[()].connect(lambda x=p1, y=p2: [
            self.board(x, y, window), self.attack(y, x, window, False)])

    def attack(self, attacker, attackee, window, retaliate=True):
        """Fire Cannons"""
        if attacker.ship.cannons == 0 or attacker.crew.number == 0:
            if attacker == window.game.current_player:
                window.textBrowser.append(
                    "You have no cannons, prolly should run")
                window.textBrowser.append(
                    "cannons: " + str(attacker.ship.cannons))
                window.textBrowser.append(
                    "crew " + str(attacker.crew.number))
            else:
                window.textBrowser.append("He must not have cannons")
        else:
            damage = 0
            fireable = min(attacker.ship.cannons, attacker.crew.number)
            for i in range(fireable):
                if random.random() * 100 < attacker.crew.accuracy:
                    damage += 1
            damage = round(damage * (1 - attackee.ship.damage_red))
            attackee.ship.health -= damage
            window.textBrowser.append("{}'s ship has {} health left"
                .format(attackee.name, max(0, attackee.ship.health)))
            if attackee.ship.health <= 0:
                window.textBrowser.append("{} just got sunk".
                    format(attackee.name))
                attackee.ship = Logic.Ship(None)
                retaliate = False
                window.game.myturn = False
        if retaliate is True:
            self.attack(attackee, attacker, window, False)

    def flee(self, attacker, attackee, window):
        """Try to run"""
        flee_speed = attacker.ship.speed * attacker.stat_sailing *\
            random.randint(80, 100)
        chase_speed = attackee.ship.speed * attackee.stat_sailing *\
            random.randint(80, 100)
        if flee_speed >= chase_speed:
            window.textBrowser.append("You're escaping")
            window.game.myturn = False
        else:
            window.textBrowser.append("He's Gaining")

    def board(self, attacker, attackee, window):
        """Attempt to board"""
        if attacker.ship.health / attackee.ship.health > 1.5:
            window.textBrowser.append("You successfully boarded")
            self.pirate_cargo(attacker, attackee, window)
            window.game.myturn = False
        else:
            window.textBrowser.append("You can't board")

    def pirate_cargo(self, attacker, attackee, window):
        """Steals other ships cargo after boarding"""
        for i in attacker.ship.cargo:
            open_bays = sum(
                attacker.ship.cargo.values()) - attacker.ship.max_cargo
            if open_bays > 0:
                stolen = min(open_bays, attackee.ship.cargo[i])
                attacker.ship.cargo[i] += stolen
                window.textBrowser.append("You stole {} {}".format(
                    stolen, i))
            else:
                break


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    form = MainWindow()
    form.show()
    app.exec_()
