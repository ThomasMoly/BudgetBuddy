# Print errors with exits ARE TO BE REPLACED BY ERROR DIALOG BOXES
from pathlib import Path
class DataManager:
    def __init__(self, usr_nm, passwrd, accnt_stat):
        # Defines "Finance Structure"
        # Defines "Name Data"
        self.usr_nm = usr_nm
        self.passwrd = passwrd
        if __name__!="__main__":
            if accnt_stat=="old":
                self.dat_retrieve()
            elif accnt_stat=="new":
                self.fin_struct = {}
        elif __name__=="__main__":
#            print(f"ACCOUNT DATA:\n  Username: {self.usr_nm}\n  Password: {self.passwrd}\n  Status: {accnt_stat}")
            self.fin_struct = {}
    def dat_retrieve(self):
        file_nm = self.usr_nm
        keywrd = self.passwrd
        file_path = Path("Account_Data/" + file_nm + "_dat.json")
        
        # See if account data file for {usr_nm} exists:
        if file_path.exists():
            print("filepath exists!")
        else:
            print(f"Error: Account with username {self.usr_nm} does not exist.")
        
        # See if password works for account:
        try:
            # 1. Decrypt file named "{file_nm}.json" in "Session_Data/" using {keywrd} as the encryption keyword:
            print(f"Using {keywrd}...")
            print(file_path)
            # 2. Extract fin_struct data structure
            print("TO BE REPLACED")
            # 3. Set self.fin_struct equal to extracted fin_struct data structure
        except:
            # 4. Keyword was false and didn't work; Thus,
            #   4a. File must be re-encrypted by the false keyword to prevent file corruption
            #   4b. Error must be thrown
            print("ADD RE-ENCRYPTION SCRIPT")
            print("Error: Password was incorrect.")
    def struct_integrate(self, in_ent):
        input_entry=in_ent
        # Tests for properly type-cast (str, int, float) inputs:
        try:
        # Type-cast itm_type:
            itm_type = str(input_entry[0])

            # Type-cast category and name:
            if itm_type == "e":
                category = str(input_entry[4])
                name = str(input_entry[5])

            # Type-cast price:
            if itm_type == "i":
                money_val = float(input_entry[3])
            elif itm_type == "e":
                money_val = float(input_entry[6])

            # Type-cast year, month, day:
            year = int(input_entry[1])
            month = int(input_entry[2])
            if itm_type == "e":
                day = int(input_entry[3])
        except:
            print("Error: One or more values has invalid type.")
            exit()

        # Checks for valid (non-negative) price:
        if money_val < 0:
            print("Error: Price must be non-negative.")
            exit()

        # Checks for valid months:
        if month not in range(1,13):
            print("Error: Invalid Month.")
            exit()
        # Checks for valid days (including leap days):
        if itm_type == "e":
            if day < 0:
                print("Error: Invalid Day.")
                exit()
            if (month in (1,3,5,7,8,10,12)) and (day > 31):
                print("Error: Invalid Day.")
                exit()
            elif (month in (4,6,9,11)) and (day > 30):
                print("Error: Invalid Day.")
                exit()
            elif (month == 2) and (((not ((((year % 4) == 0) and ((year % 100) != 0)) or ((year % 400) == 0)) and (day > 28))) or (day > 29)):
                print("Error: Invalid Day.")
                exit()

            # Defines basic expense unit of data: [Name, Price]:
            if itm_type == "e":
                money_list = input_entry[5::]

            # Creates year and month data within fin_struct if necessary:
            if (self.fin_struct).get(year, "NULL") == "NULL":
                self.fin_struct[year] = {}

            if (self.fin_struct[year]).get(month, "NULL") == "NULL":
                self.fin_struct[year][month] = {}

            # Integrates data from input_entry into fin_struct:
            if itm_type == "i":
                self.fin_struct[year][month][itm_type] = money_val
            elif itm_type == "e":
                if (self.fin_struct[year][month]).get(itm_type, "NULL") == "NULL":
                    self.fin_struct[year][month][itm_type] = {}
                if (self.fin_struct[year][month][itm_type]).get(category, "NULL") == "NULL":
                    self.fin_struct[year][month][itm_type][category] = {}
                if (self.fin_struct[year][month][itm_type][category]).get(day, "NULL") == "NULL":
                    self.fin_struct[year][month][itm_type][category][day] = []
            (self.fin_struct[year][month][itm_type][category][day]).append(money_list)
        return self.fin_struct

if __name__=="__main__":
    fin_struct = {}                                              # TO BE COPIED TO main?
    # Defines dummy input list:
    in_ent_1 = ["e", 2025, 11, 28, "Food", "eggs", 6.98]
    in_ent_2 = ["e", 2025, 11, 28, "Subscriptions", "Youtube Music", 14.95]
    in_ent_3 = ["e", 2025, 10, 23, "Debts", "Mastercard", 495.76]
    DatManage=DataManager("Adrian", "Password1234", "new")
    fin_struct = DatManage.struct_integrate(in_ent_1)
    fin_struct = DatManage.struct_integrate(in_ent_2)
    fin_struct = DatManage.struct_integrate(in_ent_3)

    print(fin_struct)