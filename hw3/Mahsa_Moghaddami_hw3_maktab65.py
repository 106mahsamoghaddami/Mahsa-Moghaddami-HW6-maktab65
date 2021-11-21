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
        self.city_name = input("enter new city:")
        self.street_name = input("enter new street name:")
        self.plaque = input("enter new plaque:")
        self.postal_code = input("enter new postal code:")
        return (self.city_name, self.street_name, self.plaque, self.postal_code)

    def __repr__(self):
        return (
            f"city:{self.city_name} ,street:{self.street_name},plaque:{self.plaque}, postal code:{self.postal_code}")


class Person:
    def __init__(self, f_name, l_name, email, national_code, phone_number):
        self.f_name = f_name
        self.l_name = l_name
        self.email = email
        self.national_code =national_code
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
        self.f_name = input("enter your new first name:")
        self.l_name = input("enter your new last name:")
        self.email = input("enter your new email address:")
        self.national_code = input("enter your new national code:")
        self.phone_number = input("enter your new phone number:")
        return (self.f_name, self.l_name, self.email, self.national_code, self.phone_number)

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
        national_code= input("enter your national code:")
        while True:
            if len(str(national_code)) == 10:
                print("national code is true!!!!")
                break
            else:
                print("wrong national code!!!")
                national_code = input("enter the correct national code: ")
        return national_code

    def __str__(self):
        return f"first name:{self.f_name} , last name:{self.l_name}"


class Ownerperson(Person):
    pass


class Tenantperson(Person):
    pass


class Buyer(Person):
    pass


class Property:  # melk
    def __init__(self, owner, tenant, number_of_room, area, number_of_floors, address, tel, faal_unfaal,
                 cost_of_mortgage, cost_of_rent, cost_of_sell, rent, sale, parking):
        self.owner = Ownerperson.get_info  # name,lastname,id_owner
        self.tenant = Tenantperson.get_info
        self.number_of_room = number_of_room
        self.area = area
        self.number_of_floors = number_of_floors
        self.address = Address.get_address
        self.tel = tel
        self.faal_unfaal = faal_unfaal
        self.cost_of_mortgage = cost_of_mortgage
        self.cost_of_rent = cost_of_rent
        self.cost_of_sell = cost_of_sell
        self.rent = rent
        self.sale = sale
        self.parking = parking

    @classmethod
    def get_property_info(cls):
        o_t = input("select you are owner or tenant-->1)owner ,2)tenant :")
        if o_t == '1':
            owner = Ownerperson.get_info()
            tenant="null"
        elif o_t == '2':
            tenant = Tenantperson.get_info()
            owner ="null"
        number_of_room = input("enter number of rooms:")
        area = input("enter area:")
        number_of_floors = input("enter number of floors")
        tel = input("enter tell number ")
        faal_unfaal = input("enter true if it's faal enter false if it's not faal: ").upper()
        case = input(" What is your case? 1)rent ,2)sell")
        if case == '1':
            rent = True
            sale = False

            cost_of_mortgage = input("enter cost of mortgage:")
            cost_of_rent = input("enter cost of rent:")
            cost_of_sell = "null"
        elif case == '2':
            rent = False
            sale = True
            cost_of_sell = input("enter cost of sell:")
            cost_of_mortgage = "null"
            cost_of_rent = "null"
        parking = input("enter number of parking:")
        return cls(owner, tenant, number_of_room, area, number_of_floors, tel, faal_unfaal, cost_of_mortgage,
                   cost_of_rent, cost_of_sell, rent, sale, parking)

    def edite_property(self):
        o_t = input("select you are owner or tenant-->1)owner ,2)tenant :")
        if o_t == '1':
            self.owner = Ownerperson.edit_info()# info of owner edit by ownerpersone calss
        elif o_t == '2':
            self.tenant = Tenantperson.edit_info()# info of owner edit by tenantpersone calss
        self.number_of_room = input("enter new number of room:")
        self.area = input("enter new area:")
        self.number_of_floors = input("enter new number of floors:")
        self.address = Address.edit_address()
        self.tel = input("enter new phone number of home:")
        case = input(" What is your case? 1)rent or 2)sell")
        if case == '1':
            self.rent = True
            self.sale = False
            self.cost_of_mortgage = input("enter new cost of mortgage:")
            self.cost_of_rent = input("enter new cost of rent:")
        elif case == '2':
            self.rent = False
            self.sale = True

            self.cost_of_sell = input("enter new cost of sell:")
        self.parking = input("enter new number of parkink:")
        return (self.owner, self.tenant, self.number_of_room, self.area, self.number_of_floors, self.tel
                , self.faal_unfaal, self.cost_of_mortgage, self.cost_of_rent, self.cost_of_sell,
                self.rent, self.sale, self.parking)

    def dispalay_property_info(self):
        return (f"owner: {self.owner}, tenant: {self.tenant}, number of rooms: {self.number_of_room},"
                f"area: {self.area}, number of floors:{self.number_of_floors}, telphone: {self.tel},"
                f"is faal or not:{self.faal_unfaal}, cost of mortgage:{self.cost_of_mortgage},"
                f"cost of rent: {self.cost_of_rent}, cost of sell:{self.cost_of_sell},"
                f"rent:{self.rent}, sale:{self.sale}, number parking:{self.parking}")

    """def store_property_info(self):
        return ({'owner': self.owner, 'tenant': self.tenant, 'number of rooms': self.number_of_room,
                 'area': self.area, 'number of floors': self.number_of_floors, 'telphone': self.tel,
                 f"is faal or not:{self.faal_unfaal}, cost of mortgage:{self.cost_of_mortgage},"
                 'cost of rent': self.cost_of_rent, 'cost of sell': self.cost_of_sell,
                 'rent': self.rent, 'sale': self.sale,
                 'number parking': self.parking})"""  # i want to append this dic to a list for store info


class Apartment(Property):
    def __int__(self, owner, tenant, number_of_room, area, number_of_floors, address, tel, faal_unfaal,
                cost_of_mortgage, cost_of_rent, cost_of_sell, rent, sale, parking, floor):
        super.__init__(owner, tenant, number_of_room, area, number_of_floors, address, tel, faal_unfaal,
                       cost_of_mortgage, cost_of_rent, cost_of_sell, rent, sale, parking)
        self.floor = floor


class House(Property):
    def __init__(self, owner, tenant, number_of_room, area, number_of_floors, address, tel, faal_unfaal,
                 cost_of_mortgage, cost_of_rent, cost_of_sell, rent, sale, parking, area_of_garden):
        super.__init__(owner, tenant, number_of_room, area, number_of_floors, address, tel, faal_unfaal,
                       cost_of_mortgage, cost_of_rent, cost_of_sell, rent, sale, parking)
        self.area_of_garden = area_of_garden


class Shop:
    def __init(self, owner, tenant, number_of_room, area, number_of_floors, address, tel, faal_unfaal,
               cost_of_mortgage, cost_of_rent, cost_of_sell, rent, sale, parking, floor):
        self.owner = Ownerperson.get_info
        self.tenant = Tenantperson.get_info
        self.area = area
        self.address = Address.get_address
        self.tel = tel
        self.faal_unfaal = faal_unfaal
        self.cost_of_mortgage = cost_of_mortgage
        self.cost_of_rent = cost_of_rent
        self.cost_of_sell = cost_of_sell
        self.rent = rent
        self.sale = sale

    @classmethod
    def get_shop_info(cls):

        o_t = input("select you are owner or tenant-->1)owner ,2)tenant :")
        if o_t == '1':
            owner = Ownerperson.get_info()
            tenant = "null"
        elif o_t == '2':
            tenant = Tenantperson.get_info()
            owner = "null"
        area = input("enter area:")
        tel = input("enter tell number ")
        faal_unfaal = input("enter true if it's faal enter false if it's not faal: ").upper()
        case = input(" What is your case? 1)rent ,2)sell")
        if case == '1':
            rent = True
            sale = False

            cost_of_mortgage = input("enter cost of mortgage:")
            cost_of_rent = input("enter cost of rent:")
        elif case == '2':
            rent = False
            sale = True
            cost_of_sell = input("enter cost of sell:")

        return cls(owner, tenant, area, tel, faal_unfaal, cost_of_mortgage,
                   cost_of_rent, cost_of_sell, rent, sale)

    def edite_shop_info(self):

        o_t = input("select you are owner or tenant-->1)owner ,2)tenant :")
        if o_t == '1':
            self.owner = Ownerperson.edit_info()
        elif o_t == '2':
            self.tenant = Tenantperson.edit_info()
        self.area = input("enter new area:")
        self.address = Address.edit_address()
        self.tel = input("enter new phone number of home:")
        case = input(" What is your case? 1)rent or 2)sell")
        if case == '1':
            self.rent = True
            self.sale = False
            self.cost_of_mortgage = input("enter new cost of mortgage:")
            self.cost_of_rent = input("enter new cost of rent:")
        elif case == '2':
            self.rent = False
            self.sale = True

            self.cost_of_sell = input("enter new cost of sell:")

        return (self.owner, self.tenant, self.area, self.tel
                , self.faal_unfaal, self.cost_of_mortgage, self.cost_of_rent, self.cost_of_sell,
                self.rent, self.sale)

    def dispalay_shop_info(self):
        return (f"owner: {self.owner}, tenant: {self.tenant},"
                f"area: {self.area}, telphone: {self.tel},"
                f"is faal or not:{self.faal_unfaal}, cost of mortgage:{self.cost_of_mortgage},"
                f"cost of rent: {self.cost_of_rent}, cost of sell:{self.cost_of_sell},"
                f"rent:{self.rent}, sale:{self.sale}")


""" def store_shope_info(self):
     return ({'owner': self.owner, 'tenant': self.tenant,
              'area': self.area, 'telphone': self.tel,
              f"is faal or not:{self.faal_unfaal}, cost of mortgage:{self.cost_of_mortgage},"
              'cost of rent': self.cost_of_rent, 'cost of sell': self.cost_of_sell,
              'rent': self.rent, 'sale': self.sale,
              })"""
all_case = []
"""------------------ i should make some instance from top classes to use theme for search!!-------------  """
while True:
    answer = input("do you want to register  or edit information of a case???   1) register or 2)edit:")
    if answer == '1':
        case = input("your case is which of theme: \n a)House ,b)Apartment ,c)shop :")
        if case == 'a':
            new_case1 = House.get_property_info()
            new_case1.dispalay_property_info()
            all_case.append(new_case1)

        elif case == 'b':
            new_case2 = Apartment.get_property_info()
            new_case2.dispalay_property_info()
            all_case.append(new_case2)
        elif case == 'c':
            new_case3 = Shop.get_shop_info()
            new_case3.dispalay_shop_info()
            all_case.append(new_case3)
        else:
            break

    elif answer == '2':
        case = input("your case is which of theme: \n a)House ,b)Apartment ,c)shop :")


        if case == 'a':
            new_case1 = House.edite_property()
            new_case1.dispalay_property_info()
            all_case.append(new_case1)

        elif case == 'b':
            new_case2 = Apartment.edite_property()
            new_case2.dispalay_property_info()
            all_case.append(new_case2)
        elif case == 'c':
            new_case3 = Shop.edite_shop_info()
            new_case3.dispalay_shop_info()
            all_case.append(new_case3)
        else:
            break

"""--------------------------------------------------------------------------------------------------------"""


class Adviser:
    def serch(self):

        for item in all_case:
            your_fild = input("enter your search filde:\n1)area ,2)sale/rent ,\n,"
                              "3)cost_of_mortgage \n4)cost_of_rent\n 5)cost of sell ")
            your_case=input("enter your filde to search:")
            if your_fild=='1':
                if item.area==your_fild:
                    item.dispalay_property_info()
            """ همین طور برای 5 تا ی دیگه چک مکنیم """
            """مربی های عزیز میدونم که باید چیکار کنم ولی واقعا دیگه توان ادامه ندارم امیدوارم بعدا بتونم تکمیلش کنم"""








# person1=Person.get_info()
#
# print(person1)

class Deal:
    pass
# a = Address.get_address()
# print(a)
# a.edit_address()
# print(a)
