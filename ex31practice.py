def decision_counter(decisions):
	decisions += 1
	return decisions


print """Before you lies the Crypt of Khar-Hezdron. Years of seaching have led you to this
moment. Future historians will point to this moment as the instance in which the most
important lost civilization was re-discovered, and it will be your name that goes in all
the history books. Speaking of..."""
name = raw_input("What IS your name? ")

print """Well %s, time to get started. The door to the crypt lies sealed in front of you.
Thankfully your research has uncovered the incantations to unlock it. What do you 
do?""" % name
print "1. Recite the unlocking incantation."
print "2. Turn back and find a braver soul to enter first."
firstDecision = raw_input("> ")

if firstDecision == "1":
	print """\tThe words seems to slither heavily off your tongue and you feel a naseous 
	feeling creep over you as you recite the words, chanting faster and faster. Finally
	after what seems an age but what the moon tells you has only been minutes the stone
	of the door lets out a deep grinding reverberation and slides to one side."""
	decision_counter(1)
elif firstDecision == "2":
	print """\tTypical of your bookish nature, you decide to enlist the aid of a professional
	when it comes to raiding tombs. As you brush the dust fussily from your coat and turn
	to leave, you find a man standing behind you. As you start to stammer out a challenge,
	he cuts your throat in a business-like manner. You fall to the ground and feel the
	life seeping out of your body. Right before you shuffle off this mortal coil the 
	stranger whispers "And thus the secret of the tomb dies with you. May it rest
	undisturbed for another thousand years.\" """
	decision_counter(1)
else:
	print """\tThat's not really an option. You're not too great at deciding things, are 
	you? Go ahead and give this another shot when you can take things seriously. %s, 
	honestly...""" % firstDecision
