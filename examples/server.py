#!/usr/bin/env python3
# laurent.martin.aspera@fr.ibm.com

import setup
import faspmanager
import faspmanager_helper
import logging

# Example 1: download
# Instead of using the soon deprecated FaspManager1 Python lib, let's use the transfer spec
# direction is relative to us, client, i.e. receive = download
logging.debug("======Test download")
t_spec_download = {
    "remote_host":"demo.asperasoft.com",
    "remote_user":"asperaweb",
    "remote_password":"demoaspera",
    "ssh_port":33001,
    "direction":"receive",
    "destination_root":".",
    "paths":[
        {"source":"/aspera-test-dir-tiny/200KB.1"}
    ]
}
faspmanager_helper.start_transfer_and_wait(t_spec_download)

# Example 2: upload: single file upload to existing folder.
logging.debug("======Test upload 1")
t_spec_upload = {
    "remote_host":"demo.asperasoft.com",
    "remote_user":"asperaweb",
    "remote_password":"demoaspera",
    "ssh_port":33001,
    "direction":"send",
    "destination_root":"/Upload",
    #"create_dir":True, # destination root is folder, else it assumes (one source) it is dest file name
    "paths":[
        {"source":"200KB.1"}
    ],
    "tags":{"mysample_tag":"hello"}
}
faspmanager_helper.start_transfer_and_wait(t_spec_upload)
# check file is uploaded by connecting to: http://demo.asperasoft.com/aspera/user/ with same creds

# Example 3: upload: single file upload to non-existing folder
# if there is only one source file and destination does not exist, then "FASP" assumes it is destination filename
# but if destination is a folder, it will send same source filename into folder
# so enforce folder creation, to be sure of what happens
logging.debug("======Test upload 2")
t_spec_upload['destination_root']='/Upload/new_folder'
t_spec_upload['create_dir']=True
faspmanager_helper.start_transfer_and_wait(t_spec_upload)

# Example 4: upload: send to sub folder, but using file pairs
logging.debug("======Test upload 3")
t_spec_upload['destination_root']='/Upload'
del t_spec_upload['create_dir']
t_spec_upload['paths']=[
        {"source":"200KB.1","destination":"xxx/newfilename.ext"}
    ]
faspmanager_helper.start_transfer_and_wait(t_spec_upload)

