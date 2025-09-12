class sru_student:
    
    def __init__(self, name, roll_no, hostel_status):
        self.name = name
        self.roll_no = roll_no
        self.hostel_status = hostel_status
        self.fee_paid = False

    def fee_update(self, status):
        self.fee_paid = status

    def display_details(self):
        print(f"Name: {self.name}")
        print(f"Roll No.: {self.roll_no}")
        print(f"Hostel Status: {self.hostel_status}")
        print(f"Fee Paid: {'Yes' if self.fee_paid else 'No'}")


# Example usage
if __name__ == "__main__":
    student = sru_student("Amit", "SRU123", "Hosteller")
    student.fee_update(True)
    student.display_details()

    """
    Module for representing SRU student information and fee status.
    Classes:
        sru_student:
            Represents a student at SRU with attributes for name, roll number, hostel status, and fee payment status.
            Methods:
                __init__(name, roll_no, hostel_status):
                    Initializes a new student with the given name, roll number, and hostel status. Fee payment status is set to False by default.
                fee_update(status):
                    Updates the fee payment status of the student.
                display_details():
                    Prints the student's details including name, roll number, hostel status, and fee payment status.
    """