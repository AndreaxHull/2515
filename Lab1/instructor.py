class Instructor:
    """ Represents an Instructor for teaching a course """

    def __init__(self, first_name, last_name, program, employee_number):
        self._first_name = first_name
        self._last_name = last_name
        self._program = program
        self._employee_number = employee_number
        self._courses = []

    def add_course(self, course):
        """ Adds a course for the instructor """

        if course not in self._courses:

            self._courses.append(course)

    def remove_course(self, course):
        """ Removes a course for the instructor """

        if course not in self._courses:
            raise ValueError("There is no course to remove")
        self._courses.remove(course)

    def check_course(self, course):
        """ Checks if the instructor is teaching a course """

        return course in self._courses

    def full_name(self):
        """ Returns the full name of the instructor """

        name = (f"{self._first_name} {self._last_name}")
        return name

    def get_details(self):
        """ Returns the instructor details """

        if self._courses:
            courses_string = (", ".join(self._courses))

            details = f"{self.full_name()} is an instructor in the {self._program} program with employee number " \
                f"{self._employee_number} teaching the following courses: {courses_string}"

        else:
            details = f"{self.full_name()} is an instructor in the {self._program} program with employee number " \
                f"{self._employee_number} teaching no courses"

        return details
