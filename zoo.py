class Zoo:
    def get_ticket_price(self, age):
        if age < 0:
            return "err"
        elif 0 <= age < 13:
            return 50
        elif 13 <= age < 21:
            return 100
        elif 21 <= age < 61:
            return 150
        elif age >= 61:
            return 100