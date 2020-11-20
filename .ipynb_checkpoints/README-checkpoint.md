# CMPSC 100: Fall 2020, Course Project

* Distributed: 2 November 2020
* Due: 7 December 2020 
  * with interim due dates; see below

## Point values

---

|Type                      |Point value |
|--------------------------|------------|
|Documentation             |50 pts.     |
|Working code and output   |40 pts.     |
|Presentation              |10 pts.     |
|                          |            |
|Total                     |100 pts.     |
|                          |10% of course|

## Table of contents

For those who just want to get to work, consult the `Instructional Materials` section. Else, for additional summary or context, read the additional sections included.

* [Accepting the assignment](#Accepting-the-assignment)
* [Overview](#Overview)
  * [Project description](#Project-description)
  * [Supporting reading](#Supporting-readings)
  * [Evaluation](#Evaluation)
    * [Requirements](#Requirements)
* [Wrap-up](#Wrap-up)
  * [GatorGrader](#GatorGrader)
  * [Submitting your work](#Submitting-your-work)
  
## Accepting the assignment

---

- [ ] Log into the `#assignments` channel in our class [Slack](https://cmpsc-100-00-fa-2020.slack.com)
- [ ] Click the link provided for the lab assignment and accept it in GitHub classroom
- [ ] Once the assignment finishes building, click the link to go to your personal repository assignment

## "Cloning" a repository

### Using the correct download link

- [ ] On this repository's page, click the `Clone or download` button in the upper right hand corner
* You may need to scroll up to see it
- [ ] In the upper right corner of the box that appears, click `Use SSH`
- [ ] Copy the link that appears in the textbox below the phrase "Use a password with a protected key."

#### Cloning

* [ ] Type `ls` in your terminal window
* You should be in your `~` directory
- [ ] Once there, "clone" the repository using the link copied above
  * If I (the instructor) were to clone my own repository, I'd enter (your link will look different):

```
git clone git@github.com:allegheny-college-cmpsc-100-fall-2020/cmpsc-100-fall-2020-course-project-dluman
```

## Overview

This semester, in the course of learning fundamental computational concepts using Python, you've been using structured, semi-guided exercises to explore topics. This project invites you to explore and expand your knowledge in greater detail by applying your skills to a different kind of "problem": one of creating a text work.

What do I mean when I write "text work"? The term is, like so many we use, necessarily ambigious. It could be a translator that [turns all words in a text into variations of the word "meow"](https://github.com/hugovk/meow.py/blob/master/meow.py); it could be a graphic novel generator that uses Flickr images and some image magic to [create visual detective comics](http://gregborenstein.com/comics/generated_detective/); it could even be someting madlib-like that tells us [what some random fictional, nameless person in a random place is doing as the clock rolls on](http://opentranscripts.org/transcript/translating-world-clock).

Your goal is deceptively complex: come up with an interesting concept and figure out how to make that concept happen -- in code. You could figure out a way to extract every word beginning with the letter `p` from _Pride & Prejudice_. You could choose 20 of your favorite (**_public domain_**) texts and select random words from each randomly until you've finished the requirements. Heck, you could even create a graphic novel about ellipses, rectangles, and polygons using `PIL` to generate and paste text.

## Supporting readings

These readings will be the subject our lab activity this week. Concentrate on the Kazemi reading and one or two of the projects there and one or two of the projects I've provided.

They are all much less complex than they seem. Don't focus on the code, though (I provide it as a reference), focus on the _process you think the author used to make them_. This is less about "load a file and read a line" and more about thinking (using _Generative Detective_ as a sample):

1. I would find a picture and do something to it to make it look like a comic book
2. I would find some detective novel or text that's interesting
3. I would randomly take a line from that text using some keywords
4. I'd then paste that line at the bottom in a box that looks like comic book descriptions
5. I will not care if it only vaguely makes sense, but it's better if it does

This post from [notoriously great internet person Darius Kazemi](https://tinysubversions.com/) should help break down some of the "OMIGOSHICAN'TDOTHATWUT" that tends to accompany the first time you do someting like this:

* [Even a beginner programmer can make a novel generator](https://tinysubversions.com/notes/nanogenmo-2019/)

### More examples

* [Translating _World Clock_](http://opentranscripts.org/transcript/translating-world-clock/)
  * This source is less about the translation and more about the process
  * Also, like most computational art, [the whole thing is available on the internet](https://nickm.com/poems/world_clock.pdf) (courtesy of the author)
* [Generative Detective](http://gregborenstein.com/comics/generated_detective/)
  * And, read about the process in [this thread](https://github.com/dariusk/NaNoGenMo-2014/issues/70)
* [_Moby Dick_ in 50,000 Meows](https://www.theatlahttps://github.com/hugovk/meow.pyntic.com/technology/archive/2014/12/moby-dick-in-50000-meows-and-other-tales-that-computers-tell/383340/)
  * Of course, the [source and more is here](https://github.com/hugovk/meow.py)

## Evaluation

Being a 100% arbitrary measure, your creative intent with this project is the goal.

Simply put, the outcome of this project should be one of the following:

* A single text file containing the complete output of one run of your program
  * This text file must contain _at least_ 5000 individual words
* A series of _at least_ 10 images, named according to the order to "read" them

But those general goals are a bit too easy. I have more requirements.

### Requirements

|Component              |Due Date    | Weight |
|-----------------------|------------|--------|
|Concept staetment      | 9 November |20 pts. |
|Progress report        | 23 November|10 pts. |
|Final report           | 7 December |20 pts. |
|Final code and output  | 7 December |40 pts. |
|Presentation           | 7 December |10 pts. |
|                       |            |        |
|Total                  |            |100 pts.|

<div class="alert alert-block alert-warning">
<p>This project assumes a very high level of autonomy. Meeting due dates is a key way to demonstrate that you're on track and that you're doing well with this kind of "free-range" project. I advise you to work iteratively (that is, in pieces over time) to complete the work and not let the due date (7 December) sneak up on you. A project like this is no fun if you start it on 6 December.</p>
<p>Plus, by that time, you've already missed a bunch of deadlines.</p>
</div>

#### The docs

Each of these documents already exists in the `docs` directory. It is up to you to complete them.

* A `concept statement` of no fewer than 100 words which:
  * Proposes a tentative/working/permanent title for your project
  * Describes the project you intend to create
  * Your motivation or interest in doing so
  * Potential roadblocks or perceived challenges
  * A description of the _ideal_ outcome/output
  
  
* A `progress report` of no fewer than 300 words that:
  * Describes the state of your project: where are you at? What do you still need to complete?
    * This should take the form of a Markdown list of outstanding tasks and a brief paragraph describing your progress
  * Summarizes your current challenges: where are you stuck? What could you use help with?
  * Celebrates your successes: surely you have some.
  
  
* A `final report` of at least 500 words which:
  * Contains the final title
  * Summarizes your end-of-project thoughts: how do you feel about the outcome of your project?
  * Describes how your project changed over time -- did you need to make it more complex? Simpler? How/why?
  * Contains a "post-mortem" which thinks about: 
    * what worked? 
    * what didn't? 
    * what would you have done differently?
    * what was the biggest challenge that you overcame? How did you do it?
  * Contains a link to your final presentation's video

#### The code

<div class="alert alert-block alert-info">
This section refers to custom or self-written modules. We have not yet encountered this content, but will over the course of the next two weeks. Using a self-written module is highly recommended, but not required.
</div>

This code should be saved as `CMPSC_100_Final_Project.py` in the `src` folder.

Your code should:

* Contain at least one function
  * If your project uses a custom module, functions like `__init__`, et al. do not count
* Use at least one kind of data structure (`list`, `tuple`, `dictionary`)
* Reads at least one file as input
* `import`s (and _uses_) at least one additional module
  * If you write your own module, this counts
* Contains at least one `for` or `while` loop
  * Though, I trust you'll have to use more
* Use a productive number of single-line comments
  * Here, the number is _at least_ 15, though I imagine you'll need many more
* Be completed in a `*.py` file
  * I am, however, open to projects which think about Jupyter notebooks as a storytelling device
    * Think about this one; it could be interesting
    
##### The repository

Because this work should take place iteratively, this repository requires at least _10_ `commit`s.

#### The presentation

A 5-7 minute presentation which:

* Takes the form of a final video presentation
  * A link to the video should be provided in the `final report`
  * You can use Google Meet to achieve this by recording a meeting in which you are the only participant
* Includes slides used during your video as a `PDF` 
* Describes your project, its overall motivation, and how you feel about its success
  * This description should include both a "high-level" view of the project (what it meant to do) and a "low-level" explanantion of _how_ the program works to achieve your higher-level intent
* Shares your favorite portion of the output (or _an_ output) 
  * Sometimes our favorite stuff doesn't make it in to the final product, but was something funny or interesting that happened along the way
* Hightlights the portion of your code of which you're most proud

## Wrap-up

---

### GatorGrader

GatorGrader is an Allegheny College-developed, student-written and maintained application that grades your work for you. The long and short of it: before and when you turn in your assignments, you can know what your approximate grade will be.

(It doesn't do _everything_ for us, but it gives us a good starting point for evaluating your work.)

You don't need to do anything to get it -- I will distribute all the files you need with every repository. You realize the following benefits:

* Complete grading transparency
* Grading criteria _never_ changes
* The criteria is very specific; you will know what changes you need to make

This application runs in your terminal tab, and can grade:

* The whole repository
* Just the docs
* Just the project source code
  * However, for this assignment, grading the source code is not always a conclusive guarantee of success

## Checking your work

---

No matter where you are in your repository, the command to start and run GatorGrader is always the same:

```
gradle grade
```

However, you need to be _in the right place_ to get the right result. The following table summarizes the various grading locations.

| Location | Grading             |
|----------|---------------------|
| Root folder | Repository requirements |
| `docs/` | Worksheet requirements |
| `src/`        | Lab requirements |

### Submitting the assignment/saving progress

The GitHub platform is a place to store your work. So, it makes some sense that should be able to _clone_ (download) from it, and push back (upload) to it. Here, we'll learn this second part.

- [ ] `cd` to your `~` folder
- [ ] Locate your `cmpsc-100-fall-2020-week-08-more-functions-and-modules` folder and `cd` to it.

Once in this folder, we need to tell git that there have been changes.

- [ ] Type `git add .` and press `Enter`
* This tells git to look through the _entire_ folder structure for new changes and "stage" them

- [ ] Type `git commit -m "YOUR COMMIT MESSAGE"` to "label" the commit
* This is typically something like `git commit -m "Fixing a typo"` -- the message in quotes should be as descriptive as possible, while still remaining somewhat short

- [ ] To send all changes to the server, type `git push`
- [ ] At the prompt, input the password associated with the `SSH Key` you created earlier in this exercise (yesterday)

Once the process finishes successfully, we're done!

#### A strong warning

<div class="alert alert-block alert-danger">
    <p><strong>While we may use this server to store code, <u>you</u> are responsible for using GitHub as your main backup.</strong></p>
    <p>While I back this server up on a regular basis, I cannot guarantee that I'll have the ability to restore up-to-the-minute data for your work.</p>
    <p>Remember: to err is human; to back up your work is divine.</p>
</div>
