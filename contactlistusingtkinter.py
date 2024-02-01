#it is usually a contact book which consists of contact name and contact number
#here, we need to make use of 4 functions= add_contact(),update_contact(),delete_contact(),search_contact()
#here we are making use of tkinter which is used to make a gui using python
#we need to import it in your program them make use of it while creating labels,entry boxes,buttons(add,update,delete,search)
#all the functions need to be mentioned in the "command" of their own button(calling function)



#TASK-5


import tkinter as tk

contact_list={}
window=tk.Tk()
window.title("contact-book")
label_instructions=tk.Label(window,text="Contact-Book")
label_instructions.pack()

def add_contact():
    name=entry_name.get()
    phone_number=entry_phone.get()
    
    contact_list[name]=phone_number
    listbox_contacts.insert(tk.END,f"{name}\t\t  {phone_number}")
    entry_name.delete(0,tk.END)
    entry_phone.delete(0,tk.END)
    entry_email.delete(0,tk.END)
    entry_address.delete(0,tk.END)
    
    
def search_contact():
    search_name=entry_search.get()
    if search_name in contact_list:
        result_label1.config(text=f"{search_name}: {contact_list[search_name]}")
    else:
        result_label1.config(text="contact not found")
        

def delete_contact():
    selected_index=listbox_contacts.curselection()
    if selected_index:
       selected_contact=listbox_contacts.get(selected_index)
       name=selected_contact.split("\t")[0]
       contact_list.pop(name)
       listbox_contacts.delete(selected_index)
       
       
def update_contact():
    selected_index=listbox_contacts.curselection()
    selected_contact=listbox_contacts.get(selected_index)
    name=selected_contact.split("\t")[0]
    updated_phone=entry_update.get()
    contact_list[name]=updated_phone
    listbox_contacts.delete(selected_index)
    listbox_contacts.insert(tk.END,f"{name}\t\t  {updated_phone}")
    entry_update.delete(0,tk.END)
    
#Add contact 
label_name=tk.Label(window,text="Name:")
entry_name=tk.Entry(window)
label_phone=tk.Label(window,text="Phone-number:")
entry_phone=tk.Entry(window)
label_email=tk.Label(window,text="Email:")
entry_email=tk.Entry(window)
label_address=tk.Label(window,text="Address:")
entry_address=tk.Entry(window)
button_add=tk.Button(window,text="Add Contact",command=add_contact)

label_name.pack()
entry_name.pack()
label_phone.pack()
entry_phone.pack()
label_email.pack()
entry_email.pack()
label_address.pack()
entry_address.pack()

button_add.pack()

#listbox of all contacts
listbox_contacts=tk.Listbox(window)
listbox_contacts.pack()

#search contact
result_label1=tk.Label(window,text="")
entry_search=tk.Entry(window)
button_search=tk.Button(window,text="Search Contact",command=search_contact)
result_label2=tk.Label(window,text="")

result_label1.pack()
entry_search.pack()
button_search.pack()
result_label2.pack()

#update contact
entry_update=tk.Entry(window)
button_update=tk.Button(window,text="Update Contact",command=update_contact)

entry_update.pack()
button_update.pack()

#delete contact
entry_delete=tk.Entry(window)
button_delete=tk.Button(window,text="Delete Contact",command=delete_contact)
button_delete.pack()

#run the tkinter main loop
window.mainloop()