# -*- coding: utf-8 -*-


class Contact:

    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email


class ContactBook:

    def __init__(self):
        self._contacts = []

    def add(self, name, phone, email):
        contact = Contact(name, phone, email)
        self._contacts.append(contact)

    def show_all(self):
        for contact in self._contacts:
            self._print_contact(contact)

    def delete(self, name):
        for idx, contact in enumerate(self._contacts):
            if contact.name.lower() == name.lower():
                del self._contacts[idx]
                break

    def search(self, name):
        for contact in self._contacts:
            if contact.name.lower() == name.lower():
                self._print_contact(contact)
                break
        else:
            self._not_found()

    def update(self, name, phone, email):
        for contact in self._contacts:
            if contact.name.lower() == name.lower():
                contact.phone = phone
                contact.email = email
                break
        else:
            self._not_found()

    def _print_contact(self, contact):
        print('--- * --- * --- * --- * --- * --- * --- * ---')
        print('Nombre: {}'.format(contact.name))
        print('Teléfono: {}'.format(contact.phone))
        print('Email: {}'.format(contact.email))
        print('--- * --- * --- * --- * --- * --- * --- * ---')

    def _not_found(self):
        print('*******')
        print('¡No encontrado!')
        print('*******')


def run():

    contact_book = ContactBook()

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
            phone = input('Escribe el telÃ©fono del contacto: ')
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