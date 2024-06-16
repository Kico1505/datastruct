
class Truck:

    # average speed and number of packages used from the assumptions provided.
    average_speed = 18
    max_packages = 16

    def __init__(self, truck_id, package_load, milage, address, depart_time, mph=average_speed,
                 max_packages=max_packages):
        self.id = truck_id
        self.mph = mph
        self.milage = milage
        self.max_packages = max_packages
        # Ensures that the amount of packages given meet the requirement of how many can be loaded at max at a time.
        # Any packages that are given past the max are dropped.
        if len(package_load) <= max_packages:
            self.package_load = package_load
        else:
            self.package_load = package_load[:max_packages]
            print("There were too many packages loaded, the following packages were not loaded:\n")
            for package in package_load[max_packages:]:
                print(package + "\n")
        self.address = address
        self.depart_time = depart_time
        self.time = depart_time

    def set_truck_id(self, new_id):
        self.id = new_id

    def get_truck_id(self):
        return self.id

    def set_mph(self, new_mph):
        self.mph = new_mph

    def get_mph(self):
        return self.mph

    def set_milage(self, new_milage):
        self.milage = new_milage

    def get_milage(self):
        return self.milage

    def set_max_packages(self, new_max_packages):
        self.max_packages = new_max_packages

    def get_max_packages(self):
        return self.max_packages

    def set_package_load(self, new_package_load):
        self.package_load = new_package_load

    def get_package_load(self):
        return self.package_load

    def set_address(self, new_address):
        self.address = new_address

    def get_address(self):
        return self.address

    def set_depart_time(self, new_depart_time):
        self.depart_time = new_depart_time

    def get_depart_time(self):
        return self.depart_time

    def set_time(self, new_time):
        self.time = new_time

    def get_time(self):
        return self.time
