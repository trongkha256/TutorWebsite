from decimal import Decimal

from store.models import Course


class Basket():
    """
    A base Basket class, providing some default behaviors that
    can be inherited or overrided, as necessary.
    """

    def __init__(self, request):
        self.session = request.session
        basket = self.session.get('skey')
        if 'skey' not in request.session:
            basket = self.session['skey'] = {}
        self.basket = basket

    def add(self, course, qty):
        """
        Adding and updating the users basket session data
        """
        course_id = str(course.id)

        if course_id in self.basket:
            self.basket[course_id]['qty'] = qty
        else:
            self.basket[course_id] = {'price': str(course.price), 'qty': qty}

        self.save()

    def __iter__(self):
        """
        Collect the course_id in the session data to query the database
        and return courses
        """
        course_ids = self.basket.keys()
        courses = Course.courses.filter(id__in=course_ids)
        basket = self.basket.copy()

        for course in courses:
            basket[str(course.id)]['course'] = course

        for item in basket.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['qty']
            yield item

    def __len__(self):
        """
        Get the basket data and count the qty of items
        """
        return sum(item['qty'] for item in self.basket.values())

    def update(self, course, qty):
        """
        Update values in session data
        """
        course_id = str(course)
        if course_id in self.basket:
            self.basket[course_id]['qty'] = qty
        self.save()

    def get_total_price(self):
        return sum(Decimal(item['price']) * item['qty'] for item in self.basket.values())

    def delete(self, course):
        """
        Delete item from session data
        """
        course_id = str(course)

        if course_id in self.basket:
            del self.basket[course_id]
            print(course_id)
            self.save()

    def save(self):
        self.session.modified = True





""" 
Code in this file has been inspried/reworked from other known works. Plese ensure that
the License below is included in any of your work that is directly copied from
this source file.


MIT License

Copyright (c) 2019 Packt

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE. 
"""
