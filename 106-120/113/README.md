# Exercise No. 113

The exercise includes a file *users.json* containing data about users of a certain application.

Implement a function called `json_to_csv()` which loads the attached *users.json* file, converts the file contents to the *csv (comma-separated values)* format, and saves it to the *users.csv* file.

In the solution, use the built-in *json* package.


**Example:**



    [IN]: json_to_csv()


**The contents of the users.csv file after calling the function:**


    id,first_name,last_name,email,gender,is_active
    1,Huntington,McComiskie,hmccomiskie0@admin.ch,None,False
    2,Lukas,Cottrill,lcottrill1@linkedin.com,None,True
    3,Heath,Rourke,hrourke2@t.co,Genderfluid,True
    4,Lucie,Brunetti,lbrunetti3@bbb.org,Non-binary,True
    5,Minette,Graysmark,mgraysmark4@fotki.com,None,True
    6,Stormi,Thresher,sthresher5@umn.edu,Non-binary,True
    7,Rochella,Berry,rberry6@moonfruit.com,Female,False
    8,Lock,Pablo,lpablo7@networkadvertising.org,Genderqueer,False
    9,Anton,Hugnin,ahugnin8@flickr.com,Genderqueer,True
    10,Stephi,Jacqueme,sjacqueme9@exblog.jp,Male,False


You just need to implement the `json_to_csv()` function. The tests run several test cases to validate the solution.