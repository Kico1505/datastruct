class Package:

    # Each package should have the id, address, city, zip, weight, and status given. The time it departed the hub and
    # the time it was delivered should also be known and each package starts in the hub.
    def __init__(self, package_id, delivery_address, delivery_city, delivery_zip, package_weight, delivery_deadline,
                 delivery_status="At The Hub"):
        self.id = package_id
        self.address = delivery_address
        self.city = delivery_city
        self.zip = delivery_zip
        self.weight = package_weight
        self.status = delivery_status
        self.deadline = delivery_deadline
        self.departure_time = None
        self.delivery_time = None
        self.truck_num = "None"
        self.truck_loaded = None

    def __str__(self):
        return "%s, %s, %s, %s, %s, %s, %s, %s, %s" % (self.id, self.address, self.city, self.zip, self.weight,
                                                       self.status, self.deadline, self.departure_time,
                                                       self.delivery_time)

    def get_status_at_time(self, time):
        if self.delivery_time < time:
            return "Delivered"
        if self.departure_time > time:
            return "En Route"
        else:
            return "At Hub"

    def get_truck_loaded_at_time(self, time):
        if self.delivery_time < time:
            return "None"
        if self.departure_time > time:
            return self.truck_loaded
        else:
            return self.truck_loaded

    def set_truck_loaded(self, new_truck_loaded):
        self.truck_loaded = new_truck_loaded

    def set_id(self, new_id):
        self.id = new_id

    def get_id(self):
        return self.id

    def set_address(self, new_address):
        self.address = new_address

    def get_address(self):
        return self.address

    def set_city(self, new_city):
        self.city = new_city

    def get_city(self):
        return self.city

    def set_zip(self, new_zip):
        self.zip = new_zip

    def get_zip(self):
        return self.zip

    def set_weight(self, new_weight):
        self.weight = new_weight

    def get_weight(self):
        return self.weight

    def set_status(self, new_status):
        self.status = new_status

    def get_status(self):
        return self.status

    def set_deadline(self, new_deadline):
        self.deadline = new_deadline

    def get_deadline(self):
        return self.deadline

    def set_departure_time(self, new_departure_time):
        self.departure_time = new_departure_time

    def get_departure_time(self):
        return self.departure_time

    def set_delivery_time(self, new_delivery_time):
        self.delivery_time = new_delivery_time

    def get_delivery_time(self):
        return self.delivery_time

    def set_truck_num(self, new_truck_num):
        self.truck_num = new_truck_num

    def get_truck_num(self):
        return self.truck_num