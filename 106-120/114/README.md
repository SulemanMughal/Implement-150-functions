# Exercise No. 114

The exercise includes a file *users.json* containing data about users of a certain application.

Implement a function called `json_to_object()` that loads the attached *users.json* file and creates the User class using the built-in *collections* module and the *namedtuple* function. Attribute names of the *User* class are the keys from *users.json* file. Then create an instance of the *User* class for each user and return all users as a list.


**Example:**


    [IN]: json_to_object()


**Output:**


    [User(id=1, first_name='Huntington', last_name='McComiskie', email='hmccomiskie0@admin.ch', gender=None, is_active=False), User(id=2, first_name='Lukas', last_name='Cottrill', email='lcottrill1@linkedin.com', gender=None, is_active=True), User(id=3, first_name='Heath', last_name='Rourke', email='hrourke2@t.co', gender='Genderfluid', is_active=True), User(id=4, first_name='Lucie', last_name='Brunetti', email='lbrunetti3@bbb.org', gender='Non-binary', is_active=True), User(id=5, first_name='Minette', last_name='Graysmark', email='mgraysmark4@fotki.com', gender=None, is_active=True), User(id=6, first_name='Stormi', last_name='Thresher', email='sthresher5@umn.edu', gender='Non-binary', is_active=True), User(id=7, first_name='Rochella', last_name='Berry', email='rberry6@moonfruit.com', gender='Female', is_active=False), User(id=8, first_name='Lock', last_name='Pablo', email='lpablo7@networkadvertising.org', gender='Genderqueer', is_active=False), User(id=9, first_name='Anton', last_name='Hugnin', email='ahugnin8@flickr.com', gender='Genderqueer', is_active=True), User(id=10, first_name='Stephi', last_name='Jacqueme', email='sjacqueme9@exblog.jp', gender='Male', is_active=False)]


**Formatted output:**


    User(id=1, first_name='Huntington', last_name='McComiskie', email='hmccomiskie0@admin.ch', gender=None, is_active=False)
    User(id=2, first_name='Lukas', last_name='Cottrill', email='lcottrill1@linkedin.com', gender=None, is_active=True)
    User(id=3, first_name='Heath', last_name='Rourke', email='hrourke2@t.co', gender='Genderfluid', is_active=True)
    User(id=4, first_name='Lucie', last_name='Brunetti', email='lbrunetti3@bbb.org', gender='Non-binary', is_active=True)
    User(id=5, first_name='Minette', last_name='Graysmark', email='mgraysmark4@fotki.com', gender=None, is_active=True)
    User(id=6, first_name='Stormi', last_name='Thresher', email='sthresher5@umn.edu', gender='Non-binary', is_active=True)
    User(id=7, first_name='Rochella', last_name='Berry', email='rberry6@moonfruit.com', gender='Female', is_active=False)
    User(id=8, first_name='Lock', last_name='Pablo', email='lpablo7@networkadvertising.org', gender='Genderqueer', is_active=False)
    User(id=9, first_name='Anton', last_name='Hugnin', email='ahugnin8@flickr.com', gender='Genderqueer', is_active=True)
    User(id=10, first_name='Stephi', last_name='Jacqueme', email='sjacqueme9@exblog.jp', gender='Male', is_active=False)


You just need to implement the `json_to_object()` function. The tests run several test cases to validate the solution.