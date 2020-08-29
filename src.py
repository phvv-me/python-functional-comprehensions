
all_names = ["Arthur", "Pedro", "John", "Aaron", "Paul", "Matthew", "Joseph"]
all_ages = [12, 23, 45, 27, 87, 33, 20]

class TestFilter:

    def test_commom_approach(self):
        names_starting_with_a = []
        for name in all_names:
            if name.startswith("A"):
                names_starting_with_a.append(name)

        assert names_starting_with_a == ["Arthur", "Aaron"]

    def test_isolating_function(self):
        def name_startswith_a(name):
            return name.startswith("A")

        names_starting_with_a = []
        for name in all_names:
            if name_startswith_a(name):
                names_starting_with_a.append(name)

        assert names_starting_with_a == ["Arthur", "Aaron"]

    def test_applying_builtin(self):
        # filter returns an iterable - lazy execution
        names_starting_with_a_iter = filter(lambda name: name.startswith("A"), all_names)

        names_starting_with_a = list(names_starting_with_a_iter)

        assert names_starting_with_a == ["Arthur", "Aaron"]

    def test_applying_list_comprehension(self):
        names_starting_with_a = [name for name in all_names if name.startswith("A")]
        assert names_starting_with_a == ["Arthur", "Aaron"]

class TestMap:

    def test_commom_approach(self):
        all_initials = []
        for name in all_names:
            initial = name[0] + '.'
            all_initials.append(initial)

        assert all_initials == ["A.", "P.", "J.", "A.", "P.", "M.", "J."]
    
    def test_isolating_function(self):
        def get_initial_from_name(name):
            return name[0] + '.'

        all_initials = []
        for name in all_names:
            initial = get_initial_from_name(name)
            all_initials.append(initial)

        assert all_initials == ["A.", "P.", "J.", "A.", "P.", "M.", "J."]

    def test_applying_builtin(self):
        # filter returns an iterable - lazy execution
        all_initials_iter = map(lambda name: name[0] + '.', all_names)

        all_initials = list(all_initials_iter)

        assert all_initials == ["A.", "P.", "J.", "A.", "P.", "M.", "J."]

    def test_applying_list_comprehension(self):
        all_initials = [name[0] + '.' for name in all_names]
        assert all_initials == ["A.", "P.", "J.", "A.", "P.", "M.", "J."]

class TestReduce:

    def test_commom_approach(self):
        sum_of_ages = 0
        for age in all_ages:
            sum_of_ages += age

        assert sum_of_ages == sum(all_ages)
    
    def test_isolating_function(self):
        def add_age(total, to_add):
            return total + to_add

        sum_of_ages = 0
        for age in all_ages:
            sum_of_ages = add_age(sum_of_ages, age)

        assert sum_of_ages == sum(all_ages)

    def test_applying_builtin(self):
        from functools import reduce
        from operator import add

        initial = 0
        sum_of_ages = reduce(add, all_ages, initial)

        assert sum_of_ages == sum(all_ages)

    def test_applying_list_comprehension(self):
        sum_of_ages = 0
        [sum_of_ages := sum_of_ages + age for age in all_ages]

        assert sum_of_ages == sum(all_ages)

class TestCombined:

    def test_applying_list_comprehension(self):
        numbers = range(1, 100)

        def my_map(n):
            return n ** (1/n)

        def my_filter(n):
            return n % 2 == 0

        value = 1
        [value := value * my_map(n) for n in numbers if my_filter(n)]

        assert value == 204.8624348467125
        