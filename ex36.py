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
	while True:
		choice = raw_input("Leave or enter? ")
	
		if choice == "enter":
			print """The words of the opening incantation seem to slither heavily off your 
tongue and you feel a naseous feeling creep over you as you recite the words, 
chanting faster and faster. Finally after what seems an age but what the moon 
tells you has only been minutes the stone of the door lets out a deep grinding 
reverberation and slides to one side."""
			#end_room()
			room_one()
		elif choice == "leave":
			dead("""Typical of your bookish nature, you decide to enlist the aid of a 
professional when it comes to raiding tombs. As you brush the dust fussily from 
your coat and turn to leave, you find a man standing behind you. As you start to 
stammer out a challenge, he cuts your throat in a business-like manner. You fall
to the ground and feel the life seeping out of your body. Right before you shuffle 
off this mortal coil the stranger whispers "And thus the secret of the tomb dies 
with you. May it rest undisturbed for another thousand years.\" """)
		elif choice == "exit":
			dead("See you soon!")
		else:
			print """That's not really an option. You're not too great at deciding things,
are you?"""
			#exit(0)
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
	elif choice == "left":
		room_three()
	elif choice == "exit":
			dead("See you soon!")
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
		elif choice == "look around":
			room_two()
		elif choice == "exit":
			dead("See you soon!")
		else:
			print "That's not really an option."
#second room end		
		
#third room start	
def room_three():		
	print """You enter a room with naturally formed ceilings, almost more a cave than part
of a tomb. You posit that the original tomb builders must have originally chosen a site
with naturally occuring features and simply added rooms onto them...fascinating! You are
so caught up in your musings that you don't notice the dust starting to pile on the
shoulder of your coat until a small rock plunks painfully off the top of your hear. 
Directing your torch upwards shows a ceiling spiderwebbed with cracks, small rocks and
bits of dirt streaming down. With a roar, the ceiling start to collapse!"""
	while True:
		choice = raw_input("What do you do?! ")
		
		if choice == "run":
			print """Before you can make a decision, your feet (seemingly of their own 
accord) start to propel you through the rocks starting to fall from the ceiling. You
manage to avoid boulders twice the size of a man to fling yourself through the doorway
at the other side of the room. Battered and bruised, but still alive, you start 
walking."""
			room_four()
			#exit(0)
		elif choice == "exit":
			dead("See you soon!")
		else:
			dead("""Your lack of decisiveness costs you dearly, and you feel the weight of
several tons of rock pressing down on your for a split second...then you feel nothing at
all""")
#third room end
		
#fourth room start
def room_four():
	print """Brushing dust from yourself, you enter into a room lined with small recesses
along the walls. Upon further inspection, they seem to be burial chambers. Of them, only
one seems to be occupied, its dessicated charge staring up at the ceiling with eyes
sockets long emptied, covered in shreds and tatters. At the opposite end of the room there
is a door. Knocking reveals that it is made of sturdy copper, covered in a patina of 
verdegris, which leaves a slight green stain on your hand. There seems to be some sort of
writing scratched into a small opening in the center of the door, which is covered in 
something that render it illegible."""
	legible = False
	unlocked = False
	key = False
	while True:
		choice = raw_input("What do you do? ")
		
		if choice == "clean the door" and not legible:
			print """You pull the sleeve of your coat over your hard and set to scrubbing
the inscription on the door. After several minutes of scraping at it, you manage to 
uncover something that is mostly legible. Consulting your notes, you translate it to "The
ancient king holds the power, all will bow before him."""
			legible = True
		elif choice == "open door" and not unlocked:
			print """You try to open the door, but the edges are set into the stone of the
lintel, and it won't budge."""
		elif choice == "read writing" and not legible:
			print """You attempt to decipher the writing on the door, but the covering of
grime on the door is too thick. In tracing the symbols to try and translate them, your
finger tips brush off a little of the covering, revealing a single letter of the
message."""
		elif choice == "read writing" and legible:
			print """You re-examine the writing on the door and check your translation.
You are now positive it reads "The ancient king holds the power, all will bow before
him."""
		elif choice == "search body" and not key:
			print """You decide to search the only other occupant of the room, the corpse
in the hollow of the wall. You pause for a moment, feeling slightly ill at the grisliness
of the task, but you plunge your hand into the bier. After feeling around the skeletal
remains for a moment, your fingers touch something rather cool and seemingly more solid
than the bones surrounding it. Drawing your hand back, you find yourself clutching a
copper key."""
			key = True
		elif choice == "search body" and key:
			print """Having already obtained the key, you can't imagine ever wanting to 
stick your hand back in there. You give a shudder at the mere thought of it."""
		elif choice == "use key" and (key and not unlocked):
			print """Having found the key, you return to the door. You slot it into the 
opening in the middle of the door and struggle to turn it first to the right, then the
left. After becomind slightly winded, you hear a slight 'click' and then hear a ticking 
like the meshing of several gears. With a ping and a scrape, the door slides into the wall
to the side and you continue through the doorway."""
			unlocked = True
			room_six()
			#exit(0)
		elif choice == "look around":
			room_four()
		elif choice == "exit":
			dead("See you soon!")
		else:
			print "That's not really an option. You'll have to try something else."
#fourth room end
			
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
			room_six()
			#exit(0)
		elif choice == "look around":
			room_five()
		elif choice == "exit":
			dead("See you soon!")
		else:
			print "That's not really an option."
#fifth room end
	
#sixth room start
def room_six():
	print """Taking a step through the doorway, you find yourself in a vast, soaring 
space. It looks to be a temple of some sort. Consulting your notes, you start to get
excited. This must be the famed Cathedral of Elios! Texts have long posited that this
site and the crypt were separate locations...you can't wait until those stuffed shirts at
the University see this with their own eyes. However, you digress. Around you are high
ceilings with curiously twisting stonework on the columns leading down to the ground. 
Before you stretches a long series of steps leading up to an altar. You start to walk up
the steps and look at the altar."""
	rune_1 = False
	rune_2 = False
	rune_3 = False
	rune_4 = False
	rune_5 = False
	rune_6 = False
	while True:
		choice = raw_input("What do you do? ")
		
		if choice == "examine altar":
			print """You take a closer look at the block of sandstone before you. The 
porous stone has been stained a deep ocher which you struggle not to investigate too 
deeply. The surface has six runes etched into the surface. You start tracing your
fingers over them. You should consult your journal in order to find which ones are 
correct"""
		elif choice == "consult journal":
			print """The symbols seem familiar. You find a section in your notes detailing
the proper sequence you should press. It seems to be a riddle..."The first rune is the 
number of rooms that led to this point. The second is double that. The third it that
doubled again, multiplied by seven, and divided by two. Press these, the press the 
altar and the path will be revealed.\" """
		elif choice == "translate runes":
			print """The runes translate into numbers! They are as follows:
144
3
27
6
42
18"""
		elif choice == "press 144":
			print """The rune makes a scraping noise and sinks into the recesses of the 
altar."""
			rune_1 = True
		elif choice == "press 3":
			print """The rune makes a scraping noise and sinks into the recesses of the 
altar."""
			rune_2 = True
		elif choice == "press 27":
			print """The rune makes a scraping noise and sinks into the recesses of the 
altar."""
			rune_3 = True
		elif choice == "press 6":
			print """The rune makes a scraping noise and sinks into the recesses of the 
altar."""
			rune_4 = True
		elif choice == "press 42":
			print """The rune makes a scraping noise and sinks into the recesses of the 
altar."""
			rune_5 = True
		elif choice == "press 18":
			print """The rune makes a scraping noise and sinks into the recesses of the 
altar."""
			rune_6 = True
		elif choice == "press altar" and (rune_2 and (rune_4 and rune_5)):
			print """With a scraping thud, the altar moves forward a couple paces and 
sinks into the floor. Once flush with the floor, a section of the wall slides aside. You
walk through."""
			end_room()
			#exit(0)
		elif choice == "press altar" and not rune_2 or not (rune_4 or not rune_5):
			dead("""You hear a clunk from the altar, but nothing appears to happen. After
a moment of confusion, you hear a whistling and feel a sting on your neck. Reaching your
hand up, you pull a dart out of your neck. Your vision rapidly starts to blur and the 
strength leaves your body within seconds. You wind up slumped over the altar, which is
perhaps where the next intrepid explored will find you centuries hence""")
		elif choice == "look around":
			room_six()
		elif choice == "exit":
			dead("See you soon!")
		else:
			print "That's not really an option."
#sixth room end

#end room start
def end_room():
	print """At last, the final burial chamber! You've cemented your place in the history
books. You look around you at the vast riches that have lain dormant for centuries. Who
would have thought that you, would have been the one to uncover such untold wealth
and acclaim? Well, you would have, but no one else! You take a moment to collect yourself,
then start documenting the tomb and all that it contains."""
	while True:
		choice = raw_input("Play again or exit? ")
		
		if choice == "play again":
			start()
		elif choice == "exit":
			dead("See you soon!")
		else:
			print "You've come this far and you can't make a decision?!"
#end room end

		
def dead(why):
	print (why)
	exit(0)
	
start()

	
	
