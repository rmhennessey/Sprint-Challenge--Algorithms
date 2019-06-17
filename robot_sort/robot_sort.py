# Understand the Problem
    # we want to sort a list of numbers
    # we can move LEFT or RIGHT
        # we cannot move past 0 on the LEFT
        # we know what our POSITION is
    # we can pick 1 item up at a time
        # if we are holding an item & try to pick up another, we SWAP
    # we can COMPARE items
        # if held > listed, RETURN 1
        # if held is < listed, RETURN -1
        # if held == listed, RETURN 0
    # we have a light that acts as a TRUE or FALSE
        # THINK: WHILE TRUE...

# Plan
    # we want to pick up the item in front of us
    # we want to move one space RIGHT 
        # we cannot move LEFT to start
    # we want to compare held item to listed item
        # if held item is > listed then compare_item == 1
            # make a SWAP
            # move LEFT 1 space & put the item down (using SWAP)
                # move RIGHT 1 space & START LOOP OVER
                    # to start loop over, use the LIGHT_ON TRUE/FALSE
        # if held item is < listed then compare_item == -1
            # move LEFT 
            # put item down in empty spot (using SWAP)
            # move RIGHT
            # pick up item (using SWAP)
        # if held item == listed, then compare_item == 0
            # move LEFT 
            # put item down in empty spot (using SWAP)
            # move RIGHT
    # move RIGHT until we cannot go any farther
    # start to move LEFT





class SortingRobot:
    def __init__(self, l):
        """
        SortingRobot takes a list and sorts it.
        """
        self._list = l          # The list the robot is tasked with sorting
        self._item = None       # The item the robot is holding
        self._position = 0      # The list position the robot is at
        self._light = "OFF"     # The state of the robot's light
        self._time = 0          # A time counter (stretch)

    def can_move_right(self):
        """
        Returns True if the robot can move right or False if it's
        at the end of the list.
        """
        return self._position < len(self._list) - 1

    def can_move_left(self):
        """
        Returns True if the robot can move left or False if it's
        at the start of the list.
        """
        return self._position > 0

    def move_right(self):
        """
        If the robot can move to the right, it moves to the right and
        returns True. Otherwise, it stays in place and returns False.
        This will increment the time counter by 1.
        """
        self._time += 1
        if self._position < len(self._list) - 1:
            self._position += 1
            return True
        else:
            return False

    def move_left(self):
        """
        If the robot can move to the left, it moves to the left and
        returns True. Otherwise, it stays in place and returns False.
        This will increment the time counter by 1.
        """
        self._time += 1
        if self._position > 0:
            self._position -= 1
            return True
        else:
            return False

    def swap_item(self):
        """
        The robot swaps its currently held item with the list item in front
        of it.
        This will increment the time counter by 1.
        """
        self._time += 1
        # Swap the held item with the list item at the robot's position
        self._item, self._list[self._position] = self._list[self._position], self._item

    def compare_item(self):
        """
        Compare the held item with the item in front of the robot:
        If the held item's value is greater, return 1.
        If the held item's value is less, return -1.
        If the held item's value is equal, return 0.
        If either item is None, return None.
        """
        if self._item is None or self._list[self._position] is None:
            return None
        elif self._item > self._list[self._position]:
            return 1
        elif self._item < self._list[self._position]:
            return -1
        else:
            return 0

    def set_light_on(self):
        """
        Turn on the robot's light
        """
        self._light = "ON"
    def set_light_off(self):
        """
        Turn off the robot's light
        """
        self._light = "OFF"
    def light_is_on(self):
        """
        Returns True if the robot's light is on and False otherwise.
        """
        return self._light == "ON"

    def sort(self):
        """
        Sort the robot's list.
        """
        # Fill this out

        # use SWAP to pick up first item and then move to right
        self.swap_item()
        self.move_right()

        # when SWAP happens, set_light_on to begin loop
        self.set_light_on()

        # light on == swap happened, so we run through
        while self.light_is_on():
            # turn light off so we can turn back on when SWAPS happen
            self.set_light_off()

            # we want to start moving right until we can't
            while self.can_move_right():
                # picking up item means we also make an empty slot
                # once we pick up, we want to move right to compare
                self.swap_item()
                self.move_right()

                # compare held to listed item (listed item = item in front of us)
                # if held > listed, SWAP
                # move LEFT to SWAP newly held item into empty slot
                # move RIGHT to start loop over (turn the light on)
                if self.compare_item() == 1:
                    self.swap_item()
                    self.move_left()
                    self.swap_item()
                    self.move_right()
                    self.set_light_on()

                # if held is < listed, move LEFT 
                # SWAP to put down
                # move RIGHT
                # made it a little DRY-er since held < listed & held == are same
                if self.compare_item() == -1 or self.compare_item() == 0:
                    self.move_left()
                    self.swap_item()
                    self.move_right()

                # if held item == listed
                # move LEFT to put back down
                # move RIGHT to start over
                # if self.compare_item() == 0:
                #     self.move_left()
                #     self.swap_item()
                #     self.move_right()

            # once we can't go RIGHT any more, move LEFT
            if self.light_is_on():
                while self.can_move_left():
                    self.move_left()


if __name__ == "__main__":
    # Test our your implementation from the command line
    # with `python robot_sort.py`

    l = [15, 41, 58, 49, 26, 4, 28, 8, 61, 60, 65, 21, 78, 14, 35, 90, 54, 5, 0, 87, 82, 96, 43, 92, 62, 97, 69, 94, 99, 93, 76, 47, 2, 88, 51, 40, 95, 6, 23, 81, 30, 19, 25, 91, 18, 68, 71, 9, 66, 1, 45, 33, 3, 72, 16, 85, 27, 59, 64, 39, 32, 24, 38, 84, 44, 80, 11, 73, 42, 20, 10, 29, 22, 98, 17, 48, 52, 67, 53, 74, 77, 37, 63, 31, 7, 75, 36, 89, 70, 34, 79, 83, 13, 57, 86, 12, 56, 50, 55, 46]

    robot = SortingRobot(l)

    robot.sort()
    print(robot._list)