# Simple Asset Management by Naz 30.05.2020 v0.7

# Get the Json package/library
import json

# Open json data file from same folder
data = open("Admin.json",)

# Load all the data from json file into dictionary
dataset = json.load(data)

# Get all staff data into a list
Staff = dataset['staff']

# Get all assets data into a list
Assets = dataset['assets']

def StaffNames():
    for key in Staff:
        Name = key['name']
        print(Name[0],Name[1])

def ShowAssets():
    for AllAssets in Assets:
        AssetName = AllAssets['asset_name']
        AssetType = AllAssets['asset_type']
        if AllAssets.get('file_type') != None:
            FileType = AllAssets['file_type']
            print(FileType,AssetType,"called",AssetName)
        elif AllAssets.get('network_address') != None:
            NetAddress = AllAssets['network_address']['ipv4']
            print(AssetName,AssetType,"on IP: {}.{}.{}.{}".format(NetAddress[0],NetAddress[1],NetAddress[2],NetAddress[3]))
        elif AllAssets.get('media_type') != None:
            MediaType = AllAssets['media_type']
            print(AssetType,AssetName,MediaType)

def AssetOwners():
    for AllAssets in Assets:
        OwnerID = AllAssets['owner']
        AssetName = AllAssets['asset_name']
        AssetType = AllAssets['asset_type']
        for key in Staff:
            Name = key['name']
            if key['id'] == OwnerID:
                print(Name[0],Name[1],"is the owner of the", AssetName,AssetType)
    
    
def showstaff():
    for key in Staff:
        ID = key['id']
        print(ID)
        NAME = key['name']
        print(NAME)
        #print("{}".format(key['department']))
        DEPT = key['department']
        print(DEPT)
        #print("{}".format(key['server_admin']))
        ISADMIN = key['server_admin']
        print(ISADMIN)

def showassets():
    for prod in dataset['assets']:
        AssetName = prod['asset_name']
        print(AssetName)
        AssetType = prod['asset_type']
        print(AssetType)
        Owner = prod['owner']
        print(Owner)
        Details = prod['details']
        #print(Details['security'])
        CIA = (Details['security']['cia'])

        print("Confidentiality:  {}\nIntegrity:  {}\nAvailability:  {}".format(CIA[0],CIA[1],CIA[2]))
        DataCat = (Details['security']['data_categories'])
        #Personal = (DataCat['personal'])
        PersonalDC = (DataCat['Personal'])

        PersonalSensitive = (DataCat['Personal Sensitive'])
        CustomerSensitive = (DataCat['Customer Sensitive'])
        print("Data Category - Personal:  ",PersonalDC)
        print("Data Category - Personal Sensitive: ",PersonalSensitive)
        print("Data Category - Customer Sensitive: ",CustomerSensitive)

        if AssetType == "Server":
            Location = (Details['location'])
            Category = (Details['location']['category'])
            Place = (Details['location']['place'])
            Address = (Details['location']['address'])
            NetworkAddress = prod['network_address']
            IPV4 = (NetworkAddress['ipv4'])
            DottedIPV4 = "{}.{}.{}.{}".format(IPV4[0],IPV4[1],IPV4[2],IPV4[3])


            print(Place)
            print(Address[0],Address[1])
            print(DottedIPV4)
            print("\n")

        elif AssetType == "File":
            Retention = (Details['retention'])
            print(Retention)
            FileType = prod['file_type']
            print(FileType)
            Server = prod['server']
            #print(Server)
            ServerName = (Server['server_name'])
            print(ServerName)
            IP = (Server['ip'])
            FullIP = "{}.{}.{}.{}".format(IP[0],IP[1],IP[2],IP[3])
            print(FullIP)
            print('\n')

        elif AssetType == "Physical Media":
            Retention = (Details['retention'])
            print(Retention)
            Location = (Details['location'])
            Category = (Details['location']['category'])
            Place = (Details['location']['place'])
            Address = (Details['location']['address'])
            MediaType = prod['media_type']
            if prod.get('encryption') != None:
                EncExist = 1
                Encryption = (prod['encryption'])
                Cipher = (prod['encryption']['cipher'])
                KeyLength = (Encryption['keylength'])

            print("Location Category: ",Category)
            print("Place: ",Place)
            print("Address: ",Address[0], Address[1])
            print("Media Type: ",MediaType)
            if EncExist == 1:
                print("Encryption Cipher: ",Cipher, "Keylength: ",KeyLength)

            print("\n")

def menu():
    print("Press 1 to get names of staff")
    print("Press 2 to get all assets")
    print("Press 3 to view asset owners")
    print("Press 4 to quit")
    return int(input("Please select an option: "))

run = menu()

while True:
    print("\n")
    if run == 1:
        StaffNames()
        print("\n")
        run = menu()
    elif run == 2:
        ShowAssets()
        print("\n")
        run = menu()
      
    elif run == 3:
        AssetOwners()
        print("\n")
        run = menu()

    elif run == 4:
        break
        
print("You quit the program")


