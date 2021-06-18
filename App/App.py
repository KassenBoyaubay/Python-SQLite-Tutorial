import database

# add a record to db
# database.add_one("Pan", "Brown", "pan@br.com")

# delete a record
# database.delete_one('7')

# add many records
# people = [
#     ('Brenda', 'Smith', 'brenda@mail.ru'),
#     ('Mura', 'Smith', 'mura@mail.ru'),
#     ('Kokki', 'Smith', 'kokki@mail.ru')
# ]
# database.add_many(people)

# lookup a record w/ email
database.email_lookup('john@code.com')

# show all records
database.show_all()
