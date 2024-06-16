# Kristijan Mikulic WGU ID 012210225

import csv
import datetime
from HashTable import CreateHashTable
from Package import Package
from Truck import Truck

# Hash Table with package data
package_data = CreateHashTable()

# Hub Address
hub = "4001 South 700 East"

# Package load for Truck 1
# Since Truck 1 is the truck that will go right at 8AM all packages that need a non-EOD delivery and is
# not delayed due to flights will be loaded here.
package_load_1 = [1, 13, 14, 15, 16, 20, 29, 30, 31, 34, 37, 40]

# Package load for Truck 2
# Since there are packages that are delayed by flights this truck will take those packages and fill up the rest with
# optimal package delivery by having close by zip codes to packages that have to be on this truck
package_load_2 = [3, 6, 8, 11, 12, 17, 18, 22, 23, 24, 25, 26, 28, 32, 36, 38]

# Package load for Truck 3
# Since this truck will start later on it will take the package that has the incorrect address and whatever remaining
# packages are left.
package_load_3 = [2, 4, 5, 7, 9, 10, 19, 21, 27, 33, 35, 39]

# Truck 1
# Start time is at 8AM due to no restrictions
truck1 = Truck(1, package_load_1, 0, hub, datetime.timedelta(hours=8))

# Truck 2
# Start time is 9:05AM due to flight delaying packages
truck2 = Truck(2, package_load_2, 0, hub, datetime.timedelta(hours=9, minutes=5))

# Truck 3
# Start time is None due to restriction of only having two drivers
truck3 = Truck(3, package_load_3, 0, hub, datetime.timedelta(hours=10, minutes=20))

# Read the package csv
with open("./packages.csv") as packages:
    package_info = csv.reader(packages)
    package_info = list(package_info)

# Read the address csv and convert to list
with open("./addresses.csv") as addresses:
    address_info = csv.reader(addresses)
    address_info = list(address_info)

# Read the distance csv and convert to list
with open("./distances.csv") as distances:
    distance_info = csv.reader(distances)
    distance_info = list(distance_info)


# Returns the address id if address is found
def get_address(address):
    for row in address_info:
        if address in row[2]:
            return int(row[0])


# Returns the distance between two addresses
def get_address_distance(address_x, address_y):
    distance = distance_info[address_x][address_y]
    if distance == "":
        distance = distance_info[address_y][address_x]
    return float(distance)


# For each item in the package csv creates a package that is inserted into package_data the hash table
def load_package_data(data):
    # Loads each package from the csv
    for package_details in package_info:
        package_id = int(package_details[0])
        package_address = package_details[1]
        package_city = package_details[2]
        package_zip = package_details[4]
        package_weight = package_details[6]
        package_deadline = package_details[5]

        # Creates a package object for each package
        package = Package(package_id, package_address, package_city, package_zip, package_weight, package_deadline)

        # inserts the package into the hash table using the package id as the key.
        data.insert(package_id, package)


def deliver_packages(truck):
    truck_number = "Truck " + str(truck.get_truck_id())
    # Array of packages that need to be delivered
    packages_need_delivery = []
    # Iterate through the truck package load for each package
    for current_package in truck.get_package_load():
        # search the hashmap for each package and append it to the array
        package = package_data.lookup(current_package)
        package.set_truck_num(truck_number)
        package.set_truck_loaded(truck_number)
        packages_need_delivery.append(package)
    # Empty the truck package load
    truck.set_package_load([])
    while len(packages_need_delivery) > 0:
        # Start with an initial address of max value 9999
        next_address = 9999
        next_package = None
        # For each package that needs to be delivered find the one that is the nearest neighbor and set that as the
        # next package that needs to be delivered
        for cur_package in packages_need_delivery:
            distance = get_address_distance(get_address(truck.get_address()), get_address(cur_package.get_address()))
            # If the current distance is less than the last packages distance replace the last package with the new one
            if distance <= next_address:
                next_address = distance
                next_package = cur_package
        # Add the new package to the trucks package load
        truck.package_load.append(next_package.get_id())
        # Remove the package that has been delivered
        packages_need_delivery.remove(next_package)
        # Update the trucks milage
        truck.set_milage(truck.get_milage() + next_address)
        # Set the current address of the truck as the place the package was delivered
        truck.set_address(next_package.get_address())
        # Set the total time the truc has been out
        truck.time += datetime.timedelta(hours=next_address / truck.get_mph())
        # Set the time the package was delivered
        next_package.set_delivery_time(truck.get_time())
        # Set the trucks departure time as the delivery time of the package
        next_package.set_departure_time(truck.depart_time)
        # Change the status of the package
        next_package.set_status("Delivered")


class Main:
    # Load all the package data into the hash table
    load_package_data(package_data)
    # Start Truck 1
    deliver_packages(truck1)
    # Start Truck 2
    deliver_packages(truck2)
    # Since the Truck 3 start time will be past 10:20am address can be updated before the truck goes out
    package_needs_update = package_data.lookup(9)
    package_needs_update.set_address("410 S State St")
    package_needs_update.set_city("Salt Lake City")
    package_needs_update.set_zip("84111")
    # Since Truck 3 cannot go out until after truck 1 and truck 2 is done, the departure time will when the first truck
    # that finishes between truck 1 and 2 is finished.
    if truck3.get_depart_time() < min(truck1.get_time(), truck2.get_time()):
        truck3_new_depart_time = min(truck1.get_time(), truck2.get_time())
        truck3.set_depart_time(truck3_new_depart_time)
        truck3.set_time(truck3_new_depart_time)
    # Start Truck 3
    deliver_packages(truck3)

    total_milage = truck1.get_milage() + truck2.get_milage() + truck3.get_milage()

    while True:
        print("-------------------------------------------------------")
        print("1. Print All Package Statuses and Total Mileage\n"
              "2. Get a Single Package Status with a Time\n"
              "3. Get All Package Statuses with a Time\n"
              "4. Exit the Program")
        print("-------------------------------------------------------")
        user_input = input("Please enter a number that corresponds to the menu options\n")

        # Total milage plus all package statuses
        if user_input == "1":
            print("\nTotal Milage: " + str(total_milage) + "\n")

            for x in range(40):
                temp_package = package_data.lookup(x + 1)
                print("| Package #%s | Status: %s | Time Delivered: %s AM | Deadline: %s | Packaged Loaded On: %s|" % (
                temp_package.get_id(), temp_package.get_status(),
                temp_package.get_delivery_time(), temp_package.get_deadline(), temp_package.get_truck_num()))

        # Single Package Status with a given time
        elif user_input == "2":
            while True:
                # try:
                package_id_input = input("Please Provide the id of the package that you want to see the status of "
                                         "or type quit to return to main menu: ")
                if package_id_input == "quit":
                    break
                if 0 < int(package_id_input) <= 40:
                    package_time_input = input("Please provide the time you would like to look up Format(HH:MM:SS): ")
                    (h, m, s) = package_time_input.split(":")
                    if 0 < int(h) < 23 or 0 < int(m) > 59 or 0 < int(s) < 59:
                        user_time = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int())
                        temp_package = package_data.lookup(int(package_id_input))
                        print("| Package #%s | Status: %s | Delivery Address: %s | Deadline: %s | Truck Number: %s"
                              % (temp_package.get_id(), temp_package.get_status_at_time(user_time),
                                 temp_package.get_address(), temp_package.get_deadline(),
                              temp_package.get_truck_loaded_at_time(user_time)))
                        break
            # except Exception:
            # print(Exception)
        # All package status with a given time and which truck it's on at that time
        elif user_input == "3":
            while True:
                #try:
                    package_time_input = input("Please provide the time you would like to look up Format(HH:MM:SS) or "
                                               "type quit to return to the main menu: ")
                    if package_time_input == "quit":
                        break
                    (h, m, s) = package_time_input.split(":")
                    if 0 < int(h) < 23 or 0 < int(m) > 59 or 0 < int(s) < 59:
                        user_time = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
                        for x in range(40):
                            temp_package = package_data.lookup(x + 1)
                            print("| Package #%s | Status: %s | Delivery Address: %s | Deadline: %s | Truck: %s |"
                                  "Time: %s" % (temp_package.get_id(), temp_package.get_status_at_time(user_time),
                                                temp_package.get_address(), temp_package.get_deadline(),
                                                temp_package.get_truck_loaded_at_time(user_time), user_time))
                        break
                #except Exception:
                    print("An invalid input has been entered\n")

        # Exits the program
        elif user_input == "4":
            print("\nNow Exiting The Program")
            exit()
