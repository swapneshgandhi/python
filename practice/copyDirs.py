import shutil, os, sys, exceptions

__author__ = 'swaps_000'

def copyTree(src, dest,symlinks=False):
    names = os.listdir(src)

    ignored_names = set()

    os.makedirs(dest,exist_ok=True)
    errors = []
    for name in names:
        if (name in ignored_names):
            continue

        srcapth = os.path.join(src,name)
        dstapth = os.path.join(dest,name)

        try:
            if symlinks and os.path.islink(srcapth):
                linkto = os.readlink(srcapth)
                os.symlink(linkto, dstapth)

            elif os.path.isfile(srcapth):
                shutil.copy2(srcapth,dstapth)

            elif os.path.isdir(srcapth):
                copyTree(srcapth,dstapth,symlinks)
        except (IOError, os.error) as why:

            errors.append((srcapth, dstapth, str(why)))
        # catch the Error from the recursive copytree so that we can
        # continue with other files
        except Exception, err:
            errors.extend(err.args[0])

    try:
        shutil.copystat(src, dest)
    except WindowsError:
        # can't copy file access times on Windows
        pass
    except OSError as why:
        errors.extend((src, dest, str(why)))
    if errors:
        raise ValueError(errors)

