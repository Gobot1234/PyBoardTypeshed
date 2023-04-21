"""
basic "operating system" services.

Descriptions taken from:
https://raw.githubusercontent.com/micropython/micropython/master/docs/library/os.rst.
==============================================

.. module:: os
   :synopsis: basic "operating system" services

|see_cpython_module| :mod:`python:os`.

The ``os`` module contains functions for filesystem access and mounting,
terminal redirection and duplication, and the ``uname`` and ``urandom``
functions.
"""

__author__ = "Howard C Lovatt"
__copyright__ = "Howard C Lovatt, 2020 onwards."
__license__ = "MIT https://opensource.org/licenses/MIT (as used by MicroPython)."
__version__ = "7.5.3"  # Version set by https://github.com/hlovatt/tag2ver

from typing import Literal, Protocol, overload, runtime_checkable

from uio import IOBase

from ._typeshed import AnyPath, FdOrAnyPath

def uname() -> tuple[str, str, str, str, str]:
    """
    Return a tuple (possibly a named tuple) containing information about the
    underlying machine and/or its operating system.  The tuple has five fields
    in the following order, each of them being a string:

         * ``sysname`` -- the name of the underlying system
         * ``nodename`` -- the network name (can be the same as ``sysname``)
         * ``release`` -- the version of the underlying system
         * ``version`` -- the MicroPython version and build date
         * ``machine`` -- an identifier for the underlying hardware (eg board, CPU)
    """

def urandom(n: int, /) -> bytes:
    """
    Return a bytes object with *n* random bytes. Whenever possible, it is
    generated by the hardware random number generator.
    """

def chdir(path: FdOrAnyPath, /) -> None:
    """
    Change current directory.
    """

def getcwd() -> str:
    """
    Get the current directory.
    """

@overload
def ilistdir() -> list[tuple[str, int, int] | tuple[str, int, int, int]]:
    """
    This function returns an iterator which then yields tuples corresponding to
    the entries in the directory that it is listing.  With no argument it lists the
    current directory, otherwise it lists the directory given by *dir*.

    The tuples have the form *(name, type, inode[, size])*:

     - *name* is a string (or bytes if *dir* is a bytes object) and is the name of
       the entry;
     - *type* is an integer that specifies the type of the entry, with 0x4000 for
       directories and 0x8000 for regular files;
     - *inode* is an integer corresponding to the inode of the file, and may be 0
       for filesystems that don't have such a notion.
     - Some platforms may return a 4-tuple that includes the entry's *size*.  For
       file entries, *size* is an integer representing the size of the file
       or -1 if unknown.  Its meaning is currently undefined for directory
       entries.
    """

@overload
def ilistdir(dir: int, /) -> list[tuple[str, int, int] | tuple[str, int, int, int]]:
    """
    This function returns an iterator which then yields tuples corresponding to
    the entries in the directory that it is listing.  With no argument it lists the
    current directory, otherwise it lists the directory given by *dir*.

    The tuples have the form *(name, type, inode[, size])*:

     - *name* is a string (or bytes if *dir* is a bytes object) and is the name of
       the entry;
     - *type* is an integer that specifies the type of the entry, with 0x4000 for
       directories and 0x8000 for regular files;
     - *inode* is an integer corresponding to the inode of the file, and may be 0
       for filesystems that don't have such a notion.
     - Some platforms may return a 4-tuple that includes the entry's *size*.  For
       file entries, *size* is an integer representing the size of the file
       or -1 if unknown.  Its meaning is currently undefined for directory
       entries.
    """

@overload
def ilistdir(dir: str, /) -> list[tuple[str, int, int] | tuple[str, int, int, int]]:
    """
    This function returns an iterator which then yields tuples corresponding to
    the entries in the directory that it is listing.  With no argument it lists the
    current directory, otherwise it lists the directory given by *dir*.

    The tuples have the form *(name, type, inode[, size])*:

     - *name* is a string (or bytes if *dir* is a bytes object) and is the name of
       the entry;
     - *type* is an integer that specifies the type of the entry, with 0x4000 for
       directories and 0x8000 for regular files;
     - *inode* is an integer corresponding to the inode of the file, and may be 0
       for filesystems that don't have such a notion.
     - Some platforms may return a 4-tuple that includes the entry's *size*.  For
       file entries, *size* is an integer representing the size of the file
       or -1 if unknown.  Its meaning is currently undefined for directory
       entries.
    """

@overload
def ilistdir(dir: bytes, /) -> list[tuple[bytes, int, int] | tuple[bytes, int, int, int]]:
    """
    This function returns an iterator which then yields tuples corresponding to
    the entries in the directory that it is listing.  With no argument it lists the
    current directory, otherwise it lists the directory given by *dir*.

    The tuples have the form *(name, type, inode[, size])*:

     - *name* is a string (or bytes if *dir* is a bytes object) and is the name of
       the entry;
     - *type* is an integer that specifies the type of the entry, with 0x4000 for
       directories and 0x8000 for regular files;
     - *inode* is an integer corresponding to the inode of the file, and may be 0
       for filesystems that don't have such a notion.
     - Some platforms may return a 4-tuple that includes the entry's *size*.  For
       file entries, *size* is an integer representing the size of the file
       or -1 if unknown.  Its meaning is currently undefined for directory
       entries.
    """

@overload
def ilistdir(dir: PathLike[str], /) -> list[tuple[str, int, int] | tuple[str, int, int, int]]:
    """
    This function returns an iterator which then yields tuples corresponding to
    the entries in the directory that it is listing.  With no argument it lists the
    current directory, otherwise it lists the directory given by *dir*.

    The tuples have the form *(name, type, inode[, size])*:

     - *name* is a string (or bytes if *dir* is a bytes object) and is the name of
       the entry;
     - *type* is an integer that specifies the type of the entry, with 0x4000 for
       directories and 0x8000 for regular files;
     - *inode* is an integer corresponding to the inode of the file, and may be 0
       for filesystems that don't have such a notion.
     - Some platforms may return a 4-tuple that includes the entry's *size*.  For
       file entries, *size* is an integer representing the size of the file
       or -1 if unknown.  Its meaning is currently undefined for directory
       entries.
    """

@overload
def ilistdir(dir: PathLike[bytes], /) -> list[tuple[bytes, int, int] | tuple[bytes, int, int, int]]:
    """
    This function returns an iterator which then yields tuples corresponding to
    the entries in the directory that it is listing.  With no argument it lists the
    current directory, otherwise it lists the directory given by *dir*.

    The tuples have the form *(name, type, inode[, size])*:

     - *name* is a string (or bytes if *dir* is a bytes object) and is the name of
       the entry;
     - *type* is an integer that specifies the type of the entry, with 0x4000 for
       directories and 0x8000 for regular files;
     - *inode* is an integer corresponding to the inode of the file, and may be 0
       for filesystems that don't have such a notion.
     - Some platforms may return a 4-tuple that includes the entry's *size*.  For
       file entries, *size* is an integer representing the size of the file
       or -1 if unknown.  Its meaning is currently undefined for directory
       entries.
    """

@overload
def listdir() -> list[str]:
    """
    With no argument, list the current directory.  Otherwise list the given directory.
    """

@overload
def listdir(dir: int, /) -> list[str]:
    """
    With no argument, list the current directory.  Otherwise list the given directory.
    """

@overload
def listdir(dir: str, /) -> list[str]:
    """
    With no argument, list the current directory.  Otherwise list the given directory.
    """

@overload
def listdir(dir: bytes, /) -> list[bytes]:
    """
    With no argument, list the current directory.  Otherwise list the given directory.
    """

@overload
def listdir(dir: PathLike[str], /) -> list[str]:
    """
    With no argument, list the current directory.  Otherwise list the given directory.
    """

@overload
def listdir(dir: PathLike[bytes], /) -> list[bytes]:
    """
    With no argument, list the current directory.  Otherwise list the given directory.
    """

def mkdir(path: AnyPath, /) -> None:
    """
    Create a new directory.
    """

def remove(path: AnyPath, /) -> None:
    """
    Remove a file.
    """

def rmdir(path: AnyPath, /) -> None:
    """
    Remove a directory.
    """

def rename(old_path: AnyPath, new_path: AnyPath, /) -> None:
    """
    Rename a file.
    """

def stat(path: FdOrAnyPath, /) -> tuple[int, int, int, int, int, int, int, int, int, int]:
    """
    Get the status of a file or directory.
    """

def statvfs(path: FdOrAnyPath, /) -> tuple[int, int, int, int, int, int, int, int, int, int]:
    """
    Get the status of a fileystem.

    Returns a tuple with the filesystem information in the following order:

         * ``f_bsize`` -- file system block size
         * ``f_frsize`` -- fragment size
         * ``f_blocks`` -- size of fs in f_frsize units
         * ``f_bfree`` -- number of free blocks
         * ``f_bavail`` -- number of free blocks for unprivileged users
         * ``f_files`` -- number of inodes
         * ``f_ffree`` -- number of free inodes
         * ``f_favail`` -- number of free inodes for unprivileged users
         * ``f_flag`` -- mount flags
         * ``f_namemax`` -- maximum filename length

    Parameters related to inodes: ``f_files``, ``f_ffree``, ``f_avail``
    and the ``f_flags`` parameter may return ``0`` as they can be unavailable
    in a port-specific implementation.
    """

def sync() -> None:
    """
    Sync all filesystems.
    """

def dupterm(stream_object: IOBase | None, index: int = 0, /) -> IOBase | None:
    """
    Duplicate or switch the MicroPython terminal (the REPL) on the given `stream`-like
    object. The *stream_object* argument must be a native stream object, or derive
    from ``io.IOBase`` and implement the ``readinto()`` and
    ``write()`` methods.  The stream should be in non-blocking mode and
    ``readinto()`` should return ``None`` if there is no data available for reading.

    After calling this function all terminal output is repeated on this stream,
    and any input that is available on the stream is passed on to the terminal input.

    The *index* parameter should be a non-negative integer and specifies which
    duplication slot is set.  A given port may implement more than one slot (slot 0
    will always be available) and in that case terminal input and output is
    duplicated on all the slots that are set.

    If ``None`` is passed as the *stream_object* then duplication is cancelled on
    the slot given by *index*.

    The function returns the previous stream-like object in the given slot.
    """

def mount(fsobj: "AbstractBlockDev", mount_point: str, /, *, readonly: bool = False) -> IOBase | None:
    """
    Mount the filesystem object *fsobj* at the location in the VFS given by the
    *mount_point* string.  *fsobj* can be a a VFS object that has a ``mount()``
    method, or a block device.  If it's a block device then the filesystem type
    is automatically detected (an exception is raised if no filesystem was
    recognised).  *mount_point* may be ``'/'`` to mount *fsobj* at the root,
    or ``'/<name>'`` to mount it at a subdirectory under the root.

    If *readonly* is ``True`` then the filesystem is mounted read-only.

    During the mount process the method ``mount()`` is called on the filesystem
    object.

    Will raise ``OSError(EPERM)`` if *mount_point* is already mounted.


    Filesystem mounting
    -------------------

    Some ports provide a Virtual Filesystem (VFS) and the ability to mount multiple
    "real" filesystems within this VFS.  Filesystem objects can be mounted at either
    the root of the VFS, or at a subdirectory that lives in the root.  This allows
    dynamic and flexible configuration of the filesystem that is seen by Python
    programs.  Ports that have this functionality provide the :func:`mount` and
    :func:`umount` functions, and possibly various filesystem implementations
    represented by VFS classes.
    """

def umount(mount_point: str, /) -> None:
    """
    Unmount a filesystem. *mount_point* can be a string naming the mount location,
    or a previously-mounted filesystem object.  During the unmount process the
    method ``umount()`` is called on the filesystem object.

    Will raise ``OSError(EINVAL)`` if *mount_point* is not found.
    """

class VfsFat(AbstractBlockDev):
    """ """

    def __init__(self, block_dev: "AbstractBlockDev", /):
        """
        Create a filesystem object that uses the FAT filesystem format.  Storage of
        the FAT filesystem is provided by *block_dev*.
        Objects created by this constructor can be mounted using :func:`mount`.
        """
    @staticmethod
    def mkfs(block_dev: "AbstractBlockDev", /) -> None:
        """
        Build a FAT filesystem on *block_dev*.
        """

class VfsLfs1(AbstractBlockDev):
    """ """

    def __init__(self, block_dev: "AbstractBlockDev", readsize: int = 32, progsize: int = 32, lookahead: int = 32, /):
        """
        Create a filesystem object that uses the `littlefs v1 filesystem format`_.
        Storage of the littlefs filesystem is provided by *block_dev*, which must
        support the :ref:`extended interface <block-device-interface>`.
        Objects created by this constructor can be mounted using :func:`mount`.

        See :ref:`filesystem` for more information.
        """
    @staticmethod
    def mkfs(block_dev: "AbstractBlockDev", readsize: int = 32, progsize: int = 32, lookahead: int = 32, /) -> None:
        """
        Build a Lfs1 filesystem on *block_dev*.

        .. note:: There are reports of littlefs v1 failing in certain situations,
              for details see `littlefs issue 347`_.
        """

class VfsLfs2(AbstractBlockDev):
    """ """

    def __init__(
        self, block_dev: "AbstractBlockDev", readsize: int = 32, progsize: int = 32, lookahead: int = 32, mtime: bool = True, /
    ):
        """
        Create a filesystem object that uses the `littlefs v2 filesystem format`_.
        Storage of the littlefs filesystem is provided by *block_dev*, which must
        support the :ref:`extended interface <block-device-interface>`.
        Objects created by this constructor can be mounted using :func:`mount`.

        The *mtime* argument enables modification timestamps for files, stored using
        littlefs attributes.  This option can be disabled or enabled differently each
        mount time and timestamps will only be added or updated if *mtime* is enabled,
        otherwise the timestamps will remain untouched.  Littlefs v2 filesystems without
        timestamps will work without reformatting and timestamps will be added
        transparently to existing files once they are opened for writing.  When *mtime*
        is enabled `os.stat` on files without timestamps will return 0 for the timestamp.

        See :ref:`filesystem` for more information.
        """
    @staticmethod
    def mkfs(
        block_dev: "AbstractBlockDev", readsize: int = 32, progsize: int = 32, lookahead: int = 32, mtime: bool = True, /
    ) -> None:
        """
        Build a Lfs2 filesystem on *block_dev*.

        .. note:: There are reports of littlefs v2 failing in certain situations,
              for details see `littlefs issue 295`_.
        """
