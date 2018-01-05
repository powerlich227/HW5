from ctypes import *
import math
import random

def zerolistmaker(n):
    listofzeros = [0] * n
    return listofzeros
    
def diffusion(spec_prob, theta_in, phi_in):
  r1 = random.random()

  if (r1 <= spec_prob):
    theta_out = theta_in
    phi_out = phi_in + math.pi

    if (phi_out >= 2.*math.pi): 
      phi_out = phi_out - 2.*math.pi
      return theta_out, phi_out
  else:
    r2 = random.random()
    theta_out = math.acos(1.-2.*r2)/2.
    r3 = random.random()
    phi_out = 2.*math.pi*r3
    return theta_out, phi_out

rand_num=1000000
step_theta=5
step_phi=20
theta_bin=(90/step_theta)
phi_bin=(360/step_phi)


spec_prob = 0.1
theta_out = 0.
phi_out = 0.

theta_out00 = zerolistmaker(theta_bin)
theta_out30 = zerolistmaker(theta_bin)
theta_out60 = zerolistmaker(theta_bin)
phi_out45 = zerolistmaker(theta_bin)


for i in range (0,rand_num):

    phi_in = 0. 
    theta_in = 0.
    theta_out, phi_out = diffusion(spec_prob, theta_in, phi_in)
    itheta = int(theta_out*180./math.pi/step_theta)
    if (itheta < theta_bin): 
	    theta_out00[itheta] = theta_out00[itheta] + 1

    theta_in = 30.*math.pi/180.
    theta_out, phi_out = diffusion(spec_prob, theta_in, phi_in)
    itheta = int(theta_out*180./math.pi/step_theta)
    if (itheta < theta_bin):
        theta_out30[itheta] = theta_out30[itheta] + 1

    theta_in = 60.*math.pi/180.
    theta_out, phi_out = diffusion(spec_prob, theta_in, phi_in)
    itheta = int(theta_out*180./math.pi/step_theta)
    if (itheta < theta_bin):
        theta_out60[itheta] = theta_out60[itheta] + 1

    theta_in = 45.*math.pi/180.
    phi_in = math.pi
    theta_out, phi_out = diffusion(spec_prob,theta_in,phi_in)
    iphi = int(phi_out*180./math.pi/step_phi)
    if (iphi < phi_bin):
        phi_out45[iphi] = phi_out45[iphi] + 1

f = open("hmwk5p_problem1a.dat",'w')

for i in range(0,theta_bin):
	f.write(str(i*step_theta) + " " + str(float(theta_out00[i])/rand_num) + " " + str(float(theta_out30[i])/rand_num) + " " + str(float(theta_out60[i])/rand_num))
	f.write("\n")
f.close

g = open("hmwk5p_problem1b.dat",'w')

for i in range(0,phi_bin):
	g.write(str(i*step_phi) + " " + str(float(phi_out45[i])/rand_num))
	g.write("\n")
g.close

