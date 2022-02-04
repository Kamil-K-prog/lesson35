from PyScripts.geocoder import *
from PyScripts.PG_maps import *
from PyScripts.business import *
from PyScripts.distance import *
import sys


def main():
    address = ' '.join(sys.argv[1:])
    lat, lon = get_coordinates(address)
    ll= f'{lat},{lon}'
    spn = '0.005,0.005'

    ll_spn = f'll={lat},{lon}&spn=0.005,0.005'
    show_map(ll_spn)

    org = find_business(ll, spn,'аптека')
    point = org['geometry']['coordinates']
    org_lat = float(point[0])
    org_lon = float(point[1])
    point_par = f'{org_lat},{org_lon},pm2rd1'
    show_map(f'{ll_spn}', add_params=point_par)

if __name__ == '__main__':
    main()