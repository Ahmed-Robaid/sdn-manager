Copyright © 2016-2018 `SoftFIRE`_ and `TU Berlin`_. Licensed under
`Apache v2 License`_.

SDN Manager
===========

The SoftFIRE SDN Manager is in charge of managing access to the SDN
resources provided by some testbeds in SoftFIRE.

The SDN Manager keeps track of the API endpoints towards the SDN proxy
services.

The SDN Manager uses the following experiment Lifecycles:

-  List
-  Provision
-  Release

Upon *list resources* the SDN manager returns a list of available SDN
endpoints to the Experimenter.

To actually use an SDN resource in an experiment an *SDNResource* has to
be included in the experiment descripton that matches a resource ID
returned by *list resources*.

Currently supported SDN Endpoints¶
----------------------------------

Each testbed can provide a different implementation of SDN resources.
The current version of the SoftFIRE SDN middleware provides access to
two types of SDN controllers:

-  The Frauhofer FOKUS testbed uses its own implementation of an SDN
   controller named OpenSDNCore.
-  The Ericsson testbed provides access to OpenDayLight SDN controllers.

Workflow
--------

The figure below depicts the workflow of the NFV Manager.

|image0|

For more information on how to use the SDN resources visit the
`documentation`_.

Technical Requirements
----------------------

The SDN Manager requires Python 3.5 or higher.

Installation and configuration
------------------------------

You can install the SDN Manager using pip:

::

    pip install sdn-manager

and then start it with the ``sdn-manager`` command.

Or you can run it from source code by cloning the git repository,
installing the dependencies as specified in the `setup.py`_ file and
executing the *sdn-manager* script.

The SDN Manager needs a configuration file present at
*/etc/softfire/sdn-manager.ini*. An example of the configuration file
can be found `here`_.

Issue tracker
-------------

Issues and bug reports should be posted to the GitHub Issue Tracker of
this project.

What is SoftFIRE?
=================

SoftFIRE provides a set of technologies for building a federated
experimental platform aimed at the construction and experimentation of
services and functionalities built on top of NFV and SDN technologies.
The platform is a loose federation of already existing testbed owned and
operated by distinct organizations for purposes of research and
development.

SoftFIRE has three main objectives: supporting interoperability,
programming and security of the federated testbed. Supporting the
programmability of the platform is then a major goal and it is the focus
of the SoftFIRE’s Second Open Call.

Licensing and distribution
--------------------------

Copyright © [2016-2018] Sof

.. _SoftFIRE: https://www.softfire.eu/
.. _TU Berlin: http://www.av.tu-berlin.de/next_generation_networks/
.. _Apache v2 License: http://www.apache.org/licenses/LICENSE-2.0
.. _documentation: http://docs.softfire.eu/sdn-manager
.. _setup.py: https://github.com/softfire-eu/sdn-manager/blob/master/setup.py
.. _here: https://github.com/softfire-eu/sdn-manager/blob/master/etc/sdn-manager.ini

.. |image0| image:: http://docs.softfire.eu/img/sdn-man-seq-dia.svg