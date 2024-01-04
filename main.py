from astropy.coordinates import SkyCoord
from astroquery.simbad import Simbad


def main():
    result_table = Simbad.query_object("IC492")
    print(result_table)


if __name__ == "__main__":
    main()
