# Source for Linux Adventure, a text-based adventure designed to introduce the
# command line. Uses the MIT open-source license.
#
# The MIT License (MIT)
#
# Copyright (c) 2015 Rebekah Aimee Yoder
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

def prompt(proper):
    # proper is the command that's supposed to be entered
    cmd = raw_input("$ ")
    if cmd != proper: #validation
        typo_error(proper) #error message
        prompt(proper) #recursion rocks :)

def typo_error(proper):
    print '''
Make sure you enter "%s" exactly into the prompt!
The command line can be picky about spelling and capitalization.
Don't include the quotation marks!
    ''' % proper

print '-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~'
print '''
Welcome to Linux Adventure! This is a text-based adventure game designed to
introduce the Linux command line to new users. In LA, you\'ll use real Linux
commands to explore your environment and help your character. Type in the
commands and press enter to advance the story. Have fun!
'''

# Teaches whoami
print '"Ugh, where am I? Wait, WHO am I?"'
print'''
Type "whoami" to remember your name. In Linux, this prints your username.
The $ is a prompt. It lets you know the system is ready to take commands.
'''
prompt("whoami")

# Teaches pwd
print '''
Your name is SPRUCE.

You should try to take a look around with "pwd". In Linux, this shows you the
name of the directory you're in. "Directory" is just another word for "folder".
'''
prompt("pwd")

# Teaches ls
print '''
It is very dark. You can't see. You're sitting on a rocky-feeling piece of
ground, and as you don't hear anything (for now) it seems you're in no
immediate danger. You could search the floor and see if there are any objects
lying around nearby.

Use ls to search the floor. In Linux, ls tells you what's in your current
directory.
'''
prompt("ls")

# Teaches touch
print '''
You grope around and find materials for a TORCH.

You should try to make a torch with your new materials. You can use the command
"touch torch" to make your torch. In Linux, the "touch" command and a name make
a file. So, "touch alligators.txt" would make a file named "alligators.txt".
'''
prompt("touch torch")

# Reinforces pwd (it's an important command!)
print '''
You make and light your TORCH. 

Try looking around again. Remember, the command is "pwd".
'''
prompt("pwd")

# Teaches cd
print '''
It looks like you're in a cave. Behind you is a dead end. In front of you is a
passageway into another section of cave.

You can go explore that passageway with "cd passageway". In Linux, "cd" means
"change directory", and it lets you move around in the directory structure.
If you want to go up a level in the directory structure, use "cd ..".
'''
prompt("cd passageway")

# Exposition and teaches cp
print '''
You cross through the passageway into the next section of the cave. In this
section, you find a girl. You recognize her. Her name is MINT. You ask what's
going on. She says that both of you are trapped in this CAVE, which is actually
a LABYRINTH OF PROPRIETARY SYSTEMS. It is controlled by Microsoft and the only
way to open the exit is to destroy the CURSED COPY OF WINDOWS hidden in the
center of the labyrinth.
But the copy is not unprotected. It can only be destroyed with the SUDO WAND,
a magical device from the LAND OF LINUX with great and dangerous powers.
You ask where to find it, but MINT does not know where the SUDO WAND is! You
decide to search for the wand together. But first you should give MINT a torch.

To use your materials to make another torch, you should "cp torch mints-torch".
This makes a copy of your torch and names it "mints-torch". You can do the same
thing to files and directories in Linux. Also note that with the command line,
it's usually easiest not to put spaces in file or directory names.
Google "escaping spaces in command line" if you're curious why.
Enough talk! It's time to "cp torch mints-torch"!
'''
prompt("cp torch mints-torch")

# Teaches grep
print '''
You copy the steps you used to make your TORCH and hand MINT the extra.

Next, you should start searching the LABYRINTH for that SUDO WAND. The grep
command will help you search within a file in Linux. But in this case, you can
also "grep labyrinth sudo-wand"!
'''
prompt("grep labyrinth sudo-wand")

# Teach mv, as in move locations
print '''
Together, you and MINT search for the SUDO WAND. You stumble upon a MICROSERF.
He is sitting in front of a crevice in the cave wall and looks up at you,
scowling. You think you see the SUDO WAND in the crevice he is hiding.
He demands to know what you're carrying. When you explain that you and MINT
are carrying TORCHES, he begins to shriek. Torches, he shouts, are an
abomination, as they represent the CURSED LIGHT OF LINUX.

You should probably move the torches out of this guy's sight. In Linux, you can
move files by typing "mv [filename] [directoryname]". Right now, you should
probably "mv torch behind-back" before this dude blasts out your eardrums.
'''
prompt("mv torch behind-back")

# Teach mv, as in rename
print '''
You and MINT hide the torches behind your backs. The MICROSERF is not fooled,
and continues to yell at you.

Maybe you should call the torches something else. You can also use mv to rename
files. If you type "mv alligators.txt swamp" and there's no directory in your
current directory that's called swamp, mv will rename your alligators.txt file
to "swamp" for you. Right now, you need a creative name for the TORCH.
Hmm... try "mv torch light-apparatus" and see where that gets you.
'''
prompt("mv torch light-apparatus")

# Teach cat
print '''
You quickly explain that you were mistaken. These are not TORCHES after all;
they are LIGHT APPARATUSES. The MICROSERF quietens down. Apparently this makes
them overcomplicated enough to satisfy him that they're from his own company.
MINT asks for the SUDO WAND the MICROSERF is guarding. He explains that he must
not give the SUDO WAND to anyone who has not read and agreed to the lengthy
TERMS AND CONDITIONS he has been issued with.

Looks like you're going to have to read those T&Cs. The "cat" command prints
a file's contents to your command line screen. You should "cat terms".
'''
prompt("cat terms")

# Teach less
print '''
You take the TERMS AND CONDITIONS. They are very long! You can't possibly read
all of this in one sitting.

The cat command works well for small files, but not stuff that's this long!
Fortunately, there's another command that lets you page through files a bit at
a time: the "less" command. It lets you see less of a file at once, get it?
You can type "less terms" to read them more efficiently.
'''
prompt("less terms")

# Teach man
print '''
This product is provided without warranty or guarantees of any kind.

By acceptance of these TERMS AND CONDITIONS and use of the product to which
they apply, you agree to conditions including but not limited to the following:
a) you must give up your firstborn son,
b) you forfeit your soul to Bill Gates,
c) you forfeit every conscious thought and movement to Microsoft,
---
It's really long, so you just skip to the end by pressing spacebar a lot (which
turns the page when you're using the "less" command) and then say you agree.
You get the SUDO WAND!
Once you leave the MICROSERF behind, MINT informs you of a MANUAL you can read
about the SUDO WAND.

You should probably try to read that manual. All Linux commands come with a man
page, short for "manual page". You can read them by typing "man [command name]"
and then paging through the manual with spacebar or pressing q to quit.
Read the manual for the SUDO WAND by typing "man sudo-wand".
'''
prompt("man sudo-wand")

# Teach rm and sudo
print '''
The MANUAL looks kind of complicated, but MINT has read it. She explains that
the SUDO WAND lets you do things that you wouldn't normally have permission to
do. She warns you that the wand is dangerous and should be used carefully, then
shows you how it works.
She then indicates that according to her compass, the CURSED COPY OF WINDOWS is
probably to the SOUTH and you should travel in that direction. You get an idea.

The command "rm" removes a file. Or walls. That's probably against some rule
somewhere, but whatever.
The command "sudo" gives you super-user permissions. Any command prefaced by
"sudo" is like telling the computer, "I don't care about your precautions or
security--execute this command anyway!" There are good reasons to use it and
some commands require it (for instance, to install things), but it's very
dangerous. If someone on the Internet tells you to use it, make sure they're
not trying to trick you into hurting your computer before you do what they say!
The sudo command usually prompts you for a password before you're allowed to
use it successfully, but we'll make an exception.
Type "sudo rm barriers" to clear your path. You're sick of this labyrinth!
'''
prompt("sudo rm barriers")

# Reinforce cd
print '''
Naturally, after all of MINT's warnings, the first thing you do with the SUDO
WAND is blast a giant hole through most of the cave system, in the direction
MINT indicated as your destination. Miraculously, the cave does not collapse,
and your path is clear, but MINT gives you a heartfelt slap across the face
for your maverick performance. Then she starts down the tunnel you just made.

Use the command "cd tunnel" to follow MINT. Remember, cd lets you change
directories and move around.
'''
prompt("cd tunnel")

# sudo and rm again for plot's sake
print '''
You've found it: the CURSED COPY OF WINDOWS that seals this labyrinth. Now you
must destroy it with the SUDO WAND. Mint looks nervous beside you, shuddering
in the presence of such great evil.

You should destroy the cursed disk with "sudo rm cursed-windows".
'''
prompt("sudo rm cursed-windows")

# mv again
print '''
You obliterate the CURSED COPY OF WINDOWS with the SUDO WAND. A great and
beautiful light shines down upon you as the ceiling of the cave opens above.
Suddenly, however, a LAWYER stops you and demands to know what you've done.
Clearly an unnecessary question, as he immediately registers a COMPLAINT
against your clear and obvious VIOLATION of the TERMS AND CONDITIONS you agreed
to when you were given the SUDO WAND: you have altered a copy of Windows!
Writing quickly, he soon hands you a long and impressive-looking sheet of paper
citing the clauses you've violated. What will you do with the complaint?

Try "mv complaint jupiter".
'''
prompt("mv complaint jupiter")

# I considered using /dev/null instead, but thought it might be too obscure.

# Teach exit
print '''
You have successfully sent the LAWYER's complaint to JUPITER. Congratulations.
He looks completely baffled, wondering what you've just done--which is no
surprise, since he probably runs Windows, and Windows's version of a command
line is PowerShell, which is terrible.

The LAWYER is confused enough for you to escape! Type "exit" to leave the
LABYRINTH. Or leave your terminal session, as the case may be.
'''
prompt("exit")

print '''
You and MINT climb through the ceiling exit. You stretch out on the grass,
enjoying the sight of daylight.
"Well done, young coders!" says a voice you don't recognize. You sit up and see
a mustachioed man in an Obi-Wan Kenobi costume. Next to him is another man, who
is eating Chinese food with two sets of chopsticks in one hand.
"Eric S. Raymond!" Mint exclaims. "And Richard Stallman!"
"Congratulations on getting out of there," Stallman says. "It takes a creative
spirit to manage that. Not a lot of people figure it out."
"What do we do now?" you ask.

(Hit Enter to continue.)
'''
prompt("")

print '''
ESR shrugs. "That's up to you. You're in a world full of interesting problems
that you now have the freedom to solve. If you have the right mindset, they'll
come to you. Or you can help other people solve problems they've found. Open
source is a big world."
"There are even free-software games," RMS says. "In fact, I have a hunch that
the last game you finished playing was free software. You should try changing
its source code so you can make the story go different ways. Then you can share
your changes with other people."

(Hit Enter to continue.)
'''
prompt("")

print '''
"You speak the TRUE WAY OF LINUX, RMS," says ESR.
"GNU/Linux, you mean," Stallman corrects.
"Anyway, congratulations again," ESR says, changing the subject. "It's time for
you to go make something cool with your new knowledge. Happy hacking!"

Congratulations! You won!
(Hit Enter again.)
'''
prompt("")

print '''
You can indeed change this game's source code. You can open its file by typing
"gedit linux-adventure.py" or "nano linux-adventure.py" (gedit and nano are
code editors), and after you've saved your changes, you can run the program
again with "python linux-adventure.py" (unless of course you change the name).

Have fun!
'''
