import os

def print_vin():
	return "1CVMN234VDFFFET"


def print_data():
        fd = os.open('ECUPIPE',os.O_RDONLY)
        data = os.read(fd,150)
        os.close(fd)
        return data
