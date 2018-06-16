### REDSHIFT CALCULATOR

def energy_obs (en_rf,z):
	en_obs = en_rf/(1+z)
	return en_obs

def energy_rf (en_obs,z):
	en_rf = en_obs*(1+z)
	return en_rf

def lambda_obs (l_rf,z):
	l_obs = l_rf*(1+z)
	return l_obs

def lambda_rf (l_obs,z):
	l_rf = l_obs/(1+z)
	return l_rf

def z_en (en_obs,en_rf):
	z = en_rf/en_obs - 1
	return z

def z_l (l_obs,l_rf):
	z = l_obs/l_rf -1
	return z

tmp = True

while (tmp == True):
	choice1 = input("What do you want to calculate? [z, obs, rf] ")
	choice2 = input("Energy[keV] or wavelength[A]? [E, w] ")

	if choice2 == 'E':
		if choice1 == 'z':
			telme1 = float(input("Tell me observed energy [keV]: "))
			telme2 = float(input("Tell me rest frame energy [keV]: "))
			z = z_en(telme1,telme2)
			print (z)
			temp = input ("Retry? [y/n]")
			if temp != 'y':
				tmp = False
		elif choice1 == 'obs':
			telme1 = float(input("Tell me rest frame energy [keV]: "))
			telme2 = float(input("Tell me z: "))
			en_obs = energy_obs(telme1,telme2)
			print (en_obs)
			temp = input ("Retry? [y/n]")
			if temp != 'y':
				tmp = False
		elif choice1 == 'rf':
			telme1 = float(input("Tell me observed energy [keV]: "))
			telme2 = float(input("Tell me z: "))
			en_rf = energy_rf(telme1,telme2)
			print (en_rf)
			temp = input ("Retry? [y/n]")
			if temp != 'y':
				tmp = False
		else:
			print ("Wrong choice. ")
			temp = input ("Retry? [y/n]")
			if temp != 'y':
				tmp = False

	elif choice2 == 'w':
		if choice1 == 'z':
			telme1 = float(input("Tell me observed wavelength [A]: "))
			telme2 = float(input("Tell me rest frame wavelength [A]: "))
			z = z_l(telme1,telme2)
			print (z)
			temp = input ("Retry? [y/n]")
			if temp != 'y':
				tmp = False
		elif choice1 == 'obs':
			telme1 = float(input("Tell me rest frame wavelength [A]: "))
			telme2 = float(input("Tell me z: "))
			l_obs = lambda_obs(telme1,telme2)
			print (l_obs)
			temp = input ("Retry? [y/n]")
			if temp != 'y':
				tmp = False
		elif choice1 == 'rf':
			telme1 = float(input("Tell me observed wavelength [A]: "))
			telme2 = float(input("Tell me z: "))
			l_rf = lambda_rf(telme1,telme2)
			print (l_rf)
			temp = input ("Retry? [y/n]")
			if temp != 'y':
				tmp = False
		else:
			print ("Wrong choice. ")
			temp = input ("Retry? [y/n]")
			if temp != 'y':
				tmp = False

	else:
		print ("Wrong choice. ")
		temp = input ("Retry? [y/n]")
		if temp != 'y':
			tmp = False
