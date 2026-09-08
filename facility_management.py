#Problem:
#You are an asset and facility management module for the Natioonal Museum of Kenya.
#The administrator wants a mordern system to track and maintain the state of individual display halls.
#Rather than storing room records as unpolished string value, you are tasked with designing a robust, object-oriented archtecture where each exhibition space acts as its own self contained entity.

import json

class Exhibition:

    def __init__(self, room, theme,is_open = True):
        self.room_no = room
        self.theme_name = theme
        self.is_open = is_open

    def close_room(self):
        self.is_open = False

    def open_room(self):
        self.is_open = True 

museum_directory = []        

def write_data():
    filename = "facility.json"
    with open(filename, "w") as file:
        json.dump(museum_directory, file, default = lambda o: o.__dict__, indent =4)
        print(f"Data saved Succesfully to {filename}")

def write_to_txt():
    filename = "facility.txt"
    with open(filename, "w") as file:
        file.write("---NATIONAL MUSEUM OF KENYA, EXHIBITION REPORT---\n\n")
        sorted_dic=sorted(museum_directory, key = lambda exhibition: exhibition.room_no) 
        for i, exhibition in enumerate(sorted_dic,1):
            status = "OPEN" if exhibition.is_open else "CLOSED" 
            line = f"{i}. Room.{exhibition.room_no}: {exhibition.theme_name} [{status}]\n"
            file.write(line) 
            
    print(f"Saved succesfully as {filename}")  

def closed_rooms():
    filename= "Closed_Rooms.txt"
    closed = [exhibition for exhibition in museum_directory if exhibition.is_open == False  ]
    if len(closed) == 0:
        print("All Rooms Are Open!!!")
        return

    with open(filename, "w", encoding="utf-8") as file:
        file.write("-----Closed Rooms-----\n\n")
        sorted_dic= sorted(closed, key= lambda exhibition: exhibition.room_no)
        for i, exhibition in enumerate(sorted_dic, 1):
            line=f"{i}. Room: {exhibition.room_no}: {exhibition.theme_name}\n"
            file.write(line)
        print(f"Saved Sucsessgully to {filename}")

def open_rooms():
    filename="Open_Rooms.txt"
    opened = [exhibition for exhibition in museum_directory if exhibition.is_open == True ] 
    if len(opened) == 0:
        print("There are no Open Rooms!!!")
        return

    with open(filename, "w") as file:
        file.write("-----All Open Rooms-----\n\n")
        sorted_dic = sorted(opened, key = lambda exhibition: exhibition.room_no)
        for i, exhibition in enumerate(sorted_dic, 1):
            line=f"{i}. Room. {exhibition.room_no}: {exhibition.theme_name}\n"
            file.write(line) 
        print(f"Saved Successfully to {filename}")            
                        

def read_data():
    global museum_directory
    filename = "facility.json"
    try:
        with open(filename, "r") as file:
            raw_json =json.load(file)
            museum_directory = []
            for item in raw_json:
                room_obj = Exhibition(
                    room=item["room_no"],
                    theme=item["theme_name"],
                    is_open=item["is_open"]
                    
                )
                museum_directory.append(room_obj)
    except FileNotFoundError:
        print("No json file yet!!!")              

def find_and_close_room(room_id):
    for exhibition in museum_directory:
        if exhibition.room_no == room_id: 
            if exhibition.is_open == True:
                exhibition.close_room()
                print(f"Room {room_id}. {exhibition.theme_name} has been closed!")
                break
            else:
                print(f"Room {room_id}. {exhibition.theme_name} is Already Closed") 
                break   
    else:
        print("Room not found!!")

def find_and_open_room(room_id): 
    for exhibition in museum_directory:
        if exhibition.room_no == room_id: 
            if exhibition.is_open == False:
                exhibition.open_room()
                print(f"Room {room_id}. {exhibition.theme_name} has been Opened!")
                break
            else:
                print(f"Room {room_id}. {exhibition.theme_name} is Already Open")  
                break  
    else:
        print("Room not found!!")


           
def view_rooms():
    print("---The Meuseum Has The Following Rooms---")
    sorted_dic = sorted(museum_directory, key = lambda exhibition: exhibition.room_no)
    for exhibition in sorted_dic:
        print(f"Room: {exhibition.room_no}. {exhibition.theme_name}")



def main():
    read_data()
    while True:
        print("---Museums CLI Interphase---")
        print(f"{int(1)}. Add a room")
        print(f"{int(2)}. View Rooms")
        print(f"{int(3)}. Check room status")
        print(f"{int(4)}. Open a room")
        print(f"{int(5)}. Close a room")
        print(f"{int(6)}. Generate Closed_Rooms.txt")
        print(f"{int(7)}. Generate Open_Rooms.txt")
        print(f"{int(8)}. Save to Txt")
        print(f"{int(9)}. Exit")
        try:

            choice =int(input("What would you like to do?:"))

            if choice == 1:
                while True:
                    try:
                        room= int(input("Enter Room Number:"))
                        for exhibition in museum_directory:
                            if exhibition.room_no == room:
                                print(f"Error!!!! Room {room} Already Exists")
                                break
                        else:    
                            theme= input("Enter Room Theme:")
                            new =Exhibition(room,theme)
                            museum_directory.append(new)
                            print(f"Room {room}. {theme} has been added Successfully ") 
                            break
                    except ValueError:
                        print("ERROR!!!! Room Number should be an integer!!") 

            elif choice == 2:
                view_rooms()           
                
            elif choice == 3:
                try:
                    room_id = int(input("Enter Room ID:"))
                    for exhibition in museum_directory:
                        status = "Open" if exhibition.is_open == True else "Closed"
                        if exhibition.room_no == room_id:
                            print(f"Room {room_id}. {exhibition.theme_name} is {status}")
                            break
                    else:
                        print(f"Room:{room_id} NOT Found!!! ")  
                except ValueError:
                    print("Error!!! Please Enter an integer.")

            elif choice == 4:
                try:
                    room_id = int(input("Enter Room ID:"))
                    find_and_open_room(room_id)
                except ValueError:     
                    print("Error!!!! Room ID should be a Number")        

            elif choice == 5:
                try:
                    room_id = int(input("Enter Room ID:"))
                    find_and_close_room(room_id)
                except ValueError:     
                    print("Error!!!! Room ID should be a Number")

            elif choice == 6:
                closed_rooms()

            elif choice == 7:
                open_rooms()            

            elif choice == 8:
                write_to_txt()

            elif choice == 9:
                write_data()
                print("Goodbye 👋")  
                break        
            else:
                print("Error!:Choice ID should be between 1 and 9. Try Again")
        except ValueError:
            print("Error: Invalid input. Please enter a whole number.") 
            

if __name__ == "__main__":
    exhibition1 = Exhibition(10, "Birds") 
    exhibition2 = Exhibition(11, "Art")
    exhibition3 = Exhibition(12, "Mammals")
    exhibition4 = Exhibition(13, "History Of Kenya")
    exhibition5 = Exhibition(14, "Kenyan cultures") 

    museum_directory.append(exhibition1)
    museum_directory.append(exhibition2)
    museum_directory.append(exhibition3)
    museum_directory.append(exhibition4)
    museum_directory.append(exhibition5) 
    main()   