#####################################################
# Thanks to xunity maintenance tool for this code   #
# We have edited slightly, original was checking    #
# for any thumbs older than 28 days. Changed to 14  #
# which should hopefully help AFTV devices.         #
#####################################################

import xbmc, os, xbmcaddon, re, datetime, glob, xbmc, xbmcgui
from sqlite3 import dbapi2 as sqlite3

path           = xbmc.translatePath('special://home/userdata/Database')
files          = glob.glob(os.path.join(path, 'Textures*.db'))
ver            = 0
dbPath         = ''

# Find the highest version number of textures, it's always been textures13.db but you can never be too careful!
for file in files:
	dbversion = int(re.compile('extures(.+?).db').findall(file)[0])
	if ver < dbversion:
		ver     = dbversion
		dbPath  = file

db   = xbmc.translatePath(dbPath)
conn = sqlite3.connect(db, timeout = 10, detect_types=sqlite3.PARSE_DECLTYPES, check_same_thread = False)
conn.row_factory = sqlite3.Row
c = conn.cursor()

# Set paramaters to check in db, cull = the datetime (we've set it to 14 days) and useCount is the amount of times the file has been accessed
cull     = datetime.datetime.today() - datetime.timedelta(days = 14)
useCount = 10

# Create an array to store paths for images and ids for database
ids    = []
images = []

c.execute("SELECT idtexture FROM sizes WHERE usecount < ? AND lastusetime < ?", (useCount, str(cull)))

for row in c:
	ids.append(row["idtexture"])

for id in ids:
	c.execute("SELECT cachedurl FROM texture WHERE id = ?", (id,))
	for row in c:
		images.append(row["cachedurl"])

print "### Community Portal Automatic Cache Removal: %d Old Textures removed" % len(images)

#clean up database
for id in ids:       
	c.execute("DELETE FROM sizes   WHERE idtexture = ?", (id,))
	c.execute("DELETE FROM texture WHERE id        = ?", (id,))

c.execute("VACUUM")
conn.commit()
c.close()

#delete files
thumbfolder = xbmc.translatePath('special://home/userdata/Thumbnails')
for image in images:
	path = os.path.join(thumbfolder, image)
	try:
		os.remove(path)
	except:
		pass
