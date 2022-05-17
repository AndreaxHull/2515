from instructor import Instructor


def main():
    mike_mulder = Instructor("Mike",
                             "Mulder",
                             "CIT",
                             "A01317798")
    susan_lee = Instructor("Susan",
                           "Lee",
                           "CIT",
                           "A01317799")
    andrew_hull = Instructor("Andrew",
                             "Hull",
                             "CIT",
                             "A01317710")

    mike_mulder.add_course("ACIT2515")
    mike_mulder.add_course("COMP1516")
    mike_mulder.remove_course("ACIT2515")
    if mike_mulder.check_course("ACIT2515") == False:
        print("I should be enrolled in ACIT2515!")
    print(mike_mulder.get_details())

    susan_lee.add_course("ACIT1515")
    susan_lee.add_course("ACIT2116")
    susan_lee.add_course("ACIT1111")
    susan_lee.add_course("ACIT2515")
    susan_lee.add_course("MATH1511")
    susan_lee.remove_course("ACIT1515")
    susan_lee.remove_course("ACIT2116")
    susan_lee.remove_course("ACIT1111")
    susan_lee.add_course("MATH1511")
    print(susan_lee.get_details())

    print(andrew_hull.get_details())


if __name__ == "__main__":
    main()
