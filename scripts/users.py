class Users:
    def __init__(
        self,
        username,
        firstname,
        surname,
        house_number,
        street_name,
        postcode,
        email,
        dob,
    ):
        self.username = username
        self.firstname = firstname
        self.surname = surname
        self.house_number = house_number
        self.street_name = street_name
        self.postcode = postcode
        self.email = email
        self.dob = dob

    def get_username(self):
        return self.username

    def get_firstname(self):
        return self.firstname

    def get_surname(self):
        return self.surname

    def get_house_number(self):
        return self.house_number

    def get_street_name(self):
        return self.street_name

    def get_postcode(self):
        return self.postcode

    def get_email(self):
        return self.email

    def get_dob(self):
        return self.dob

    def edit_firstname(self, firstname):
        self.firstname = firstname

    def edit_surname(self, surname):
        self.surname = surname

    def edit_email(self, email):
        self.email = email

    def edit_dob(self, dob):
        self.dob = dob
