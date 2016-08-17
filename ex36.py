from sys import exit

names = []


#entrance room start
def start():
	print """Before you lies the Crypt of Khar-Hezdron. Years of seaching have led you to 
this moment. Future historians will point to this moment as the instance in which the 
most important lost civilization was re-discovered, and it will be your name that goes
in all the history books. Speaking of..."""
	name = raw_input("What IS your name? ")
	
	for name in names:
		name.append(names)
	
	print """Well %s, time to get started. The door to the crypt lies sealed in front of 
you. Thankfully your research has uncovered the incantations to unlock it. What do you 
do?""" % name
	
	choice = raw_input("Leave or enter? ")
	
	if choice == "enter":
		print """The words of the opening incantation seem to slither heavily off your 
tongue and you feel a naseous feeling creep over you as you recite the words, 
chanting faster and faster. Finally after what seems an age but what the moon 
tells you has only been minutes the stone of the door lets out a deep grinding 
reverberation and slides to one side."""
		room_one()
		exit(0)
	elif choice == "leave":
		dead("""Typical of your bookish nature, you decide to enlist the aid of a 
professional when it comes to raiding tombs. As you brush the dust fussily from 
your coat and turn to leave, you find a man standing behind you. As you start to 
stammer out a challenge, he cuts your throat in a business-like manner. You fall
to the ground and feel the life seeping out of your body. Right before you shuffle 
off this mortal coil the stranger whispers "And thus the secret of the tomb dies 
with you. May it rest undisturbed for another thousand years.\" """)
	else:
		print """That's not really an option. You're not too great at deciding things, are
you?"""
		exit(0)
#entrance room end

#first room start
def room_one():
	print """You find yourself in the dim entry hall of the Crypt. Cobwebs and dust catch
the small bits of moonlight that filter through the open doorway. Hearing a scraping 
behind you, you turn to see the door sliding shut, sealing you in. Your fingers feel 
clumsy as you fumble for your torch and flick it to life. The weak light reveals two 
doorways stretching off. Which do you take?"""
	
	choice = raw_input("Right or left? ")
	
	if choice == "right":
		room_two()
		#exit(0)
	elif choice == "left":
		#room_three()
		exit(0)
	else:
		print """That's not really an option. You're not too great at deciding things, are
you?"""
		room_one()
#first room end

#second room start
def room_two():
	print """You step through the doorway, the light playing on the crumbling walls. You
take one step forward and suddenly your foot hovers over empty air. You fling yourself
back and narrowly avoid falling into what your torch reveals to be a pit of ancient but 
deadly looking spikes. The pit stretches about 10 feet in front of you. Looking around,
you find some old rotting boards next to you."""
	crossable = False
	while True:
		choice = raw_input("What do you do? ")
		
		if choice == "jump" and not crossable:
			dead("""You take a moment to back up and get a running start. Right before the 
edge of the pit, you leap into the air! You soar for a few feet...just not quite enough.
You meet your grisly end.""")
		elif choice == "jump" and crossable:
			dead("""You take a running leap and land square on the boards. Unfortunately,
the boards are rotted and give way, spilling you onto the spikes.""")
		elif choice == "use the boards" and not crossable:
			print """The boards, while rotting through, seem stable enough and you create a
narrow if servicable path over the spikes."""
			crossable = True
		elif choice == "use the boards" and crossable:
			print "Unfortunately, you're out of boards."
		elif choice == "walk across" and crossable:
			print """You start out over the boards. They creak alarmingly under you, but
beyond a few pulse pounding shifts, you manage to make it across unharmed. You pass
through the doorway into a long all with steps leading down."""
			room_five()
			#exit(0)
		else:
			print "That's not really an option."
#second room end		
		
	

#third room start	
#def room_three():		
		
#fourth room start
#def room_four():

#fifth room start
def room_five():
	print """You head down several flights of rough hewn stairs and pass through the
doorway at the end of the hallway. Upon exiting, you see a fey light that dimly 
illuminates the room around you. The chamber around you is expansive to the point where
the natural illumination does little to reaval its true dimensions to you. Before you
stretches a vast underground lake. Beneath its smooth surface, a pulsing light reveals 
itself to be the source of the rooms wan glow. In the distance, you can see the far shore
on the other side of the lake. The ground slopes down under your feet to gently meet with 
the surface of the water, and a bell stands on your side of the shore at the ends of a 
pole."""
	boat = False
	while True:
		choice = raw_input("What do you do? ")
		
		if choice == "swim" and not boat:
			dead("""The lake doesn't seem that deep, and after dipping a finger in the 
temperature seems warmer than you would expect. You decide to swim across. You are halfway
across when you feel something brush your leg. Before you can start to react, you are 
roughly yanked under the surface. No matter how much you thrash you cannot seem to break 
free of the embrace of whatever creature is pulling you under. As the air leaves your
lungs, you feel yourself black out, and the water rushes in.""")
		elif choice == "ring the bell" and not boat:
			print """You tug the leather thong attached to the clapper on the bell. A low
sound emanates from the bell, shaking you deep in your chest as it seems to reverberate 
from the surfaces of the room. Finally the peals die out after several minutes and a 
silence engulfs the room. You consider ringing the bell again, but before you can, a small
boat glides silently out of the darkness and beaches itself on the shore next to you."""
			boat = True
		elif choice == "ring the bell" and boat:
			print """Rather than the droning ring you'd previously heard, you hear just a
slight dull thud, and no sound rings out."""
		elif choice == "get in the boat" and boat:
			print """You clamber awkwardly into the boat, flopping to the bottom after
getting your ankles wet. As you pick yourself up and start to examine the boat for oars
or paddles, the boat slowly starts to glide across the lake under its own power. You look
over the side and realize the light is coming from bunches of crystals underneath the 
surface of the water, pulsing as if in time to the beating of an unseen heart. Disturbed
by the thought, you jump a little as the boat scrapes itself onto the far shore. You
disembark, dust yourself off, and walk through the doorway now revealed before you."""
		#room_6()
			exit(0)
		else:
			print "That's not really an option."
#fifth room end
	

#sixth room start
#def room_six():

#end room start
#def end_room():

		
def dead(why):
	print (why)
	exit(0)
	
start()

	
	
