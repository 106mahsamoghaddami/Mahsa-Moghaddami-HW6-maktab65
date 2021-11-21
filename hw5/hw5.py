import csv


class Address:
    def __init__(self, city_name, street_name, plaque, postal_code):
        self.city_name = city_name
        self.street_name = street_name
        self.plaque = plaque
        self.postal_code = postal_code

    @classmethod
    def get_address(cls):
        city_name = input("enter your city:")
        street_name = input("enter street:")
        plaque = input("enter plaque:")
        postal_cod = input("enter postal code")
        return cls(city_name, street_name, plaque, postal_cod)

    def edit_address(self):
        my_address = self.__dict__

        while True:
            item = input("which one do you want to change: 1)city 2)street 3)plaque 4)postal_code:")
            if item == '1':
                new_city = input("enter new city:")
                my_address['city_name'] = new_city
                print("changed successfully")
            elif item == '2':
                new_street = input("enter new street:")
                my_address['street_name'] = new_street
            elif item == '3':
                new_plaque = input("enter new plaque:")
                my_address['plaque'] = new_plaque
            elif item == '4':
                new_postal_code = input("enter new postal code:")
                my_address['postal_code'] = new_postal_code
            else:
                break
        return self

    def display(self):
        print (
            f"city:{self.city_name} ,street:{self.street_name},plaque:{self.plaque}, postal code:{self.postal_code}")

    def __repr__(self):
        return (
            self.city_name, self.street_name, self.plaque, self.postal_code)


class Person:
    def __init__(self, f_name, l_name, email, national_code, phone_number):
        self.f_name = f_name
        self.l_name = l_name
        self.email = email
        self.national_code = national_code
        self.phone_number = phone_number

    @classmethod
    def get_info(cls):
        first_name = input("inter your fist name:")
        last_name = input("inter your last name:")
        email_address = Person.validation_email()
        national_code = Person.validation_national_code()
        phone_number = input("inter your phone number:")
        return cls(first_name, last_name, email_address, national_code, phone_number)

    def edit_info(self):
        my_info = self.__dict__
        while True:
            item = input("which one do you want to change: 1)f_name 2)l_name 3)email 4)national_code 5)phone_number:")
            if item == '1':
                new = input("enter new first name:")
                my_info['f_name'] = new
            elif item == '2':
                new = input("enter new last name:")
                my_info['l_name'] = new
            elif item == '3':
                new = Person.validation_email()
                my_info['email'] = new
            elif item == '4':
                new = Person.validation_national_code()
                my_info['national_code'] = new
            elif item == '5':
                new = input("enter new phone number:")
                my_info['phone_number'] = new
            else:
                break
        return self

    @staticmethod
    def validation_email():  # i think that's better to define it as a static method
        email = input("enter your email:")
        while True:
            if '@' in email and email[-4:] == '.com':
                print("email is true!!")
                break
            else:
                print("wrong email!!")
                email = input("enter the correct email:")
        return email

    @staticmethod
    def validation_national_code():
        national_code = input("enter your national code:")
        while True:
            if len(str(national_code)) == 10 and national_code.isdigit():
                print("national code is true!!!!")
                break
            else:
                print("wrong national code!!!")
                national_code = input("enter the correct national code: ")
        return national_code

    def __repr__(self):
        return f"first name:{self.f_name} , last name:{self.l_name}"




class OwnerPerson(Person):
    o_counter = 0

    def __init__(self, f_name, l_name, email, national_code, phone_number):
        Person.__init__(self, f_name, l_name, email, national_code, phone_number)
        OwnerPerson.o_counter += 1
        self.id = 'O' + str(OwnerPerson.o_counter)


class TenantPerson(Person):
    t_counter = 0

    def __init__(self, f_name, l_name, email, national_code, phone_number):
        Person.__init__(self, f_name, l_name, email, national_code, phone_number)
        TenantPerson.t_counter += 1
        self.id = 't' + str(TenantPerson.t_counter)


class Buyer(Person):
    b_counter = 0

    def __init__(self, f_name, l_name, email, national_code, phone_number):
        Person.__init__(self, f_name, l_name, email, national_code, phone_number)
        Buyer.b_counter += 1
        self.id = 'b' + str(Buyer.b_counter)


class Apartment:
    counter = 0

    def __init__(self, owner, tenant, number_of_room, area, number_of_floors, address, tel, active_inactive,
                 cost_of_mortgage, cost_of_rent, cost_of_sell, rent_sale, parking, floor):
        self.owner = owner  # name,lastname,id_owner
        self.tenant = None
        self.number_of_room = number_of_room
        self.area = area
        self.number_of_floors = number_of_floors
        self.address = address
        self.tel = tel
        self.active_inactive = active_inactive
        self.cost_of_mortgage = cost_of_mortgage
        self.cost_of_rent = cost_of_rent
        self.cost_of_sell = cost_of_sell
        self.rent_sale = rent_sale

        self.parking = parking
        self.floor = floor
        Apartment.counter += 1
        self.id = '@P' + str(Apartment.counter)

    @classmethod
    def get_apartment_info(cls):
        owner = OwnerPerson.get_info()

        tenant = None

        number_of_room = input("enter number of rooms:")
        area = input("enter area:")
        number_of_floors = input("enter number of floors")
        address = Address.get_address()
        tel = input("enter tell number ")
        active_inactive = input("enter true if it's active enter false if it's inactive: ").upper()

        cost_of_sell = input("enter cost of sell:")

        cost_of_mortgage = input("  enter cost of mortgage:")
        cost_of_rent = input("enter cost of rent:")

        parking = input("enter number of parking:")
        floor = input("enter number of floor")
        rent_sale = input("enter rent or sale:")

        return cls(owner, tenant, number_of_room, area, number_of_floors, address, tel, active_inactive,
                   cost_of_mortgage,
                   cost_of_rent, cost_of_sell, rent_sale, parking, floor)

    def edit_apartment(self):
        my_object = self.__dict__
        while True:
            print("which one do you want??")
            case = input(
                "1)owner, 2)tenant, 3)number_of_room, 4)area, 5)number_of_floors, 6)address, 7)tel, 8)active_inactive,"
                "9)cost_of_mortgage, 10)cost_of_rent, 11)cost_of_sell, 12)rent_sale, 14)parking, 15)floor")
            if case == '1':
                new = OwnerPerson.edit_info(self)
                my_object['owner'] = new
            elif case == '2':
                new = TenantPerson.edit_info(self)
                my_object['tenant'] = new
            elif case == '3':
                while True:
                    try:
                        new = int(input("new number of rooms ? "))
                        my_object['number_of_room'] = new
                    except ValueError:
                        print("add integer!!!")
                    else:
                        break
            elif case == '4':
                while True:
                    try:
                        new = int(input("area ? "))
                        my_object['area'] = new
                    except ValueError:
                        print("add integer")
                    else:
                        break
            elif case == '5':
                while True:
                    try:
                        new = int(input("number of floors? "))
                        my_object['number_of_floors'] = new
                    except ValueError:
                        print("add integer")
                    else:
                        break
            elif case == '6':
                new = Address.edit_address(self)
                my_object['address'] = new

            elif case == '7':
                while True:
                    try:
                        new = int(input("enter tell "))
                        my_object['tel'] = new
                    except ValueError:
                        print("add integer")
                    else:
                        break
            elif case == '8':
                while True:
                    try:
                        new = bool(input("this apartment is active or inactive? true or false"))
                        my_object['active_inactive'] = new
                    except ValueError:
                        print("enter true ot false")
                    else:
                        break
            elif case == '9':
                while True:
                    try:
                        new = int(input("cost_of_mortgage? "))
                        my_object['cost_of_mortgage'] = new
                    except ValueError:
                        print("add integer")
                    else:
                        break
            elif case == '10':
                while True:
                    try:
                        new = int(input("cost_of_rent? "))
                        my_object['cost_of_rent'] = new
                    except ValueError:
                        print("add integer")
                    else:
                        break
            elif case == '11':
                while True:
                    try:
                        new = int(input("cost of sell? "))
                        my_object['cost_of_sell'] = new
                    except ValueError:
                        print("add integer")
                    else:
                        break

            elif case == '12':
                while True:
                    try:
                        new = input("enter sale or rent? ").lower()
                        my_object['rent_sale'] = new
                    except ValueError:
                        print("enter string value")
                    else:
                        break
            elif case == '13':
                while True:
                    try:
                        new = int(input(" enter number of parking? "))
                        my_object['parking'] = new
                    except ValueError:
                        print("enter integer value")
                    else:
                        break

            elif case == '14':
                while True:
                    try:
                        new = int(input(" which floor is? "))
                        my_object['floor'] = new
                    except ValueError:
                        print("enter integer value")
                    else:
                        break
            else:
                break



    def __repr__(self):
        return (f"owner: {self.owner}, tenant: {self.tenant}, number of rooms: {self.number_of_room},"
                f"area: {self.area} ,number of floors:{self.number_of_floors}, address:{self.address}, phone: {self.tel},"
                f"is active or not:{self.active_inactive}, cost of mortgage:{self.cost_of_mortgage},"
                f"cost of rent: {self.cost_of_rent}, cost of sell:{self.cost_of_sell},"
                f"rent:{self.rent_sale}, number parking:{self.parking},floor:{self.floor} ,ID_apartment:{self.id}")

    def display_apartment(self):
        print(f"owner: {self.owner}, tenant: {self.tenant}, number of rooms: {self.number_of_room},"
              f"area: {self.area} ,number of floors:{self.number_of_floors}, address:{self.address}, phone: {self.tel},"
              f"is active or not:{self.active_inactive}, cost of mortgage:{self.cost_of_mortgage},"
              f"cost of rent: {self.cost_of_rent}, cost of sell:{self.cost_of_sell},"
              f"rent:{self.rent_sale}, number parking:{self.parking},floor:{self.floor} ,ID_apartment:{self.id}")


class House:
    counter = 0

    def __init__(self, owner, tenant, number_of_room, area, number_of_floors, address, tel, active_inactive,
                 cost_of_mortgage, cost_of_rent, cost_of_sell, rent_sale, parking, area_of_garden):
        self.owner = owner
        self.tenant = tenant
        self.number_of_room = number_of_room
        self.area = area
        self.number_of_floors = number_of_floors
        self.address = address
        self.tel = tel
        self.active_inactive = active_inactive
        self.cost_of_mortgage = cost_of_mortgage
        self.cost_of_rent = cost_of_rent
        self.cost_of_sell = cost_of_sell
        self.rent_sale = rent_sale

        self.parking = parking
        self.area_of_garden = area_of_garden
        House.counter += 1
        self.id = '#H' + str(House.counter)

    @classmethod
    def get_house_info(cls):
        owner = OwnerPerson.get_info()

        tenant = None

        number_of_room = input("enter number of rooms:")
        area = input("enter area:")
        number_of_floors = input("enter number of floors")
        address = Address.get_address()
        tel = input("enter tell number ")
        active_inactive = input("enter true if it's active enter false if it's inactive: ").upper()
        cost_of_mortgage = input("  enter cost of mortgage:")
        cost_of_rent = input("enter cost of rent:")

        cost_of_sell = input("enter cost of sell:")
        rent_sale = input("enter sale or rent?").lower

        parking = input("enter number of parking:")
        area_of_garden = input("enter number of floor")

        return cls(owner, tenant, number_of_room, area, number_of_floors, address, tel, active_inactive,
                   cost_of_mortgage,
                   cost_of_rent, cost_of_sell, rent_sale, parking, area_of_garden)

    def edit_house(self):
        my_object = self.__dict__
        while True:
            print("which one do you want??")
            case = input(
                "1)owner, 2)tenant, 3)number_of_room, 4)area, 5)number_of_floors, 6)address, 7)tel, 8)active_inactive,"
                "9)cost_of_mortgage, 10)cost_of_rent, 11)cost_of_sell, 12)rent_sale, 13)parking, 14)area_of_garden")
            if case == '1':
                new = OwnerPerson.edit_info(self)
                my_object['owner'] = new
            elif case == '2':
                new = TenantPerson.edit_info(self)
                my_object['tenant'] = new
            elif case == '3':
                while True:
                    try:
                        new = int(input("new number of rooms ? "))
                        my_object['number_of_room'] = new
                    except ValueError:
                        print("add integer!!!")
                    else:
                        break
            elif case == '4':
                while True:
                    try:
                        new = int(input("area ? "))
                        my_object['area'] = new
                    except ValueError:
                        print("add integer")
                    else:
                        break
            elif case == '5':
                while True:
                    try:
                        new = int(input("number of floors? "))
                        my_object['number_of_floors'] = new
                    except ValueError:
                        print("add integer")
                    else:
                        break
            elif case == '6':
                new = Address.edit_address(self)
                my_object['address'] = new

            elif case == '7':
                while True:
                    try:
                        new = int(input("enter tell "))
                        my_object['tel'] = new
                    except ValueError:
                        print("add integer")
                    else:
                        break
            elif case == '8':
                while True:
                    try:
                        new = bool(input("this apartment is active or inactive? true or false"))
                        my_object['active_inactive'] = new
                    except ValueError:
                        print("enter true ot false")
                    else:
                        break
            elif case == '9':
                while True:
                    try:
                        new = int(input("cost_of_mortgage? "))
                        my_object['cost_of_mortgage'] = new
                    except ValueError:
                        print("add integer")
                    else:
                        break
            elif case == '10':
                while True:
                    try:
                        new = int(input("cost_of_rent? "))
                        my_object['cost_of_rent'] = new
                    except ValueError:
                        print("add integer")
                    else:
                        break
            elif case == '11':
                while True:
                    try:
                        new = int(input("cost of sell? "))
                        my_object['cost_of_sell'] = new
                    except ValueError:
                        print("add integer")
                    else:
                        break

            elif case == '12':
                while True:
                    try:
                        new = input("enter sale or rent? ").lower()
                        my_object['rent_sale'] = new
                    except ValueError:
                        print("enter string value")
                    else:
                        break
            elif case == '13':
                while True:
                    try:
                        new = int(input(" enter number of parking? "))
                        my_object['parking'] = new
                    except ValueError:
                        print("enter integer value")
                    else:
                        break

            elif case == '14':
                while True:
                    try:
                        new = int(input(" enter area of garden? "))
                        my_object['area_of_garden'] = new
                    except ValueError:
                        print("enter integer value")
                    else:
                        break
            else:
                break

    def __repr__(self):
        return str(f"{self.owner}, {self.tenant}, {self.number_of_room},"
                f"{self.area}, {self.number_of_floors},{self.address}, {self.tel},"
                f" {self.active_inactive}, {self.cost_of_mortgage},"
                f"{self.cost_of_rent}, {self.cost_of_sell},"
                f"{self.rent_sale}, {self.parking}, {self.area_of_garden}, {self.id}")

    def display_house(self):
        print(f"owner: {self.owner}, tenant: {self.tenant}, number of rooms: {self.number_of_room},"
              f"")



class Shop:
    counter = 0

    def __init__(self, owner, tenant, area, address, tel, active_inactive,
                 cost_of_mortgage, cost_of_rent, cost_of_sell, rent_sale):
        self.owner = owner
        self.tenant = tenant
        self.area = area
        self.address = address
        self.tel = tel
        self.active_inactive = active_inactive
        self.cost_of_mortgage = cost_of_mortgage
        self.cost_of_rent = cost_of_rent
        self.cost_of_sell = cost_of_sell
        self.rent_sale = rent_sale

        Shop.counter += 1
        self.id = '$h' + str(Shop.counter)

    @classmethod
    def get_shop_info(cls):
        owner = OwnerPerson.get_info()

        tenant = None

        area = input("enter area:")

        address = Address.get_address()
        tel = input("enter tell number ")
        active_inactive = input("enter true if it's active enter false if it's inactive: ").upper()

        cost_of_sell = input("enter cost of sell:")

        cost_of_mortgage = input("  enter cost of mortgage:")
        cost_of_rent = input("enter cost of rent:")

        rent_sale = input("enter sale or rent").lower()

        return cls(owner, tenant, area, address, tel, active_inactive,
                   cost_of_mortgage,
                   cost_of_rent, cost_of_sell, rent_sale)

    def edit_shop_info(self):
        my_object = self.__dict__
        while True:
            print("which one do you want??")
            case = input(
                "1)owner, 2)tenant,  3)area,  4)address, 5)tel, 6)active_inactive,"
                "7)cost_of_mortgage, 8)cost_of_rent, 9)cost_of_sell, 10)rent_sale")
            if case == '1':
                new = OwnerPerson.edit_info(self)
                my_object['owner'] = new
            elif case == '2':
                new = TenantPerson.edit_info(self)
                my_object['tenant'] = new

            elif case == '3':
                while True:
                    try:
                        new = int(input("area ? "))
                        my_object['area'] = new
                    except ValueError:
                        print("add integer")
                    else:
                        break

            elif case == '4':
                new = Address.edit_address(self)
                my_object['address'] = new

            elif case == '5':
                while True:
                    try:
                        new = int(input("enter tell "))
                        my_object['tel'] = new
                    except ValueError:
                        print("add integer")
                    else:
                        break
            elif case == '6':
                while True:
                    try:
                        new = bool(input("this apartment is active or inactive? true or false"))
                        my_object['active_inactive'] = new
                    except ValueError:
                        print("enter true ot false")
                    else:
                        break
            elif case == '7':
                while True:
                    try:
                        new = int(input("cost_of_mortgage? "))
                        my_object['cost_of_mortgage'] = new
                    except ValueError:
                        print("add integer")
                    else:
                        break
            elif case == '8':
                while True:
                    try:
                        new = int(input("cost_of_rent? "))
                        my_object['cost_of_rent'] = new
                    except ValueError:
                        print("add integer")
                    else:
                        break
            elif case == '9':
                while True:
                    try:
                        new = int(input("cost of sell? "))
                        my_object['cost_of_sell'] = new
                    except ValueError:
                        print("add integer")
                    else:
                        break

            elif case == '10':
                while True:
                    try:
                        new = input("enter sale or rent? ").lower()
                        my_object['rent_sale'] = new
                    except ValueError:
                        print("enter string value")
                    else:
                        break

            else:
                break

    def display_shop_info(self):
        print(f"owner: {self.owner}, tenant: {self.tenant},"
              f"area: {self.area},address:{self.address} ,phone: {self.tel},"
              f"is active or not:{self.active_inactive}, cost of mortgage:{self.cost_of_mortgage},"
              f"cost of rent: {self.cost_of_rent}, cost of sell:{self.cost_of_sell},"
              f"rent:{self.rent_sale}")

    def __repr__(self):
        return (self.owner, self.tenant, self.area, self.address, self.tel,
                self.active_inactive,
                self.cost_of_mortgage, self.cost_of_rent, self.cost_of_sell,
                self.rent_sale)


class AstateAgent:

    def search(self, *args):
        """ in this part you should read from file
        base on user search a spacial case
        """

        with open('all_melk.csv') as csv_file:
            # reading the csv file using DictReader
            csv_reader = csv.DictReader(csv_file)

            # converting the file to dictionary
            # by first converting to list
            # and then converting the list to dict
            dict_from_csv = dict(list(csv_reader)[0])

            print(dict_from_csv['area'])
        # it's defective

class Deal:
    pass


def write_on_file(filepath):
    toCSV = all_case
    with open(filepath, 'w', encoding='utf8', newline='') as output_file:
        fc = csv.DictWriter(output_file,
                            fieldnames=toCSV[0].keys(),)
        fc.writeheader()
        fc.writerows(toCSV)




all_case = []
house_list = []
apartment_list = []
shop_list = []



"""------------------ i should make some instance from top classes to use theme for search!!-------------  """
while True:
    answer = input("do you want to register or edit or show information of a case??? "
                   "  1) register or 2)show property 3)edit")
    if answer == '1':
        case = input("your case is which of theme: \n a)House ,b)Apartment ,c)shop :")
        if case == 'a':
            print("you as a owner of house registering!!! ")
            new_case1 = House.get_house_info()
            house_list.append(new_case1)
            temp = new_case1.__dict__
            all_case.append(temp)

            print(f" Your id is {new_case1.id} registration was completed successfully")





        elif case == 'b':
            print("you as a owner of apartment registering!!! ")
            new_case2 = Apartment.get_apartment_info()
            temp2 = new_case2.__dict__
            all_case.append(temp2)
            apartment_list.append(new_case2)

            print(f" Your id is {new_case2.id} registration was completed successfully")


        elif case == 'c':
            print("you as a owner of shop registering!!! ")
            new_case3 = Shop.get_shop_info()
            temp3 = new_case3.__dict__
            all_case.append(temp3)
            shop_list.append(new_case3)
            print(f" Your id is {new_case3.id} registration was completed successfully")



        else:
            break


    elif answer == '2':
        if len(all_case) == 0:
            print("There are no registered items!!! ")
            break
        else:
            item = input("which one's information do you want to see: \n a)House ,b)Apartment ,c)shop :")
            if item == 'a':
                id_check = input("enter your house id :")
                for h in house_list:
                    if h.id == id_check:
                        h.display_house()
            elif item == 'b':
                id_check = input("enter your house id :")
                for a in apartment_list:
                    if a.id == id_check:
                        a.display_apartment()
            elif item == 'c':
                id_check = input("enter your house id :")
                for s in shop_list:
                    if s.id == id_check:
                        s.display_apartment()
    elif answer == '3':
        if len(all_case) == 0:
            print("There are no registered items!!! ")
            break
        else:
            item = input("which one's information do you want to edit: \n a)House ,b)Apartment ,c)shop :")
            if item == 'a':
                id_check = input("enter your house id :")
                for h in house_list:
                    if h.id == id_check:
                        h.edit_house()
            elif item == 'b':
                id_check = input("enter your house id :")
                for a in apartment_list:
                    if a.id == id_check:
                        a.edit_apartment()
            elif item == 'c':
                id_check = input("enter your house id :")
                for s in shop_list:
                    if s.id == id_check:
                        s.edit_shop_info()
    else:
        break
"""--------------------------------------------------------------------------------------------------------"""
write_on_file("all_melk.csv")
# q = AstateAgent()
# q.search()
