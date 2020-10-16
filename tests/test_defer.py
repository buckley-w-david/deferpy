from deferpy import defer

def test_defer_runs():
    defer_ran = False

    @defer()
    def func():
        def inner():
            nonlocal defer_ran
            defer_ran = True
        func.defer(inner)

    func()
    assert defer_ran

def test_defer_runs_on_exit():
    values = []

    @defer()
    def func():
        def inner():
            nonlocal values
            values.append('inner')
        func.defer(inner)
        values.append('outer')

    func()
    assert len(values) == 2
    assert values[0] == 'outer'
    assert values[1] == 'inner'

# A deferred function's arguments are evaluated when the defer statement is evaluated.
def test_defer_evaluated_on_defer():
    values = []

    @defer()
    def func():
        def inner(value):
            nonlocal values
            values.append(value)
        x = 0
        func.defer(inner, x)
        x += 1

    func()
    assert len(values) == 1
    assert values[0] == 0

# Deferred function calls are executed in Last In First Out order after the surrounding function returns.
def test_defer_is_lifo():
    values = []

    @defer()
    def func():
        def inner(value):
            nonlocal values
            values.append(value)
        func.defer(inner, 1)
        func.defer(inner, 2)
        func.defer(inner, 3)

    func()
    assert len(values) == 3
    assert values[0] == 3
    assert values[1] == 2
    assert values[2] == 1

def test_defer_can_access_return(capsys):
    values = []

    @defer()
    def func():
        func.defer(print, _)
        return 5

    func()
    captured = capsys.readouterr()
    assert captured.out == "5\n"

# Deferred functions may read and assign to the returning function's named return values.
def test_defer_can_edit_return():
    @defer()
    def func():
        def edit():
            global _ # Unfortunatly have to use global
            _ += 1
        func.defer(edit)
        return 1
    rval = func()
    assert rval == 2


def test_defer_can_edit_named_return():
    @defer(name='i')
    def func():
        def edit():
            global i # Unfortunatly have to use global
            i += 1
        func.defer(edit)
        return 1
    rval = func()
    assert rval == 2
