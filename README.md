dipatch.py
==========

dispatch.py is python implementation of Debain PTS dipatch.pl[Original author: Raphael Hertzog] used to recieve a mail and forward to already subscribed users/developers based upon a number of parameters.

And yes, this is not a line-by-line translation. The original script uses procedural paradigm, I've used Object-oriented programming paradigm and have tried to the code cleaner and less cumber some.

To run this dispatch.py use following commands:
1. python manage.py syncdb
2. python manage.py send_mailes <packagename>