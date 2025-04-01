from school_schedule.student import Student


# Write your tests here!
def test_instance_created_correctly():
    # Arrange
    name = "Stella"
    grade = "junior"
    classes = ["Programming", "Databases", "Computer Architecture"]

    # Act
    new_student = Student(name, grade, classes)

    # Assert
    assert new_student.name == name
    assert new_student.grade == grade
    assert new_student.classes == classes


def test_add_class_to_non_empty_list():
    # Arrange
    name = "Stella"
    grade = "junior"
    classes = ["Programming", "Databases", "Computer Architecture"]
    new_student = Student(name, grade, classes)

    # Act
    updated_classes = new_student.add_class("Web Development")

    # Assert
    assert len(new_student.classes) == 4
    assert len(updated_classes) == 4
    assert updated_classes == new_student.classes


def test_get_num_classes_nonempty_list():
    # Arrange
    name = "Stella"
    grade = "junior"
    classes = ["Programming", "Databases", "Computer Architecture"]
    new_student = Student(name, grade, classes)

    # Act
    num_classes = new_student.get_num_classes()

    # Assert
    assert num_classes == 3


def test_get_num_classes_empty_list():
    # Arrange
    name = "Stella"
    grade = "junior"
    classes = []
    new_student = Student(name, grade, classes)

    # Act
    num_classes = new_student.get_num_classes()

    # Assert
    assert num_classes == 0


def test_display_correct_classes():
    # Arrange
    name = "Stella"
    grade = "junior"
    classes = ["Programming", "Databases", "Computer Architecture"]
    new_student = Student(name, grade, classes)

    # Act
    display_string = new_student.display_classes()

    # Assert
    assert display_string == "Programming, Databases, Computer Architecture"


def test_diplay_when_classes_list_empty():
    # Arrange
    name = "Stella"
    grade = "junior"
    classes = []
    new_student = Student(name, grade, classes)

    # Act
    classes_message = new_student.display_classes()

    # Assert
    assert classes_message == ""


def test_summary_message_has_correct_values():
    # Arrange
    name = "Stella"
    grade = "junior"
    classes = ["Programming", "Databases", "Computer Architecture"]
    new_student = Student(name, grade, classes)

    # Act
    summary_output = new_student.summary()

    # Assert
    assert summary_output == "Stella is a junior enrolled in 3 classes: Programming, Databases, Computer Architecture"
