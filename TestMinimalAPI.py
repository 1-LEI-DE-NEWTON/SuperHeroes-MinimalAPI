import pip._vendor.requests
#Dont check SSL certificate
pip._vendor.requests.urllib3.disable_warnings(pip._vendor.requests.urllib3.exceptions.InsecureRequestWarning)
url = 'https://localhost:7108/superhero'


metodos = {
    '1': 'GET',
    '2': 'POST',
    '3': 'PUT',
    '4': 'DELETE',
    '5': 'Exit'
}
#See if the server is up
def ServerUp():
    try:
        r = pip._vendor.requests.get(url, verify=False)
        if r.status_code == 200:
            return True
        else:
            return False
    except:
        return False

#Asks the user what method to use
def GetMethod():
    print('Select the method to use:')
    for key, value in metodos.items():
        print(key, value)
    method = input('Method: ')
    if method not in metodos:
        print('Invalid option')
        return GetMethod()
    return method

def Do_Again():
    print("Anything else?")
    do_again_option = input("1. Yes, lets run one more time\n2. No, quit the program")
    if do_again_option == '1':
        API_Requests(GetMethod())
    elif do_again_option == '2':
        quit()
    else:
        print("Invalid option")

#Request the API what the user wants
def API_Requests(method):
    if method == '1':
        print("GET method selected, type the id to search or look all superheroes")
        id = input("Enter the id, if none all superheroes will appear: ")
        r = pip._vendor.requests.get(url + '/' + id, verify=False)
        print(r.text)
    elif method == '2':
        print("POST method selected")
        firstname = input("Enter the first name: ")
        lastname = input("Enter the last name: ")
        heroname = input("Enter the hero name: ")
        r = pip._vendor.requests.post(url, json={'firstname': firstname, 'lastname': lastname, 'heroname': heroname}, verify=False)
        print(r.text)
    elif method == '3':
        print("PUT method selected")
        id = input("Enter the id: ")
        firstname = input("Enter the first name: ")
        lastname = input("Enter the last name: ")
        heroname = input("Enter the hero name: ")
        r = pip._vendor.requests.put(url + '/' + id, json={'firstname': firstname, 'lastname': lastname, 'heroname': heroname}, verify=False)
        print(r.text)
    elif method == '4':
        print("DELETE method selected")
        id = input("Enter the id: ")
        r = pip._vendor.requests.delete(url + '/' + id, verify=False)
        print(r.text)
    elif method == '5':
        print("Exit")
        exit()
    else:
        print("Invalid option")
        return API_Requests(GetMethod())
ServerUp()
API_Requests(GetMethod())
Do_Again()