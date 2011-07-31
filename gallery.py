import sys, os.path, os, shutil, subprocess, glob 

MY_GALLERY='C:/tools/php-photo-gallery' # replace with your dir

script_name = sys.argv[0]
verbose=True

if len(sys.argv) < 2:
    print "Usage: py %s <source_dir> [<dest_dir>]" % script_name
    print "Example: py gallery.py C:/tmp/iphone-photos/1"
    sys.exit(1)

src_dir = sys.argv[1]

dest_dir = "c:/temp/gal"
if len(sys.argv) >= 3: dest_dir = sys.argv[2]

if not os.path.exists(src_dir):
    print "source dir '%s' NOT exists" % src_dir
    sys.exit(2)

if os.path.exists(dest_dir):
    print "destination dir '%s' exists, re/move it first" % dest_dir
    sys.exit(3)

os.makedirs(dest_dir+'/img/th')

for src_file in os.listdir(src_dir):
    if(verbose) print "src_file",src_file
    lowercase_src_file = src_file.lower()
    if not os.path.isdir(os.path.join(src_dir,src_file)) and (lowercase_src_file.endswith('.jpg') or lowercase_src_file.endswith('.jpeg')):
        resz_file = '_'.join(src_file.split())
        if(verbose) print "resz_file",resz_file
        args=[MY_GALLERY+'/bin/convert.exe',os.path.join(src_dir,src_file),'-resize', '1024x768', dest_dir+'/img/'+resz_file] #resize img
        subprocess.call(args)
        args=[MY_GALLERY+'/bin/convert.exe',os.path.join(src_dir,src_file),'-resize', '240x160', dest_dir+'/img/th/'+resz_file] #create thumbnail 
        subprocess.call(args)

for fname in glob.iglob(MY_GALLERY+'/site/*.*'):
    shutil.copy(fname, dest_dir)

print 'gallery created: %s' % (dest_dir)

