import re
import glob,os.path
import shutil

from colorama import init, Fore, Back, Style 
highgreen = Fore.RESET + Style.BRIGHT + Fore.GREEN
highmagenta = Fore.RESET + Style.BRIGHT + Fore.MAGENTA
highred = Fore.RESET + Style.BRIGHT + Fore.RED
grey = Fore.RESET+Fore.BLACK+Style.BRIGHT
green = Fore.RESET + Fore.GREEN + Style.NORMAL
magenta = Fore.RESET + Fore.MAGENTA + Style.NORMAL
cyan = Fore.RESET + Fore.CYAN
red = Fore.RESET + Fore.RED
blue = Fore.RESET + Fore.BLUE
yellow = Fore.RESET + Fore.YELLOW
reset = Fore.RESET

music_root="/media/target_directory"
music_unsorted="/media/unsorted_ungodly_mess_of_fucking_downloads"
dupe_dir="/media/where_you_want_dupes_to_go"

music_categories={
  "genre": {
    "b": music_root+"/blaxploitation",
    "c": music_root+"/chill",
    "d": music_root+"/dubstep",
    "f": music_root+"/flac",
    "h": music_root+"/hiphop",
    "j": music_root+"/jungle",
    "o": music_root+"/OST",
    "s": music_root+"/singles",
    "t": music_root+"/techno",
    "mi": music_root+"/misc",
    "du": music_root+"/dupes",
    "co": music_root+"/comedy",
    "ro": music_root+"/rock",
    "ul": music_root+"/ultrachill",
    "wo": music_root+"/world",
    "va": music_root+"/va",
    "me": music_root+"/metal",
    "ma": music_root+"/mashups",
    "crap": "/media/3teeb/PROJECT_SORT/crap"
  },
}

#print("%scustomer_name = cakemarketing" %(green), file=stream)

def target_genre_input(sortname):
    print "%s[%sb%s]%slaxploitation, %s[%sc%s]%shill, %s[%sd%s]%substep, %s[%sf%s]%slac, %s[%sh%s]%siphop, %s[%sj%s]%sungle, %s[%so%s]%sst, %s[%ss%s]%singles, %s[%st%s]%sechno%s" % (cyan, highmagenta, cyan, highmagenta,cyan, highmagenta, cyan, highmagenta,cyan, highmagenta, cyan, highmagenta,cyan, highmagenta, cyan, highmagenta,cyan, highmagenta, cyan, highmagenta,cyan, highmagenta, cyan, highmagenta,cyan, highmagenta, cyan, highmagenta,cyan, highmagenta, cyan, highmagenta,cyan, highmagenta, cyan, highmagenta, reset )
    print "%s[%smi%s]%ssc, %s[%sdu%s]%spes, %s[%sco%s]%smedy, %s[%sro%s]%sck, %s[%sul%s]%strachill, %s[%swo%s]%srld, %s[%sva%s]%s, %s[%sme%s]%stal, %s[%sma%s]%sshups %s[%scr%s]%sap%s" % (cyan, highmagenta, cyan, highmagenta,cyan, highmagenta, cyan, highmagenta,cyan, highmagenta, cyan, highmagenta,cyan, highmagenta, cyan, highmagenta,cyan, highmagenta, cyan, highmagenta,cyan, highmagenta, cyan, highmagenta,cyan, highmagenta, cyan, highmagenta,cyan, highmagenta, cyan, highmagenta,cyan, highmagenta, cyan, highmagenta,cyan, highmagenta, cyan, highmagenta,reset)
    print "%sWhat genre is %s%s" % (green, highgreen, sortname)
    target_genre = str(raw_input('genre: '))
    if target_genre == "skip":
        return "poop", "poop"
    if target_genre == "delete":
        return "delete", "delete"
    else:        
        if not music_categories.get("genre").get(target_genre):
            return "genre not found", None        
        else:
            target_dir = music_categories.get("genre").get(target_genre)
            returned_input = target_genre
            return target_genre, target_dir

def delete_filez(source_dir):
    try:
        print "deleting %s" % (source_dir) 
        shutil.rmtree(source_dir)
    except shutil.Error:
        print "Error, Deleting"

def move_filez(source_dir, target_dir):
    try:
        shutil.move(source_dir, target_dir)
    except shutil.Error:
        print "Error, dupe: moving to dupes."
        shutil.move(source_dir, dupe_dir)

filesDepth1 = glob.glob(music_unsorted+"/*")
dirsDepth1 = filter(lambda f: os.path.isdir(f), filesDepth1)
for musicdir in dirsDepth1:
    if "poop" in musicdir: continue
    sortname=musicdir.replace(music_unsorted+"/", "")
    album_letter = sortname[:1].lower()
    target_genre,target_dir = target_genre_input(sortname)
    if target_genre == "delete":
        #print "would have deleted %s" % (musicdir)
        delete_filez(musicdir)
        continue
    if target_genre == None:
        pass
    if target_genre == "poop":
        print "skipped"
        continue
    if not target_dir:
        print "%sgenre not found" % (highred)
        quit(0)    
    if target_genre == "h":
        if not re.match(r"[a-zA-Z]", album_letter):
        #print "non letter"
            album_letter = str(raw_input('letter: '))
            source_dir = musicdir
            target_dir = music_root+"/hiphop/"+album_letter
            #print target_dir
            print "%s moving %s%s %sto %s%s" % (red, yellow, source_dir, red, yellow, target_dir)
            #shutil.move(source_dir, target_dir)
            move_filez(source_dir, target_dir)
        else:
            source_dir = musicdir
            target_dir = music_root+"/hiphop/"+album_letter
            #print target_dir
            print "%s moving %s%s %sto %s%s" % (red, yellow, source_dir, red, yellow, target_dir)
            #shutil.move(source_dir, target_dir)
            move_filez(source_dir, target_dir)
    else:
         source_dir = musicdir
         print "%s moving %s%s %sto %s%s" % (red, yellow, source_dir, red, yellow, target_dir)
         #shutil.move(source_dir, target_dir)
         move_filez(source_dir, target_dir)



    
