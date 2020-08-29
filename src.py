
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
        names_starting_with_a_iter = filter(
            lambda name: name.startswith("A"), all_names)

        names_starting_with_a = list(names_starting_with_a_iter)

        assert names_starting_with_a == ["Arthur", "Aaron"]

    def test_applying_list_comprehension(self):
        names_starting_with_a = [
            name for name in all_names if name.startswith("A")]
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
        # map returns an iterable - lazy execution
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
        from itertools import accumulate
        from operator import add

        sum_of_ages = 0
        accumulated_ages = [sum_of_ages := sum_of_ages +
                            age for age in all_ages]  # amazing!

        assert sum_of_ages == sum(all_ages)
        assert accumulated_ages == list(accumulate(all_ages, add))


class TestCombined:

    def test_join_strings(self):
        from functools import reduce
        from operator import add

        awesome_names = ["Amanda", "William", "Bob", "Evangeline",
                         "Mark", "Sarah", "Oliver", "Joe", "Matthew", "Edward"]

        # 1. filter
        filtered = list(filter(lambda name: len(name) > 4, awesome_names))

        # 2. map
        mapped = list(map(lambda name: name[0], filtered))

        # 3. reduce
        reduced = reduce(add, mapped, "")

        assert reduced == "".join(mapped)

    def test_join_strings_list_comprehension(self):
        from itertools import accumulate

        awesome_names = ["Amanda", "William", "Bob", "Evangeline",
                         "Mark", "Sarah", "Oliver", "Joe", "Matthew", "Edward"]

        list_comprehension = ""
        accumulated = [list_comprehension := list_comprehension + name[0]
                       for name in awesome_names if len(name) > 4]

        assert list_comprehension == "AWESOME"

    def test_join_strings_list_comprehension_clean_code(self):
        from functools import reduce
        from operator import add

        awesome_names = ["Amanda", "William", "Bob", "Evangeline",
                         "Mark", "Sarah", "Oliver", "Joe", "Matthew", "Edward"]

        mapped_and_filtered = [name[0]
                               for name in awesome_names if len(name) > 4]

        result = reduce(add, mapped_and_filtered, "")

        assert result == "".join(mapped_and_filtered)


class TestExtra:

    def test_build_matrix_with_list_comprehension(self):
        matrix = [[1 if x == y else 0 for x in range(5)] for y in range(5)]

        assert matrix == [[1, 0, 0, 0, 0],
                          [0, 1, 0, 0, 0],
                          [0, 0, 1, 0, 0],
                          [0, 0, 0, 1, 0],
                          [0, 0, 0, 0, 1]]

    def test_flatten_with_list_comprehension(self):
        matrix = [[10, 11, 12, 13],
                  [14, 15, 16, 17],
                  [18, 19, 20, 21],
                  [22, 23, 24, 25]]

        flattened = [n for row in matrix for n in row]

        assert flattened == list(range(10, 26))

    def test_build_dict_list_comprehension(self):
        keys = ["a", "b", "c"]
        vals = [100, 200, 300]

        my_dict = {k: v for k, v in zip(keys, vals)}

        assert my_dict == {"a": 100, "b": 200, "c": 300}

    def test_list_of_dicts_into_dict_of_lists(self):
        # list of dicts
        lod = [
            {'a': 'hi', 'y': 'bye'},
            {'x': 1, 'y': 2, 'z': 3},
            {'z': 'wow!', 'a': [99, '66']},
        ]

        # flat set of keys
        set_of_keys = {key for dic in lod for key in dic.keys()} 

        # dict of lists
        dol = {key: [dic[key] for dic in lod if key in dic] for key in set_of_keys}

        assert dol == {
            'a': ['hi', [99, '66']],  # ATTENTION: it does not flatten!
            'x': [1],
            'y': ['bye', 2],
            'z': [3, 'wow!']
        }

    def test_dict_of_lists_into_list_of_dicts(self):
        from itertools import zip_longest

        # dict of lists
        dol = {
            'a': ['hi', [99, '66']],
            'x': [1],
            'y': ['bye', 2],
            'z': [3, 'wow!']
        }

        _keys = dol.keys()
        _values = zip_longest(*dol.values())  # this will make all lists "the same size"

        lod = [{key: val for key, val in zip(_keys, column) if val is not None} for column in _values]  # then we filter the None values off

        assert lod == [
           {'a': 'hi', 'x': 1, 'y': 'bye', 'z': 3},
           {'a': [99, '66'], 'y': 2, 'z': 'wow!'},
        ]
    

    def test_applying_list_comprehension(self):
        numbers = range(1, 100)

        def my_map(n):
            return n ** (1/n)

        def my_filter(n):
            return n % 2 == 0

        value = 1
        [value := value * my_map(n) for n in numbers if my_filter(n)]

        assert value == 204.8624348467125
