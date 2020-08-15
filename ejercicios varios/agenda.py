# -*- coding: utf-8 -*-

import csv

class Contact:

    def __init__(self, name, phone, email): #constructor de Contact
        self.name = name
        self.phone = phone
        self.email = email


class ContactBook:

    def __init__(self): #constructor de contactbook inicializo la lista
        self._contacts = []

    def add(self, name, phone, email):  #agregar nuevo contacto
        contact = Contact(name, phone, email)
        self._contacts.append(contact)
        self._save()

    def show_all(self): #mostrar todos los contactos
        for contact in self._contacts:
            self._print_contact(contact)

    def delete(self, name): #borrar contacto, para evitar errores paso a minúsculas
        for idx, contact in enumerate(self._contacts):
            if contact.name.lower() == name.lower(): 
                del self._contacts[idx]
                self._save()
                break

    def search(self, name): #buscar contacto
        for contact in self._contacts:
            if contact.name.lower() == name.lower():
                self._print_contact(contact)
                break
        else:
            self._not_found()

    def update(self, current_name, name, phone, email):   #actualizar contacto
        for contact in self._contacts:
            if contact.name.lower() == current_name.lower():
                if name != '':
                    contact.name = name
                if phone != '':
                    contact.phone = phone
                if email != '':    
                    contact.email = email
                self._save()
                break
        else:
            self._not_found()

    def _save(self):
        with open('contacts.csv', 'w', newline='') as f:
            writer = csv.writer(f, lineterminator='\r')
            writer.writerow(('name','phone','email'))

            for contact in self._contacts:
                writer.writerow((contact.name,contact.phone, contact.email))

    def _print_contact(self, contact):  #se llama desde search y show_all, para mostrar el contacto encontrado
        print('--- * --- * --- * --- * --- * --- * --- * ---')
        print('Nombre: {}'.format(contact.name))
        print('Teléfono: {}'.format(contact.phone))
        print('Email: {}'.format(contact.email))
        print('--- * --- * --- * --- * --- * --- * --- * ---')

    def _not_found(self):   #se llama desde search y update si no se encontró el contacto
        print('***********')
        print('¡Contacto no encontrado!')
        print('***********')


def run():

    contact_book = ContactBook()    #creo instancia de la clase contactbook (objeto)
    with open('contacts.csv', 'r') as f:
        reader = csv.reader(f)
        for idx, row in enumerate(reader):
            if idx == 0:
                continue
            contact_book.add(row[0], row[1], row[2])

    while True:
        command = str(input('''
            ¿Qué deseas hacer?

            1) Añadir contacto
            2) Atualizar contacto
            3) Buscar contacto
            4) Eliminar contacto
            5) Listar contactos
            6) Salir
        '''))

        if command == '1':
            name = input('Escribe el nombre del contacto: ')
            phone = input('Escribe el tel del contacto: ')
            email = input('Escribe el email del contacto: ')
            contact_book.add(name, phone, email)

        elif command == '2':
            name = input('Escribe el nombre del contacto: ')
            phone = input('Escribe el teléfono del contacto: ')
            email = input('Escribe el email del contacto: ')

            contact_book.update(name, phone, email)

        elif command == '3':

            name = input('Escribe el nombre del contacto: ')

            contact_book.search(name)

        elif command == '4':
            name = input('Escribe el nombre del contacto: ')

            contact_book.delete(name)

        elif command == '5':

            contact_book.show_all()

        elif command == '6':
            break
        else:
            print('Comando no encontrado.')


if __name__ == '__main__':
    print('B I E N V E N I D O  A  L A  A G E N D A')
    run()