=======================================
So what exactly is a local environment?
=======================================

As aspiring members of the data community you've learned a lot about
the math and theory needed to build effective predictive models, and
interact with and draw insights from data. The biggest tools we have
to assist with that, besides the one between our ears, are computers
and the language we use in order to be able to interact with and
communicate with them is Python, for many of you your first, but hopefully
not last programming languages in your tool kit. So far for the most
part everyone has been using Colab, which as scientist we can think of
as our laboratory. For reasons which you will learn it is not always
effective or optimal to have our laboratories on Google's servers.
So in a way we can think of setting up our local environments as procuring
and configuring the various tools we will need in our laboratory to
be effective scientists.


Concepts
~~~~~~~~

#. Operating System

#. Shell

#. Terminals and Terminal Emulators

#. Version Control Systems

#. Version Management

#. Virtual Environment

#. Package Management

#. Interpreters

#. Text Editors

What's even is your OS?
~~~~~~~~~~~~~~~~~~~~~~~

At a simple level your operating system is a set of programs to interact
with all the silicon and gold inside the computer in front of you.
It manages hardware, software resources and provides some sort of base
functionality. So why does it matter which one you use? That goes mainly
to the difference between Windows and Unix Systems. Historically, the
Python and Data Science communities have gravitated towards UNIX-based
systems such as MacOS or any of the various Linux distributions (Ubuntu generally being the most popular). While
using one of these systems is not a hard-requirement of the course, nor will it
impact your grade in either a positive or negative way, familiarizing yourself
with a UNIX-based system can have many benefits, and the 2-3 days spent getting
used to your new operating system, will be repaid to you many, many times over
your career.

Shell commands from the Bourne Shell(sh), Bourne-Again Shell(bash), and the
Z Shell are considered by many to be an integral part of what could be called
the Data Science “lingua franca”. Many of the shell commands you used last unit
have their roots in, or are exclusively available on UNIX-based systems, and while
it may come as a surprise to you, you already have spent some significant time
using Linux, since Google Colab is no more than an instance of Jupyter notebooks
running on one of Google’s servers.

Today it’s easier than ever to start developing in Linux. Ubuntu, probably the
most popular recommendation for new Linux users, can be downloaded for free, and
installed in less than 30 minutes with ease. Microsoft itself has in recent years
developed the Windows Subsystem for Linux, which allows users to install and make
use of an actual Linux OS from inside Windows. Many people find this a comfortable
first step in experimenting with Linux. After having been a life-long Windows user
myself, WSL was actually my first step into the Linux world, and a guide I wrote
to setting it up is available `here <https://medium.com/@BrianThomasRoss/windows-for-data-science-part-i-what-is-wsl2-and-how-to-install-it-1187e4367098>`_


Shell
~~~~~

A shell is software that provides an interface for an operating system's users
to provide access to the kernel's services. On Unix-based or Linux-based operating
systems, a shell can be invoked through the shell command in the command line
interface (CLI), allowing users to direct operations through computer commands,
text or script.

Shells also exist for programming languages, providing them with autonomy
from the operating system and allowing cross-platform compatibility.


