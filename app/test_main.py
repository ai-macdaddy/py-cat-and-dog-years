import pytest
from app import main


@pytest.mark.parametrize(
    "cat_age, dog_age",
    [
        ("1", 1),
        (1, "1"),
        ([1], 1),
        (1, [1]),
        (None, 1),
        (1, None),
        (1.5, 1),
        (1, 1.5),
        ({1}, 1),
        (1, {1}),
        (True, 1),
        (1, True),
        ((1,), 1),
        (1, (1,)),
    ],
)
def test_function_parameters_are_integers(cat_age, dog_age):
    with pytest.raises(TypeError):
        main.get_human_age(cat_age, dog_age)


# Test2


@pytest.mark.parametrize(
    "cat_age, dog_age",
    [
        (1, 1),
        (0, 0),
    ],
)
def test_function_returns_list(cat_age, dog_age):
    assert (
        type(main.get_human_age(cat_age, dog_age)) is list
    ), "The function should return a list"


# Test3


@pytest.mark.parametrize(
    "cat_age, dog_age, expected",
    [
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 28, [2, 2]),
        (28, 29, [3, 3]),
        (100, 100, [21, 17]),
    ],
)
def test_function_calculates_human_age_correctly(cat_age, dog_age, expected):
    result = main.get_human_age(cat_age, dog_age)
    assert result == expected, (
        f"Expected {expected} but got {result} "
        f"for cat_age={cat_age} and dog_age={dog_age}"
    )


# Test4


@pytest.mark.parametrize(
    "cat_age, dog_age",
    [
        (-1, 1),
        (1, -1),
    ],
)
def test_function_with_negative_ages(cat_age, dog_age):
    with pytest.raises(ValueError):
        main.get_human_age(cat_age, dog_age)
        print(
            "Test failed for negative ages. "
            "Both cat_age and dog_age should be non-negative integers."
        )


# Test5


@pytest.mark.parametrize(
    "cat_age, dog_age",
    [
        (101, 102),
        (1001, 1002),
        (10001, 10002),
    ],
)
def test_function_with_large_ages(cat_age, dog_age):
    with pytest.raises(ValueError):
        main.get_human_age(cat_age, dog_age)
