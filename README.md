arequal - Tool to test data security of GlusterFS
=======

```console
Usage: arequal-checksum [-?] [-i IGNORED] [-p PATH] [--ignore=IGNORED]
            [--path=PATH] [--help] [--usage]
```


0. Install arequal
------------------
```console
  # ./autogen.sh
  # ./configure
  # make
  # make install
```
  Perform the above installation steps on both clients and servers


1. Generate data set
--------------------
  Create a data set to be used for the test. This data set should
have file sizes and file count similar to the data set to be used
in production. You could also use existing data (like /usr) as
your dataset as it will not be modified. This document will use
/usr as the example source directory.


2. Mount GlusterFS
------------------
  Install, configure and start glusterfs servers and client. If
the Replicate module is loaded, this tool can be used to perform
data consistency check among the replicas. This document will
use /mnt/glusterfs as the example mount point.


3. Start the test
-----------------
```console
  # arequal-run.sh /usr/ /mnt/gluster/usr
```

4. Verify the output
--------------------
   The tool outputs two sets of checksums one after another on
the standard output. Verify that all the values match against
each other. This ensures that the data has been copied over
properly into the GlusterFS mountpoint.


5. Extensive Replicate testing
------------------------------
   The rest of the document is for testing the high availability
and healing features of Replicate.


6. High availability testing
----------------------------
   Restart step 3. While the script is in progress, kill one of the
servers. Let the script continue to completion. The script should
not fail because of one of the server getting killed. The checksums
should still match.


7. Consistency testing
----------------------
  After step 3, run the following command on both the servers

```console
  # arequal-checksum /export/directory
```

  The output values should match


8. Recovery testing
-------------------
   If step 7 is performed after step 6, the output values will not
match since changes performed when one of the servers was down has
not propagated to the backend.

   Bring back the server up again. On the same mountpoint, run an
ls -lR to force an access to all the files on the files involved.

   Now calculate the checksums on both the backends as described
in step 7. The output values should match.
