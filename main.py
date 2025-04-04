from school_schedule.student import Student

# first instance
quinn = Student(
                "Quinn",
                "junior",
                [
                    "Pre-Calc",
                    "English III",
                    "World History",
                    "Gym",
                    "Chemistry",
                    "Music Composition"
                ]
            )

quinn.add_class("Painting")
quinn.get_num_classes()
print(quinn.summary())

# second instance
claire = Student(
                "Claire",
                "freshmen",
                [
                    "Algebra",
                    "Writing",
                    "Contemporary Issues",
                    "Gym",
                    "Earth Science",
                    "Painting"
                ]
            )

claire.get_num_classes()
print(claire.summary())
