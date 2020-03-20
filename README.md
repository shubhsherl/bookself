# Bookself

Peer to peer sharing of books(hard-copies).

Django(version: 3.0.4) based book sharing application for local communities like a college.

Add books to your profile, mark it as available to lend, set time available for lend. 
Somebody can borrow, you can keep track of it (no loosing books any more, trying to recall who borrowed what)

Other benefit is that some books are not easily available to order, but are sometimes just around us.

### Requirements
1. django(version >=3.x)
2. python (version >=3.x)
3. django-extensions

### How to Run
```
# Install requirements: 
pip instll -r requirements.txt # with root privilages

# make migrations
python manage.py makemigrations
python manage.py migrate

# run server
python manage.py runserver
```

 