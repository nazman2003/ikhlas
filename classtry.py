# Information Asset Register
# by Naeem Ahmed Moghul
# version 0.1

import json, sys

# Open json data file 'admin.json' for reading from same folder
data = open("admin.json",'r')

# Check type of data then hash out
#print(type(data))

maindct = json.load(data)
# Check if maindct is of type dictionary then hash out
#print(type(maindct))

staff_data = maindct['staff']
# Check if staff_data is of type list then hash out
#print(type(staff_data))

asset_data = maindct['assets']
# Check if staff_data is of type list then hash out
#print(type(asset_data))

# Create class for Staff information
class Staff:
    def __init__(self, id, name, department, server_admin):
        self.id = id
        self.name = name
        self.department = department
        self.server_admin = server_admin

    # Display in an understandable, readable format for the user
    def prntStaff(self):
        print("\nID:", self.id, "\nName:", self.name, "\nDept:", self.department, "\nServer Admin:", self.server_admin)

def show_staff_info():
    # Count/display number of Admin Staff
    print("There are", len(staff_data), "Admin staff members:\n")

    for lines in staff_data:
        Id = lines['id']
        Names = lines['name']
        Name = (Names[0] + " " + Names[1])
        Dept = lines['department']['name']
        Svradmin = lines['server_admin']
        staff_member = Staff(Id, Name, Dept, Svradmin)
        staff_member.prntStaff()

class File_Assets:
    def __init__(self, asset_name, asset_type, owner, details, retention, file_type, server):
        self.asset_name = asset_name
        self.asset_type = asset_type
        self.owner = owner
        self.details = details
        self.retention = retention
        self.file_type = file_type
        self.server = server

    # Display in an understandable, readable format for the user
    def prntFileAsset(self):
        print("\n")
        print(self.file_type, self.asset_type, "named", self.asset_name,
              "\nOwner ID:", self.owner, "\nRetention:", self.retention, self.details, "\nOn server:", self.server)

class Server_Assets:
    def __init__(self, asset_name, asset_type, owner, details, location, place, address, serverip):
        self.asset_name = asset_name
        self.asset_type = asset_type
        self.owner = owner
        self.details = details
        self.location = location
        self.place = place
        self.address = address
        self.serverip = serverip

    # Display in an understandable, readable format for the user
    def prntServerAsset(self):
        print("\n")
        print(self.asset_name, self.asset_type, "\nOwner ID:", self.owner, self.details, "\nServer IP:",
              self.serverip, "In", self.place, self.location, "\nAddress:", self.address)

class Media_Assets:
    def __init__(self, asset_name, asset_type, owner, details, retention, location, place, address, media_type):
        self.asset_name = asset_name
        self.asset_type = asset_type
        self.owner = owner
        self.details = details
        self.retention = retention
        self.location = location
        self.place = place
        self.address = address
        self.media_type = media_type
        
    # Display in an understandable, readable format for the user    
    def prntMediaAsset(self):
        print("\n")
        print(self.asset_type, "-",self.media_type, "\nName:", self.asset_name, "\nOwner ID:", self.owner,
              self.details, "\nRetention:", self.retention, "\nIn", self.place, self.location, "\nAddress:", self.address)

# Create a function to show the File information
def show_file_info():
    print("There are", len(asset_data), "assets:\n")
    for assets in asset_data:
        AssetName = assets['asset_name']
        AssetType = assets['asset_type']
        Owner = assets['owner']
        CIA = assets['details']['security']['cia']
        Conf = CIA[0]
        Integrity = CIA[1]
        Availability = CIA[2]
        DataCat = assets['details']['security']['data_categories']
        DataCatP = DataCat['Personal']
        DataCatPS = DataCat['Personal Sensitive']
        DataCatCS = DataCat['Customer Sensitive']
        Details = "\nConfidentiality: {}\nIntegrity: {}\nAvailability: {}\nData Category Personal:{}" \
                  "\nData Category Personal Sensitive: {}\nData Category Customer Sensitive:{}".format(
            Conf, Integrity, Availability, DataCatP, DataCatPS, DataCatCS)

        if AssetType == 'File':
            Retention = assets['details']['retention']
            FileType = assets['file_type']
            ServerName = assets['server']['server_name']
            ServerIP = assets['server']['ip']
            DotAddrs = "{}.{}.{}.{}".format(ServerIP[0],ServerIP[1],ServerIP[2],ServerIP[3])
            asset_record = File_Assets(AssetName, AssetType, Owner, Details, Retention, FileType, ServerName)
            asset_record.prntFileAsset()

# Create a function to show the Server information
def show_server_info():
    for assets in asset_data:
        AssetName = assets['asset_name']
        AssetType = assets['asset_type']
        Owner = assets['owner']
        CIA = assets['details']['security']['cia']
        Conf = CIA[0]
        Integrity = CIA[1]
        Availability = CIA[2]
        DataCat = assets['details']['security']['data_categories']
        DataCatP = DataCat['Personal']
        DataCatPS = DataCat['Personal Sensitive']
        DataCatCS = DataCat['Customer Sensitive']
        Details = "\nConfidentiality: {}\nIntegrity: {}\nAvailability: {}\nData Category Personal:{}" \
                  "\nData Category Personal Sensitive: {}\nData Category Customer Sensitive:{}".format(
            Conf, Integrity, Availability, DataCatP, DataCatPS, DataCatCS)
        if AssetType == 'Server':
            Location = assets['details']['location']['category']
            Place = assets['details']['location']['place']
            Addrlist = assets['details']['location']['address']
            Address = ("{}, {}, {}".format(Addrlist[0], Place, Addrlist[1]))
            NetAddress = assets['network_address']['ipv4']
            DotAddrs =("{}.{}.{}.{}".format(NetAddress[0], NetAddress[1], NetAddress[2], NetAddress[3]))
            asset_record = Server_Assets(AssetName, AssetType, Owner, Details, Location, Place, Address, DotAddrs)
            asset_record.prntServerAsset()

# Create a function to show the Media information
def show_media_info():
    for assets in asset_data:
        AssetName = assets['asset_name']
        AssetType = assets['asset_type']
        Owner = assets['owner']
        CIA = assets['details']['security']['cia']
        Conf = CIA[0]
        Integrity = CIA[1]
        Availability = CIA[2]
        DataCat = assets['details']['security']['data_categories']
        DataCatP = DataCat['Personal']
        DataCatPS = DataCat['Personal Sensitive']
        DataCatCS = DataCat['Customer Sensitive']
        Details = "\nConfidentiality: {}\nIntegrity: {}\nAvailability: {}\nData Category Personal:{}" \
                  "\nData Category Personal Sensitive: {}\nData Category Customer Sensitive:{}".format(
            Conf, Integrity, Availability, DataCatP, DataCatPS, DataCatCS)
        if AssetType == 'Physical Media':
            Retention = assets['details']['retention']
            Location = assets['details']['location']['category']
            Place = assets['details']['location']['place']
            Addrlist = assets['details']['location']['address']
            Address = ("{}, {}, {}".format(Addrlist[0], Place, Addrlist[1]))
            MediaType = assets['media_type']
            if MediaType == 'CD':
                EncryptC = assets['encryption']['cipher']
                EncryptL = assets['encryption']['keylength']
                Encryption = "\nEncryption cipher: {} with keylength: {}".format(EncryptC,EncryptL)
                MediaEnc = "{}{}".format(MediaType, Encryption)
                asset_record = Media_Assets(AssetName, AssetType, Owner, Details, Retention, Location, Place, Address, MediaEnc)
                asset_record.prntMediaAsset()
            elif MediaType == 'USB Stick':
                
                asset_record = Media_Assets(AssetName, AssetType, Owner, Details, Retention, Location, Place, Address, MediaType)
                asset_record.prntMediaAsset()

# Create a menu procedure for the user
def menu():
    print("Press 1 to get staff info")
    print("Press 2 to get all assets")
    print("Press 3 to view asset owners")
    print("Press 4 to quit")
    return (input("Please select an option: "))


run = menu()

while True:
    print("\n")
    if run == '1':
        show_staff_info()
        print("\n")
        run = menu()
    elif run == '2':
        show_file_info()
        show_server_info()
        show_media_info()
        print("\n")
        run = menu()

    elif run == '3':
        # to be developed in future release
        #AssetOwners()
        print("This option is not complete at this time\n")
        run = menu()

    elif run == '4':
        break
    
    else:
        print("\nOptions are 1 - 4 only\n")
        run = menu()

print("You quit the program")
input()