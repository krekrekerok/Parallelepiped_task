import math as mt


def get_avg_diag(characteristics: dict) -> str:
    """
    Calculates the average main diagonal of all parallelepipeds in the dataset.

    Parameters:
    characteristics (dict): A dictionary containing characteristics of multiple parallelepipeds.

    Returns:
    str: The average main diagonal, rounded to 2 decimal places.
    """

    diags = [float(figure["diag"]) for figure in characteristics.values()]
    return str(round(sum(diags) / len(diags), 2))


def get_avg_volume(characteristics: dict) -> str:
    """
    Calculates the average volume of all parallelepipeds in the dataset.

    Parameters:
    characteristics (dict): A dictionary containing characteristics of multiple parallelepipeds.

    Returns:
    str: The average volume, rounded to 2 decimal places.
    """

    volumes = [float(figure["volume"]) for figure in characteristics.values()]
    return str(round(sum(volumes) / len(volumes), 2))


def get_avg_surface(characteristics: dict) -> str:
    """
    Calculates the average surface area of all parallelepipeds in the dataset.

    Parameters:
    characteristics (dict): A dictionary containing characteristics of multiple parallelepipeds.

    Returns:
    str: The average surface area, rounded to 2 decimal places.
    """

    surface = [float(figure["surface_area"]) for figure in characteristics.values()]
    return str(round(sum(surface) / len(surface), 2))


def get_avg_alpha(characteristics: dict) -> str:
    """
    Calculates the average angle alpha (between the diagonal and side a)
    of all parallelepipeds in the dataset.

    Parameters:
    characteristics (dict): A dictionary containing characteristics of multiple parallelepipeds.

    Returns:
    str: The average angle alpha in radians, rounded to 2 decimal places.
    """

    alpha = [float(figure["alpha"]) for figure in characteristics.values()]
    return str(round(sum(alpha) / len(alpha), 2))


def get_avg_beta(characteristics: dict) -> str:
    """
    Calculates the average angle beta (between the diagonal and side b)
    of all parallelepipeds in the dataset.

    Parameters:
    characteristics (dict): A dictionary containing characteristics of multiple parallelepipeds.

    Returns:
    str: The average angle beta in radians, rounded to 2 decimal places.
    """

    beta = [float(figure["beta"]) for figure in characteristics.values()]
    return str(round(sum(beta) / len(beta), 2))


def get_avg_gamma(characteristics: dict) -> str:
    """
    Calculates the average angle gamma (between the diagonal and side c)
    of all parallelepipeds in the dataset.

    Parameters:
    characteristics (dict): A dictionary containing characteristics of multiple parallelepipeds.

    Returns:
    str: The average angle gamma in radians, rounded to 2 decimal places.
    """

    gamma = [float(figure["gamma"]) for figure in characteristics.values()]
    return str(round(sum(gamma) / len(gamma), 2))


def get_avg_sphr_radius(characteristics: dict) -> str:
    """
    Calculates the average radius of the circumscribed sphere
    for all parallelepipeds in the dataset.

    Parameters:
    characteristics (dict): A dictionary containing characteristics of multiple parallelepipeds.

    Returns:
    str: The average radius of the circumscribed sphere, rounded to 2 decimal places.
    """

    sphr_radius = [
        float(figure["radius_described_sphere"]) for figure in characteristics.values()
    ]
    return str(round(sum(sphr_radius) / len(sphr_radius), 2))


def get_avg_sphr_volume(characteristics: dict) -> str:
    """
    Calculates the average volume of the circumscribed sphere
    for all parallelepipeds in the dataset.

    Parameters:
    characteristics (dict): A dictionary containing characteristics of multiple parallelepipeds.

    Returns:
    str: The average volume of the circumscribed sphere, rounded to 2 decimal places.
    """

    sphr_volume = [
        float(figure["volume_described_sphere"]) for figure in characteristics.values()
    ]
    return str(round(sum(sphr_volume) / len(sphr_volume), 2))


def calc_stats(characteristics_json: dict = {}) -> dict:
    """
    Calculates statistical averages for various characteristics of parallelepipeds.

    Parameters:
    characteristics_json (dict): A dictionary containing characteristics of multiple parallelepipeds.

    Returns:
    dict: A dictionary containing the average values for:
        - Main diagonal
        - Volume
        - Surface area
        - Alpha angle
        - Beta angle
        - Gamma angle
        - Radius of the circumscribed sphere
        - Volume of the circumscribed sphere
    """

    statistics = {
        "avg_diag": get_avg_diag(characteristics_json),
        "avg_volume": get_avg_volume(characteristics_json),
        "avg_surface_area": get_avg_surface(characteristics_json),
        "avg_alpha": get_avg_alpha(characteristics_json),
        "avg_beta": get_avg_beta(characteristics_json),
        "avg_gamma": get_avg_gamma(characteristics_json),
        "avg_radius_described_sphere": get_avg_sphr_radius(characteristics_json),
        "avg_volume_described_sphere": get_avg_sphr_volume(characteristics_json),
    }

    return statistics
