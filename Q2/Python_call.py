from ctypes import *
import math

Diffusion_Libs = CDLL('./libhmwk5p2.so')

def zerolistmaker(n):
    listofzeros = [0] * n
    return listofzeros

rand_num=1000000
step_theta=5
step_phi=20
theta_bin=(90/step_theta)
phi_bin=(360/step_phi)


spec_prob = c_double(0.1)
theta_out = c_double(0.)
phi_out = c_double(0.)

theta_out00 = zerolistmaker(theta_bin)
theta_out30 = zerolistmaker(theta_bin)
theta_out60 = zerolistmaker(theta_bin)
phi_out45 = zerolistmaker(theta_bin)

#itheta = c_int(0)

for i in range (0,rand_num):

    phi_in = c_double(0.)   
    theta_in = c_double(0.)
    Diffusion_Libs.diffusion(spec_prob,theta_in,phi_in,byref(theta_out),byref(phi_out))
    itheta = int(theta_out.value*180./math.pi/step_theta)
    if (itheta < theta_bin): 
	theta_out00[itheta] = theta_out00[itheta] + 1

    theta_in = c_double(30.*math.pi/180.)
    Diffusion_Libs.diffusion(spec_prob,theta_in,phi_in,byref(theta_out),byref(phi_out))
    itheta = int(theta_out.value*180./math.pi /step_theta)
    if (itheta < theta_bin):
        theta_out30[itheta] = theta_out30[itheta] + 1

    theta_in = c_double(60.*math.pi/180.)
    Diffusion_Libs.diffusion(spec_prob,theta_in,phi_in,byref(theta_out),byref(phi_out))
    itheta = int(theta_out.value*180./math.pi/step_theta)
    if (itheta < theta_bin):
        theta_out60[itheta] = theta_out60[itheta] + 1

    theta_in = c_double(45.*math.pi/180.)
    phi_in = c_double(math.pi)
    Diffusion_Libs.diffusion(spec_prob,theta_in,phi_in,byref(theta_out),byref(phi_out))
    iphi = int(phi_out.value*180./math.pi/step_theta)
    if (iphi < phi_bin):
        phi_out45[iphi] = phi_out45[iphi] + 1

f = open("hmwk5_problem2a.dat",'w')

for i in range(0,theta_bin):
	f.write(str(i*step_theta) + " " + str(float(theta_out00[i])/rand_num) + " " + str(float(theta_out30[i])/rand_num) + " " + str(float(theta_out60[i])/rand_num))
	f.write("\n")
f.close

g = open("hmwk5_problem2b.dat",'w')

for i in range(0,phi_bin):
	g.write(str(i*step_phi) + " " + str(float(phi_out45[i])/rand_num))
	g.write("\n")
g.close

