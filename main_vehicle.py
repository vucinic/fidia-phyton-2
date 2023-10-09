from vehicle import Vehicle
from my_package.points import Point

if __name__ == '__main__':
    print('1)', Vehicle.get_vehicles_count())
    v = Vehicle()
    v.__x = "Az123Za"

    v = Vehicle()
    print(v._z)

    print(v.get_X())

    v.z = 100
    print(v.z)
    print(v.get_Z())



