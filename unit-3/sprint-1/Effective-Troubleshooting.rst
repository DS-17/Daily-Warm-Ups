.. -*- coding: utf-8 -*-
.. Author: Brian Thomas Ross <ML@brianthomasross.com>
.. License: BSD-4-Clause

=========================
Effective Troubleshooting
=========================

.. pull-quote::
    Be warned that being an expert is more than understanding how a system
    is supposed to work. Expertise is gained by investigating why a system
    doesn't work.

    --`Brian Redman <https://en.wikipedia.org/wiki/Brian_Redman>`_

Troubleshooting is a foundational skill in software engineering, not
only for the individual, but also for the team as a whole. What leaves
one person befuddled, may seem glaringly obvious to another, and to that
end what often defines the effectiveness of a programmer, data scientist
or team is not how many lines of code they can produce in a predetermined
amount of time, or how seemingly beautiful or elegant each line of code
produced appears, but rather how effectively can the individuals within
a team diagnose, communicate and resolve errors when they inevitably
arise. One saying which I have come to repeat many times is::

 There are only five actual programmers in the world, and the rest of
 us read their StackOverflow posts.

A bit of this can be taken in jest, but the rest should be taken with
seriousness. With almost absolute certainty each of us has leaned on
the questions and answers that populate the StackOverflow forums as we
have navigated this path towards entry into this industry of the future.
For each answer that we have come across we have also quickly hit
backspace and continued searching for another post five more times. So
perhaps to understand how to more effectively troubleshoot, we should
examine what exactly constitutes a good StackOverflow question.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Anatomy of a Good StackOverflow Question
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Good answers on StackOverflow, and in life in general, are usually
preceded by well-placed questions. StackOverflow has it's own guidelines
for `how to ask a good question <https://stackoverflow.com/help/how-to-ask>`_.
Let's summarize the main points briefly, although it is highly encouraged
that you come back to the linked reference in your own time.

#. Do a little digging on your own
    This follows along with the general 20 minute rule we should all be
    familiar with by now. Not only does this help to push you to earnestly
    examine the problem and push yourself to independently devise a
    solution, but also when you do encounter a unique problem or error
    you will be able to sufficiently communicate to your supervisor or
    teammate as to why this error is in fact unique, and how it differs
    from similar, but distinct errors.

#. An Effective Title
    This title can be thought of as a brief summary of the issue or
    trouble you are encountering. From the StackOverflow guidelines

    .. tip::
        * Pretend you're talking to a busy colleague
        * Spelling, grammar and punctuation are important!
        * If you're having trouble summarizing the problem,
          write the title last

#. Introduce the problem before the code
    How did you encounter the problem? What solutions have you tried
    so far? Any constraints that a solution has to conform to?

#. HELP OTHERS TO REPRODUCE THE PROBLEM
    - Don't copy and paste the entire file / program!
        Not only is this unnecessary, but it also places unnecessary
        burdens on those you're asking for help.
    - Produce a minimal example:
        This is just enough code to reproduce the problem.
    - Eliminate any ancillary issues
        Even if your code was in a rough stage when you encountered the
        error, it doesn't need to be when documenting the problem. A basic
        clean up and tidying of the code will make it easier for your
        teammates to focus on helping you with your issue, instead of
        deciphering the Rosetta Stone.
    - Double-check that the error is reproduced
        (duh!)
    - DO NOT POST IMAGES OF CODE
        DON'T DO IT.
            EVER.
                NOT EVEN ONCE.
                    - You cannot copy / paste a picture of code into your editor
                    - Images are sometimes hard to read
                    - You cannot search through the code in images
                    - Is your problem due to encoding errors or invisible characters? We will never know if you post
                      an image
    - DO NOT POST IMAGES OF CODE
        Repeated for emphasis.

For further information on how to write effective questions
`check out this blog post <https://codeblog.jonskeet.uk/2010/08/29/writing-the-perfect-question/>`_.

----------------------
Providing Good Answers
----------------------

Be polite and civil in your responses, we should aim to attack problems,
not generate them in attacking those asking for help. As the saying goes
if you cannot find something nice to say, better to say nothing at all.
You can always ask for clarification or give advice on how to better pose
questions in the future. A net-neutral response is always better than a
net-negative response. If you do have answer reference contextual
material that supports your answer. Summarize important parts of pertinent
links, especially when the source material is lengthy in nature. Lastly,
write clearly and concisely.

`Here is an example of a good question and answer on StackOverflow <https://stackoverflow
.com/questions/493386/how-to-print-without-newline-or-space>`_

Take the rest of the time before lecture to search through Slack for a
question you previously posed and improve on it. Share the before and
after with your teammates. As always remember to give yourself 5-10 minutes
to get up and stretch / walk around before we continue.
