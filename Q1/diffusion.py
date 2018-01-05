import math
def diffusion(spec_prob, theta_in, phi_in):
	r1 = random.random()
	if (r1 <= spec_prob):
		theta_out = theta_in
		phi_out = phi_in + math.pi
		if (phi_out >= 2*math.pi): 
		    phi_out = phi_out - 2*math.pi
		return theta_out,phi_out
	else:
	r2 = random.random()
	theta_out = math.acos(1-2*r2)/2
	r3 = random.random()
  	phi_out = 2*math.pi*r3
  	return theta_out,phi_out
