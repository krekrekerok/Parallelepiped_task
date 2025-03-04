import math as mt


def get_diag(a: float, b: float, c: float) -> str:
    """
    Calculates the main diagonal of a parallelepiped using the formula:
    sqrt(a^2 + b^2 + c^2).

    Parameters:
    a (float): Length of one side of the parallelepiped.
    b (float): Length of the second side of the parallelepiped.
    c (float): Length of the third side of the parallelepiped.

    Returns:
    str: The main diagonal, rounded to 2 decimal places.
    """
    return str(round(mt.sqrt(a**2 + b**2 + c**2), 2))


def get_volume(a: float, b: float, c: float) -> str:
    """
    Calculates the volume of a parallelepiped using the formula: a * b * c.

    Parameters:
    a (float): Length of one side of the parallelepiped.
    b (float): Length of the second side of the parallelepiped.
    c (float): Length of the third side of the parallelepiped.

    Returns:
    str: The volume of the parallelepiped, rounded to 2 decimal places.
    """
    return str(round(a * b * c, 2))


def get_surface(a: float, b: float, c: float) -> str:
    """
    Calculates the surface area of a parallelepiped using the formula:
    2 * (a * b + a * c + b * c).

    Parameters:
    a (float): Length of one side of the parallelepiped.
    b (float): Length of the second side of the parallelepiped.
    c (float): Length of the third side of the parallelepiped.

    Returns:
    str: The surface area of the parallelepiped, rounded to 2 decimal places.
    """
    return str(round(2 * (a * b + a * c + b * c), 2))


def get_alpha(a: float, b: float, c: float) -> str:
    """
    Calculates the angle alpha between the diagonal and side a of the parallelepiped
    using the formula: acos(a / sqrt(a^2 + b^2 + c^2)).

    Parameters:
    a (float): Length of one side of the parallelepiped.
    b (float): Length of the second side of the parallelepiped.
    c (float): Length of the third side of the parallelepiped.

    Returns:
    str: Angle alpha in radians, rounded to 2 decimal places.
    """
    return str(round(mt.acos(a / mt.sqrt(a**2 + b**2 + c**2)), 2))


def get_beta(a: float, b: float, c: float) -> str:
    """
    Calculates the angle beta between the diagonal and side b of the parallelepiped
    using the formula: acos(b / sqrt(a^2 + b^2 + c^2)).

    Parameters:
    a (float): Length of one side of the parallelepiped.
    b (float): Length of the second side of the parallelepiped.
    c (float): Length of the third side of the parallelepiped.

    Returns:
    str: Angle beta in radians, rounded to 2 decimal places.
    """
    return str(round(mt.acos(b / mt.sqrt(a**2 + b**2 + c**2)), 2))


def get_gamma(a: float, b: float, c: float) -> str:
    """
    Calculates the angle gamma between the diagonal and side c of the parallelepiped
    using the formula: acos(c / sqrt(a^2 + b^2 + c^2)).

    Parameters:
    a (float): Length of one side of the parallelepiped.
    b (float): Length of the second side of the parallelepiped.
    c (float): Length of the third side of the parallelepiped.

    Returns:
    str: Angle gamma in radians, rounded to 2 decimal places.
    """
    return str(round(mt.acos(c / mt.sqrt(a**2 + b**2 + c**2)), 2))


def get_sphr_radius(a: float, b: float, c: float) -> str:
    """
    Calculates the radius of the circumscribed sphere of the parallelepiped
    using the formula: sqrt(a^2 + b^2 + c^2) / 2.

    Parameters:
    a (float): Length of one side of the parallelepiped.
    b (float): Length of the second side of the parallelepiped.
    c (float): Length of the third side of the parallelepiped.

    Returns:
    str: The radius of the circumscribed sphere, rounded to 2 decimal places.
    """
    return str(round(mt.sqrt(a**2 + b**2 + c**2) / 2, 2))


def get_sphr_volume(a: float, b: float, c: float) -> str:
    """
    Calculates the volume of the circumscribed sphere of the parallelepiped
    using the formula: 4/3 * pi * (sqrt(a^2 + b^2 + c^2) / 2)^3.

    Parameters:
    a (float): Length of one side of the parallelepiped.
    b (float): Length of the second side of the parallelepiped.
    c (float): Length of the third side of the parallelepiped.

    Returns:
    str: The volume of the circumscribed sphere, rounded to 2 decimal places.
    """
    return str(round(4 / 3 * mt.pi * (mt.sqrt(a**2 + b**2 + c**2) / 2) ** 3, 2))


def calc_char(parallelepipeds_json: dict = {}) -> dict:
    """
    Calculates the characteristics (main diagonal, volume, surface area, angles,
    radius, and volume of circumscribed sphere) for each parallelepiped in the input dictionary.

    Parameters:
    parallelepipeds_json (dict): A dictionary where each key is an identifier for a parallelepiped
                                 and the value is another dictionary containing side lengths 'a', 'b', and 'c'.

    Returns:
    dict: A dictionary of calculated characteristics for each parallelepiped.
    """

    for fig_values in parallelepipeds_json.values():
        for value in fig_values:
            fig_values[value] = float(fig_values[value])

    characteristics = {
        key: {
            "diag": get_diag(value["a"], value["b"], value["c"]),
            "volume": get_volume(value["a"], value["b"], value["c"]),
            "surface_area": get_surface(value["a"], value["b"], value["c"]),
            "alpha": get_alpha(value["a"], value["b"], value["c"]),
            "beta": get_beta(value["a"], value["b"], value["c"]),
            "gamma": get_gamma(value["a"], value["b"], value["c"]),
            "radius_described_sphere": get_sphr_radius(
                value["a"], value["b"], value["c"]
            ),
            "volume_described_sphere": get_sphr_volume(
                value["a"], value["b"], value["c"]
            ),
        }
        for key, value in parallelepipeds_json.items()
    }

    return characteristics
