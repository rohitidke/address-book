
'''Create your own command-line address-book program using which you can browse, add,
modify, delete or search for your contacts such as friends, family and colleagues
and their information such as email address and/or phone number. Details must
be stored for later retrieval.'''


import pickle, os, sys


# Class containing all background stuff (vague).
class AddressBook:
    def load_ab(self):
        global ab
        if os.path.exists(addressbook_path):
            f = open(addressbook_path,'rb')
            ab = pickle.load(f)
        else:
            ab = []

    def get_ab(self):
        name = input('Enter contact\'s name: ')
        email = input('Enter contact\'s email: ')
        phone = input('Enter contact\'s cellphone number: ')
        contactinfo = {
            'name' : name,
            'email' : email,
            'phone' : phone
            }
        ab.append(contactinfo)

    def save_ab(self):
        f = open(addressbook_path,'wb')
        pickle.dump(ab,f)
        f.close

    def browse_ab(self):
        f = open(addressbook_path,'rb')
        ab = pickle.load(f)
        for contact in ab:
            for key,value in contact.items():
                print(' - {1}'.format(key,value))
            print('\n\n')
        print('\n\n##### For browsing structure only!#!!!!',ab,'\n\n')

    def search_ab(self,searchterm,searchby='name'):
        f = open(addressbook_path,'rb')
        ab = pickle.load(f)
        for contact in ab:
            for key1,value1 in contact.items():
                if searchby == key1:
                    if searchterm == value1:
                        for key2,value2 in contact.items():
                            print('- {0} '.format(value2),end='')
                        print('\n')

    def delete_ab(self,searchterm):
        global ab
        f = open(addressbook_path,'rb')
        ab = pickle.load(f)
        count = -1
        for contact in ab:
            count = count + 1
            for key,value in contact.items():
                if searchterm == value:
                    print('You have deleted the details of '+value+'.')
                    del ab[count]
                    AddressBook.save_ab(self)

    def modify_ab(self,searchby,searchterm,newterm):
        global ab
        f = open(addressbook_path,'rb')
        ab = pickle.load(f)
        count = -1
        for contact in ab:
            count = count + 1
            for key,value in contact.items():
                if searchby == key:
                    if searchterm == value:
                        contact[searchby] = newterm
                        ab[count] = contact



# Path to our address book.
addressbook_path = 'C:\python\\address_book.info'


# Chooses where the 'mode' variable is defined.
if len(sys.argv[1:]) != 0:
    mode = sys.argv[1]
else:
    mode = input('Type what you would like to do to your address book contacts:\
\nbrowse, add, modify, delete or search?:\n\n')


# Switch statement detailing what mode we want to use our address book in.
if mode == 'browse':
    abc = AddressBook()
    abc.browse_ab()

elif mode == 'add':
    abc = AddressBook()
    abc.load_ab()
    abc.get_ab()
    abc.save_ab()

elif mode == 'modify':
    searchby = input('Please enter what field type you would like to modify.\
For example, name, email, phone, etc.\n\n')
    searchterm = input('Please enter the detail that you would like to change of your old contact\n\n')
    newterm = input('Please enter the new value that you would like it to be changed to.\n\n')
    abc = AddressBook()
    abc.modify_ab(searchby,searchterm,newterm)

elif mode == 'delete':
    if len(sys.argv[2:]) != 0:
        searchterm = sys.argv[2]
    else:
        searchterm = input('Please enter the name of the contact you would like to delete.')
    abc = AddressBook()
    abc.delete_ab(searchterm)

elif mode == 'search':
    if len(sys.argv[2:]) != 0:
        searchterm = sys.argv[2]
    else:
        searchterm = input('\n\nWho\'s details would you like to search for?\n\n')
    if len(sys.argv[3:]) != 0:
        searchby = sys.argv[3]
    else:
        searchby = input('\n\nWould you like to search by name(default), email, or phone?\n\n')
    abc = AddressBook()
    abc.search_ab(searchterm,searchby)

else:
    print('\nTypo bro!\n')
