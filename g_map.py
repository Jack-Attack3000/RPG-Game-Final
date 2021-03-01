# Course: CS 30
# Period: 1
# Date Created: 21/02/28
# Date Last Modified: 21/02/28
# Name: Jack Anderson
# Description: Classes for the map and location


class Location:
    def __init__(self, name, description, inv_item, chara, exits):
        self.name = name
        self.description = description
        self.chara = chara
        self.inv_item = inv_item
        self.exits = exits

    def print_loc(self):
        """Prints out location and info"""
        print(f"You are now in the {self.name}")
        print(f"{self.description}.")
        print(f"{self.chara} is here")
        print(f"There's a {self.inv_item} in here.")
        print(f"There are exits {self.exits}.")


class GMap:
    def __init__(self, loc_list):
        self.loc_list = loc_list
        self.game_map = []
        self.player_start = ''
        self.restart()

    def restart(self):
        """Restarts the game map"""
        row = 0
        column = 0
        row_vals = []
        col_vals = []
        for location in self.loc_list:
            if location.chara == 'player':
                self.player_start = location
            col_vals.append(location)
            column = column + 1
            if column > 2:
                row_vals.append(col_vals)
                col_vals = []
                row = row + 1
                column = 0
        self.game_map = row_vals

    def move_direction(self, player_loc, direction):
        """Moves player around"""
        exit_found = False
        for exit in player_loc.exits:
            if exit == direction:
                exit_found = True
                break

        if exit_found is False:
            print("You run into a wall. Maybe try a different direction")
        else:
            print(f"You move {direction}")

        found_row = 0
        found_col = 0
        for row in range(3):
            for col in range(3):
                if self.game_map[row][col].name == player_loc.name:
                    found_row = row
                    found_col = col
                    break;
    
        if direction == "up":
            found_row = found_row - 1
        elif direction == "down":
            found_row = found_row + 1
        elif direction == "right":
            found_col = found_col + 1
        elif direction == "left":
            found_col == found_col - 1
        else:
            print(f"{direction} is not a direction")
        
        return self.game_map[found_row][found_col]
