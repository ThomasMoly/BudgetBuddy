# Print errors with exits ARE TO BE REPLACED BY ERROR DIALOG BOXES
from pathlib import Path
from cryptography.fernet import Fernet
import json

class DataManager:
    def __init__(self, usr_nm, passwrd, accnt_stat):
        # Defines "Finance Structure"
        # Defines "Name Data"
        self.usr_nm = usr_nm
        self.passwrd = passwrd
        self.fin_struct = {}
        if __name__!="__main__":
            if accnt_stat=="old":
                self.dat_retrieve()
        elif __name__=="__main__":
#            print(f"ACCOUNT DATA:\n  Username: {self.usr_nm}\n  Password: {self.passwrd}\n  Status: {accnt_stat}")
            self.fin_struct = {}
    def dat_retrieve(self):
        file_nm = self.usr_nm
        keywrd = self.passwrd
        file_path = Path(f"Account_Data/{file_nm}.bin")
        key_path = Path("key.json")

        if not file_path.exists():
            print(f"Error: No data file found for {self.usr_nm}.")
            return

        # --- Load keys.json ---
        with open(key_path, "r") as f:
            try:
                key_data = json.load(f)
            except json.JSONDecodeError:
                print("Error: key.json is corrupted.")
                return

        # --- Check that password exists in key.json ---
        if keywrd not in key_data:
            print("Error: Password incorrect.")
            return

        key = key_data[keywrd].encode()
        cipher = Fernet(key)

        # --- Read encrypted data as bytes ---
        with open(file_path, "rb") as f:
            encrypted_bytes = f.read()

        try:
            # --- Decrypt ---
            decrypted_bytes = cipher.decrypt(encrypted_bytes)
        except:
            print("Error: Password incorrect or data corrupted.")
            return

        # --- Convert JSON text back to Python dict ---
        decrypted_str = decrypted_bytes.decode()
        self.fin_struct = json.loads(decrypted_str)

        print("Data decrypted successfully.")
        return(self.fin_struct)

    def struct_integrate(self, in_ent):
        input_entry=in_ent
        # Tests for properly type-cast (str, int, float) inputs:
        try:
        # Type-cast itm_type:
            itm_type = str(input_entry[0])

            # Type-cast category and name:
            if itm_type == "e":
                category = str(input_entry[3])
                name = str(input_entry[4])

            # Type-cast price:
            if itm_type == "i":
                money_val = float(input_entry[3])
            elif itm_type == "e":
                money_val = float(input_entry[5])

            # Type-cast year, month, day:
            year = int(input_entry[1])
            month = int(input_entry[2])
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

            # Defines basic expense unit of data: [Name, Price]:
        if itm_type == "e":
            money_list = input_entry[4::]

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
                self.fin_struct[year][month][itm_type][category] = []
        (self.fin_struct[year][month][itm_type][category]).append(money_list)

    def dat_save(self):

        file_nm = self.usr_nm
        keywrd = self.passwrd
        file_path = Path(f"Account_Data/{file_nm}.bin")
        key_path = Path("key.json")

        # --- Load keys.json ---
        with open(key_path, "r") as f:
            try:
                key_data = json.load(f)
            except json.JSONDecodeError:
                key_data = {}

        # --- Get or create encryption key ---
        if keywrd in key_data:
            key = key_data[keywrd].encode()
        else:
            key = Fernet.generate_key()
            key_data[keywrd] = key.decode()
            with open(key_path, "w") as f:
                json.dump(key_data, f, indent=2)

        cipher = Fernet(key)

        # --- Convert Python dict → JSON string → bytes ---
        json_string = json.dumps(self.fin_struct)
        json_bytes = json_string.encode()

        # --- Encrypt ---
        encrypted = cipher.encrypt(json_bytes)

        # --- Write encrypted data ---
        file_path.parent.mkdir(parents=True, exist_ok=True)
        with open(file_path, "wb") as f:
            f.write(encrypted)

        print("Saved encrypted data.")

    def dat_wipe(self):
        # Delete encrypted data
        file_path = Path(f"Account_Data/{self.usr_nm}.bin")
        key_path = Path("key.json")

        if file_path.exists():
            file_path.unlink()
            print("Encrypted data deleted.")
        else:
            print("No encrypted data found for this user.")

        # --- Remove this user's password/key from key.json ---
        if key_path.exists():
            with open(key_path, "r") as f:
                try:
                    key_data = json.load(f)
                except json.JSONDecodeError:
                    print("Error: key.json could not be read.")
                    return

            # If the password exists, delete it
            if self.passwrd in key_data:
                del key_data[self.passwrd]
                print("Password/key entry removed from key.json.")
            else:
                print("No matching password/key entry found in key.json.")

            # Save the updated key.json
            with open(key_path, "w") as f:
                json.dump(key_data, f, indent=2)
        else:
            print("No key.json exists to modify.")


    def ch_passwrd(self, new_password):

        old_password = self.passwrd
        key_path = Path("key.json")

        # Load key.json
        with open(key_path, "r") as f:
            try:
                key_data = json.load(f)
            except json.JSONDecodeError:
                print("Error: key.json cannot be read.")
                return

        # Ensure the old password exists
        if old_password not in key_data:
            print("Error: Old password does not exist in key.json.")
            return

        # Retrieve the existing key (do NOT regenerate a new key yet)
        key = key_data[old_password]

        # Delete the old entry
        del key_data[old_password]

        # Insert the new password → SAME key
        key_data[new_password] = key

        # Save updated key.json
        with open(key_path, "w") as f:
            json.dump(key_data, f, indent=2)

        # Update the object's password for future operations
        self.passwrd = new_password

        print("Password updated safely.")




if __name__=="__main__":
    fin_struct = {}                                              # TO BE COPIED TO main?
    # Defines dummy input list:
    in_ent_1 = ["e", 2025, 11, "Food", "eggs", 6.98]
    in_ent_2 = ["e", 2025, 11, "Subscriptions", "Youtube Music", 14.95]
    in_ent_3 = ["e", 2025, 10, "Debts", "Mastercard", 495.76]
    DatManage=DataManager("Adrian", "Password1234", "new")
    fin_struct = DatManage.struct_integrate(in_ent_1)
    fin_struct = DatManage.struct_integrate(in_ent_2)
    fin_struct = DatManage.struct_integrate(in_ent_3)

    DatManage.dat_save()

    data = DatManage.dat_retrieve()
    print(data)
