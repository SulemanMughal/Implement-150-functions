# Exercise No. 112

The exercise includes a file *users.json* containing data about users of a certain application.

Implement a function called `filter_active_users()`, which loads the attached *users.json* file and extracts all active users (*is_active -> true*):


    "is_active": true


Then dump active users to a new *active_users.json* file (set indent level to 2).

In the solution, use the built-in *json* package.


**Example:**


    [IN]: filter_active_users()


**The content of the active_users.json file after calling the function:**


    [
      {
        "id": 2,
        "first_name": "Lukas",
        "last_name": "Cottrill",
        "email": "lcottrill1@linkedin.com",
        "gender": null,
        "is_active": true
      },
      {
        "id": 3,
        "first_name": "Heath",
        "last_name": "Rourke",
        "email": "hrourke2@t.co",
        "gender": "Genderfluid",
        "is_active": true
      },
      {
        "id": 4,
        "first_name": "Lucie",
        "last_name": "Brunetti",
        "email": "lbrunetti3@bbb.org",
        "gender": "Non-binary",
        "is_active": true
      },
      {
        "id": 5,
        "first_name": "Minette",
        "last_name": "Graysmark",
        "email": "mgraysmark4@fotki.com",
        "gender": null,
        "is_active": true
      },
      {
        "id": 6,
        "first_name": "Stormi",
        "last_name": "Thresher",
        "email": "sthresher5@umn.edu",
        "gender": "Non-binary",
        "is_active": true
      },
      {
        "id": 9,
        "first_name": "Anton",
        "last_name": "Hugnin",
        "email": "ahugnin8@flickr.com",
        "gender": "Genderqueer",
        "is_active": true
      }
    ]


You only need to implement the `filter_active_users()` function. The tests run several test cases to validate the solution.