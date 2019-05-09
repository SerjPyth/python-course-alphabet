from __future__ import annotations
import math


class Cat:
    """
    Write Class Cat which will receive age from user
    * Add to class average_speed variable which will get it's values
      from private method _set_average_speed()

    * Add to class saturation_level variable with value 50

    * Implement private methods _increase_saturation_level and _reduce_saturation_level
      that will receive value and add/subtract from saturation_level this value
      if saturation_level is less than 0, return 0
      if saturation_level is grosser than 100, return 100

    * Implement method eat which will receive from user product value
      if product eq fodder use _increase_saturation_level with value eq 10
      if product eq apple use _increase_saturation_level with value eq 5
      if product eq milk use _increase_saturation_level with value eq 2

    * Implement private method _set_average_speed
      if age less or eq 7 return 12
      if age between 7(not including) and 10(including) return 9
      if age grosser than 10(not including) return 6

    * Implement method run it receives hours value
      Calculate run km per hours remember that you have average_speed value
      Than if your cat run less or eq than 25 _reduce_saturation_level with value 2
      if it runs between 25(not including) and 50(including) than _reduce_saturation_level with value 5
      if it runs between 50(not including) and 100(including) than _reduce_saturation_level with value 15
      if it runs between 100(not including) and 200(including) than _reduce_saturation_level with value 25
      if it runs more than 200(not including) than _reduce_saturation_level with value 50

      return text like this: f"Your cat ran {ran_km} kilometers"

    * Implement get_saturation_level and return saturation_level
      if saturation_level eq 0 return text like this: "Your cat is died :("

    * Implement get_average_speed and return average_speed

    """

    def __init__(self, age):
        self.age = age
        self.average_speed = self._set_average_speed()
        self.saturation_level = 50

    def eat(self, product):
        if product is "fodder":
            self._increase_saturation_level(10)
        elif product is "apple":
            self._increase_saturation_level(5)
        elif product is "milk":
            self._increase_saturation_level(2)
        else:
            print("I won`t eat that!")

    def _reduce_saturation_level(self, value):
        self.saturation_level = self.saturation_level - value
        if self.saturation_level > 0:
            return self.saturation_level
        else:
            self.saturation_level = 0
            return self.saturation_level

    def _increase_saturation_level(self, value):
        self.saturation_level = self.saturation_level + value
        if self.saturation_level < 100:
            return self.saturation_level
        else:
            self.saturation_level = 100
            print("Stop it! I`m getting chunky.")
            return self.saturation_level

    def _set_average_speed(self):
        if self.age <= 7:
            return 12
        elif 7 < self.age < 11:
            return 9
        else:
            return 6

    def run(self, hours):
        ran_km = self.average_speed * hours
        print(f"Your cat ran {ran_km} kilometers")
        if hours <= 25:
            self._reduce_saturation_level(2)
        elif 25 < hours < 51:
            self._reduce_saturation_level(5)
        elif 50 < hours < 101:
            self._reduce_saturation_level(15)
        elif 100 < hours < 201:
            self._reduce_saturation_level(25)
        else:
            self._reduce_saturation_level(50)

    def get_saturation_level(self):
        if self.saturation_level > 0:
            return self.saturation_level
        else:
            print("Your cat is died :()")

    def get_average_speed(self):
        return self.average_speed


# a = Cat(12)
# print(a.get_saturation_level())
# print(a.run(5))
# print(a.get_average_speed())
# print(a.get_saturation_level())
# a.eat("milk")
# a.eat("banana")
# a.eat("fodder")
# a.eat("fodder")
# a.eat("fodder")
# a.eat("fodder")
# a.eat("apple")
# a.eat("apple")
# print(a.get_saturation_level())


class Cheetah(Cat):
    """
    * Inherit from class Cat

    * Redefine method eat from parent class it will receive product value
      if product eq gazelle use _increase_saturation_level from parent class with value 30
      if product eq rabbit use _increase_saturation_level from parent class with value 15

    * Redefine method _set_average_speed
      if age less or eq 5 return 90
      if age between 5 and 15(including) return 75
      if age grosser 15(not including) return 40

    """
    def eat(self, product):
        if product is "gazelle":
            self._increase_saturation_level(30)
        elif product is "rabbit":
            self._increase_saturation_level(15)
        else:
            print("I won`t eat that!")

    def _set_average_speed(self):
        if self.age <= 5:
            return 90
        elif 5 < self.age < 16:
            return 75
        else:
            return 40


class Wall:
    """
    * Implement class Wall which receives such parameters: width and height

    * Implement method wall_square which return result of simple square formula of rectangle

    * Implement method number_of_rolls_of_wallpaper which receives such parameters: roll_width_m, roll_length_m
      (_m in the parameters name means meters) return number of rolls of wallpaper

      Example:
          count of lines in roll eq roll length in meters divide height of the wall (use rounding down)
          count of lines eq width of the wall divide roll width in meters
          number of rolls of wallpaper eq count of lines divide count of lines in roll
    """

    def __init__(self, width, height):
        self.width = float(width)
        self.height = float(height)

    def wall_square(self):
        return self.width * self.height

    def number_of_rolls_of_wallpaper(self, roll_width_m, roll_length_m):
        roll_h = math.floor(roll_length_m / self.height)
        roll_w = self.width / roll_width_m
        rolls = roll_w / roll_h
        return math.ceil(rolls)


# w = Wall(15, 5)
# print(w.wall_square())
# print(w.number_of_rolls_of_wallpaper(1, 10))


class Roof:
    """
        * Implement class Roof which receives such parameters: width, height and roof_type

        * Implement method roof_square that returns square of the roof
          if roof_type eq "gable" the roof square if simple rectangle square formula multiplied 2
          if roof_type eq "single-pitch" the roof square if simple rectangle square formula
          if other roof_type raise ValueError like this "Sorry there is only two types of roofs"

    """

    def __init__(self, width, height, roof_type):
        self.width = width
        self.height = height
        self.roof_type = roof_type

    def roof_square(self):
        if self.roof_type is "gable":
            return (self.width * self.height) * 2
        elif self.roof_type is "single_pitch":
            return self.width * self.height
        else:
            print("Sorry there is only two types of roofs")
            raise ValueError


# c = Roof(3, 10, "strpitch")
# print(c.roof_square())


class Window:
    """
       * Implement class Window which receives such parameters: width and height

       * Implement method window_square which return result of simple square formula of rectangle

    """
    def __init__(self, width, height):
        self.width = float(width)
        self.height = float(height)

    def window_square(self):
        return self.width * self.height

# w = Window(2, 1.5)
# print(w.window_square())


class Door:
    """
     * Implement class Door which receives such parameters: width and height
      add variables wood_price eq 10, metal_price eq 3

     * Implement method door_square which return result of simple square formula of rectangle

     * Implement method door_price which receives material value as a parameter
       if material eq wood return door_square multiplied on wood_price
       if material eq metal return door_square multiplied on metal_price
       if material value is another one (not metal or wood) raise ValueError "Sorry we don't have such material"

     *  Implement method update_wood_price which receives new_price value and updates your old price

     *  Implement method update_metal_price which receives new_price value and updates your old price

    """
    def __init__(self, width, height):
        self.width = float(width)
        self.height = float(height)
        self.wood_price = 10
        self.metal_price = 3

    def door_square(self):
        return self.width * self.height

    def door_price(self, material):
        if material is "wood":
            return self.wood_price * self.door_square()
        elif material is "metal":
            return self.metal_price * self.door_square()
        else:
            print("Sorry we don`t have such material")
            raise ValueError

    def update_wood_price(self, new_price):
        self.wood_price = new_price
        return self.wood_price

    def update_metal_price(self, new_price):
        self.metal_price = new_price
        return self.metal_price


# d = Door(1.5, 2)
# print(d.door_square())
# print(d.door_price("bro"))
# d.update_metal_price(5)
# print(d.door_price("metal"))


class House:
    """
    !!!! DON'T WRITE NEW METHODS TO THIS CLASS EXCEPT FOR THOSE LISTED BELOW !!!

    * Add super private variable __walls and its value will be empty list
    * Add super private variable __windows and its value will be empty list
    * Add super private variable __roof and its value will be None
    * Add super private variable __door and its value will be None

    * Implement method create_wall which will create new wall using class Wall and add it to the __walls list
      it receives parameters width and height
      if width or height eq 0 raise ValueError "Value must be not 0"
      if user have more than 4 walls raise ValueError "Our house can not have more than 4 walls"

    * Implement method create_roof which will create new roof using class Roof and assign it to the __roof variable
      it receives parameters width, height and roof_type
      if width or height eq 0 raise ValueError "Value must be not 0"
      Check that we won't have another roof if we already have another one,
              otherwise raise ValueError "The house can not have two roofs"

    * Implement method create_window which will create new window using class Window and add it to the __windows list
      it receives parameters width and height
      if width or height eq 0 raise ValueError "Value must be not 0"

    * Implement method create_door which will create new door using class Door and assign it to the __door variable
      it receives parameters width and height
      if width or height eq 0 raise ValueError "Value must be not 0"
      Check that we won't have another door if we already have another one,
              otherwise raise ValueError "The house can not have two doors"

    * Implement method get_count_of_walls that returns count of walls

    * Implement method get_count_of_windows that returns count of windows

    * Implement method get_door_price that receives material value and returns price of the door

    * Implement method update_wood_price that receives new_wood_price and updates old one

    * Implement method update_metal_price that receives new_metal_price and updates old one

    * Implement method get_roof_square that returns the roof square

    * Implement method get_walls_square that returns sum of all walls square that we have

    * Implement method get_windows_square that returns sum of all windows square that we have

    * Implement method get_door_square that returns the square of the door

    * Implement method get_number_of_rolls_of_wallpapers that returns sum of the number of rolls of wallpapers
      needed for all our walls
      it receives roll_width_m, roll_length_m parameters
      Check if roll_width_m or roll_length_m eq 0 raise ValueError "Sorry length must be not 0"

    * Implement method get_room_square that returns the square of our room
      (from walls_square divide windows and door square)

    """

    def __init__(self):
        self.__walls = []
        self.__windows = []
        self.__roof = None
        self.__door = None

    def create_wall(self, width, height):
        wa = Wall(width, height)
        if width is 0 or height is 0:
            print("Value must not be 0")
        elif self.get_count_of_walls() > 4:
            print("Our house can not have more than 4 walls")
        else:
            self.__walls.append(wa)

    def create_roof(self, width, height, roof_type):
        r = Roof(width, height, roof_type)
        if width is 0 or height is 0:
            print("Value must not be 0")
        elif self.__roof is not None:
            print("The house can not have two roofs")
        else:
            self.__roof = r

    def create_window(self, width, height):
        wi = Window(width, height)
        if width is 0 or height is 0:
            print("Value must not be 0")
        else:
            self.__windows.append(wi)

    def create_door(self, width, height):
        do = Door(width, height)
        if width is 0 or height is 0:
            print("Value must not be 0")
        elif self.__door is not None:
            print("The house can not have two doors")
        else:
            self.__door = do

    def get_count_of_walls(self):
        return len(self.__walls)

    def get_count_of_windows(self):
        return len(self.__windows)

    def get_door_price(self, material):
        return Door.door_price(self.__door, material)

    def update_wood_price(self, new_price):
        return Door.update_wood_price(self.__door, new_price)

    def update_metal_price(self, new_price):
        return Door.update_metal_price(self.__door, new_price)

    def get_roof_square(self):
        return Roof.roof_square(self.__roof)

    def get_walls_square(self):
        total = []
        for wall in self.__walls:
            single = Wall.wall_square(wall)
            total.append(single)
        return sum(total)

    def get_windows_square(self):
        total = []
        for window in self.__windows:
            single = Window.window_square(window)
            total.append(single)
        return sum(total)

    def get_door_square(self):
        return Door.door_square(self.__door)

    def get_number_of_rolls_of_wallpapers(self, roll_width_m, roll_length_m):
        total = []
        if roll_width_m is 0 or roll_length_m is 0:
            print("Sorry length must be not 0")
        else:
            for wall in self.__walls:
                single = Wall.number_of_rolls_of_wallpaper(wall, roll_width_m, roll_length_m)
                total.append(single)
            return sum(total)

    def get_room_square(self):
        return self.get_walls_square() - (self.get_windows_square() + self.get_door_square())


h = House()
h.create_wall(5, 10)
h.create_wall(1, 10)
h.create_wall(5, 10)
h.create_wall(5, 10)
# h.create_wall(5, 10)
# print(h.get_count_of_walls())
h.create_roof(10, 5, "single_pitch")
# h.create_roof(10, 5, "single_sided")
# h.create_roof(0, 5, "single_sided")
h.create_window(1, 2)
# print(h.get_count_of_windows())
h.create_window(1, 3)
# h.create_window(0, 2)
# print(h.get_count_of_windows())
h.create_door(2, 1.5)
# h.create_door(0, 1.5)
# h.create_door(2, 1.5)
h.get_door_price("wood")
# print(h.get_door_price("wood"))
# print(h.get_door_price("metal"))
h.update_wood_price(5)
# print(h.get_door_price("wood"))
# print(h.get_roof_square())
print(h.get_walls_square())
print(h.get_windows_square())
print(h.get_door_square())
# print(h.get_number_of_rolls_of_wallpapers(1, 10))
print(h.get_room_square())