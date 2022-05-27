#!/usr/bin/env python3
# Created by: Hunter Connolly
# Created on: May 15, 2022
# This program calculates the surface area and volume of a cone

import math


def calc_surface_area(radius, height):
    # calculate area
    surface_area = (
        math.pi * radius * (radius + math.sqrt((height**2) + (radius**2)))
    )

    # return the area
    return surface_area


def calc_volume(radius, height):
    # calculate area
    volume = math.pi * radius**2 * height / 3

    # return
    return volume


def main():
    # greet the user
    print("This program calculates the volume and surface area of a cone!")
    print("")
    play_again = input(
        "Would you like to calculate the surface area and volume of a cone? (y/n): "
    )

    while play_again == "y" or play_again == "yes":
        units = input("What units are you using? (mm, cm, etc.): ")
        # error check
        try:
            # get the radius and height
            radius_u = float(
                input("What is the radius of your cone? ({}): ".format(units))
            )
            height_u = float(
                input("What is the height of your cone? ({}): ".format(units))
            )
            print("")

            # call function
            surface_area = calc_surface_area(radius_u, height_u)
            volume = calc_volume(radius_u, height_u)

            # display the answers
            print(
                "The surface area of your cone is: {:.2f}{}^2".format(
                    surface_area, units
                )
            )
            print("The volume of your cone is: {:.2f}{}^3".format(volume, units))
            print()

            # ask the user if they want to play again
            play_again = input("Do you want to play again?: ")
            print("")

            # if they enter yes it will continue, if they enter anything
            # else, the program will end
            if play_again == "yes" or play_again == "y":
                continue
            else:
                print("Thanks for playing!!")
                break
        except:
            print("Invalid input please enter a valid number!")
            print()
            continue


if __name__ == "__main__":
    main()
