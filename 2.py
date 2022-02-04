from PyScripts.geocoder import *
from PyScripts.PG_maps import *


def main():
    address = input()
    lat, lon = get_coordinates(address)

    ll_spn = f'll={lat},{lon}&spn=0.005,0.005'
    show_map(ll_spn)

    ll, spn = get_ll_span(address)
    ll_spn = f'll={lat},{lon}&spn={spn}'
    show_map(ll_spn)

    point_param = f'pt={ll}&pm2rd1'
    show_map(ll_spn, add_params=point_param)


if __name__ == '__main__':
    main()
