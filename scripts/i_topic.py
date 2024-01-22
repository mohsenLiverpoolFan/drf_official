from topic_form.models import Book, Author
import names
import random
from randdate import randdate
import datetime


# //------------------------insert Authors-----------------//
# import
def run():
    data = []
    for i in range(1, 25):
        data.append({
            'name': names.get_first_name(),
            'title': names.get_last_name(),
            'birth_date': datetime.datetime.now()
        })
    Author.objects.bulk_create([
        Author(**d) for d in data
    ])

# //--------insert Book--------------

# def run():
#     data = []
#     authors = Author.objects.all()
#     for i in range(1, 100):
#         data.append({
#             'author': random.choice(authors),
#             'title': names.get_first_name(),
#             'number_of_pages': random.randint(1, 500)
#         })
#     Book.objects.bulk_create([Book(**d) for d in data])
